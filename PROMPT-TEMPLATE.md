---
id: prompt-template
status: current
read_when: >-
  Writing the prompt that generates a page from this system. Not a rules
  document — the rules live in README.md; this is brief-level direction only.
depends_on: README.md, skills/equinet-layout/SKILL.md
verified: 2026-10-13
---

# Claude Design prompt template

For generating pages against this design system. Replace `{CONTEXT}` with the
name of the idea — the page's subject in a few words.

---

## The shortest prompt — use this

As of 2026-10-02 the layout skill builds in everything that used to need
spelling out: interaction states, entrance motion, an accordion FAQ with
FAQPage markup, AEO structure, asset selection and the never-invent-data rule.
A prompt now only needs what changes from page to page.

```
Using the Equinet design system, follow skills/equinet-layout/SKILL.md.

Build a landing page on: [topic].
Audience: [who it's for].
Goal: [the one thing the reader should do]. CTA: [button label and destination].

Build directly — skip the brief. One design only.
```

**Optional lines**, added only when they apply:

- `Produce the layout brief first and wait for my approval.` — instead of
  building directly, for a page whose layout you want to review first.
- `Link to [page] from this page; don't edit [page].` — for a spin-off, so it
  links to the parent rather than redesigning it as well.
- `Use these figures, with their sources: [paste].` — the only way statistics
  appear. Without it, the page uses none (or sourced figures from
  `assets/charts/data.json` where they genuinely fit).
- `Allow two or three variations.` — on a first exploration, before you've
  chosen a direction.

**Before prompting:** if the repo has changed, refresh the design system's
import in Claude Design first. A prompt can't fetch the repo.

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
> **Every section gets a visual.** Place a whole illustration from
> `assets/illustrations/INDEX.md` when its subject matches {CONTEXT}. When none
> does, **compose** a bespoke infographic from the set's structural primitives
> — cards, connectors, nodes, panels, one orange accent — in the style of
> `assets/marketing/`. Use `assets/comps/` as layout blueprints. Never a
> mismatched whole illustration; never a bare section.
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
> `sectors/` carry their own light gradient — fill the frame, keep them off
> dark sections. `systems/` and `flows/` are transparent and need a surface.
> `pictonodes/` are square and belong beside a heading or list item, not in a
> 16:9 row.
>
> **Icons — `assets/icons/`.** Only the three root icons take `currentColor`.
> For anything with no Equinet geometry, use Lucide — generously, on cards,
> lists, stats and steps. 24×24 canvas, round caps and joins,
> `stroke-width="1"`, no icon over 48px, a `<!-- lucide/name -->` source
> comment. Fetch paths from the library; never draw a glyph by hand.
> See `ICON-REFERENCE.md`. `nodes/` are white glyphs on dark tiles: keep the
> tile, swap the glyph for Lucide (except `node-hubspot`, a brand mark). For `service-tiles/`, the tile is the brand asset but the white glyph
> inside it is iconography: swap it for a context-appropriate Lucide icon
> (1px stroke, round caps, white, ~27px box) and leave the rect, gradient and
> radius untouched. Replace the whole set or none of it — a 1px substitute
> next to a delivered 2px glyph looks mixed.
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

## Does this need pasting every session?

**Mostly no.** The design-system format specifies that an agent reads
`README.md` first, and this system's rules now sit in a digest at the
very top of it. Tokens, icons, illustrations, spacing, motion and the
escalation rule are genuinely built in — Claude Design gets them from the
system itself.

**What can't be built in, and always needs stating:** `{CONTEXT}` — the page
subject — and the AEO section. Answer-engine structure describes how a page
is written and organised, not how the brand looks. It belongs to the brief,
not the design system, and putting it in `tokens.css` or the README would
blur what the system is for.

So the practical shape of a session prompt is short: name the subject, name
the structure you want, and let the system carry the rest. The long version
below is for a first run, an audit, or when you want the rules restated in
front of the model at generation time rather than trusting they were read.

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
| "Compose when nothing matches" | Without it, a model either forces a near-miss illustration or — as an earlier version of this rule caused — leaves sections bare. Composing from primitives avoids both. |
| Named h2 rules | An earlier bug set the stagger heading from a 48px token with a 36px fallback — right only when `tokens.css` failed to load. |
| Opaque `scenes/` warning | Dropping one on a white card leaves a hard dark rectangle. Only found on the third audit pass. |
| "Sample from `tokens.css`, not artwork" | Eight colours across the illustration set are logged but unsanctioned; extraction propagates them silently. |
| Lucide named specifically | The house chevron *is* Lucide's `arrow-right` — same path, different notation. Any other library needs rework to match. |
| "Tell me plainly if it can't be satisfied" | Otherwise gaps get filled with something plausible instead of surfaced. |

## Minimum viable prompt

Once the design system is loaded, most of the long prompt is redundant —
the rules live in the repo and Claude Design reads them. Checked line by line
against the system on 2026-09-24:

| Your line | Status |
| --- | --- |
| "Pull updated GitRep from [URL]" | **Can't work either way.** Private repo, read through a configured import. Refresh before prompting; the line does nothing in a prompt and can't be a rule. |
| "Enhance layout with assets in illustrations and icons" | **Built in** — the README digest rules on icons, illustrations, every-section-gets-a-visual and backgrounds, plus `INDEX.md` and `ICON-REFERENCE.md`. Includes the compose-from-primitives fallback and the 1px/48px icon rule. |
| "Best practice UI/UX methodologies" | **Built in** — contrast, alignment, hierarchy and density are all in the instructions section. |
| "Reorder graphical layouts…" | **Built in** — the kit-of-parts rule plus the `.eq-stagger` pointer. |
| "AEO principles" | **Not built in, on purpose.** Editorial, not design. Must be in the prompt. |

So the per-session prompt reduces to the subject plus the editorial brief:

> Build a **{CONTEXT}** pillar page using the Equinet Design System, following
> its rules.
>
> Structure it for answer engines: question-shaped H2s that match how someone
> would actually ask; each section opening with a direct, self-contained
> answer in 1–2 sentences before expanding; terms defined on first use; tables
> and lists only where content is genuinely enumerable; entities named
> explicitly rather than "it" or "this approach"; one idea per section so a
> chunk stands alone as a citation.
>
> Tell me plainly if anything can't be satisfied rather than approximating.

**One honest caveat.** A rule in the repo is *available* to the model; a rule
in the prompt is *in front of* it at generation time. Those aren't the same,
and a long README is not guaranteed to be read end to end — which is why the
rules digest was hoisted to the top of `README.md`. If output drifts on a
specific rule, restate that one rule in the prompt rather than reverting to
pasting everything. Treat the full template as a fallback for when something
goes wrong, not the default.

## Short version

For iterating, once the system is loaded:

> **{CONTEXT}** pillar page, Equinet Design System. Tokens only — no invented
> colours or typefaces. Section headings 36px uppercase with the heading
> shadow. Check `assets/illustrations/INDEX.md` and match illustrations on
> subject; if none fits {CONTEXT}, compose one from primitives. Illustrations are
> reference — recompose freely, but colour, type and icons stay per the
> system. `scenes/` are opaque; `pictonodes/` are square. Lucide for missing
> icons, used generously. `.eq-stagger` rows. Structure for AEO:
> question-shaped H2s, answer-first sections, defined terms, self-contained
> chunks. Flag anything you can't satisfy.
