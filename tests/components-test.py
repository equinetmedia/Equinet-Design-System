#!/usr/bin/env python3
"""Component test — .eq-card, .eq-faq and [data-reveal] (components/bundle.css
+ components/motion.js), in a real headless browser.

Run from the repo root:
    pip install playwright && python -m playwright install chromium
    python tests/components-test.py

Checks: cards and FAQ work with no JS; reveals arm hidden below the fold and
arrive in sequence; reveal classes are removed afterwards so hover has no
stagger delay; linked cards lift 6px on hover and keyboard focus, unlinked
cards don't; collapsed FAQ answers stay in the document; the accordion opens
through intermediate heights; Enter and Space toggle it; assistive tech hears
expanded true/false; the FAQPage JSON-LD matches the visible questions; and
reduced motion removes all movement while keeping feedback.
"""
import os, re, json, tempfile
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP=tempfile.mkdtemp(prefix="eq-components-")
chev=open(os.path.join(REPO,'assets/icons/arrow-chevron.svg')).read()
chev=re.sub(r'<svg[^>]*>','<svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">',chev,count=1)
def card(i,link=True):
    t=f'<a class="eq-card__link" href="#c{i}">Card {i} title</a>' if link else f'Card {i} title'
    return f'<article class="eq-card" data-reveal id="card{i}"><h3 class="eq-card__title">{t}</h3><p class="eq-card__text">Body text for card {i}.</p></article>'
faq=[("What is GEO?","Generative Engine Optimization is the practice of structuring content so AI answer engines can find, understand and cite it."),
     ("How is GEO different from SEO?","SEO targets rankings in a list of links; GEO targets being quoted inside a generated answer.")]
