---
id: methodology
status: current
read_when: >-
  Deciding how a page is composed, what moves, what responds and how the CTA
  works — before Phase 1. The reasoning behind the rules in README.md and the
  layout skill; read it when a rule needs applying to a case it doesn't cover.
depends_on: README.md, skills/equinet-layout/SKILL.md
verified: 2026-10-17
---

# METHODOLOGY.md

How this system thinks about layout, motion, interaction and conversion.

`README.md` holds the rules. This holds the reasoning. When a rule covers the
case, follow the rule — it is more specific and already measured. Read this
when a build hits something the rules don't cover, or when a rule looks wrong
and someone needs to know what it was protecting.

## Where this comes from, and what it is not

Three bodies of work, used for different things:

- **Nielsen Norman Group** — the heuristics, scanning behaviour, response-time
  thresholds, progressive disclosure. Used for how a page is read.
- **Baymard Institute** — large-scale usability testing, with the deepest
  evidence base on forms, and on how people evaluate an offer before
  committing. Used for the conversion path.
- **Interaction Design Foundation** — Gestalt grouping, affordances and
  signifiers, Fitts's and Hick's laws. Used for what a component looks like it
  does.

**This is a synthesis, not a citation.** Nothing here reproduces their
material; each principle is restated in this system's terms and tied to a
rule it produces. Where a principle is theirs, it is named.

**One honest limit.** Baymard's evidence base is overwhelmingly e-commerce —
product pages, carts, checkouts. Equinet builds B2B marketing pages where the
conversion is a booked call, not a purchase. The form and offer-evaluation
findings transfer well; the cart and checkout findings do not apply at all,
and are not invoked here. Where something is weaker evidence for our case,
this document says so rather than borrowing authority.

---

## 1. Layout — how a page is read

**People scan before they read, and they scan in predictable shapes.** NN/g's
work on the F-pattern and the layer-cake pattern says the same thing from two
directions: readers move down the left edge and across headings, sampling, and
only settle into prose once something has earned it.

What that produces here:

- **Every section opens with a direct answer, then expands.** Already the AEO
  rule in the skill, and it is the same rule for human readers as for answer
  engines. A section that opens with throat-clearing is a section that gets
  scanned past.
- **Headings carry the argument.** A reader who reads only the headings should
  get the whole case. If the headings are labels rather than claims, the page
  only works for someone reading every word, which is nobody.
- **The left edge is load-bearing.** Content that starts flush left is found;
  content centred or indented is sampled less. This is why the stat label sits
  left and the figure right in `.eq-card--stacked` — the label is what is
  scanned, the figure is what is found.

**Banner blindness is about position and styling, not about ads.** NN/g's
finding is that readers learn to ignore anything that looks like decoration in
a place decoration usually sits. Consequences:

- A real offer that looks like a banner gets skipped. The CTA panel is a
  section, styled as one, not a strip across the top.
- This is why the draughtsman's line work never carries meaning, and why
  `.eq-surface` is a wash rather than a shape. Decoration that is trying to be
  read is the worst of both.

**Gestalt grouping does the work that borders pretend to.** IxDF's treatment
of proximity, similarity and common region is the practical answer to "how do
I show these belong together": move them closer, make them match, or put them
on a shared surface. In that order. A border is the last resort, not the
first, and a box drawn around things that are already close adds noise without
adding grouping.

This is why `.eq-surface` exists at all — a shared ground groups a set of
sections more cleanly than giving each one a frame.

**Hick's Law is why a page offers few choices.** Decision time grows with the
number and complexity of options. A page with one clear next step converts
better than a page with five, not because readers are lazy but because
choosing is work. Hence: one primary CTA per page, repeated, rather than
several competing ones.

**Progressive disclosure is how depth gets added without cost.** NN/g's
principle: show the common case, make the detail reachable. It is why
multi-part graphics are tab sets rather than everything-at-once, why the FAQ
is an accordion, and why a detail panel carries what the graphic can't draw.
The reader who wants the summary is not taxed by the reader who wants the
detail.

