"""Build the typeset Persian PDF of the handbook.

Pipeline
  1. Read enterprise-ai-strategy-and-implementation-handbook-fa.md (built by assemble_fa.py).
  2. Render every Mermaid diagram to SVG in headless Chrome with the Vazirmatn font. Flowcharts are
     rendered in two orientations; the one that displays larger on the page is kept.
  3. Size every figure to the text block: never upscaled, shrunk only as far as needed to fit the
     page width and a maximum height, centred.
  4. Convert the Markdown to a book-structured HTML document (cover, title page, copyright page,
     contents, chapter openers, running heads, Persian page numbers) and print it with Chrome.
  5. Two passes: the first finds the page of every section, the second writes those numbers into
     the contents.

Requirements: Python 'pypdf'; Google Chrome; network access on first run to fetch mermaid@11.4.1,
marked@12.0.2 (Markdown to HTML, run inside Chrome) and Vazirmatn 33.0.3 (SIL Open Font License)
into the work directory.
Usage:  python build_pdf_fa.py            (PDF_WORK env var overrides the work directory)
"""
from pathlib import Path
import base64, html, json, os, re, subprocess, sys, urllib.request
from pypdf import PdfReader

P = Path(__file__).parent
WORK = Path(os.environ.get('PDF_WORK', P / 'pdf-build'))
VENDOR = WORK / 'vendor'
CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')
SRC = P / 'enterprise-ai-strategy-and-implementation-handbook-fa.md'
OUT = P / 'enterprise-ai-strategy-and-implementation-handbook-fa.pdf'
REPO = 'https://github.com/pirayeah/ai-implementation-handbook'
ASSETS = {
    'mermaid.min.js': 'https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js',
    'marked.min.js': 'https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js',
    'Vazirmatn.woff2': 'https://cdn.jsdelivr.net/npm/vazirmatn@33.0.3/fonts/webfonts/Vazirmatn%5Bwght%5D.woff2',
}
# Geometry (CSS px, 96 per inch). A4 with 20 mm side margins -> 642 px text block.
FIG_W = 626          # widest figure, leaving the frame padding inside the text block
FIG_H = 820          # tallest figure (about 217 mm), leaving room for a caption
LAND_W, LAND_H = 940, 520   # figure box on a landscape A4 page (257 x 164 mm text block, minus frame and caption)
LAND_BELOW = 0.62    # a figure that would print smaller than this goes on its own landscape page ...
LAND_GAIN = 1.2      # ... if that makes it at least 20% larger
NAVY, GOLD, INK, MUTED = '#1B3A63', '#B8892D', '#1A2433', '#66758C'
FA = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

WORK.mkdir(parents=True, exist_ok=True); VENDOR.mkdir(exist_ok=True)
for name, url in ASSETS.items():
    if not (VENDOR / name).exists():
        urllib.request.urlretrieve(url, VENDOR / name)
FONT_B64 = base64.b64encode((VENDOR / 'Vazirmatn.woff2').read_bytes()).decode()
FONT_FACE = ("@font-face{font-family:'Vazirmatn';src:url(data:font/woff2;base64,%s) format('woff2');"
             "font-weight:100 900;font-style:normal}" % FONT_B64)


def chrome(args, timeout=600):
    prof = WORK / 'chrome-profile'
    cmd = [CHROME, '--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
           '--disable-extensions', f'--user-data-dir={prof}'] + args
    return subprocess.run(cmd, capture_output=True, timeout=timeout)


# ------------------------------------------------------------------ 1. source
text = SRC.read_text(encoding='utf-8')
text = re.sub(r'^<div dir="rtl" lang="fa">\s*', '', text).rsplit('</div>', 1)[0]
text = text.replace('](handbook-evidence-companion.md)', f']({REPO}/blob/main/handbook-evidence-companion.md)')
text = text.replace('](../handbook-evidence-companion.md)', f']({REPO}/blob/main/handbook-evidence-companion.md)')

figs = []                                  # mermaid sources in document order


def grab(m):
    figs.append(m.group(1).strip())
    return f'\n\n@@FIG{len(figs) - 1}@@\n\n'


text = re.sub(r'```mermaid\n(.*?)```', grab, text, flags=re.S)


# ------------------------------------------------------------------ sections
parts = re.split(r'<a id="([\w-]+)"></a>', text)
sections = [('preface', parts[0])] + [(parts[j], parts[j + 1]) for j in range(1, len(parts), 2)]
ORDINAL = {'a': 'الف', 'b': 'ب', 'c': 'ج', 'd': 'د'}
secs, toc = [], []
for sid, body in sections:
    body = re.sub(r'^\s*---\s*$', '', body, flags=re.M).strip()
    if sid == 'preface':
        body = re.sub(r'^# .*\n+## .*\n', '', body)
        body = re.sub(r'### فهرست مطالب\n.*?(?=\n\nفهرست کامل)', '', body, flags=re.S)
        label, title, kind = '', 'پیش‌گفتار', 'front'
    else:
        first = re.match(r'(#+)\s+(.*)\n', body)
        heading, body = first.group(2).strip(), body[first.end():]
        if sid.startswith('ch'):
            num, title = re.match(r'([۰-۹]+)\.\s+(.*)', heading).groups()
            label, kind = f'فصل {num}', 'chapter'
            body = re.sub(r'^#### ', '### ', re.sub(r'^### ', '## ', body, flags=re.M), flags=re.M)
        elif sid.startswith('appendix'):
            letter = ORDINAL[sid[-1]]
            title = heading.split('—', 1)[1].strip()
            label, kind = f'پیوست {letter}', 'appendix'
        else:
            label, title, kind = '', heading, 'front'
            body = re.sub(r'^### ', '## ', body, flags=re.M)
    secs.append({'id': sid, 'label': label, 'title': title, 'kind': kind, 'md': body})
    toc.append((sid, label, title, kind))


