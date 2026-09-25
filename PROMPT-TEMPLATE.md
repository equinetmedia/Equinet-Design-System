# Claude Design prompt template

For generating pages against this design system. Replace `{CONTEXT}` with the
name of the idea — the page's subject in a few words.

---

## Before you prompt

**Refresh the design system first, outside the prompt.** This repo is private
and Claude Design reads it through a configured GitHub import, not by fetching
a URL mid-conversation. An instruction like "pull the latest from
github.com/..." either does nothing or produces a confident claim that it did.
If the system is stale, re-run the import (or `/design-sync` from a local
clone) *before* starting, then prompt normally.

---

## The prompt

> Build a **{CONTEXT}** pillar page using the Equinet Design System.
>
> **Design system — non-negotiable.** Every colour, type size, weight,
> tracking and spacing value comes from `tokens.css`. No invented hues, no
> third typeface. Headings: Open Sans at weight 800, or the body family at
> 900 — never mix the two rules. Section headings are 36px
> (`--equinet-fontsize-section-heading`), uppercase, with
> `text-shadow: -2px 2px 4px rgba(0,0,0,0.15)`. Eyebrows are uppercase with
> `0.2em` tracking at 12px.
>
> **Illustrations — read `assets/illustrations/INDEX.md` before choosing.**
> Match on subject, not on how a filename sounds. **If no illustration
> matches {CONTEXT}, use none** — the set covers Equinet's service lines,
> sectors and business-process concepts only, and a near-miss reads as filler.
> Say so explicitly rather than substituting something approximate.
>
> Illustrations are artistic reference, not sealed artwork: crop into details,
> scale, overlap, and pull elements out to recombine into new compositions.
> Rearranging is licence to compose, never licence to invent a colour,
> typeface or glyph. Two traps — an extracted element loses the ground it was
> drawn against, so re-check contrast; and several colours in those files are
> unsanctioned, so sample from `tokens.css`, not from the artwork.
>
> The 12 files in `scenes/` are opaque with a navy gradient across the full
> artboard — media panels and card headers, never dropped on a white surface.
> `sectors/` and `systems/` are transparent and need a surface behind them.
> `pictonodes/` are square and belong beside a heading or list item, not in a
> 16:9 row.
>
> **Icons — `assets/icons/`.** Only the three root icons take `currentColor`.
> For anything with no Equinet geometry, use Lucide (24×24, 2px stroke, round
> caps and joins — an exact match to the house style, see
> `ICON-REFERENCE.md`) and mark it in a comment as a placeholder. Never
> fabricate a glyph. `nodes/` are brand marks — place them, don't take them
> apart. For `service-tiles/`, the tile is the brand asset but the white glyph
> inside it is iconography: swap it for a context-appropriate Lucide icon
> (2px stroke, round caps, white, ~27px box) and leave the rect, gradient and
> radius untouched.
>
> **Layout.** Use `.eq-stagger` from `components/bundle.css` for alternating
> media/text rows. Vary the rhythm where it serves the content — reorder,
> regroup, break the alternation for a full-width moment — but keep spacing on
> the `--equinet-space-*` scale and don't mix square and 16:9 art in one row.
>
> **Structure for answer engines (AEO).** Write so an AI answer engine can
> extract and cite a section without the surrounding page:
> - Question-shaped H2s that match how someone would actually ask.
> - Answer first: each section opens with a direct, self-contained answer in
>   1–2 sentences, then expands. No throat-clearing.
> - Define terms on first use; don't rely on a definition three sections up.
> - Use tables and lists where the content is genuinely enumerable — they
>   extract cleanly. Don't force prose into a table to look structured.
> - Name entities explicitly and consistently rather than leaning on "it" or
>   "this approach".
> - One idea per section, so a section can stand alone as an answer.
>
> **Accessibility.** WCAG 2.1 AA. Decorative illustrations take `alt=""`; one
> carrying meaning needs a real accessible name. Any motion sits behind both
> a `prefers-reduced-motion: no-preference` wrapper and a `reduce` fallback.
>
> Tell me plainly if any part of this can't be satisfied — a missing
> illustration, a subject outside the set, a token that doesn't exist — rather
> than approximating.

---

## What's already built in, and what isn't

Most of this prompt restates rules that live in the repo — `README.md`'s
"Instructions for AI-generated design" section, `assets/illustrations/INDEX.md`,
and the per-folder READMEs. Claude Design reads those when it reads the design
system, so the prompt is reinforcement, not the only place the rules exist.
Restating them is still worth doing: a rule in a prompt is in front of the
model at generation time, a rule in a README may or may not be.

**Deliberately not built into the design system: the AEO section.** Answer-engine
structure is editorial guidance about how a page is written and organised —
question-shaped headings, answer-first sections, self-contained chunks. None
of it is a design decision, none of it belongs in `tokens.css` or a component,
and putting it in the design system would blur what that system is for. It
stays in the prompt, where it applies to the brief rather than to the brand.

The same goes for `{CONTEXT}` itself and any subject-specific direction: the
design system describes how Equinet looks and behaves, not what a given page
should say.

## Why each constraint is there

| Constraint | What goes wrong without it |
| --- | --- |
| "If nothing matches, use none" | A prompt asking to "enhance with assets" reads as an instruction to use one, and a near-miss gets chosen. This happened on the AI-addiction test page. |
| Named h2 rules | An earlier bug set the stagger heading from a 48px token with a 36px fallback — right only when `tokens.css` failed to load. |
| Opaque `scenes/` warning | Dropping one on a white card leaves a hard dark rectangle. Only found on the third audit pass. |
| "Sample from `tokens.css`, not artwork" | Eight colours across the illustration set are logged but unsanctioned; extraction propagates them silently. |
| Lucide named specifically | The house chevron *is* Lucide's `arrow-right` — same path, different notation. Any other library needs rework to match. |
| "Tell me plainly if it can't be satisfied" | Otherwise gaps get filled with something plausible instead of surfaced. |

## Short version

For iterating, once the system is loaded:

> **{CONTEXT}** pillar page, Equinet Design System. Tokens only — no invented
> colours or typefaces. Section headings 36px uppercase with the heading
> shadow. Check `assets/illustrations/INDEX.md` and match illustrations on
> subject; if nothing fits {CONTEXT}, use none and say so. Illustrations are
> reference — recompose freely, but colour, type and icons stay per the
> system. `scenes/` are opaque; `pictonodes/` are square. Lucide for missing
> icons, marked as placeholders. `.eq-stagger` rows. Structure for AEO:
> question-shaped H2s, answer-first sections, defined terms, self-contained
> chunks. Flag anything you can't satisfy.
