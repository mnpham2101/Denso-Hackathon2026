---
title: Your Deck Title
description: One-line description shown in the HTML <meta> tag
---

# Your Deck Title

**A short tracked eyebrow label, if this lone line is the only thing in
its paragraph and fully wrapped in `**bold**`** — rendered above the
title in small caps.

A regular subtitle/scope statement can go here — any other paragraph
placed before the first `##` is shown under the title's rule, in a style
distinct from both the eyebrow and the title (nothing needed for a
title/cover slide beyond this).

## Table of contents

1. **Team information**
2. **Project description** — the problem and the goal
3. **Technical approach** — architecture and stack
4. **Closing** — why this proposal

# Team information

<!-- Team roster: a table whose header-row cells each start with an image.
     Each cell is one member card: ![photo](path), then **Name**, then
     *Role*, then any number of plain detail lines, all separated by <br>. -->

## Team information

| ![Jane Doe](assets/jane.png)<br>**Jane Doe**<br>*Team Lead*<br>10 yrs experience<br>Python · Systems design | ![John Smith](assets/john.png)<br>**John Smith**<br>*Engineer*<br>5 yrs experience<br>C++ · Embedded |
| --- | --- |

**Two engineers** across systems design and embedded software.

# Project description

![bg](assets/section-bg.png)

Every `#` section renders as a full-bleed divider, in one of two looks:
add a `![bg](path)` line anywhere before the first `##` to use your own
photo for that one section (white title, dark overlay for contrast); leave
it out and only the deck's first and last sections (cover and closing)
fall back to the tool's bundled default photo. Every other section instead
renders on a plain light background with the same orange-number/navy-title
colors as a content slide's title — no photo to re-embed on every divider.

## Project goals — one short sentence per slide title

**The problem**, stated as one bold lead-in sentence, then the detail.

- **First point.** Supporting detail for the first bullet — bullets render
  with the same skewed-square marker as the reference deck.
- **Second point.** You can use `inline code`, *italic*, **bold**, and
  [links](https://example.com) inside any bullet or paragraph.
- **Third point.** Keep bullets to one or two lines for readability.

![h:260 Caption describing the figure](assets/diagram.svg)

Closing paragraph for the slide, again with **bold** emphasis where useful.

## A slide built around a table

Any GFM pipe table (more than one row) renders as a rounded card table.

### Optional sub-heading

A `###` heading inside a slide renders as a small in-slide label — useful
to break one slide's body into a couple of labeled parts.

| Column A | Column B | Column C |
| -------- | -------- | -------- |
| **Row 1** | Detail text | More detail |
| **Row 2** | Detail text | More detail |

# Closing

## Why this proposal

**Point one — stated boldly.**

**Point two — stated boldly.**

# Thank you!

Your Deck Title · Event name
