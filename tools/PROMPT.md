# Original request (saved verbatim)

Date: 2026-08-27

> write script to read a markdown an generate a HTML presentation, static page, self contained. with style similar to C:\Users\MinhP\Documents\Work\FPT-Hackathon2026\Round1-presentation
>
> include the template markdown, style information. Place in tools
>
> tool can be used by running simple command python [path/to/script] [path/to/source] [path/to/output]
>
> path to source can be a folder contain multiple markdowns
> path to output can be a folder or in same directory if not given.
>
> script must be clearly comment; functions must be re-usable. Helpers functions must be separated from main logic. Keep function concised, condense to single purpose.

## Reference material inspected

- `C:\Users\MinhP\Documents\Work\FPT-Hackathon2026\Round1-presentation\m1-proposal-deck.md`
  Marp-flavored markdown deck: YAML front matter, `---`-separated slides,
  `<!-- _class: lead -->` / `<!-- _paginate: false -->` directives, `![bg](...)`
  full-bleed background images, `![h:NNN caption](path)` sized images, GFM
  tables, bullet lists, and a "single header row" table hack used to lay out
  team-member photo cards.
- `C:\Users\MinhP\Documents\Work\FPT-Hackathon2026\Round1-presentation\m1-proposal-deck.html`
  Hand/tool-rendered single-file HTML slideshow in that style: fixed
  1280x720 slides scaled to fit the viewport, keyboard/touch/click
  navigation, a progress bar, print-to-PDF support, and a light/navy card
  based visual language (orange/green/blue/teal/navy accents, skewed bullet
  markers, rounded card tables). Some hand-written quirks in that file
  (e.g. the team-photo table degrading to broken `<a>` tags, `<style
  scoped>` leaking into paragraph text) were treated as bugs to avoid
  reproducing, not behavior to copy.

## Resulting deliverable

`tools/md_to_html_deck.py` (entry point) plus the `tools/md2deck/` package
(`helpers.py`, `deck.py`, `style.css`, `template.md`) — see `tools/md2deck/template.md`
for the supported markdown syntax.

## Follow-up request (2026-08-27)

> can you remove the Marp style?
>
> Instead use the headers as indicator for new slide. `#` is section slide;
> `##` is slide

This replaced the Marp `---`/`<!-- _class: lead -->`-driven slide
boundaries with a pure heading-hierarchy model: a `#` heading starts a new
auto-numbered section (rendered as a full-bleed divider slide; any
paragraphs before the first `##` become its subtitle), and a `##` heading
starts a content slide within that section. `![bg](...)` full-bleed photos
are still supported on sections. Dedicated "cover"/"thank you" slide kinds
(previously triggered by `_class: lead` + first/last-slide position) were
dropped since that signal no longer exists — a plain `# Title` section now
serves as both; TOC and team-roster-table detection (by heading text /
table shape) were kept as-is.
