#!/usr/bin/env python3
"""Motion test — verifies components/motion.js + the GRAPHIC MOTION section of
components/bundle.css in a real headless browser.

Run from the repo root:
    pip install playwright pillow && python -m playwright install chromium
    python tests/motion-test.py

Checks: nothing hidden without JS; graphics armed but unrevealed below the
fold; self-animating artwork left alone; stroked connectors start fully
undrawn and genuinely draw; every element at rest afterwards; elements with an
SVG transform attribute never displaced; reduced motion never armed; and the
resting state matches the static artwork (max channel diff <= 4/255).
"""
import os, tempfile
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP=tempfile.mkdtemp(prefix="eq-motion-")
G=[('dh','systems/system-data-health-enrichment.svg'),('fb','systems/system-insight-feedback-loops.svg'),
   ('sys','systems/system-crm-erp-integration.svg'),('flow','flows/flow-content-operations.svg'),
   ('anim','sectors/sector-built-environment-animated.svg')]
body=''.join(f'<div class="g" id="{i}">{open(os.path.join(REPO,"assets/illustrations",n)).read()}</div>' for i,n in G)
def page(js): return f"""<!doctype html><html><head><link rel="stylesheet" href="file://{REPO}/tokens.css">
<link rel="stylesheet" href="file://{REPO}/components/bundle.css"><style>body{{margin:0}}.spacer{{height:1400px}}
.g{{width:900px}}.g svg{{width:100%;height:auto;display:block}}</style></head><body><div class="spacer"></div>
{body}<div class="spacer"></div>{js}</body></html>"""
open(os.path.join(TMP,'static.html'),'w').write(page(''))
open(os.path.join(TMP,'motion.html'),'w').write(page(f'<script src="file://{REPO}/components/motion.js"></script>'))
os.chdir(TMP)
from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops
R={}
def ok(n,c,d=''): R[n]=bool(c); print(("  PASS " if c else "  FAIL ")+n+(f"  — {d}" if d else ''))
IDS=['dh','fb','sys','flow']           # 'anim' excluded on purpose
BOXES='''()=>[...document.querySelectorAll('.g:not(#anim) [data-role][transform]')].map(e=>{const b=e.getBoundingClientRect();return [Math.round((b.x+scrollX)*10)/10,Math.round((b.y+scrollY)*10)/10,Math.round(b.width*10)/10,Math.round(b.height*10)/10]})'''
OPAC='''(sel)=>[...document.querySelectorAll(sel+' [data-role]')].map(e=>parseFloat(getComputedStyle(e).opacity))'''
def scroll(pg,i): pg.evaluate(f"document.getElementById('{i}').scrollIntoView()")
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1100,'height':800}); pg.goto('file://'+TMP+'/static.html'); pg.wait_for_timeout(300)
    ok("T1 no JS: every element visible", min(pg.evaluate(OPAC,'svg[data-asset]'))==1.0)
    sb=pg.evaluate(BOXES)
    for i in IDS: scroll(pg,i); pg.wait_for_timeout(100); pg.locator('#'+i).screenshot(path=f's_{i}.png')
    pg.close()

    pg=b.new_page(viewport={'width':1100,'height':800}); pg.goto('file://'+TMP+'/motion.html'); pg.wait_for_timeout(200)
    ok("T2 four graphics armed, none revealed", pg.evaluate("document.querySelectorAll('svg.eq-motion').length")==4 and pg.evaluate("document.querySelectorAll('svg.is-visible').length")==0)
    ok("Guard: self-animating sector left alone", pg.evaluate("!document.querySelector('#anim svg').classList.contains('eq-motion')"))
    nd=pg.evaluate("document.querySelectorAll('#dh [data-draw], #fb [data-draw]').length")
    ok("T8 stroked connectors marked for drawing", nd==20, f"{nd} of 20 expected")
    lens=pg.evaluate("[...document.querySelectorAll('#dh [data-draw]')].map(e=>getComputedStyle(e).strokeDashoffset)")
    ok("T8 hidden state: connectors fully undrawn", all(float(v.replace('px',''))>0 for v in lens), f"offsets e.g. {lens[:3]}")
    scroll(pg,'dh'); pg.wait_for_timeout(420)
    mid=[float(v.replace('px','')) for v in pg.evaluate("[...document.querySelectorAll('#dh [data-draw]')].map(e=>getComputedStyle(e).strokeDashoffset)")]
    full=[float(v.replace('px','')) for v in lens]
    drawing=sum(1 for m,f in zip(mid,full) if 0<m<f)
    ok("T8 connectors genuinely drawing mid-entrance", drawing>0, f"{drawing} part-drawn")
    for i in IDS: scroll(pg,i); pg.wait_for_timeout(2400)
    ok("T3 after entrance: every element visible", min(pg.evaluate(OPAC,'svg.eq-motion'))==1.0)
    ok("T3 dash properties cleaned up", pg.evaluate("document.querySelectorAll('[data-draw]').length")==0)
    ab=pg.evaluate(BOXES); same=sum(1 for x,y in zip(ab,sb) if x==y)
    ok("T4 transform-attribute elements not displaced", same==len(sb), f"{same}/{len(sb)} identical")
    for i in IDS: scroll(pg,i); pg.wait_for_timeout(100); pg.locator('#'+i).screenshot(path=f'a_{i}.png')
    pg.close()

    c=b.new_context(reduced_motion='reduce',viewport={'width':1100,'height':800}); pg=c.new_page()
    pg.goto('file://'+TMP+'/motion.html'); pg.wait_for_timeout(200)
    ok("T6 reduced motion: never armed, all visible", pg.evaluate("document.querySelectorAll('.eq-motion').length")==0 and min(pg.evaluate(OPAC,'svg[data-asset]'))==1.0)
    c.close(); b.close()
for i in IDS:
    a=Image.open(f's_{i}.png').convert('RGB'); z=Image.open(f'a_{i}.png').convert('RGB')
    dd=ImageChops.difference(a,z); px=dd.get_flattened_data() if hasattr(dd,'get_flattened_data') else dd.getdata()
    m=max(max(v) for v in px)
    ok(f"T5 {i}: end state matches static (max diff <= 4/255)", m<=4, "identical" if m==0 else f"max {m}/255 — below perception")
print(f"\n{sum(R.values())}/{len(R)} passed")
