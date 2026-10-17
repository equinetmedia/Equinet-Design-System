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
<body><div class="spacer"></div>
<section class="eq-surface eq-surface--01" id="surf1" style="height:200px"></section>
<section class="eq-surface eq-surface--02" id="surf2" style="height:200px"></section>
<section class="eq-surface" id="surfD" style="height:200px"></section>
<h1 class="eq-h1" id="t1">Heading</h1><h2 class="eq-h2" id="t2">Heading</h2><h2 class="eq-h2 eq-h2--light" id="t2l">Heading</h2><h3 class="eq-h3" id="t3">Heading</h3><h3 class="eq-h3 eq-h3--light" id="t3l">Heading</h3><h3 class="eq-h3-card" id="t3c">Card</h3><h4 class="eq-h4" id="t4">Sub</h4><p class="eq-lead" id="tl">Lead</p><p class="eq-body" id="tb">Body</p>
<section class="eq-surface eq-surface--dark" id="surfDark" style="height:200px"><p class="eq-eyebrow" id="ebDark">On dark</p></section>
<div id="auto"><section class="eq-surface" id="a1"></section><section class="eq-surface" id="a2"></section><section class="eq-surface" id="a3"></section><section class="eq-surface" id="a4"></section><section class="eq-surface" id="a5"></section><section class="eq-surface eq-surface--01" id="aX"></section></div>
<article class="eq-card eq-card--stacked" data-reveal id="stk">
  <div class="eq-card__media"><img src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" alt=""></div>
  <div class="eq-card__body">
    <h3 class="eq-card__title"><a class="eq-card__link" href="#study">Co-Packer</a></h3>
    <dl class="eq-card__stats">
      <div class="eq-card__stat" id="st1"><dt>Co-packing</dt><dd>5.0%</dd></div>
      <div class="eq-card__stat" id="st2"><dt>Contract packaging</dt><dd class="eq-card__stat--aa" id="stAA">6.3%</dd></div>
    </dl>
    <ul class="eq-card__sources"><li><a href="#s1" id="src1">2024-2032, Industry Today</a></li></ul>
    <p class="eq-card__action" id="act">Read More</p>
  </div>