# ------------------------------------------------------------------ 2. render diagrams
DECISION = re.compile(r'(?<![\w{])([A-Za-z]\w*)\{(?!\{)"(.*?)"\}(?!\})')


def compact_decisions(code):
    """Rhombus nodes grow with the square of their text; draw decisions as gold-tinted rounded boxes."""
    ids = []

    def sub(m):
        ids.append(m.group(1))
        return f'{m.group(1)}("{m.group(2)}")'

    code = DECISION.sub(sub, code)
    if ids:
        code += ('\n    classDef decision fill:#FBF4E2,stroke:#B8892D,stroke-width:1.4px,color:#1A2433'
                 f'\n    class {",".join(dict.fromkeys(ids))} decision')
    return code


def variants(code):
    head = code.split('\n', 1)[0].strip()
    m = re.match(r'(flowchart|graph)\s+(LR|RL|TD|TB|BT)\b', head)
    if m:
        code = compact_decisions(code)
    out = {'o': code}
    if m and not re.search(r'^\s*direction\s', code, re.M):   # authored row layouts keep their orientation
        alt = 'TB' if m.group(2) in ('LR', 'RL') else 'RL'
        out['a'] = re.sub(r'^(flowchart|graph)\s+\w+', r'\1 ' + alt, code, count=1)
    if head.startswith('gantt'):
        out['o'] = gantt_rtl(code)
    if head.startswith('pie'):
        out['o'] = re.sub(r'^(\s*)"([^"]+)"(\s*:)', lambda m: f'{m.group(1)}"{RLI}{m.group(2)}{PDI}"{m.group(3)}', code, flags=re.M)
        out['o'] = re.sub(r'^(\s*title\s+)(.+)$', lambda m: f'{m.group(1)}{RLI}{m.group(2).strip()}{PDI}', out['o'], flags=re.M)
    return out


RLI, PDI = '⁧', '⁩'


def gantt_rtl(code):
    """Gantt geometry is left-to-right (time axis); keep its SVG text LTR-anchored and isolate each Persian
    label as a right-to-left run. Axis ticks show bare numbers (the title names the unit)."""
    out = []
    for line in code.split('\n'):
        s = line.strip()
        if s.startswith('axisFormat'):
            fmt = re.search(r'%-?(\w)', s).group(1)
            line = f'    axisFormat %-{fmt}'
        elif s.startswith(('title ', 'section ')):
            key, txt = s.split(' ', 1)
            line = f'    {key} {RLI}{txt.strip()}{PDI}'
        elif ':' in s and not s.startswith(('dateFormat', 'gantt')):
            name, rest = s.split(':', 1)
            line = f'    {RLI}{name.strip()}{PDI} :{rest}'
        out.append(line)
    return '\n'.join(out)


