"""
Core markdown-deck -> HTML-presentation logic.

Slide structure is driven purely by heading level — no Marp-style `---`
separators or `<!-- _class: lead -->` comments:

    # Heading   -> starts a new SECTION: renders as one full-bleed divider
                   slide, auto-numbered in document order (01, 02, ...).
                   Any paragraphs between the `#` and the first `##` become
                   the divider's subtitle text.
    ## Heading  -> starts a new SLIDE within the current section: renders
                   as one content slide titled with the heading text; every
                   block up to the next `##`/`#` is that slide's body.

Pipeline (see convert_markdown_to_html at the bottom for the entry point):

    markdown text
      -> parse_front_matter          (front matter dict, remaining body)
      -> split_into_sections         (body -> [(h1 text, section body), ...])
      -> split_section_into_slides   (section body -> leading text, [(h2 text, slide body), ...])
      -> extract_bg_directive        (pull an optional ![bg](...) photo out of some text)
      -> parse_blocks                (remaining text -> list of block dicts)
      -> a render_* function         (blocks -> one <section class="slide"> string)
      -> build_html_document         (all slide sections -> full standalone HTML)

Supported markdown subset is documented in template.md alongside this file.
"""

import re
from pathlib import Path

from . import helpers

# ---------------------------------------------------------------------------
# Front matter + heading-driven structure splitting
# ---------------------------------------------------------------------------

