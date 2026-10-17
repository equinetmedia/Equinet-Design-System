/* ============================================================================
   EQUINET — GRAPHIC MOTION
   Entrance choreography for inline SVG graphics annotated with data-role,
   and for HTML blocks marked data-reveal (cards, stat panels, sections).
   Pairs with the "GRAPHIC MOTION" section of components/bundle.css.

   Does only what CSS can't:
     1. measures stroked connectors so they can be drawn on,
     2. numbers elements within each role for the stagger,
     3. arms each graphic, then starts it once it scrolls into view,
     4. removes its own dash properties afterwards, so the resting state is
        the original artwork exactly.

   Progressive: if this script never runs, fails, or the reader prefers
   reduced motion, nothing is ever hidden — the graphic is simply static.

   In a HubSpot module, this is the body of module.js; scope the selector to
   the module root instead of `document`.
   ========================================================================== */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reduce.matches || !('IntersectionObserver' in window)) return;

  // Entrance length = latest role start (640ms) + stagger cap (480ms)
  // + longest transition (600ms). Clean up a little after that.
  var CLEANUP_AFTER_MS = 1900;

  // A connector can be drawn on only if it is a real stroke: it has a
  // stroke, no fill, and isn't already dashed by the artwork. 76 of 117
  // connectors are filled outline shapes — those fade instead.
  function isDrawable(el) {
    if (typeof el.getTotalLength !== 'function') return false;
    var stroke = el.getAttribute('stroke');
    var fill = (el.getAttribute('fill') || '').toLowerCase();
    if (!stroke || stroke === 'none') return false;
    if (fill && fill !== 'none') return false;
    if (el.getAttribute('stroke-dasharray')) return false;
    return true;
  }

  function prepare(svg) {
    var counts = {};
    var els = svg.querySelectorAll('[data-role]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      var role = el.getAttribute('data-role');
      counts[role] = (counts[role] || 0) + 1;
      el.style.setProperty('--i', counts[role] - 1);

      if (role === 'connector' && isDrawable(el)) {
        var len = Math.ceil(el.getTotalLength());
        if (len > 0) {
          el.setAttribute('data-draw', '');
          el.style.setProperty('--len', len + 'px');  // must carry a unit: Chrome rejects a bare number for stroke-dashoffset in CSS and silently uses 0
        }
      }
    }
  }

  // Return the graphic to exactly its original rendering. Removing the dash
  // properties restores the DOM, but Chrome keeps the raster it painted while
  // strokes were dashed — measured at up to 35/255 on line-end pixels, all of
  // them on drawn connectors. A fresh copy of the node has no render history
  // and was measured pixel-identical to the static artwork, so swap one in.
  // Nothing is lost: the clone carries every attribute and class, and these
  // decorative SVGs hold no listeners.
  function cleanup(svg) {
    var drawn = svg.querySelectorAll('[data-draw]');
    for (var i = 0; i < drawn.length; i++) {
      drawn[i].removeAttribute('data-draw');
      drawn[i].style.removeProperty('--len');
    }
    if (svg.parentNode) svg.parentNode.replaceChild(svg.cloneNode(true), svg);
  }

  function reveal(svg) {
    svg.classList.add('is-visible');
    window.setTimeout(function () { cleanup(svg); }, CLEANUP_AFTER_MS);
  }

  // Entrance motion is for GRAPHICS, not icons. A page can easily carry 50
  // small icons; annotating each one puts a few hundred elements into the
  // entrance choreography for line art a few pixels across, which buys
  // nothing a reader notices and makes scrolling stutter. 2026-10-14: a GEO
  // page animated 234 elements, 149 of them inside icons 64px or smaller.
  //
  // The gate is applied here as well as in the skill, because a build that
  // over-annotates should still produce a smooth page.
  var MIN_GRAPHIC_PX = 64;

  function isGraphic(svg) {
    if (svg.hasAttribute('data-motion-always')) return true;   // deliberate override
    var box = svg.getBoundingClientRect();
    // A zero box means it is not laid out yet (display:none, or off-screen in
    // a collapsed panel). Treat it as a graphic and let the observer decide.
    if (!box.width && !box.height) return true;
    return Math.max(box.width, box.height) > MIN_GRAPHIC_PX;
  }

  var graphics = Array.prototype.filter.call(
    document.querySelectorAll('svg[data-asset]:not([data-motion-ready])'),
    isGraphic
  );
  // HTML blocks marked data-reveal: cards, stat panels, section blocks.
  var blocks = document.querySelectorAll('[data-reveal]:not([data-motion-ready])');
  if (!graphics.length && !blocks.length) return;

  // After a block's entrance, drop the reveal classes so the element returns
  // to its own styles — otherwise a revealed .eq-card would keep the reveal's
  // staggered transition-delay and its hover lift would lag.
  function revealBlock(el) {
    el.classList.add('is-visible');
    window.setTimeout(function () {
      el.classList.remove('eq-reveal', 'is-visible');
      el.style.removeProperty('--i');
    }, CLEANUP_AFTER_MS);
  }

  var observer = new IntersectionObserver(function (entries) {
    for (var i = 0; i < entries.length; i++) {
      if (entries[i].isIntersecting) {
        var t = entries[i].target;
        observer.unobserve(t);
        if (t.hasAttribute('data-reveal')) revealBlock(t); else reveal(t);
      }
    }
  }, { threshold: 0.25, rootMargin: '0px 0px -10% 0px' });

  // Arm blocks. Stagger siblings that share a parent, so a row of cards
  // arrives in order. Same no-transition arming as graphics.
  var siblingIndex = new Map();
  for (var r = 0; r < blocks.length; r++) {
    var el = blocks[r];
    el.setAttribute('data-motion-ready', '');
    var n = siblingIndex.get(el.parentNode) || 0;
    siblingIndex.set(el.parentNode, n + 1);
    el.style.setProperty('--i', n);
    el.classList.add('eq-reveal', 'eq-reveal--arming');
    void el.getBoundingClientRect();
    el.classList.remove('eq-reveal--arming');
    observer.observe(el);
  }

  // Leave self-animating artwork alone. sector-built-environment-animated
  // carries its own embedded @keyframes loop; layering this on top would put
  // two animation systems on the same elements.
  function animatesItself(svg) {
    var styles = svg.querySelectorAll('style');
    for (var s = 0; s < styles.length; s++) {
      if (/@keyframes|animation\s*:/.test(styles[s].textContent)) return true;
    }
    return false;
  }

  for (var g = 0; g < graphics.length; g++) {
    var svg = graphics[g];
    svg.setAttribute('data-motion-ready', '');
    if (animatesItself(svg)) continue;
    prepare(svg);
    // Arm WITHOUT transitions. prepare() calls getTotalLength(), which forces
    // a style computation — so the visible, fully drawn state is already on
    // record. Adding .eq-motion with transitions live would then ANIMATE into
    // the hidden state: elements fade out and lines un-draw, and a graphic
    // visible on load flickers. Disable transitions, flush, then re-enable.
    svg.classList.add('eq-motion', 'eq-motion--arming');
    void svg.getBoundingClientRect();
    svg.classList.remove('eq-motion--arming');
    observer.observe(svg);
  }

  // If the reader switches on reduced motion mid-session, show everything
  // at once and stop observing.
  function onPreferenceChange(e) {
    if (!e.matches) return;
    observer.disconnect();
    for (var k = 0; k < graphics.length; k++) {
      graphics[k].classList.add('is-visible');
      cleanup(graphics[k]);
    }
    for (var q = 0; q < blocks.length; q++) {
      blocks[q].classList.remove('eq-reveal', 'is-visible');
    }
  }
  if (typeof reduce.addEventListener === 'function') {
    reduce.addEventListener('change', onPreferenceChange);
  } else if (typeof reduce.addListener === 'function') {
    reduce.addListener(onPreferenceChange);
  }
})();