**The first screenful sets expectations; it does not have to contain
everything.** The "above the fold" rule as usually stated is wrong — readers
scroll readily. What NN/g's research supports is narrower and more useful:
attention is densest at the top, and what is there determines whether the
scroll happens. So the top of the page carries the claim and the proof that it
is credible, not the entire argument.

---

## 2. Motion — what it is allowed to do

**Motion answers an action or marks an arrival. It never decorates.** That
sentence is already the rule in the skill; this is why.

**Response-time thresholds are the hard constraint.** Nielsen's three limits,
after Miller, are the ones to design against:

| | |
| --- | --- |
| ~0.1s | feels instantaneous — a direct response to an action |
| ~1s | flow is unbroken, though the delay is noticed |
| ~10s | attention is lost |

The practical floor is tighter than the first limit suggests. IxDF teaches the
**Doherty threshold**: productivity rises sharply when a system responds
within about 400ms. Hover feedback at 120ms sits inside the instantaneous
band; the 0.6s exit is outside it deliberately, because leaving is not an
action the reader is waiting on.

**In fast, out slow.** The asymmetry is not a style choice. The pointer
arriving is a question and the answer must feel instant; the pointer leaving
is not a question at all, and a fast exit reads as the interface flinching.

**Entrance motion marks arrival; it must never gate content.** A reveal that
delays reading is a cost with no benefit. This is why entrance is scoped to
graphics over 64px and to blocks, why the whole thing degrades to visible
under `prefers-reduced-motion`, and why nothing on the page is hidden until it
animates.

**A promise and a report are different things.** Norman's affordance /
signifier distinction cuts both ways. A hover lift is a signifier — it says
something is actionable — so it may only sit on something that is. But motion
that reports the reader's own progress signifies nothing about
actionability; it answers *where am I*, which is Nielsen's first heuristic,
visibility of system status, applied to a document rather than a system. That
is why `[data-progress]` is allowed on content that links nowhere and a hover
lift is not.

**Nothing may exist only in motion.** This follows from the first of Nielsen's
heuristics, visibility of system status, read in reverse: if the only way to
learn something is to watch it happen, a reader who looked away has lost it. A
spotlight emphasises; it never informs.

**Reduced motion means less movement, never less function.** Every behaviour
in this system has a static form that still communicates. A reader with
vestibular sensitivity gets the same information, delivered without travel.

---

## 3. Interaction — what a thing looks like it does

**Affordance is what is possible; a signifier is how the reader knows.**
Norman's distinction, taught through IxDF, is the one that matters most here,
because this system's recurring failure has been the opposite: a signifier
with no affordance behind it.

The rule it produces is already in the digest — a card lifts only if it links
somewhere — and it generalises:

> Every visual promise must be keepable. A hover state is a promise. A cursor
> change is a promise. Motion under a pointer is a loud promise.

A page of seventeen inert cards is not a failure of styling. It is seventeen
things that look available and are not, and readers learn from it that nothing
on the page is clickable.

**Fitts's Law sets target sizes.** Time to hit a target falls with size and
rises with distance. The practical consequences: a hit area of at least
24 × 24 (WCAG 2.5.8 agrees, for a different reason), the whole card as the
target rather than just its title link, and a CTA large enough that reaching
it is not a task.

**Consistency beats cleverness — Jakob's Law.** Readers spend nearly all their
time on other sites, and arrive expecting what those sites do. Native
`<details>` for an accordion, a real `<a>` for a link, tabs that respond to
arrow keys. An invented interaction has to be better than the familiar one by
enough to pay for the learning, and almost nothing is.

**A status mark is a signifier with no spare channels.** A check says
*included*, and for it to work three things must hold, none of them about
looks. It must be **keepable**: a check on something that isn't included is
the same false promise as a hover state on something inert. It must be
**non-visual too**: colour is not the only signal — inclusion is a shape and
absence is a different shape — and a mark that is the only indicator in a cell
needs a text name, or it is an empty cell to a screen reader (WCAG 1.4.1 and
1.1.1). And **absence must be marked**: a blank cell is ambiguous between not
included, not applicable and not known, so the reader has to guess, and
guessing is the work a comparison table exists to remove. That last point is
reasoning from the ambiguity, not a cited finding — nothing here claims an
NN/g or Baymard study on blank cells.