_RE_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
_RE_FRONT_MATTER_LINE = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")
_RE_COMMENT = re.compile(r"<!--(.*?)-->", re.DOTALL)
_RE_H1_LINE = re.compile(r"(?m)^#\s+(.*)$")
_RE_H2_LINE = re.compile(r"(?m)^##\s+(.*)$")


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Split leading `---\\n key: value ... \\n---` front matter from the
    rest of the document. Only flat `key: value` pairs are supported (the
    handful of keys this tool understands: title, description).
    """
    match = _RE_FRONT_MATTER.match(text)
    if not match:
        return {}, text
    meta = {}
    for line in match.group(1).splitlines():
        line_match = _RE_FRONT_MATTER_LINE.match(line.strip())
        if line_match:
            meta[line_match.group(1)] = line_match.group(2).strip()
    return meta, text[match.end():]


def strip_comments(text: str) -> str:
    """Drop `<!-- author notes -->` anywhere in the body; they're no longer
    meaningful directives, just authoring comments that shouldn't leak into
    rendered paragraphs.
    """
    return _RE_COMMENT.sub("", text)


def split_into_sections(text: str) -> list[tuple[str, str]]:
    """Split the document on top-level `# Heading` lines.

    Returns a list of (heading_text, section_body) pairs, where
    section_body is everything up to (not including) the next `#` heading.
    A `## Heading` line never matches here (see _RE_H1_LINE), so h2's stay
    inside their enclosing section's body.
    """
    headings = list(_RE_H1_LINE.finditer(text))
    sections = []
    for i, m in enumerate(headings):
        start = m.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        sections.append((m.group(1).strip(), text[start:end]))
    return sections


def split_section_into_slides(section_body: str) -> tuple[str, list[tuple[str, str]]]:
    """Split one section's body on `## Heading` lines.

    Returns (leading_text, [(heading_text, slide_body), ...]) where
    leading_text is whatever appears before the first `##` (used as the
    section divider's subtitle) and each slide_body runs up to the next
    `##` heading or the end of the section.
    """
    headings = list(_RE_H2_LINE.finditer(section_body))
    leading_text = section_body[: headings[0].start()] if headings else section_body
    slides = []
    for i, m in enumerate(headings):
        start = m.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(section_body)
        slides.append((m.group(1).strip(), section_body[start:end]))
    return leading_text, slides


# ---------------------------------------------------------------------------
# ![bg](...) background-photo directive
# ---------------------------------------------------------------------------

_RE_BG_LINE = re.compile(r"(?m)^!\[bg[^\]]*\]\(([^)]+)\)\s*$")


def extract_bg_directive(text: str) -> tuple[str | None, str]:
    """Pull an optional `![bg](path)` full-bleed background photo line out
    of `text`. Returns (bg_src_or_None, remaining_text).
    """
    match = _RE_BG_LINE.search(text)
    if not match:
        return None, text
    return match.group(1), _RE_BG_LINE.sub("", text).strip()


# ---------------------------------------------------------------------------
# Block parsing: turn a slide's markdown body into a list of block dicts
# ---------------------------------------------------------------------------

_RE_SUBHEADING = re.compile(r"^###\s+(.*)$")
_RE_LIST_ITEM = re.compile(r"^[-*]\s+(.*)$")
_RE_ORDERED_ITEM = re.compile(r"^\d+\.\s+(.*)$")
_RE_TABLE_ROW = re.compile(r"^\|.*\|\s*$")
_RE_TABLE_SEPARATOR = re.compile(r"^\|?[\s:|-]+\|?$")
_RE_IMAGE_LINE = re.compile(r"^!\[(.*?)\]\((\S+)\)\s*$")
_RE_IMAGE_HEIGHT = re.compile(r"^h:(\d+)\s+(.*)$")
_RE_HORIZONTAL_RULE = re.compile(r"^(-{3,}|\*{3,}|_{3,})\s*$")


def _flush_paragraph(lines: list[str], blocks: list[dict]) -> None:
    if lines:
        blocks.append({"type": "paragraph", "text": " ".join(lines)})
        lines.clear()


def parse_blocks(text: str) -> list[dict]:
    """Parse a slide's (or a section's leading) markdown body into an
    ordered list of block dicts: heading / paragraph / list / table /
    image. `#`/`##` never appear here (already consumed by the section/
    slide split); a `<style ...>...</style>` block and bare `---`/`***`
    horizontal rules are dropped as visual noise this tool doesn't need.
    """
    text = re.sub(r"(?s)<style\b.*?</style>", "", text)
    lines = text.splitlines()
    blocks: list[dict] = []
    paragraph_buf: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line.strip() or _RE_HORIZONTAL_RULE.match(line.strip()):
            _flush_paragraph(paragraph_buf, blocks)
            i += 1
            continue

        heading_match = _RE_SUBHEADING.match(line)
        if heading_match:
            _flush_paragraph(paragraph_buf, blocks)
            blocks.append({"type": "heading", "text": heading_match.group(1).strip()})
            i += 1
            continue

        image_match = _RE_IMAGE_LINE.match(line)
        if image_match:
            _flush_paragraph(paragraph_buf, blocks)
            blocks.append(_make_image_block(image_match.group(1), image_match.group(2)))
            i += 1
            continue

        if _RE_LIST_ITEM.match(line) or _RE_ORDERED_ITEM.match(line):
            _flush_paragraph(paragraph_buf, blocks)
            ordered = bool(_RE_ORDERED_ITEM.match(line))
            items: list[str] = []
            # Consume marker lines as new items; a non-blank line with no
            # marker is a wrapped continuation of the previous item (lazy
            # continuation, same as CommonMark) unless it starts a new
            # block (heading/image/table), which ends the list.
            while i < len(lines) and lines[i].strip():
                item_match = _RE_ORDERED_ITEM.match(lines[i]) if ordered else _RE_LIST_ITEM.match(lines[i])
                if item_match:
                    items.append(item_match.group(1).strip())
                elif items and not (_RE_SUBHEADING.match(lines[i]) or _RE_IMAGE_LINE.match(lines[i]) or _RE_TABLE_ROW.match(lines[i])):
                    items[-1] += " " + lines[i].strip()
                else:
                    break
                i += 1
            blocks.append({"type": "list", "ordered": ordered, "items": items})
            continue

        if _RE_TABLE_ROW.match(line):
            _flush_paragraph(paragraph_buf, blocks)
            table_lines = []
            while i < len(lines) and _RE_TABLE_ROW.match(lines[i]):
                table_lines.append(lines[i].strip())
                i += 1
            blocks.append(_make_table_block(table_lines))
            continue

        paragraph_buf.append(line.strip())
        i += 1

    _flush_paragraph(paragraph_buf, blocks)
    return blocks


def _split_table_row(row: str) -> list[str]:
    """Split a pipe-delimited table row into trimmed cell strings, dropping
    the empty leading/trailing cell produced by a row's outer '|' chars.
    """
    cells = row.strip().split("|")
    if cells and cells[0].strip() == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [c.strip() for c in cells]


def _make_table_block(table_lines: list[str]) -> dict:
    header_cells = _split_table_row(table_lines[0])
    body_rows = [
        _split_table_row(row)
        for row in table_lines[2:]  # skip header + '---' separator row
        if not _RE_TABLE_SEPARATOR.match(row.replace("|", ""))
    ]
    return {"type": "table", "header": header_cells, "rows": body_rows}


def _make_image_block(alt: str, src: str) -> dict:
    height_match = _RE_IMAGE_HEIGHT.match(alt)
    if height_match:
        return {"type": "image", "src": src, "caption": height_match.group(2), "height": int(height_match.group(1))}
    return {"type": "image", "src": src, "caption": alt, "height": None}


# ---------------------------------------------------------------------------
# Block -> HTML rendering (generic, reused by every content slide)
# ---------------------------------------------------------------------------


def render_heading_block(block: dict) -> str:
    return f'<div class="subhead">{helpers.render_inline(block["text"])}</div>'


def render_image_block(block: dict, base_dir: Path) -> str:
    src = helpers.resolve_image_src(block["src"], base_dir)
    style = f' style="height:{block["height"]}px"' if block["height"] else ""
    alt = helpers.render_inline(block["caption"])
    caption_html = f'<div class="cap">{alt}</div>' if block["caption"] else ""
    return f'<div class="imgbox"><img src="{src}"{style} alt="{alt}">{caption_html}</div>'


def render_list_block(block: dict) -> str:
    tag = "ol" if block["ordered"] else "ul"
    items = "".join(f"<li>{helpers.render_inline(item)}</li>" for item in block["items"])
    return f'<{tag} class="points">{items}</{tag}>'


def render_table_block(block: dict) -> str:
    header = "".join(f"<th>{helpers.render_inline(c)}</th>" for c in block["header"])
    body_rows = "".join(
        "<tr>" + "".join(f"<td>{helpers.render_inline(c)}</td>" for c in row) + "</tr>"
        for row in block["rows"]
    )
    return f'<table class="fpt"><thead><tr>{header}</tr></thead><tbody>{body_rows}</tbody></table>'


def render_paragraph_block(block: dict) -> str:
    return f'<p class="lead">{helpers.render_inline(block["text"])}</p>'


def render_generic_block(block: dict, base_dir: Path) -> str:
    """Dispatch a single block to its renderer."""
    renderers = {
        "heading": lambda b: render_heading_block(b),
        "image": lambda b: render_image_block(b, base_dir),
        "list": lambda b: render_list_block(b),
        "table": lambda b: render_table_block(b),
        "paragraph": lambda b: render_paragraph_block(b),
    }
    return renderers[block["type"]](block)


# ---------------------------------------------------------------------------
# Slide-kind detection (by content shape) + per-kind renderers
# ---------------------------------------------------------------------------

_RE_TOC_ITEM = re.compile(r"^\*\*(.+?)\*\*\s*(?:—\s*(.*))?$")


def _accents_html() -> str:
    return (
        '<div class="accents"><span style="background:var(--accent-1)"></span>'
        '<span style="background:var(--accent-2)"></span>'
        '<span style="background:var(--accent-3)"></span>'
        '<span style="background:var(--accent-4)"></span></div>'
    )


def render_divider_subtitle(leading_blocks: list[dict]) -> str:
    """Render a section's pre-`##` paragraphs as light-on-dark subtitle
    text under its divider title. Other block types found before the
    first `##` (lists, tables, images) are ignored — dividers stay clean
    full-bleed slides, not content slides.
    """
    return "".join(f'<p class="divider-sub">{helpers.render_inline(b["text"])}</p>' for b in leading_blocks if b["type"] == "paragraph")


def render_divider_slide(section_num: str, title_html: str, subtitle_html: str, bg_src: str | None, base_dir: Path) -> str:
    if bg_src:
        bg = helpers.resolve_image_src(bg_src, base_dir)
        open_tag = f'<section class="slide divider" style="background-image: linear-gradient(rgba(16,23,63,.85), rgba(16,23,63,.90)), url(\'{bg}\')">'
    else:
        open_tag = '<section class="slide divider bg-navy">'  # no photo: plain navy gradient
    return (
        f'{open_tag}<div class="sec-num">{section_num}</div><h1>{title_html}</h1>'
        f'<div class="rule"></div>{subtitle_html}{_accents_html()}</section>'
    )


def render_toc_slide(blocks: list[dict]) -> str:
    ordered = next(b for b in blocks if b["type"] == "list")
    items_html = []
    for i, raw_item in enumerate(ordered["items"], start=1):
        item_match = _RE_TOC_ITEM.match(raw_item.strip())
        title = helpers.strip_inline_markers(item_match.group(1)) if item_match else helpers.render_inline(raw_item)
        desc = item_match.group(2) or "" if item_match else ""
        items_html.append(
            f'<div class="item"><div class="n">{i:02d}</div><div><h3>{title}</h3><p>{helpers.render_inline(desc)}</p></div></div>'
        )
    return (
        '<section class="slide bg-light content">'
        '<div class="slide-head"><div class="num">§</div><h2>Table of contents</h2></div>'
        f'<div class="toc">{"".join(items_html)}</div>'
        '</section>'
    )


def _is_team_table(block: dict) -> bool:
    return block["type"] == "table" and block["header"] and all(c.strip().startswith("![") for c in block["header"])


def render_team_card(cell_markdown: str) -> str:
    """Render one team-roster table cell (photo + <br>-separated bio lines,
    where the name is **bold** and the role is *italic*) as a card.
    """
    photo_match = _RE_IMAGE_LINE.match(cell_markdown.split("<br>", 1)[0].strip())
    photo_html = f'<img src="{photo_match.group(2)}" alt="{helpers.render_inline(photo_match.group(1))}">' if photo_match else ""
    remaining = cell_markdown.split("<br>", 1)[1] if "<br>" in cell_markdown else ""
    lines = [line.strip() for line in remaining.split("<br>") if line.strip()]

    name_html, role_html, detail_lines = "", "", []
    for idx, line in enumerate(lines):
        if idx == 0:
            name_html = f'<span class="name">{helpers.strip_inline_markers(line)}</span>'
        elif idx == 1:
            role_html = f'<span class="role">{helpers.strip_inline_markers(line)}</span>'
        else:
            detail_lines.append(f'<span class="detail">{helpers.render_inline(line)}</span>')

    return f'<div class="team-card">{photo_html}{name_html}{role_html}{"".join(detail_lines)}</div>'


def render_team_slide(section_num: str, title_html: str, blocks: list[dict], base_dir: Path) -> str:
    table = next(b for b in blocks if _is_team_table(b))
    cards = "".join(render_team_card(cell) for cell in table["header"])
    other_blocks = "".join(render_generic_block(b, base_dir) for b in blocks if b is not table)
    return (
        '<section class="slide bg-light content">'
        f'<div class="slide-head"><div class="num">{section_num}</div><h2>{title_html}</h2></div>'
        f'<div class="team-grid">{cards}</div>{other_blocks}'
        '</section>'
    )


def render_content_slide(section_num: str, title_html: str, blocks: list[dict], base_dir: Path) -> str:
    body_html = "".join(render_generic_block(b, base_dir) for b in blocks)
    return (
        '<section class="slide bg-light content">'
        f'<div class="slide-head"><div class="num">{section_num}</div><h2>{title_html}</h2></div>'
        f'{body_html}'
        '</section>'
    )


def render_slide_by_kind(section_num: str, heading_text: str, blocks: list[dict], base_dir: Path) -> str:
    """Pick a slide renderer from the `##` heading text / body shape: a
    heading of "Table of contents" gets the TOC layout, a body built
    around a team-roster table gets the team layout, everything else is a
    generic content slide.
    """
    title_html = helpers.render_inline(heading_text)
    plain_title = helpers.strip_inline_markers(heading_text).lower()
    if plain_title in ("table of contents", "contents"):
        return render_toc_slide(blocks)
    if any(_is_team_table(b) for b in blocks):
        return render_team_slide(section_num, title_html, blocks, base_dir)
    return render_content_slide(section_num, title_html, blocks, base_dir)


def append_footer(section_html: str, deck_title: str, page_number: int) -> str:
    """Content/TOC/team slides carry a footer with the deck title and an
    auto-numbered page badge; inserted just before the closing </section>.
    """
    footer = f'<div class="footer"><span>{helpers.render_inline(deck_title)}</span><span class="page">{page_number}</span></div>'
    return section_html[: -len("</section>")] + footer + "</section>"


def _mark_first_slide_active(section_html: str) -> str:
    """The deck script toggles `.active` at runtime, but the very first
    slide needs it present up front so the page isn't blank before the
    script (or a no-JS print view) kicks in.
    """
    return section_html.replace('class="slide ', 'class="slide active ', 1)


# ---------------------------------------------------------------------------
# Full-document assembly
# ---------------------------------------------------------------------------

_DECK_SCRIPT = """
const slides = Array.from(document.querySelectorAll('.slide'));
let cur = 0;