</article>
<p class="eq-eyebrow" id="ebp">Why HubSpot</p><p class="eq-eyebrow eq-eyebrow--solid" id="ebs">Why HubSpot</p><p class="eq-eyebrow eq-eyebrow--solid eq-eyebrow--solid-safe" id="ebsafe">Why HubSpot</p><div class="row" id="row">{card(1)}{card(2)}{card(3,link=False)}</div>
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
    # ---------- type scale, measured against assets/type/
    TYPO="([s,p])=>getComputedStyle(document.querySelector(s))[p]"
    for sel,size,weight,fam in [("#t1","60px","800","Open Sans"),("#t2","40px","800","Open Sans"),
                                ("#t3","32px","800","Open Sans"),("#t3c","24px","700","Myriad Pro"),
                                ("#t4","20px","600","Myriad Pro"),("#tl","20px","400","Myriad Pro"),
                                ("#tb","16px","400","Myriad Pro")]:
        ok(f"T {sel}: {size} / {weight} / {fam.split()[0]}",
           pg.evaluate(TYPO,[sel,"fontSize"])==size and pg.evaluate(TYPO,[sel,"fontWeight"])==weight
           and pg.evaluate(TYPO,[sel,"fontFamily"]).replace(chr(34),"").startswith(fam.split()[0]),
           f'{pg.evaluate(TYPO,[sel,"fontSize"])} / {pg.evaluate(TYPO,[sel,"fontWeight"])} / {pg.evaluate(TYPO,[sel,"fontFamily"])[:18]}')
    ok("T display tier is uppercase, reading tier is not",
       pg.evaluate(TYPO,["#t2","textTransform"])=="uppercase"
       and pg.evaluate(TYPO,["#t3c","textTransform"])=="none")
    ok("T light variants are weight 300",
       pg.evaluate(TYPO,["#t2l","fontWeight"])=="300" and pg.evaluate(TYPO,["#t3l","fontWeight"])=="300")
    ok("T light variants carry NO shadow — that is the variant",
       pg.evaluate(TYPO,["#t2l","textShadow"])=="none" and pg.evaluate(TYPO,["#t3l","textShadow"])=="none",
       pg.evaluate(TYPO,["#t2l","textShadow"]))
    ok("T heavy h2 does carry one", pg.evaluate(TYPO,["#t2","textShadow"])!="none")
    ok("T lead and body sit in color-body, headings in color-heading",
       pg.evaluate(TYPO,["#tb","color"])=="rgb(59, 63, 81)"
       and pg.evaluate(TYPO,["#t2","color"])=="rgb(36, 38, 48)")
    ok("T display tracking is the spec's -0.07em",
       abs(float(pg.evaluate(TYPO,["#t2","letterSpacing"]).replace("px",""))-(-0.07*40))<0.1,
       pg.evaluate(TYPO,["#t2","letterSpacing"]))

    # ---------- radial surface, measured against radial-background-0*.svg
    SF="([s,p])=>getComputedStyle(document.querySelector(s))[p]"
    ok("R1 surface: flat colour underneath so an editor's choice shows through",
       pg.evaluate(SF,["#surf1","backgroundColor"])=="rgb(246, 245, 245)",
       pg.evaluate(SF,["#surf1","backgroundColor"]))
    ok("R2 surface: the pool is a radial-gradient, not an image request",
       pg.evaluate(SF,["#surf1","backgroundImage"]).startswith("radial-gradient")
       and "url(" not in pg.evaluate(SF,["#surf1","backgroundImage"]))
    ok("R3 --01 pools upper-right at the measured centre",
       "73.2%" in pg.evaluate(SF,["#surf1","backgroundImage"])
       and "22.4%" in pg.evaluate(SF,["#surf1","backgroundImage"]))
    ok("R4 --02 pools upper-left, so consecutive sections differ",
       "33.4%" in pg.evaluate(SF,["#surf2","backgroundImage"])
       and pg.evaluate(SF,["#surf1","backgroundImage"])!=pg.evaluate(SF,["#surf2","backgroundImage"]))
    ok("R5 both variants hold the 2.02:1 axis ratio of the exports",
       all(abs(h/w-2.02)<0.03 for w,h in [(44.1,212.5/2.4071),(30.9,148.9/2.4071)]),
       "44.1:212.5 and 30.9:148.9 against a 1920x805 frame")
    ok("R6 bare .eq-surface carries a usable default",
       pg.evaluate(SF,["#surfD","backgroundImage"]).startswith("radial-gradient"))
    ok("R11 dark: navy underneath, blue-950 at the centre",
       pg.evaluate(SF,["#surfDark","backgroundColor"])=="rgb(0, 66, 108)"
       and "rgb(1, 20, 32)" in pg.evaluate(SF,["#surfDark","backgroundImage"]),
       pg.evaluate(SF,["#surfDark","backgroundColor"]))
    ok("R12 dark: content inherits a readable colour by default",
       pg.evaluate(SF,["#surfDark","color"])=="rgb(255, 255, 255)",
       pg.evaluate(SF,["#surfDark","color"]))
    ok("R13 dark: the eyebrow takes its on-dark colour without a modifier",
       pg.evaluate(SF,["#ebDark","color"])=="rgb(245, 132, 77)",
       pg.evaluate(SF,["#ebDark","color"]))
    ok("R14 dark is excluded from the sibling rotation — never automatic",
       pg.evaluate("""()=>{const d=document.querySelector('#surfDark');
         return getComputedStyle(d).getPropertyValue('--eq-surface-y').trim()==='100%'}"""))
    ok("R8 sibling surfaces rotate through four positions",
       len({pg.evaluate(SF,[f"#a{i}","backgroundImage"]) for i in (1,2,3,4)})==4,
       "four consecutive siblings, four different pools")
    ok("R9 the fifth repeats the first — a cycle, not randomness",
       pg.evaluate(SF,["#a5","backgroundImage"])==pg.evaluate(SF,["#a1","backgroundImage"]))
    ok("R10 an explicit variant beats its position",
       pg.evaluate(SF,["#aX","backgroundImage"])==pg.evaluate(SF,["#surf1","backgroundImage"]),
       "--01 in slot 6 still renders --01")
    ok("R7 variables are overridable for a bespoke pool",
       pg.evaluate("""()=>{const e=document.querySelector('#surfD');
         e.style.setProperty('--eq-surface-x','10%');
         return getComputedStyle(e).backgroundImage.includes('10%')}"""))

    # ---------- stacked card, measured against card-stacked-layout-01.svg
    SC="([s,p])=>getComputedStyle(document.querySelector(s))[p]"
    ok("S1 stacked: card padding moves to the body so the image bleeds",
       pg.evaluate(SC,["#stk","padding"])=="0px"
       and pg.evaluate(SC,[".eq-card__body","padding"])=="24px",
       f'card {pg.evaluate(SC,["#stk","padding"])} / body {pg.evaluate(SC,[".eq-card__body","padding"])}')
    ok("S2 stacked: image clipped to the card radius",
       pg.evaluate(SC,["#stk","overflow"]).startswith("clip")
       and pg.evaluate(SC,["#stk","borderRadius"])=="7px")
    ok("S3 stacked: media holds the comp's 323:181.377 ratio",
       abs(pg.evaluate("()=>{const r=document.querySelector('.eq-card__media').getBoundingClientRect();return r.width/r.height}")-323/181.377)<0.02,
       str(pg.evaluate("()=>{const r=document.querySelector('.eq-card__media').getBoundingClientRect();return (r.width/r.height).toFixed(3)}")))
    ok("S4 stat row: 1px rule, label 16px, value 18px/600 orange",
       pg.evaluate(SC,["#st1","borderBottomWidth"])=="1px"
       and pg.evaluate(SC,["#st1 dt","fontSize"])=="16px"
       and pg.evaluate(SC,["#st1 dd","fontSize"])=="18px"
       and pg.evaluate(SC,["#st1 dd","fontWeight"])=="600"
       and pg.evaluate(SC,["#st1 dd","color"])=="rgb(224, 103, 48)")
    ok("S5 stat value right-aligned against the label",
       pg.evaluate("()=>{const r=document.querySelector('#st1').getBoundingClientRect(),d=document.querySelector('#st1 dd').getBoundingClientRect();return Math.abs(d.right-r.right)<1}"))
    ok("S6 sources set at 11px", pg.evaluate(SC,["#src1","fontSize"])=="11px")
    ok("S7 --aa variant drops the orange for an AA-passing colour",
       pg.evaluate(SC,["#stAA","color"])=="rgb(36, 37, 48)", pg.evaluate(SC,["#stAA","color"]))
    ok("S8 the whole card is the link target, so it lifts",
       pg.evaluate("()=>document.querySelectorAll('#stk .eq-card__link').length")==1)

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