**Recognition over recall.** Nielsen's heuristic. The tab set keeps all four
labels visible while showing one panel; the reader never has to remember what
was in the others. An accordion that collapses everything and shows nothing
fails this, which is why the FAQ's first item can open.

**Feedback is mandatory, instant and local.** Every control changes visibly on
hover, on focus and on activation, and the change happens where the pointer
is. A control with no pressed state leaves the reader wondering whether the
click landed.

**Keyboard parity is not a courtesy.** Anything a pointer can do, a keyboard
must do, and the focus state must be as visible as the hover state. This
system's spotlight centres itself on focus for that reason.

---

## 4. Conversion — how the page earns the next step

**The conversion is a booked call, not a purchase.** That changes what the
page has to do. A buyer with a cart is already convinced; a B2B reader
weighing a diagnostic is deciding whether this is credible and whether the
next step is cheap.

**Reduce the perceived cost of the next step, not just the friction of
taking it.** Baymard's form research is unambiguous that fewer fields, visible
labels rather than placeholders, and inline validation all raise completion.
But for a booked call the larger lever is earlier: the reader needs to know
what the call is, how long it takes, and what happens afterwards. "Book a
Commercial Diagnostic" with no indication of cost or commitment asks for more
than it looks like.

The CTA panel therefore states the shape of the thing — duration, what you
leave with, what it costs — before the button. That is not copywriting
preference; it is the same mechanism as a shipping cost shown before
checkout rather than after.

**Information scent, and why headings matter twice.** NN/g's information
foraging work: readers follow the strongest cue toward what they want and
abandon a path that stops smelling right. A heading that describes rather than
claims gives weak scent. So does a CTA labelled "Submit" or "Learn more" —
the reader cannot tell where it goes, so it is not followed.

**One primary action, repeated, never competing.** Hick's Law again. The page
may offer a secondary path — an FAQ, a detail panel — but exactly one thing is
styled as the primary action, and it appears more than once because a reader
convinced at section four should not have to scroll for it.

**Proof near the claim.** A figure without a source is a claim about a claim.
This system's rule that a statistic carries its source beside it is a
conversion rule as much as an honesty one: an unattributed number raises a
question the reader then has to resolve, and the resolving happens somewhere
other than this page.

**Nothing may depend on motion or hover to be understood.** Repeated here
because it bites hardest at the CTA: a reader on a touch device, or one who
has scrolled past the entrance animation, must still see the offer whole.

---

## 5. What this produces, in build order

The rules in `README.md` and the layout skill, in the sequence a build applies
them:

1. **Find the content's shapes** before choosing any format. A sequence, a
   comparison and a set of claims each want a different thing.
2. **Lead each section with its answer.** Headings carry the argument.
3. **Group by proximity and surface, not by border.**
4. **Give every section one job** and one visual that does it.
5. **Make the depth reachable, not present** — tabs, accordions, panels.
6. **Promise only what is keepable.** Hover states and lifts belong to things
   that do something.
7. **Respond within 120ms, release over 600ms.**
8. **State the shape of the offer before the button**, and use one primary
   action throughout.
9. **Check it works with no JavaScript, no pointer and no motion.** If it
   does, it works for everyone.

---

## 6. Where this document is weaker than it sounds

**Generalising from e-commerce.** The Baymard findings used here are the ones
about forms and offer evaluation, which transfer. Cart, checkout and product
listing findings are not invoked and should not be borrowed.

**No testing of our own.** Everything above is received practice applied to
this system's decisions. Equinet has not usability-tested its own pages, so
where a rule here conflicts with observed behaviour on a real Equinet page,
**the observation wins** and this document is what gets updated.

**Principles are not permissions.** "Hick's Law" is not an argument for
removing a section someone needs, and "progressive disclosure" is not an
argument for hiding something the reader came for. A principle invoked to
justify a decision already made is decoration of a different kind.