function fit() {
  const s = Math.min(innerWidth / 1280, innerHeight / 720);
  slides.forEach(sl => sl.style.transform = `scale(${s})`);
}
function show(i) {
  cur = Math.max(0, Math.min(slides.length - 1, i));
  slides.forEach((sl, k) => sl.classList.toggle('active', k === cur));
  document.getElementById('ctr').textContent = `${cur + 1} / ${slides.length}`;
  document.getElementById('prog').style.width = `${(cur + 1) / slides.length * 100}%`;
  location.hash = cur ? `#${cur + 1}` : '';
}
addEventListener('resize', fit);
addEventListener('keydown', e => {
  if (['ArrowRight', 'PageDown', ' ', 'Enter'].includes(e.key)) { e.preventDefault(); show(cur + 1); }
  else if (['ArrowLeft', 'PageUp', 'Backspace'].includes(e.key)) { e.preventDefault(); show(cur - 1); }
  else if (e.key === 'Home') show(0);
  else if (e.key === 'End') show(slides.length - 1);
  else if (e.key.toLowerCase() === 'f') document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen();
});
document.getElementById('prev').onclick = () => show(cur - 1);
document.getElementById('next').onclick = () => show(cur + 1);
let tx = null;
addEventListener('touchstart', e => tx = e.touches[0].clientX);
addEventListener('touchend', e => { if (tx !== null) { const dx = e.changedTouches[0].clientX - tx; if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1)); tx = null; } });

