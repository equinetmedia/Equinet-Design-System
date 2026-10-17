#!/usr/bin/env python3
"""Regenerate assets/manifest.json from the SVG files themselves.

Run from the repo root after adding, renaming or editing any asset:
    python tools/build-manifest.py

The manifest is derived, never hand-edited. For each asset it records category,
dimensions, background, live-text count, data-role counts and palette mapped
to tokens; for illustrations and tiles the subject/topics from INDEX.md; for
charts the figures and sources from assets/charts/data.json.
"""
import glob, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

CATEGORY = {'illustrations': 'illustration', 'icons': 'icon', 'brand': 'brand',
            'buttons': 'button-source', 'comps': 'layout-blueprint',
            'marketing': 'style-reference', 'charts': 'chart',
            'backgrounds': 'background', 'components': 'component-source', 'type': 'type-spec'}
# Colours decided to be an existing token rather than a separate value.
FOLDED = {'#FFE6DB': '--equinet-color-orange--pale'}

tokens = open('tokens.css', encoding='utf-8').read()
hex2tok, sanctioned = {}, {}
for m in re.finditer(r'(--equinet-[a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})\b', tokens):
    h = m.group(2).upper()
    hex2tok.setdefault(h, m.group(1))
    # Status colours are reserved for UI state and must never be proposed as a
    # replacement for ink in artwork. Added to tokens.css 2026-10-16, and
    # without this they immediately out-competed amber-100 on two warm hexes
    # (chart-robotic-arms-roi -> caution--pale, marketing-hubspot-agents ->
    # danger--pale), which is nearest by RGB and wrong by meaning.
    STATUS = ('--equinet-color-success', '--equinet-color-caution',
              '--equinet-color-danger')
    if m.group(1).startswith('--equinet-color-') and not m.group(1).startswith(STATUS):
        sanctioned.setdefault(h, m.group(1))
hex2tok.setdefault('#FFFFFF', '--equinet-color-surface')

def rgb(h): return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
def nearest(h):
    r = rgb(h)
    best = min(sanctioned, key=lambda k: sum((a - b) ** 2 for a, b in zip(r, rgb(k))))
    return sanctioned[best], best

# Subject metadata from INDEX.md tables:  | `name` | depicts | topics |
meta = {}
idx = open('assets/illustrations/INDEX.md', encoding='utf-8').read()
for m in re.finditer(r'^\| `([a-z0-9-]+)` \| ([^|]+)\|(?: ([^|]+)\|)?', idx, re.M):
    name, a, b = m.group(1), m.group(2).strip(), (m.group(3) or '').strip()
    if b: meta[name] = {'depicts': a, 'topics': [t.strip() for t in b.split(',') if t.strip()]}
    else: meta[name] = {'topics': [t.strip() for t in a.split(',') if t.strip()]}

charts = {}
if os.path.exists('assets/charts/data.json'):
    for c in json.load(open('assets/charts/data.json'))['charts']:
        charts[c['file'][:-4]] = c