defs = {f'{i}{k}': v for i, c in enumerate(figs) for k, v in variants(c).items()}
mm_conf = {
    'startOnLoad': False, 'securityLevel': 'loose', 'theme': 'base', 'fontFamily': 'Vazirmatn',
    'themeVariables': {
        'fontFamily': 'Vazirmatn', 'fontSize': '15px', 'primaryColor': '#EEF2F8', 'primaryBorderColor': NAVY,
        'primaryTextColor': INK, 'secondaryColor': '#FBF4E2', 'secondaryBorderColor': GOLD,
        'tertiaryColor': '#FFFFFF', 'tertiaryBorderColor': '#C9D2DF', 'lineColor': '#7D8BA0',
        'clusterBkg': '#FAFBFD', 'clusterBorder': GOLD, 'edgeLabelBackground': '#FFFFFF', 'titleColor': NAVY,
        'pie1': NAVY, 'pie2': GOLD, 'pie3': '#4F74A8', 'pie4': '#E2C47A', 'pie5': '#8FA6C6',
        'pie6': '#8A6620', 'pie7': '#B9C6D9', 'pie8': '#F1E3BC', 'pieStrokeColor': '#FFFFFF',
        'pieStrokeWidth': '1.5px', 'pieOuterStrokeWidth': '0px', 'pieSectionTextColor': '#FFFFFF',
        'pieTitleTextSize': '17px', 'pieLegendTextSize': '14px', 'pieSectionTextSize': '13px',
        'taskBkgColor': NAVY, 'taskBorderColor': NAVY, 'taskTextColor': '#FFFFFF',
        'taskTextOutsideColor': INK, 'taskTextDarkColor': INK, 'taskTextLightColor': '#FFFFFF',
        'sectionBkgColor': '#F3F5F9', 'altSectionBkgColor': '#FFFFFF', 'sectionBkgColor2': '#FBF6EA',
        'gridColor': '#E1E6EE', 'todayLineColor': 'transparent', 'critBkgColor': GOLD,
        'activeTaskBkgColor': GOLD, 'activeTaskBorderColor': GOLD, 'doneTaskBkgColor': '#8FA6C6',
        'quadrant1Fill': '#E6ECF5', 'quadrant2Fill': '#FBF4E2', 'quadrant3Fill': '#F6F7FA',
        'quadrant4Fill': '#F3EEE2', 'quadrantPointFill': NAVY, 'quadrantPointTextFill': INK,
        'quadrantTitleFill': NAVY, 'quadrantXAxisTextFill': INK, 'quadrantYAxisTextFill': INK,
        'quadrant1TextFill': NAVY, 'quadrant2TextFill': '#7A5A12', 'quadrant3TextFill': MUTED,
        'quadrant4TextFill': '#7A5A12', 'quadrantInternalBorderStrokeFill': '#C9D2DF',
        'quadrantExternalBorderStrokeFill': NAVY,
        'xyChart': {'plotColorPalette': NAVY, 'titleColor': NAVY, 'xAxisLabelColor': INK,
                    'yAxisLabelColor': INK, 'xAxisTitleColor': INK, 'yAxisTitleColor': INK,
                    'xAxisLineColor': '#9AA7B8', 'yAxisLineColor': '#9AA7B8', 'xAxisTickColor': '#9AA7B8',
                    'yAxisTickColor': '#9AA7B8', 'backgroundColor': '#FFFFFF'},
    },
    'flowchart': {'useMaxWidth': False, 'htmlLabels': True, 'curve': 'basis', 'nodeSpacing': 30,
                  'rankSpacing': 40, 'padding': 12, 'diagramPadding': 10, 'wrappingWidth': 380},
    'gantt': {'useMaxWidth': False, 'useWidth': FIG_W, 'barHeight': 24, 'barGap': 7, 'topPadding': 46,
              'leftPadding': 150, 'rightPadding': 24, 'gridLineStartPadding': 30, 'fontSize': 13,
              'sectionFontSize': 13, 'numberSectionStyles': 2},
    'pie': {'useMaxWidth': False, 'textPosition': 0.7},
    'quadrantChart': {'useMaxWidth': False, 'chartWidth': 540, 'chartHeight': 470, 'titleFontSize': 17,
                      'pointLabelFontSize': 13, 'quadrantLabelFontSize': 14, 'xAxisLabelFontSize': 14,
                      'yAxisLabelFontSize': 14},
    'xyChart': {'useMaxWidth': False, 'width': 600, 'height': 430, 'titleFontSize': 17},
    'themeCSS': '.nodeLabel,.edgeLabel,.cluster-label,.label{direction:rtl;unicode-bidi:plaintext;line-height:1.55}'
                '.edgeLabel{font-size:13px}',
}
render_html = f"""<!doctype html><html dir="rtl" lang="fa"><head><meta charset="utf-8">
<style>{FONT_FACE} body{{font-family:Vazirmatn;margin:0}} #box{{width:{FIG_W}px}}
.nodeLabel,.edgeLabel,.cluster-label,.label{{direction:rtl;unicode-bidi:plaintext;line-height:1.55}} svg[aria-roledescription="gantt"] text, svg[aria-roledescription="pie"] text{{direction:ltr}}</style>
<script>{(VENDOR / 'mermaid.min.js').read_text(encoding='utf-8')}</script>
<script>{(VENDOR / 'marked.min.js').read_text(encoding='utf-8')}</script></head>
<body><div id="box"></div><div id="out"></div><script>
const defs = {json.dumps(defs, ensure_ascii=False)};
const mds = {json.dumps({s['id']: s['md'] for s in secs}, ensure_ascii=False)};
(async () => {{
  const mdOut = {{}};
  for (const [k, src] of Object.entries(mds)) mdOut[k] = marked.parse(src, {{gfm: true, breaks: false}});
  await document.fonts.load('400 15px Vazirmatn'); await document.fonts.load('700 15px Vazirmatn');
  await document.fonts.ready;
  mermaid.initialize({json.dumps(mm_conf, ensure_ascii=False)});
  const res = {{}};
  for (const [k, code] of Object.entries(defs)) {{
    try {{ const r = await mermaid.render('mm' + k, code, document.getElementById('box')); res[k] = {{svg: r.svg}}; }}
    catch (e) {{ res[k] = {{error: String(e)}}; }}
  }}
  const bytes = new TextEncoder().encode(JSON.stringify({{figs: res, md: mdOut}}));
  let bin = ''; for (const b of bytes) bin += String.fromCharCode(b);
  document.getElementById('out').textContent = 'B64:' + btoa(bin) + ':END';
}})();
</script></body></html>"""
(WORK / 'render.html').write_text(render_html, encoding='utf-8')
r = chrome(['--virtual-time-budget=240000', '--dump-dom', (WORK / 'render.html').as_uri()], timeout=900)
m = re.search(r'B64:([A-Za-z0-9+/=]+):END', r.stdout.decode('utf-8', 'replace'))
if not m:
    sys.exit('Diagram rendering failed:\n' + r.stderr.decode('utf-8', 'replace')[-3000:])
payload = json.loads(base64.b64decode(m.group(1)).decode('utf-8'))
rendered, md_html = payload['figs'], payload['md']
errors = {k: v['error'] for k, v in rendered.items() if 'error' in v and k.endswith('o')}
if errors:
    sys.exit('Mermaid errors: ' + json.dumps(errors, ensure_ascii=False)[:3000])


def box(svg):
    vb = re.search(r'viewBox="([-\d.]+)[ ,]+([-\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)"', svg)
    return float(vb.group(3)), float(vb.group(4))


def scale(w, h, W=FIG_W, H=FIG_H):
    return min(1.0, W / w, H / h)


def persian_text(svg):  # Persian digits in SVG <text> (axis ticks, pie values); HTML labels already Persian
    return re.sub(r'(<(?:text|tspan)\b[^>]*>)([^<]*)', lambda t: t.group(1) + t.group(2).translate(FA), svg)