const h = parseInt((location.hash || '').slice(1), 10);
fit(); show(isNaN(h) ? 0 : h - 1);
"""


def build_html_document(meta: dict, slides_html: str, style_css: str) -> str:
    """Wrap rendered <section> slides and the shared stylesheet/script into
    one standalone HTML document.
    """
    title = meta.get("title", "Presentation")
    description = meta.get("description", "")
    description_tag = f'<meta name="description" content="{helpers.render_inline(description)}">\n' if description else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{helpers.render_inline(title)}</title>
{description_tag}<style>
{style_css}
</style>
</head>
<body>

<div class="deck">
{slides_html}
</div>

<div class="hint">&larr; &rarr; navigate &middot; F fullscreen &middot; print for PDF</div>
<div class="hud">
  <button id="prev" aria-label="Previous slide">&lsaquo;</button>
  <span class="ctr" id="ctr"></span>
  <button id="next" aria-label="Next slide">&rsaquo;</button>
</div>
<div class="progress" id="prog"></div>

<script>{_DECK_SCRIPT}</script>

</body>
</html>
"""


def convert_markdown_to_html(md_text: str, base_dir: Path, style_css: str) -> str:
    """Top-level conversion: markdown deck source -> full standalone HTML.

    `base_dir` is the directory markdown-relative image paths resolve
    against (normally the source .md file's own parent directory).
    """
    meta, body = parse_front_matter(md_text)
    deck_title = meta.get("title", "")
    body = strip_comments(body)

    section_htmls = []
    page_number = 0
    for section_index, (heading_text, section_body) in enumerate(split_into_sections(body), start=1):
        section_num = f"{section_index:02d}"
        leading_text, slide_texts = split_section_into_slides(section_body)

        bg_src, leading_text = extract_bg_directive(leading_text)
        subtitle_html = render_divider_subtitle(parse_blocks(leading_text))
        section_htmls.append(render_divider_slide(section_num, helpers.render_inline(heading_text), subtitle_html, bg_src, base_dir))

        for slide_heading, slide_body in slide_texts:
            _, slide_body = extract_bg_directive(slide_body)  # content slides don't use a background photo
            slide_html = render_slide_by_kind(section_num, slide_heading, parse_blocks(slide_body), base_dir)
            page_number += 1
            section_htmls.append(append_footer(slide_html, deck_title, page_number))

    if not section_htmls:
        raise ValueError("no '#' section headings found in the markdown — see tools/md2deck/template.md for the expected structure")

    section_htmls[0] = _mark_first_slide_active(section_htmls[0])
    return build_html_document(meta, "\n".join(section_htmls), style_css)