def background(svg, body, roles, W, H):
    if 'tile' in roles:
        return 'dark tile'
    if 'background' in roles:
        stops = re.findall(r'stop-color="(#[0-9A-Fa-f]{6})"', svg)
        return 'opaque light' if stops and stops[0].upper() in ('#F6F5F5', '#FFFFFF') else 'opaque dark'
    # Un-annotated files: look for a full-artboard rect directly.
    for m in re.finditer(r'<rect([^>]*)>', body):
        a = m.group(1)
        w = re.search(r'\swidth="([\d.]+)"', a); h = re.search(r'\sheight="([\d.]+)"', a)
        if not (w and h) or re.search(r'\s(x|y)="[1-9]', a): continue
        if abs(float(w.group(1)) - W) < 2 and abs(float(h.group(1)) - H) < 2:
            f = (re.search(r'fill="([^"]+)"', a) or [None, ''])[1].upper()
            # Light vs dark is a luminance question, not a whitelist one. The
            # old list of three literals called the pale #FCE9E0 eyebrow pill
            # "opaque dark" (2026-10-16). Same threshold as the gradient
            # branch below, so the two agree.
            if f == 'WHITE': return 'opaque light'
            if re.fullmatch(r'#[0-9A-F]{6}', f):
                return 'opaque light' if sum(rgb(f)) / 3 > 200 else 'opaque dark'
            if f.startswith('URL('):
                gid = re.search(r'URL\(#([^)]+)\)', f)
                g = re.search(r'id="' + re.escape(gid.group(1).lower() if gid else '') + r'"[\s\S]*?</(?:linear|radial)Gradient>', svg, re.I) if gid else None
                stops = re.findall(r'stop-color="(#[0-9A-Fa-f]{6}|white)"', g.group(0) if g else '', re.I)
                cols = ['#FFFFFF' if c.lower() == 'white' else c.upper() for c in stops]
                if cols:
                    lum = sum(sum(rgb(c)) / 3 for c in cols) / len(cols)
                    return 'opaque light' if lum > 200 else 'opaque dark'
                return 'opaque (gradient)'
            return 'opaque dark' if f else 'transparent'
    return 'transparent'

assets = []
for p in sorted(glob.glob('assets/**/*.svg', recursive=True)):
    s = open(p, encoding='utf-8').read()
    rel = p[len('assets/'):]; parts = rel.split('/')
    group = parts[1] if len(parts) > 2 else parts[0]
    vb = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', s)
    W, H = (float(vb.group(1)), float(vb.group(2))) if vb else (None, None)
    roles = {}
    for r in re.findall(r'data-role="([a-z]+)"', s): roles[r] = roles.get(r, 0) + 1
    d0 = s.find('<defs'); body = s[:d0] if d0 != -1 else s
    palette = []
    for h in sorted({x.upper() for x in re.findall(r'(?:fill|stroke|stop-color)="(#[0-9A-Fa-f]{6})"', s)}):
        e = {'hex': h, 'token': hex2tok.get(h)}
        if h in FOLDED:
            e.update(token=FOLDED[h], status='folded — treat as this token')
        elif not e['token']:
            t, hx = nearest(h); e.update(status='unsanctioned', nearest_token=t, nearest_hex=hx)
        palette.append(e)
    name = os.path.basename(p)[:-4]
    entry = {'name': name, 'path': p, 'category': CATEGORY[parts[0]], 'group': group,
             'width': W, 'height': H, 'aspect': round(W / H, 3) if W and H else None,
             'background': background(s, body, roles, W, H),
             'live_text': s.count('<text'), 'reworkable': bool(roles),
             'roles': roles, 'palette': palette}
    entry.update(meta.get(name, {}))
    if name in charts:
        c = charts[name]
        entry['chart'] = {'title': c['title'], 'form': c['form'],
                          'source': c.get('source_correct') or c.get('source_as_printed'),
                          'data': 'assets/charts/data.json',
                          'note': 'Figures are outlined in the SVG. Rebuild live from data.json; never retype from the artwork.'}
    assets.append(entry)

doc = {
    'schema': 'equinet-asset-manifest/1',
    'note': 'Generated by tools/build-manifest.py from the SVG files. Do not hand-edit.',
    'roles': {'background': 'full-artboard fill (opaque artwork)', 'tile': 'brand container behind an icon glyph',
              'card': 'content card', 'panel': 'pale grouping surface', 'connector': 'line or arrow linking elements',
              'node': 'circular point on a flow or loop', 'glyph': 'icon or pictographic line-work',
              'accent': 'the orange outcome/emphasis element — once per graphic',
              'data': 'chart-blue data element', 'shape': 'unclassified (usually invisible bounds)'},
    'palette_note': ("'unsanctioned' marks a colour found in artwork that is not a token; replace it with "
                     "nearest_token (by RGB distance — a suggestion, not a ruling) rather than carrying the raw hex forward."),
    'count': len(assets), 'assets': assets}
json.dump(doc, open('assets/manifest.json', 'w'), indent=2)
print(f"manifest: {len(assets)} assets")