/* ============================================================================
   GRAPHIC HOTSPOTS — pairs with .eq-graphic__hotspot in bundle.css.
   Added 2026-10-13, reworked the same day to the APG tabs pattern.

   TWO FORMS, picked from the role the author wrote:

   role="tab"     Several hotspots in one graphic, one detail panel showing at
                  a time. This is the normal case: a flow, a system diagram, a
                  set of stages. Implemented as WAI-ARIA Authoring Practices
                  tabs, because that is what it is — "select one of several
                  related panels" — and readers already know how it behaves.

   role="button"  A single hotspot toggling one panel independently. A
                  disclosure, not a tab set. Use when there is no "one of
                  several" relationship to express.

   WHY TABS AND NOT EIGHT BUTTONS:
   A roving tabindex gives the whole graphic ONE tab stop. Arrow keys move
   between hotspots, Home and End jump to the ends. Eight separately focusable
   hotspots would mean eight tab stops a keyboard reader has to pass through
   to reach the next section — technically operable, miserable to use.

   ACTIVATION IS AUTOMATIC: moving to a tab selects it. APG sanctions this
   where switching is instantaneous and local, which it is — the panels are
   inline text already in the document. Arrowing through the graphic and
   watching the context change is the point.

   NO-JS: panels are NOT hidden in markup. This block hides them. With no
   script every panel stays visible and readable, and an answer engine sees
   all of the content — which is the entire reason the detail is on the page.

   Runs regardless of prefers-reduced-motion. Reduced motion means less
   movement, never less function.
   ========================================================================== */