items=''.join(f'<details class="eq-faq__item"><summary class="eq-faq__question">{q}<span class="eq-faq__icon" aria-hidden="true">{chev}</span></summary><div class="eq-faq__answer"><p>{a}</p></div></details>' for q,a in faq)
ld=json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})
page=f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://{REPO}/tokens.css"><link rel="stylesheet" href="file://{REPO}/components/bundle.css">
<style>body{{margin:0;font-family:sans-serif}}.spacer{{height:1400px}}.row{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;padding:40px}}.faq{{padding:40px;max-width:800px}}</style></head>
<body><div class="spacer"></div><p class="eq-eyebrow" id="ebp">Why HubSpot</p><p class="eq-eyebrow eq-eyebrow--solid" id="ebs">Why HubSpot</p><p class="eq-eyebrow eq-eyebrow--solid eq-eyebrow--solid-safe" id="ebsafe">Why HubSpot</p><div class="row" id="row">{card(1)}{card(2)}{card(3,link=False)}</div>
<section class="faq" aria-labelledby="faqh"><h2 id="faqh">FREQUENTLY ASKED QUESTIONS</h2><div class="eq-faq" id="faq">{items}</div></section>
<script type="application/ld+json">{ld}</script><div class="spacer"></div>__JS__</body></html>"""
open(os.path.join(TMP,'static.html'),'w').write(page.replace('__JS__',''))
open(os.path.join(TMP,'motion.html'),'w').write(page.replace('__JS__',f'<script src="file://{REPO}/components/motion.js"></script>'))
from playwright.sync_api import sync_playwright
R={}
def ok(n,c,d=''): R[n]=bool(c); print(("  PASS " if c else "  FAIL ")+n+(f"  — {d}" if d else ''))
TY="(s)=>{const m=getComputedStyle(document.querySelector(s)).transform;if(m==='none')return 0;const v=m.match(/-?[\\d.]+/g).map(Number);return v.length===6?v[5]:0}"
with sync_playwright() as p:
    b=p.chromium.launch()
    # ---------- no JS
    pg=b.new_page(viewport={'width':1200,'height':800}); pg.goto('file://'+TMP+'/static.html'); pg.wait_for_timeout(200)
    ok("C1 no JS: cards fully visible", pg.evaluate("[...document.querySelectorAll('.eq-card')].every(e=>getComputedStyle(e).opacity==='1')"))
    # ---------- eyebrow, measured against assets/components/eyebrow-*.svg
    EB="([s,p])=>getComputedStyle(document.querySelector(s))[p]"
    ok("E1 eyebrow: 12px / 700 / 0.2em, uppercase",
       pg.evaluate(EB,["#ebp","fontSize"])=="12px" and pg.evaluate(EB,["#ebp","fontWeight"])=="700"
       and pg.evaluate(EB,["#ebp","letterSpacing"]).startswith("2.4")
       and pg.evaluate(EB,["#ebp","textTransform"])=="uppercase",
       f'{pg.evaluate(EB,["#ebp","fontSize"])} / {pg.evaluate(EB,["#ebp","fontWeight"])} / {pg.evaluate(EB,["#ebp","letterSpacing"])}')
    ok("E2 eyebrow: orange label", pg.evaluate(EB,["#ebp","color"])=="rgb(224, 103, 48)",
       pg.evaluate(EB,["#ebp","color"]))
    ok("E3 solid: pale pill, 8px radius, 24px side padding",
       pg.evaluate(EB,["#ebs","backgroundColor"])=="rgb(252, 233, 224)"
       and pg.evaluate(EB,["#ebs","borderRadius"])=="8px"
       and pg.evaluate(EB,["#ebs","paddingLeft"])=="24px",
       f'{pg.evaluate(EB,["#ebs","backgroundColor"])} / {pg.evaluate(EB,["#ebs","borderRadius"])} / {pg.evaluate(EB,["#ebs","paddingLeft"])}')
    ok("E4 solid: 32px tall, matching the 115x32 export",
       abs(pg.evaluate("document.querySelector('#ebs').getBoundingClientRect().height")-32)<1,
       str(pg.evaluate("document.querySelector('#ebs').getBoundingClientRect().height")))
    ok("E5 plain: no pill behind it",
       pg.evaluate(EB,["#ebp","backgroundColor"]) in ("rgba(0, 0, 0, 0)","transparent"))
    ok("E6 solid-safe: label is the AA-passing text colour",
       pg.evaluate(EB,["#ebsafe","color"])=="rgb(36, 37, 48)", pg.evaluate(EB,["#ebsafe","color"]))
    ok("F0 no JS: FAQ works natively", pg.evaluate("(()=>{const d=document.querySelector('.eq-faq__item');d.querySelector('summary').click();return d.open})()"))
    pg.close()
    # ---------- motion
    pg=b.new_page(viewport={'width':1200,'height':800}); pg.goto('file://'+TMP+'/motion.html'); pg.wait_for_timeout(200)
    ok("C2 below fold: cards armed and hidden", pg.evaluate("[...document.querySelectorAll('.eq-card')].every(e=>e.classList.contains('eq-reveal')&&getComputedStyle(e).opacity==='0')"))
    pg.evaluate("document.getElementById('row').scrollIntoView({block:'center'})"); pg.wait_for_timeout(250)
    mid=pg.evaluate("[...document.querySelectorAll('.eq-card')].map(e=>parseFloat(getComputedStyle(e).opacity))")
    ok("C2 cards reveal in sequence", any(0<v<1 for v in mid) or mid[0]>mid[-1], f"opacities mid-entrance {[round(v,2) for v in mid]}")
    pg.wait_for_timeout(2200)
    ok("C2 after entrance: visible, reveal classes removed", pg.evaluate("[...document.querySelectorAll('.eq-card')].every(e=>getComputedStyle(e).opacity==='1'&&!e.classList.contains('eq-reveal'))"))
    ok("C4 hover has no leftover stagger delay", pg.evaluate("getComputedStyle(document.querySelector('#card2')).transitionDelay.split(',').every(d=>parseFloat(d)===0)"),
       pg.evaluate("getComputedStyle(document.querySelector('#card2')).transitionDelay"))
    pg.hover('#card1'); pg.wait_for_timeout(450)
    ok("C3 linked card lifts 6px on hover", abs(pg.evaluate(TY,'#card1')+6)<0.5, f"translateY {pg.evaluate(TY,'#card1')}")
    pg.hover('#card3'); pg.wait_for_timeout(450)
    ok("C3 unlinked card does NOT lift", pg.evaluate(TY,'#card3')==0)
    pg.mouse.move(5,5); pg.wait_for_timeout(800)
    pg.evaluate("document.querySelector('#card2 .eq-card__link').focus({focusVisible:true})"); pg.keyboard.press('Shift+Tab'); pg.keyboard.press('Tab'); pg.wait_for_timeout(450)
    focused=pg.evaluate("document.activeElement.closest('.eq-card')?.id")
    oc=pg.evaluate("getComputedStyle(document.querySelector('#'+document.activeElement.closest('.eq-card').id)).outlineStyle")
    ok("C5 keyboard focus lifts and outlines the card", focused and oc=='solid' and abs(pg.evaluate(TY,'#'+focused)+6)<0.5, f"{focused}, outline {oc}, y {pg.evaluate(TY,'#'+focused)}")
    # ---------- FAQ
    pg.evaluate("document.getElementById('faq').scrollIntoView({block:'center'})"); pg.wait_for_timeout(200)
    ok("F2 collapsed answers remain in the document", pg.evaluate("[...document.querySelectorAll('.eq-faq__answer')].every(a=>a.textContent.trim().length>40)"))
    H="document.querySelector('.eq-faq__item').getBoundingClientRect().height"
    closed=pg.evaluate(H); pg.focus('.eq-faq__question'); pg.keyboard.press('Enter')
    samples=[]
    for _ in range(10): pg.wait_for_timeout(50); samples.append(pg.evaluate(H))
    isopen=pg.evaluate("document.querySelector('.eq-faq__item').open")
    between=[s for s in samples if closed+2<s<samples[-1]-2]
    ok("F3 opening animates through intermediate heights", isopen and between, f"{round(closed)} -> {[round(s) for s in samples[:7]]}")
    ok("F1 Enter opens the item", isopen)

    rot=pg.evaluate("getComputedStyle(document.querySelector('.eq-faq__icon')).transform")
    ok("F4 chevron points up when open", rot.startswith('matrix(') and abs(float(re.findall(r'-?[\d.e-]+',rot)[1])+1)<0.01, rot)
    pg.keyboard.press(' '); pg.wait_for_timeout(500)
    ok("F1 Space closes it", not pg.evaluate("document.querySelector('.eq-faq__item').open"))
    cdp=pg.context.new_cdp_session(pg)
    def ax():
        for n in cdp.send('Accessibility.getFullAXTree')['nodes']:
            if n.get('name',{}).get('value','').startswith('What is GEO'):
                pr={x['name']:x['value'].get('value') for x in n.get('properties',[])}
                if 'expanded' in pr: return pr['expanded']
    closed_state=ax(); pg.keyboard.press('Enter'); pg.wait_for_timeout(400); open_state=ax(); pg.keyboard.press(' '); pg.wait_for_timeout(400)
    ok("F5 assistive tech hears expanded true/false", open_state is True and closed_state is False, f"closed={closed_state} open={open_state}")
    ld=json.loads(pg.evaluate("document.querySelector('script[type=\"application/ld+json\"]').textContent"))
    qs=[q['name'] for q in ld['mainEntity']]; vq=pg.evaluate("[...document.querySelectorAll('.eq-faq__question')].map(s=>s.firstChild.textContent.trim())")
    ok("F6 FAQPage JSON-LD valid and matches visible questions", ld['@type']=='FAQPage' and qs==vq)
    pg.close()
    # ---------- reduced motion
    c=b.new_context(reduced_motion='reduce',viewport={'width':1200,'height':800}); pg=c.new_page(); pg.goto('file://'+TMP+'/motion.html'); pg.wait_for_timeout(200)
    ok("C6 reduced motion: cards never hidden", pg.evaluate("[...document.querySelectorAll('.eq-card')].every(e=>getComputedStyle(e).opacity==='1')"))
    pg.evaluate("document.getElementById('row').scrollIntoView({block:'center'})"); pg.hover('#card1'); pg.wait_for_timeout(300)
    ok("C6 reduced motion: no lift, but shadow feedback remains", pg.evaluate(TY,'#card1')==0 and '34px' in pg.evaluate("getComputedStyle(document.querySelector('#card1')).boxShadow"))
    pg.evaluate("document.getElementById('faq').scrollIntoView()"); pg.click('.eq-faq__question')
    ok("F7 reduced motion: FAQ opens instantly", pg.evaluate("document.querySelector('.eq-faq__item').open"))
    c.close(); b.close()
print(f"\n{sum(R.values())}/{len(R)} passed")
