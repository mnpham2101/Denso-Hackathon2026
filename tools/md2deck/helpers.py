"""
Low-level, deck-agnostic helpers: HTML escaping/inline markdown rendering,
image embedding, and filesystem plumbing.

Nothing in this module knows what a "slide" or a "deck" is — that logic
lives in deck.py. Keeping the split this way means every function here can
be reused (and unit-tested) independently of the slide-classification
rules.
"""

import base64
import html
import mimetypes
import re
from pathlib import Path

# Placeholder used to protect literal "<br>" tags from HTML-escaping while
# the rest of a text run is escaped; restored to a real <br> at the end of
# render_inline().
_BR_PLACEHOLDER = "\x00BR\x00"

_RE_BR = re.compile(r"<br\s*/?>", re.IGNORECASE)
_RE_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_RE_BOLD = re.compile(r"\*\*(.+?)\*\*")
_RE_ITALIC = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)|(?<!_)_([^_\n]+)_(?!_)")
_RE_CODE = re.compile(r"`([^`]+)`")


def render_inline(text: str) -> str:
    """Render one line/run of inline markdown (bold, italic, code, links,
    literal <br>) into safe HTML. Everything else is HTML-escaped first,
    so raw '<', '>' and '&' in source text always come through literally.
    """
    text = _RE_BR.sub(_BR_PLACEHOLDER, text)
    text = html.escape(text, quote=False)

    # Code spans are stashed before link/bold/italic run, so e.g. a literal
    # `![bg](path)` shown as sample syntax inside backticks doesn't get
    # misread as a real link — CommonMark gives code spans top precedence.
    code_spans: list[str] = []

    def _stash_code(match: re.Match) -> str:
        code_spans.append(match.group(1))
        return f"\x00CODE{len(code_spans) - 1}\x00"

    text = _RE_CODE.sub(_stash_code, text)
    text = _RE_LINK.sub(r'<a href="\2">\1</a>', text)
    text = _RE_BOLD.sub(r"<strong>\1</strong>", text)
    text = _RE_ITALIC.sub(lambda m: f"<em>{m.group(1) or m.group(2)}</em>", text)
    for i, code in enumerate(code_spans):
        text = text.replace(f"\x00CODE{i}\x00", f"<code>{code}</code>")

    return text.replace(_BR_PLACEHOLDER, "<br>")


def strip_inline_markers(text: str) -> str:
    """Strip **bold**/*italic*/`code` markers to get plain text, e.g. for
    deriving a slide's page title from a heading that itself uses markdown.
    """
    text = _RE_BOLD.sub(r"\1", text)
    text = _RE_ITALIC.sub(lambda m: m.group(1) or m.group(2), text)
    text = _RE_CODE.sub(r"\1", text)
    return text.strip()


def resolve_image_src(src: str, base_dir: Path) -> str:
    """Turn a markdown image path into a self-contained data: URI so the
    generated HTML has no external file dependencies.

    Remote URLs (http/https) and files that can't be read are returned
    unchanged — the deck still renders, it just isn't self-contained for
    that one image.
    """
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", src) or src.startswith("data:"):
        return src
    file_path = (base_dir / src).resolve()
    try:
        data = file_path.read_bytes()
    except OSError:
        return src
    mime_type, _ = mimetypes.guess_type(file_path.name)
    mime_type = mime_type or "application/octet-stream"
    encoded = base64.b64encode(data).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def find_markdown_files(source_dir: Path) -> list[Path]:
    """List *.md files directly inside a directory (non-recursive), sorted
    for stable, predictable output ordering.
    """
    return sorted(p for p in source_dir.glob("*.md") if p.is_file())


def ensure_parent_dir(path: Path) -> None:
    """Create the parent directory of `path` if it doesn't exist yet."""
    path.parent.mkdir(parents=True, exist_ok=True)
