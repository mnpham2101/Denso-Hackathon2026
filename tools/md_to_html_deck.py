#!/usr/bin/env python3
"""
md_to_html_deck.py — convert a Marp-style markdown deck (or a folder of
them) into a self-contained, single-file HTML presentation, in the visual
style of the FPT-Hackathon2026 Round1-presentation reference deck.

Usage:
    python md_to_html_deck.py <source> [output]

  <source>  A single markdown file, OR a folder containing one or more
            *.md files (searched non-recursively) — each file becomes its
            own standalone presentation.
  [output]  Optional.
              - omitted                        -> write each deck.html next
                                                   to its source .md file
              - a folder (existing, or path with no file extension)
                                                -> write every deck inside it
              - a single source file + a path
                ending in a file extension      -> write exactly there

Every generated .html embeds its own CSS/JS and inlines local images as
base64 data URIs, so each output file is a standalone artifact that needs
no other files alongside it to open and present.

See tools/md2deck/template.md for the supported markdown syntax and
tools/md2deck/style.css for the visual style — both are the reusable
building blocks this script drives; this file only handles CLI plumbing.
"""

import argparse
import sys
from pathlib import Path

from md2deck import deck, helpers

STYLE_CSS_PATH = Path(__file__).parent / "md2deck" / "style.css"


def resolve_output_pairs(source: Path, output: Path | None) -> list[tuple[Path, Path]]:
    """Work out the (markdown_path, html_output_path) pairs to generate,
    following the CLI's source/output directory-vs-file rules described
    in this file's module docstring.
    """
    if source.is_dir():
        md_files = helpers.find_markdown_files(source)
        # A folder source always produces a folder of outputs — even if
        # `output` looks like a filename, multiple decks can't share it.
        out_dir = output if output is not None else source
        return [(md, out_dir / f"{md.stem}.html") for md in md_files]

    if output is None:
        return [(source, source.with_suffix(".html"))]
    looks_like_a_folder = output.is_dir() or output.suffix == ""
    if looks_like_a_folder:
        return [(source, output / f"{source.stem}.html")]
    return [(source, output)]


def convert_one(md_path: Path, html_path: Path, style_css: str) -> None:
    """Render one markdown deck to HTML and write it to disk.

    Images are resolved relative to the markdown file's own directory, so
    a deck's `assets/...` paths keep working regardless of where the
    output file ends up.
    """
    md_text = md_path.read_text(encoding="utf-8")
    html_text = deck.convert_markdown_to_html(md_text, base_dir=md_path.parent, style_css=style_css)
    helpers.ensure_parent_dir(html_path)
    html_path.write_text(html_text, encoding="utf-8")
    print(f"{md_path} -> {html_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", type=Path, help="Markdown file, or a folder of markdown files")
    parser.add_argument("output", type=Path, nargs="?", default=None, help="Output HTML file or folder (default: alongside the source)")
    args = parser.parse_args()

    if not args.source.exists():
        sys.exit(f"error: source not found: {args.source}")

    style_css = STYLE_CSS_PATH.read_text(encoding="utf-8")
    pairs = resolve_output_pairs(args.source, args.output)
    if not pairs:
        sys.exit(f"error: no .md files found in {args.source}")

    for md_path, html_path in pairs:
        convert_one(md_path, html_path, style_css)


if __name__ == "__main__":
    main()