def gantt_svg(code):
    """Right-to-left timeline for the Persian book: label column on the right, time running leftwards,
    section header rows, navy bars, gold milestones, Persian numerals. Reads the Mermaid gantt subset used
    in the handbook (dateFormat YYYY-MM-DD; 'id, start, Nd' / 'id, after x, Nd' / 'milestone, id, date, 0d')."""
    from datetime import date, timedelta
    title, axis, rows, tasks = '', 'روز %j', [], {}
    for line in code.split('\n')[1:]:
        s = line.strip()
        if not s or s.startswith('dateFormat'):
            continue
        if s.startswith('title '):
            title = s[6:].strip(); continue
        if s.startswith('axisFormat'):
            axis = s.split(None, 1)[1].strip(); continue
        if s.startswith('section '):
            rows.append(('section', s[8:].strip())); continue
        name, spec = s.rsplit(':', 1)
        toks = [t.strip() for t in spec.split(',')]
        milestone = 'milestone' in toks
        toks = [t for t in toks if t not in ('milestone', 'crit', 'done', 'active')]
        tid = toks[0] if len(toks) == 3 else None
        start_tok, dur_tok = toks[-2], toks[-1]
        start = tasks[start_tok.split()[1]][1] if start_tok.startswith('after ') else date.fromisoformat(start_tok)
        end = start + timedelta(days=int(dur_tok.rstrip('d')))
        tasks[tid or f'_{len(tasks)}'] = (start, end)
        rows.append(('milestone' if milestone else 'task', name.strip(), start, end))
    t0 = min(r[2] for r in rows if r[0] != 'section')
    t1 = max(r[3] for r in rows if r[0] != 'section')
    unit = re.sub(r'%-?\w', '', axis).strip()
    span = (t1 - t0).days
    W, LABEL_W, PAD, ROW, HEAD = FIG_W, 272, 8, 25, 26
    x_right, x_left = W - LABEL_W - 16, PAD + 4
    fx = lambda d: x_right - ((d - t0).days / span) * (x_right - x_left)
    out, y = [], 0
    if title:
        out.append(f'<text x="{W / 2}" y="20" text-anchor="middle" style="direction:rtl" font-size="15" font-weight="700" fill="{NAVY}">{html.escape(title)}</text>')
        y = 34
    # axis ticks
    if 'j' in axis:
        step = 7 if span <= 120 else 14
        ticks = [(t0 + timedelta(days=d), str(d + 1)) for d in range(0, span + 1, step)]
    elif 'W' in axis:
        ticks = [(t0 + timedelta(days=d), str(d // 7 + 1)) for d in range(0, span + 1, 7)]
    else:
        ticks, d = [], t0
        while d <= t1:
            ticks.append((d, str(d.month))); d = date(d.year + (d.month == 12), d.month % 12 + 1, 1)
    axis_y = y + 16
    out.append(f'<text x="{x_right + 18}" y="{axis_y}" text-anchor="end" style="direction:rtl" font-size="11" font-weight="700" fill="{MUTED}">{html.escape(unit)}</text>')
    for d, lab in ticks:
        out.append(f'<text x="{fx(d):.1f}" y="{axis_y}" text-anchor="middle" font-size="10.5" fill="{MUTED}">{lab.translate(FA)}</text>')
    grid_top = axis_y + 8
    y = grid_top + 4
    body = []
    band = 0
    for r in rows:
        if r[0] == 'section':
            band += 1
            body.append(f'<rect x="{PAD}" y="{y}" width="{W - 2 * PAD}" height="{HEAD}" fill="#FBF6EA"/>')
            body.append(f'<text x="{W - PAD - 8}" y="{y + 17}" text-anchor="start" style="direction:rtl" font-size="12" font-weight="700" fill="#8A6620">{html.escape(r[1])}</text>')
            y += HEAD
            continue
        kind, name, a, b = r
        body.append(f'<line x1="{PAD}" x2="{W - PAD}" y1="{y + ROW}" y2="{y + ROW}" stroke="#EEF1F5" stroke-width="0.8"/>')
        body.append(f'<text x="{W - PAD - 8}" y="{y + 16.5}" text-anchor="start" style="direction:rtl" font-size="11" fill="{INK}">{html.escape(name)}</text>')
        if kind == 'milestone':
            cx, cy = fx(a), y + ROW / 2
            body.append(f'<path d="M{cx:.1f} {cy - 7} L{cx + 7:.1f} {cy} L{cx:.1f} {cy + 7} L{cx - 7:.1f} {cy} Z" fill="{GOLD}" stroke="#fff" stroke-width="1.2"/>')
        else:
            xa, xb = fx(a), fx(b)
            body.append(f'<rect x="{xb:.1f}" y="{y + 6}" width="{xa - xb:.1f}" height="13" rx="3" fill="{NAVY}"/>')
        y += ROW
    grid = [f'<line x1="{fx(d):.1f}" x2="{fx(d):.1f}" y1="{grid_top}" y2="{y}" stroke="#E1E6EE" stroke-width="0.8"/>' for d, _ in ticks]
    sep = f'<line x1="{x_right + 8}" x2="{x_right + 8}" y1="{grid_top}" y2="{y}" stroke="#C9D2DF" stroke-width="1"/>'
    H = y + 6
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Vazirmatn">'
           + ''.join(grid) + sep + ''.join(body) + ''.join(out) + '</svg>')
    return svg, W, H


fig_html, fig_report = [], []
for i in range(len(figs)):
    cands = []
    if figs[i].startswith('gantt'):
        sv, w, h = gantt_svg(figs[i]); cands.append((scale(w, h), 'o', w, h, sv))
    for k in ('o', 'a'):
        v = rendered.get(f'{i}{k}')
        if not cands and v and 'svg' in v:
            w, h = box(v['svg']); cands.append((scale(w, h), k, w, h, v['svg']))
        elif cands and k == 'a' and v and 'svg' in v and not figs[i].startswith('gantt'):
            w, h = box(v['svg']); cands.append((scale(w, h), k, w, h, v['svg']))
    s0 = cands[0][0]
    best = max(cands, key=lambda c: c[0])
    if best[1] != 'o' and best[0] < s0 * 1.12:      # keep authored orientation unless clearly better
        best = cands[0]
    s, k, w, h, svg = best
    wide = False
    if s < LAND_BELOW:
        land = max(((scale(c[2], c[3], LAND_W, LAND_H), c[1], c[2], c[3], c[4]) for c in cands), key=lambda c: c[0])
        if land[0] >= s * LAND_GAIN:
            s, k, w, h, svg = land; wide = True
    svg = re.sub(r'\sstyle="max-width:[^"]*"', '', svg, count=1)
    svg = re.sub(r'<svg\b', f'<svg width="{w * s:.1f}" height="{h * s:.1f}"', svg, count=1)
    svg = re.sub(r'(<svg[^>]*?)\swidth="100%"', r'\1', svg, count=1)
    fig_html.append({'svg': persian_text(svg), 'wide': wide})
    fig_report.append({'fig': i + 1, 'type': figs[i].split()[0], 'orientation': 'authored' if k == 'o' else 'flipped',
                       'page': 'landscape' if wide else 'inline',
                       'natural_px': [round(w), round(h)], 'scale': round(s, 2),
                       'candidates': {c[1]: [round(c[2]), round(c[3]), round(c[0], 2)] for c in cands}})

# ------------------------------------------------------------------ 3. sections
CITE = re.compile(r'\[((?:[^\[\]<>]|</?strong>)*?(?:\bD\d{2}\b|\bE\d{2}\b|FINOS|\bA0\d\b|توصیه‌های منبع|توصیهٔ منبع)(?:[^\[\]<>]|</?strong>)*?)\]')


def figure(n, caption, sid):
    f = fig_html[int(n)]
    cls = f' class="wide pw-{sid}"' if f['wide'] else ''
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    return f'<figure{cls}>{f["svg"]}{cap}</figure>'


def polish(h, sid):
    h = re.sub(r'<p>@@FIG(\d+)@@</p>\s*<p>(<em>.*?)</p>', lambda m: figure(m.group(1), m.group(2), sid), h, flags=re.S)
    h = re.sub(r'<p>@@FIG(\d+)@@</p>', lambda m: figure(m.group(1), '', sid), h)
    parts_ = re.split(r'(<svg.*?</svg>|<code>.*?</code>)', h, flags=re.S)   # never touch SVG or code
    for n in range(0, len(parts_), 2):
        parts_[n] = CITE.sub(lambda m: f'<span class="cite" dir="auto">[{m.group(1)}]</span>', parts_[n])
    h = ''.join(parts_)
    h = re.sub(r'<p><strong>(پیش‌فرض آغازین[^<]*)</strong>', r'<p class="note-default"><strong>\1</strong>', h)
    h = re.sub(r'<p><strong>(رویهٔ مستند:|اختلاف نظر منابع:)</strong>', r'<p class="note-practice"><strong>\1</strong>', h)
    h = re.sub(r'<p><strong>(نشانه‌های شکست[^<]*)</strong>', r'<p class="note-fail"><strong>\1</strong>', h)
    h = re.sub(r'<table>\s*<thead>\s*<tr>\s*<th>کارت فصل</th>\s*<th></th>\s*</tr>\s*</thead>',
               '<table class="card"><caption>کارت فصل</caption>', h)
    h = re.sub(r'<h([23])>((?:[۰-۹]+|الف|ب|ج|د)\.[۰-۹]+)\s', r'<h\1><span class="num">\2</span> ', h)
    h = re.sub(r'<a href="(https?://[^"]+)">', r'<a class="ext" href="\1">', h)
    return h


for s in secs:
    s['html'] = polish(md_html[s['id']], s['id'])

# ------------------------------------------------------------------ 4. book HTML
def esc_css(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')


TITLE = 'راهنمای راهبرد و پیاده‌سازی هوش مصنوعی در سازمان'
SUBTITLE = 'از هدف کسب‌وکار تا بهره‌برداری پایدار'

page_rules = []
for s in secs:
    head = f"{s['label']} · {s['title']}" if s['label'] else s['title']
    page_rules.append(f'@page p-{s["id"]} {{ @top-center {{ content: "{esc_css(head)}"; }} }}')
    page_rules.append(f'.sec-{s["id"]} {{ page: p-{s["id"]}; }}')
    page_rules.append(f'@page w-{s["id"]} {{ size: A4 landscape; @top-center {{ content: "{esc_css(head)}"; }} }}')
    page_rules.append(f'figure.pw-{s["id"]} {{ page: w-{s["id"]}; }}')

CSS = f"""{FONT_FACE}
@page {{ size: A4; margin: 24mm 20mm 22mm 20mm;
  @top-center {{ font-family: Vazirmatn; font-size: 8.3pt; color: {MUTED}; vertical-align: bottom;
                 padding-bottom: 3mm; border-bottom: 0.5pt solid {GOLD}; }}
  @bottom-center {{ content: counter(page, persian); font-family: Vazirmatn; font-size: 9pt;
                    color: {NAVY}; font-weight: 600; vertical-align: top; padding-top: 4mm; }} }}
@page cover {{ margin: 0; @top-center {{ content: none; border: none; }} @bottom-center {{ content: none; }} }}
@page plain {{ @top-center {{ content: none; border: none; }} @bottom-center {{ content: none; }} }}
@page toc {{ @top-center {{ content: "فهرست مطالب"; }} @bottom-center {{ content: none; }} }}
{chr(10).join(page_rules)}
html {{ direction: rtl; }}
body {{ font-family: Vazirmatn; font-size: 10.4pt; line-height: 1.95; color: {INK}; background: #fff;
        margin: 0; text-align: justify; text-justify: inter-word; font-feature-settings: "kern"; }}
p {{ margin: 0 0 7pt; orphans: 3; widows: 3; }}
a {{ color: {NAVY}; text-decoration: none; }}
a.ext {{ border-bottom: 0.4pt dotted {GOLD}; overflow-wrap: anywhere; }}
em {{ font-style: normal; }}
strong {{ font-weight: 700; color: #0F2541; }}
code {{ font-family: Vazirmatn; font-size: 0.86em; background: #F3F5F9; padding: 0 3pt; border-radius: 2pt;
        unicode-bidi: isolate; direction: ltr; }}
.cite {{ font-size: 0.8em; color: {MUTED}; unicode-bidi: isolate; display: inline-block; max-width: 100%; line-height: 1.7; text-align: start; }}
h2, h3, h4 {{ color: {NAVY}; break-after: avoid; page-break-after: avoid; text-align: start; line-height: 1.6; }}
h2 {{ font-size: 15pt; font-weight: 800; margin: 20pt 0 8pt; padding-bottom: 4pt; border-bottom: 0.6pt solid #DCE2EA; }}
h3 {{ font-size: 12pt; font-weight: 700; margin: 14pt 0 6pt; }}
h2 .num, h3 .num {{ color: {GOLD}; margin-left: 6pt; }}
ul, ol {{ margin: 0 0 8pt; padding-right: 18pt; padding-left: 0; }}
li {{ margin-bottom: 3pt; }}
blockquote {{ margin: 10pt 0; padding: 8pt 14pt; border-right: 2.5pt solid {GOLD}; background: #FCF8EE;
              color: #0F2541; font-weight: 600; break-inside: avoid; }}
blockquote p {{ margin: 0; }}
table {{ width: 100%; border-collapse: collapse; margin: 8pt 0 12pt; font-size: 8.4pt; line-height: 1.6;
         border-top: 1.4pt solid {NAVY}; border-bottom: 1pt solid {NAVY}; }}
thead {{ display: table-header-group; }}
th {{ background: {NAVY}; color: #fff; font-weight: 700; padding: 5pt 6pt; text-align: start; vertical-align: bottom; }}
td {{ padding: 4.5pt 6pt; border-bottom: 0.4pt solid #DCE2EA; vertical-align: top; text-align: start; }}
th, td {{ unicode-bidi: plaintext; }}
tbody tr:nth-child(even) td {{ background: #F7F9FC; }}
tr {{ break-inside: avoid; page-break-inside: avoid; }}
table.card {{ border: 0.8pt solid {GOLD}; border-top: 3pt solid {GOLD}; background: #FFFDF8; margin: 4pt 0 16pt; font-size: 9pt; }}
table.card caption {{ caption-side: top; text-align: start; font-weight: 800; color: {NAVY}; font-size: 10pt;
                      padding: 0 0 5pt; }}
table.card td {{ background: transparent !important; border-bottom: 0.4pt solid #EFE4C8; }}
table.card td:first-child {{ width: 27%; color: {NAVY}; }}
figure {{ margin: 12pt auto 14pt; padding: 12pt 8pt 8pt; text-align: center; break-inside: avoid;
          page-break-inside: avoid; border-top: 1pt solid {GOLD}; border-bottom: 0.5pt solid #DCE2EA; }}
figure svg {{ display: block; margin: 0 auto; }}
figure svg[aria-roledescription="gantt"] text, figure svg[aria-roledescription="pie"] text {{ direction: ltr; }}
figure.wide {{ border: none; margin: 0 auto; padding: 0; min-height: 158mm; display: flex; flex-direction: column;
               justify-content: center; align-items: center; }}
figure.wide figcaption {{ margin-top: 6mm; }}
figure svg foreignObject, figure svg foreignObject * {{ margin: 0 !important; padding: 0; text-align: center !important;
  text-justify: auto; line-height: 1.55 !important; orphans: 1; widows: 1; font-feature-settings: normal; }}
figcaption {{ font-size: 8.6pt; color: {MUTED}; line-height: 1.75; margin: 9pt 12pt 0; text-align: center; }}
.note-default, .note-practice, .note-fail {{ padding: 7pt 11pt; margin: 9pt 0 11pt; break-inside: avoid; }}
.note-default {{ background: #FCF8EE; border-right: 2.5pt solid {GOLD}; }}
.note-practice {{ background: #F3F6FA; border-right: 2.5pt solid {NAVY}; }}
.note-fail {{ background: #FFFFFF; border: 0.6pt solid #D6DCE5; border-right: 2.5pt solid {NAVY}; }}
section.unit {{ break-before: page; }}
.opener {{ padding-top: 30mm; margin-bottom: 14pt; }}
.opener .label {{ color: {GOLD}; font-size: 13pt; font-weight: 700; }}
.opener .big {{ color: {GOLD}; font-size: 64pt; font-weight: 800; line-height: 1; margin: 2pt 0 6pt; }}
.opener h1 {{ color: {NAVY}; font-size: 25pt; font-weight: 900; line-height: 1.45; margin: 0 0 12pt; text-align: start; }}
.opener .rule {{ width: 34mm; height: 2.4pt; background: {GOLD}; }}
.front .opener {{ padding-top: 8mm; }}
.front .opener h1 {{ font-size: 21pt; }}
.mk {{ font-size: 1pt; color: #fff; line-height: 0; }}
/* cover */
.cover {{ page: cover; height: 297mm; position: relative; overflow: hidden; }}
.cover .band {{ position: absolute; top: 0; right: 0; width: 14mm; height: 297mm; background: {NAVY}; }}
.cover .band i {{ position: absolute; top: 0; left: 0; width: 1.6mm; height: 297mm; background: {GOLD}; }}
.cover .inner {{ position: absolute; top: 46mm; right: 34mm; left: 26mm; }}
.cover .kicker {{ color: {GOLD}; font-size: 12pt; font-weight: 700; }}
.cover h1 {{ color: {NAVY}; font-size: 34pt; font-weight: 900; line-height: 1.5; margin: 6mm 0 7mm; text-align: start; }}
.cover .rule {{ width: 46mm; height: 3pt; background: {GOLD}; margin-bottom: 7mm; }}
.cover .sub {{ color: #33465F; font-size: 15pt; font-weight: 500; }}
.cover .art {{ position: absolute; bottom: 30mm; left: 22mm; }}
.cover .foot {{ position: absolute; bottom: 16mm; right: 34mm; color: {MUTED}; font-size: 9.5pt; }}
/* plain front pages */
.plainpage {{ page: plain; break-before: page; }}
.titlepage {{ text-align: center; padding-top: 60mm; }}
.titlepage h1 {{ color: {NAVY}; font-size: 26pt; font-weight: 900; line-height: 1.6; margin: 0 0 8mm; text-align: center; }}
.titlepage .rule {{ width: 30mm; height: 2.4pt; background: {GOLD}; margin: 0 auto 8mm; }}
.titlepage .sub {{ font-size: 14pt; color: #33465F; }}
.titlepage .aud {{ margin-top: 70mm; font-size: 9.5pt; color: {MUTED}; line-height: 2; }}
.copyright {{ padding-top: 150mm; font-size: 8.8pt; color: #44536A; line-height: 1.95; text-align: start; }}
.copyright p {{ margin-bottom: 6pt; }}
/* contents */
.tocpage {{ page: toc; break-before: page; }}
.tocpage h1 {{ color: {NAVY}; font-size: 24pt; font-weight: 900; margin: 6mm 0 4mm; }}
.tocpage .rule {{ width: 30mm; height: 2.4pt; background: {GOLD}; margin-bottom: 8mm; }}
.toc-row {{ display: flex; align-items: baseline; gap: 6pt; margin: 0 0 4pt; font-size: 10.6pt; }}
.toc-row.chapter {{ font-weight: 700; color: {NAVY}; margin-top: 7pt; }}
.toc-row.appendix {{ font-weight: 600; color: {NAVY}; margin-top: 5pt; }}
.toc-row .lab {{ color: {GOLD}; min-width: 15mm; font-weight: 700; }}
.toc-row .dots {{ flex: 1; border-bottom: 0.8pt dotted #B9C3D1; transform: translateY(-3pt); }}
.toc-row .pg {{ min-width: 9mm; text-align: left; color: {NAVY}; font-weight: 700; }}
.toc-group {{ margin: 12pt 0 4pt; color: {MUTED}; font-size: 9pt; }}
"""

COVER_ART = f"""<svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
<g stroke="{NAVY}" stroke-width="0.9" opacity="0.55" fill="none">
<path d="M20 160 L80 110 L150 130 L210 60 L280 90"/><path d="M80 110 L120 40 L210 60"/><path d="M150 130 L190 180 L280 90"/>
<path d="M20 160 L60 60 L120 40"/><path d="M60 60 L80 110"/><path d="M190 180 L120 170 L150 130"/><path d="M120 170 L80 110"/></g>
<g stroke="{GOLD}" stroke-width="1.6" fill="none"><path d="M20 160 L80 110 L150 130 L210 60 L280 90"/></g>
<g fill="{NAVY}"><circle cx="60" cy="60" r="4"/><circle cx="120" cy="40" r="4"/><circle cx="190" cy="180" r="4"/>
<circle cx="120" cy="170" r="4"/></g>
<g fill="#fff" stroke="{GOLD}" stroke-width="2.2"><circle cx="20" cy="160" r="6"/><circle cx="80" cy="110" r="6"/>
<circle cx="150" cy="130" r="6"/><circle cx="210" cy="60" r="6"/></g><circle cx="280" cy="90" r="8" fill="{GOLD}"/></svg>"""


def toc_html(pages):
    rows, last_kind = [], None
    for sid, label, title, kind in toc:
        if kind != last_kind and kind == 'appendix':
            rows.append('<div class="toc-group">پیوست‌ها</div>')
        if kind != last_kind and kind == 'chapter':
            rows.append('<div class="toc-group">فصل‌ها</div>')
        last_kind = kind
        pg = str(pages.get(sid, '')).translate(FA) if pages else '۰۰۰'
        lab = label.replace('فصل ', '').replace('پیوست ', '')
        rows.append(f'<div class="toc-row {kind}"><span class="lab">{lab}</span><a href="#{sid}">{html.escape(title)}</a>'
                    f'<span class="dots"></span><span class="pg">{pg}</span></div>')
    return '\n'.join(rows)


def book(pages):
    out = [f'<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><title>{TITLE}</title>'
           f'<style>{CSS}</style></head><body>']
    out.append(f'''<div class="cover"><div class="band"><i></i></div><div class="inner">
<div class="kicker">راهنمای عملی برای سازمان‌ها</div><h1>{TITLE}</h1><div class="rule"></div>
<div class="sub">{SUBTITLE}</div></div><div class="art">{COVER_ART}</div>
<div class="foot">روش، ابزار و شواهد برای انتخاب، ساخت، عرضه و سنجش کاربردهای هوش مصنوعی</div></div>''')
    out.append(f'''<section class="plainpage titlepage"><h1>{TITLE}</h1><div class="rule"></div>
<div class="sub">{SUBTITLE}</div><div class="aud">برای هیئت‌مدیره و نهادهای راهبری، حامیان اجرایی، مدیران کسب‌وکار،<br/>
تیم‌های محصول، داده و فناوری، منابع انسانی، حقوقی و انطباق، ریسک و امنیت اطلاعات</div></section>''')
    out.append(f'''<section class="plainpage copyright">
<p><strong>{TITLE}</strong><br/>{SUBTITLE}</p>
<p>این اثر با مجوز «کریتیو کامنز، انتساب ۴٫۰ بین‌المللی» (CC BY 4.0) منتشر شده است. استفاده، بازنشر و اقتباس از آن با ذکر منبع آزاد است.
متن کامل مجوز: <a class="ext" href="https://creativecommons.org/licenses/by/4.0/">creativecommons.org/licenses/by/4.0</a></p>
<p>نسخهٔ انگلیسی، فایل همراه شواهد و سوابق راستی‌آزمایی: <a class="ext" href="{REPO}">github.com/pirayeah/ai-implementation-handbook</a></p>
<p>حقوق منابعی که در این راهنما به آن‌ها ارجاع شده متعلق به صاحبان آن‌هاست. مثال پیوست ب فرضی است. نام شرکت‌ها و محصولات فقط برای ارجاع آمده و به معنای توصیه نیست.
این راهنما مشاورهٔ حقوقی، مالی یا نظارتی نیست؛ پیش از اجرا، الزامات قانونی محل فعالیت خود را با مشاور صاحب صلاحیت بررسی کنید.</p>
<p>حروف‌چینی با قلم وزیرمتن (Vazirmatn)، اثر صابر راستی‌کردار، با مجوز SIL Open Font License.</p></section>''')
    out.append(f'<section class="tocpage"><h1>فهرست مطالب</h1><div class="rule"></div>{toc_html(pages)}</section>')
    for n, s in enumerate(secs):
        big = s['label'].split(' ', 1)[1] if s['label'] else ''
        lab = s['label'].split(' ', 1)[0] if s['label'] else ''
        opener = (f'<div class="opener"><div class="label">{lab}</div><div class="big">{big}</div><h1>{html.escape(s["title"])}</h1><div class="rule"></div></div>'
                  if s['label'] else
                  f'<div class="opener"><h1>{html.escape(s["title"])}</h1><div class="rule"></div></div>')
        cls = 'front' if s['kind'] == 'front' else s['kind']
        out.append(f'<section id="{s["id"]}" class="unit {cls} sec-{s["id"]}"><span class="mk">QZM{n:02d}QZ</span>{opener}{s["html"]}</section>')
    out.append('</body></html>')
    return '\n'.join(out)


def print_pdf(doc, pdf):
    hp = WORK / 'book.html'
    hp.write_text(doc, encoding='utf-8')
    if pdf.exists():
        pdf.unlink()
    r = chrome(['--no-pdf-header-footer', '--generate-pdf-document-outline', '--run-all-compositor-stages-before-draw',
                '--virtual-time-budget=20000', f'--print-to-pdf={pdf}', hp.as_uri()], timeout=900)
    if not pdf.exists():
        sys.exit('PDF printing failed:\n' + r.stderr.decode('utf-8', 'replace')[-3000:])


def section_pages(pdf):
    found = {}
    for i, pg in enumerate(PdfReader(str(pdf)).pages, 1):
        for n in re.findall(r'QZM(\d\d)QZ', (pg.extract_text() or '').replace(' ', '')):
            found.setdefault(secs[int(n)]['id'], i)
    return found


tmp = WORK / 'pass1.pdf'
print_pdf(book(None), tmp)
pages = section_pages(tmp)
missing = [s['id'] for s in secs if s['id'] not in pages]
print_pdf(book(pages), OUT)
check = section_pages(OUT)
report = {'pdf': OUT.name, 'pages': len(PdfReader(str(OUT)).pages), 'figures': len(fig_html),
          'sections_located': len(check), 'sections_missing': missing,
          'toc_stable': check == pages, 'smallest_figure_scale': min(f['scale'] for f in fig_report),
          'figures_detail': fig_report}
(WORK / 'pdf-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
print(json.dumps({k: v for k, v in report.items() if k != 'figures_detail'}, ensure_ascii=False, indent=1))
for f in fig_report:
    print(f)