(function () {
  'use strict';

  var graphics = document.querySelectorAll('.eq-graphic:not([data-hotspot-ready])');
  if (!graphics.length) return;

  function panelFor(hotspot) {
    var id = hotspot.getAttribute('aria-controls');
    return id ? document.getElementById(id) : null;
  }

  function nameMissing(hotspot) {
    return !hotspot.getAttribute('aria-label') && !hotspot.querySelector('title');
  }

  // ------------------------------------------------------------- tab set --
  function initTabs(graphic, tabs) {
    var list = tabs[0].closest('[role="tablist"]') || graphic.querySelector('svg');
    if (list && !list.getAttribute('role')) list.setAttribute('role', 'tablist');

    function select(index, moveFocus) {
      for (var i = 0; i < tabs.length; i++) {
        var on = i === index;
        tabs[i].setAttribute('aria-selected', on ? 'true' : 'false');
        // Roving tabindex: exactly one hotspot is in the tab order.
        tabs[i].setAttribute('tabindex', on ? '0' : '-1');
        var panel = panelFor(tabs[i]);
        if (panel) {
          if (on) { panel.removeAttribute('hidden'); }
          else { panel.setAttribute('hidden', ''); }
        }
      }
      if (moveFocus) tabs[index].focus();
    }

    for (var i = 0; i < tabs.length; i++) {
      (function (tab, index) {
        if (nameMissing(tab)) {
          console.warn('[equinet] tab hotspot has no accessible name:', tab);
        }
        var panel = panelFor(tab);
        if (panel) {
          if (!panel.getAttribute('role')) panel.setAttribute('role', 'tabpanel');
          if (!panel.getAttribute('aria-labelledby') && tab.id) {
            panel.setAttribute('aria-labelledby', tab.id);
          }
          // A panel holding focusable content needs its own tab stop so a
          // keyboard reader can reach that content from the tab.
          if (!panel.hasAttribute('tabindex')) panel.setAttribute('tabindex', '0');
        }

        tab.addEventListener('click', function () { select(index, true); });

        tab.addEventListener('keydown', function (e) {
          var next = null;
          switch (e.key) {
            case 'ArrowRight': case 'ArrowDown': next = (index + 1) % tabs.length; break;
            case 'ArrowLeft':  case 'ArrowUp':   next = (index - 1 + tabs.length) % tabs.length; break;
            case 'Home':       next = 0; break;
            case 'End':        next = tabs.length - 1; break;
            // Enter and Space are redundant under automatic activation, but a
            // reader who presses them should not scroll the page instead.
            case 'Enter': case ' ': case 'Spacebar': next = index; break;
            default: return;
          }
          e.preventDefault();
          select(next, true);
        });
      })(tabs[i], i);
    }

    // Honour an author-chosen starting tab; otherwise open the first.
    var start = 0;
    for (var k = 0; k < tabs.length; k++) {
      if (tabs[k].getAttribute('aria-selected') === 'true') { start = k; break; }
    }
    select(start, false);
  }

  // --------------------------------------------------------- disclosures --
  function initButtons(buttons) {
    for (var i = 0; i < buttons.length; i++) {
      (function (hotspot) {
        if (nameMissing(hotspot)) {
          console.warn('[equinet] hotspot has no accessible name:', hotspot);
        }
        if (!hotspot.hasAttribute('tabindex')) hotspot.setAttribute('tabindex', '0');
        if (hotspot.getAttribute('aria-expanded') === null) {
          hotspot.setAttribute('aria-expanded', 'false');
        }
        var panel = panelFor(hotspot);
        if (panel && hotspot.getAttribute('aria-expanded') === 'false') {
          panel.setAttribute('hidden', '');
        }

        function toggle() {
          var open = hotspot.getAttribute('aria-expanded') === 'true';
          hotspot.setAttribute('aria-expanded', open ? 'false' : 'true');
          if (panel) {
            if (open) { panel.setAttribute('hidden', ''); }
            else { panel.removeAttribute('hidden'); }
          }
        }

        hotspot.addEventListener('click', toggle);
        hotspot.addEventListener('keydown', function (e) {
          // A <g role="button"> is not a button to the browser: no implicit
          // activation, and Space would scroll the page.
          if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') {
            e.preventDefault();
            toggle();
          }
        });
      })(buttons[i]);
    }
  }

  for (var g = 0; g < graphics.length; g++) {
    var graphic = graphics[g];
    var tabs = graphic.querySelectorAll('.eq-graphic__hotspot[role="tab"]');
    var buttons = graphic.querySelectorAll('.eq-graphic__hotspot[role="button"]');
    if (!tabs.length && !buttons.length) continue;
    graphic.setAttribute('data-hotspot-ready', '');
    if (tabs.length) initTabs(graphic, tabs);
    if (buttons.length) initButtons(buttons);
  }
})();
