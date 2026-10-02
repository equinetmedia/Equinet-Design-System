# Brand mark

The Equinet Media wordmark, provided 2026-09-22 as two ready-made variants —
unlike `assets/icons/`, this folder holds real, usable files, not an
inventory waiting on source material.

| File | Fill | Use on |
| --- | --- | --- |
| `wordmark-light.svg` | `#FFFFFF` (solid white) | Navy or other dark grounds — the navigation header, the `plain_hero_banner` background |
| `wordmark-dark.svg` | `#242530` | White or light grounds — footers, light-background modules |

Both files are the same artwork: identical path geometry, `viewBox="0 0 727 305"`
(≈2.38:1), differing only in fill colour. This mirrors the same light/dark
toggle pattern already used for the primary button's hover SVGs — pick the
variant by background, the same way the *Toggle Dark or Light* field does for
buttons.

**A useful data point for an open question.** The dark variant's fill is
`#242530` — that's `equinet-color-text`, not `equinet-color-heading`
(`#242630`). The two tokens are one hex digit apart and already flagged in
`README.md` as "visually identical, kept separate." This doesn't resolve
whether they should merge, but it's evidence the brand mark itself was built
against `equinet-color-text` specifically, not the heading colour — worth
knowing before merging in either direction.

## Usage rules

- The wordmark conveys meaning (it's the brand name, not a decoration), so it
  needs an accessible name where it appears — `role="img"` with
  `aria-label="Equinet Media"`, or wrapped in a link to the homepage with
  that as the link's accessible name. It does not take `aria-hidden`.
- Pick the variant by contrast with its background, not by which one was
  used last. A navy or photo background gets `wordmark-light.svg`; a white
  or pale-surface background gets `wordmark-dark.svg`.
- No minimum size or clear-space rule is documented yet — nothing in the
  supplied files specifies one, so none is asserted here. Add one if the
  brand guidelines ever state it explicitly.

## Emblem — The Commercial Intelligence Engine

`emblem-commercial-intelligence-engine.svg`, added 2026-10-02. The mark of
Equinet's named methodology: a gear with orbiting nodes, an entry arrow and a
check. Single ink — `#242630`, 4px stroke, no fill — on a 284 × 275 artboard.

Delivered as an "icon", but it isn't one: it's nearly six times the 48px icon
ceiling and functions as identity, not as a control glyph. So it lives with
the wordmark.

It's the same emblem that sits in the centre card of
`hero-commercial-intelligence-engine`, where it's drawn in orange — 16 of its
24 path shapes match that hero exactly.

**Minimum size: about 72px.** The 4px stroke scales with the artboard, so at
smaller sizes the line thins below 1px and the small nodes close up. At 72px it
renders roughly 1px; at 48px about 0.7px.

**Colour.** It's a single ink, so inline it and set the stroke from a token to
recolour it — `#242630` on light grounds, white or `--equinet-color-orange` on
navy, as the hero does. Placed as an `<img>` it stays `#242630`.
