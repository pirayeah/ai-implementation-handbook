"""Assemble the handbook (v2.0) and its evidence companion, then verify them.

Outputs
- enterprise-ai-strategy-and-implementation-handbook.md : chapters + Appendix A (source key, generated)
  + Appendix B (worked example) + Appendix C (tools) + Appendix D (defaults, external sources)
- handbook-evidence-companion.md : full source register, evidence map and verification record
- verification-report.json
"""
from pathlib import Path
import json, re, hashlib, collections, os

P = Path(__file__).parent
# Set AI_SOURCES_ROOT to the source collection folder to re-check file fingerprints; skipped when unset.
ROOT = Path(os.environ['AI_SOURCES_ROOT']) if os.environ.get('AI_SOURCES_ROOT') else None
R = json.loads((P / 'source-register.json').read_text(encoding='utf-8'))
by_id = {r['id']: r for r in R}


def read(fn):
    return (P / fn).read_text(encoding='utf-8').strip()


# ------------------------------------------------------------------ source key (Appendix A)
chapters_txt = read('handbook-chapters.md')
body_for_ids = chapters_txt + read('appendix-b-worked-example.md') + read('appendix-c-editable-tools.md') + read('appendix-d-defaults-and-sources.md')
finos_used = sorted(set(re.findall(r'\b((?:mi|ri|uc)-\d+)\b', body_for_ids)), key=lambda s: (s[:2], int(s[3:])))
folder = {'mi': '_mitigations', 'ri': '_risks', 'uc': '_usecases'}


def finos_entry(fid):
    pre = f"ai-governance-framework-main/docs/{folder[fid[:2]]}/{fid}_"
    hits = [r for r in R if r['filename'].startswith(pre)]
    return hits[0] if hits else None


def cell(s):
    return str(s).replace('|', '/').replace('\n', ' ').strip()


key = ['# Appendix A — Source key', '',
       'Short IDs used in citations resolve here. Each entry’s evidential status matters: company accounts, consultancy analysis, community specifications and regulators’ reports carry different weight (see the evidence labels in [How to use the handbook](#how-to-use-the-handbook)). Full filenames, review depth, reviewed locators, limitations and SHA-256 fingerprints for all 197 workspace files are in [handbook-evidence-companion.md](handbook-evidence-companion.md), Part 1. External sources E01–E12 are registered in [Appendix D.2](#appendix-d).', '',
       '## A.1 Principal documents', '',
       '| ID | Title | Organization / speaker; date | Source type |', '|---|---|---|---|']
for r in R:
    if r['id'].startswith('D'):
        key.append(f"| {r['id']} | {cell(r['title'])} | {cell(r['organization_or_speaker'])}; {cell(r['date'])} | {cell(r.get('source_type', ''))} |")
key += ['', '## A.2 Images and diagrams cited', '', '| ID | Content | Parent / relationship |', '|---|---|---|']
for r in R:
    if r['id'].startswith('A') or r['id'] in ('F11', 'F12', 'F13', 'F14', 'F15', 'F16'):
        key.append(f"| {r['id']} | {cell(r['title'])} | {cell(r.get('parent_source', ''))} |")
key += ['', '## A.3 FINOS AI Governance Framework files cited', '',
        'Repository snapshot in `ai-governance-framework-main/`. "Draft" and "Approved-Specification" are project statuses, not legal status.', '',
        '| Citation | Title | Register ID | Project status |', '|---|---|---|---|']
missing_finos = []
for fid in finos_used:
    r = finos_entry(fid)
    if not r:
        missing_finos.append(fid); continue
    key.append(f"| FINOS {fid} | {cell(r['title'])} | {r['id']} | {cell(r.get('specification_status', 'not stated'))} |")
key.append('| FINOS heuristic assessment | Heuristic assessment guide (`docs/heuristic-assessment.md`) | ' +
           next(r['id'] for r in R if r['filename'].endswith('docs/heuristic-assessment.md')) + ' | not stated |')
(P / 'appendix-a-source-key.md').write_text('\n'.join(key) + '\n', encoding='utf-8')

# ------------------------------------------------------------------ assemble handbook
hb_parts = [('handbook-chapters.md', None), ('appendix-a-source-key.md', 'appendix-a'), ('appendix-b-worked-example.md', 'appendix-b'),
            ('appendix-c-editable-tools.md', 'appendix-c'), ('appendix-d-defaults-and-sources.md', 'appendix-d')]
manuscript = '\n\n---\n\n'.join(((f'<a id="{a}"></a>\n\n' if a else '') + read(fn)) for fn, a in hb_parts) + '\n'
dest = P / 'enterprise-ai-strategy-and-implementation-handbook.md'
dest.write_text(manuscript, encoding='utf-8')

# ------------------------------------------------------------------ assemble companion
def renumber(txt, old_letter, part):
    txt = re.sub(rf'^# Appendix {old_letter} — ', f'# Part {part} — ', txt, flags=re.M)
    txt = re.sub(rf'^(#+) {old_letter}\.(\d+)', rf'\1 {part}.\2', txt, flags=re.M)
    return txt

comp_parts = [renumber(read('appendix-a-source-register.md'), 'A', 1),
              renumber(read('evidence-map-and-patterns.md'), 'B', 2),
              renumber(read('appendix-d-verification.md'), 'D', 3)]
comp = ('# Evidence Companion to the Enterprise AI Strategy and Implementation Handbook\n\n'
        '**Version 2.0 · 9 November 2026.** This companion holds the audit trail behind the [handbook](enterprise-ai-strategy-and-implementation-handbook.md): '
        'Part 1, the complete 197-file workspace source register; Part 2, the evidence map, case accounting and cross-case pattern matrix; '
        'Part 3, the verification, limitations and research record. In version 1.0 these were Appendices A, B and D of the handbook. '
        'References to "Appendix A" inside Part 2 refer to Part 1. Chapter references refer to the handbook.\n\n---\n\n'
        + '\n\n---\n\n'.join(comp_parts) + '\n')
comp = comp.replace('resolve to exact filenames in Appendix A', 'resolve to exact filenames in Part 1').replace('Appendix A identifies every filename', 'Part 1 identifies every filename')
(P / 'handbook-evidence-companion.md').write_text(comp, encoding='utf-8')

# ------------------------------------------------------------------ verification
assert len(R) == 197 and len({r['id'] for r in R}) == 197
assert len({r['filename'] for r in R}) == 197
actual = {f.relative_to(ROOT).as_posix(): f for f in ROOT.rglob('*') if f.is_file()} if ROOT else {}
missing = set(actual) - {r['filename'] for r in R}
stale = ({r['filename'] for r in R} - set(actual)) if ROOT else set()
changed = [r['filename'] for r in R if r['filename'] in actual and hashlib.sha256(actual[r['filename']].read_bytes()).hexdigest() != r['sha256']]
assert not missing and not stale and not changed, (missing, stale, changed)
assert not any('Pending' in r['review_status'] for r in R)
images = [r for r in R if r['type'] in ['.png', '.jpeg', '.jpg', '.webp', '.ico']]
assert len(images) == 18 and all(r['review_status'] == 'Visually reviewed' and r.get('parent_source') for r in images)

chapters = re.findall(r'^## (\d+)\. ', manuscript, re.M)
assert chapters == [str(i) for i in range(1, 11)], chapters
templates = re.findall(r'^## C\.(\d+) ', manuscript, re.M)
assert templates == [str(i) for i in range(0, 15)], templates
for doc in (manuscript, comp):
    assert doc.count('```') % 2 == 0
    assert '\ufffd' not in doc
assert not re.search(r'Q0?15\b|30 billion|30-billion|12 FTE|26.week', manuscript, re.I)

# every chapter opens with a chapter card that states requirement levels
cards = re.findall(r'^## \d+\. .+\n\n\| Chapter card \| \|\n\|---\|---\|\n((?:\|.*\n)+)', manuscript, re.M)
assert len(cards) == 10 and all('Requirement level' in c for c in cards), len(cards)
level_terms = {k: len(re.findall(rf'\b{k}\b', manuscript)) for k in ('Core', 'Conditional', 'Optional')}
assert all(v > 0 for v in level_terms.values()), level_terms

# short-form workspace citations: bounds and type checks
loc_errors = []; checked = 0
for m in re.finditer(r'\b(D\d{2}) (pp?\.|ll?\.) ((?:\d+(?:[–-]\d+)?)(?:,\s*\d+(?:[–-]\d+)?)*)', manuscript):
    sid, kind, spec = m.groups(); r = by_id.get(sid); checked += 1
    if not r:
        loc_errors.append((sid, 'unknown id')); continue
    limit_key = 'pages' if kind.startswith('p') else 'lines'
    limit = int(r.get(limit_key, 0) or 0)
    if not limit:
        loc_errors.append((sid, f'{kind} used but source has no {limit_key}')); continue
    for part in re.split(r',\s*', spec):
        nums = [int(x) for x in re.split(r'[–-]', part)]
        if not all(1 <= n <= limit for n in nums) or nums != sorted(nums):
            loc_errors.append((sid, kind, part, limit))
assert not loc_errors, loc_errors
assert not missing_finos, missing_finos

# no long workspace filenames left in the reading body (chapters, worked example, tools)
long_names = re.findall(r'`[^`\n]+\.(?:pdf|md|png|jpeg|webp|puml|txt)`',
                        chapters_txt + read('appendix-b-worked-example.md') + read('appendix-c-editable-tools.md'))
assert not long_names, long_names

# external citations resolve to Appendix D.2
ext_cited = set(re.findall(r'\bE(\d{2})\b', chapters_txt + read('appendix-b-worked-example.md') + read('appendix-c-editable-tools.md')))
ext_registered = set(re.findall(r'^\| E(\d{2}) \|', read('appendix-d-defaults-and-sources.md'), re.M))
assert ext_cited <= ext_registered, ext_cited - ext_registered

# markdown table shape (outside code fences)
table_errors = []
for name, txt in (('handbook', manuscript), ('companion', comp)):
    expected = None; fence = False
    for n, line in enumerate(txt.splitlines(), 1):
        if line.startswith('```'):
            fence = not fence; expected = None; continue
        if not fence and line.startswith('|'):
            count = len(re.split(r'(?<!\\)\|', line)) - 2
            if expected is None: expected = count
            elif count != expected: table_errors.append((name, n, expected, count))
        else:
            expected = None
assert not table_errors, table_errors

diagrams = re.findall(r'```mermaid\n(\w[\w-]*)', manuscript)
report = {
    'status': 'PASS', 'version': '2.0',
    'source_snapshot_files': len(R), 'source_fingerprints_unchanged': (not changed) if ROOT else 'not checked (AI_SOURCES_ROOT unset)', 'unaccounted_files': sorted(missing), 'stale_entries': sorted(stale),
    'pdf_files': sum('pages' in r for r in R), 'pdf_pages_in_collection': sum(int(r.get('pages', 0) or 0) for r in R),
    'standalone_images_visually_reviewed': len(images), 'review_depth_counts': dict(collections.Counter(r['review_status'] for r in R)),
    'chapters': len(chapters), 'chapter_cards': len(cards), 'editable_tools': len(templates), 'requirement_level_mentions': level_terms,
    'short_D_citations_checked': checked, 'locator_bounds_errors': loc_errors, 'finos_ids_cited': len(finos_used),
    'external_sources_registered': len(ext_registered), 'external_sources_cited': sorted('E' + e for e in ext_cited),
    'mermaid_diagrams': len(diagrams), 'diagram_types': dict(collections.Counter(diagrams)),
    'markdown_table_errors': table_errors,
    'handbook_words': len(manuscript.split()), 'handbook_lines': len(manuscript.splitlines()),
    'companion_words': len(comp.split()), 'outputs': [dest.name, 'handbook-evidence-companion.md'],
    'limitations': ['Locator checks establish existence and bounds, not semantic entailment; claim/source alignment reviewed editorially.',
                    'Selected review of long documents; no exhaustive visual rendering of embedded PDF figures.',
                    'Mermaid syntax is not rendered by this script; diagrams should be previewed in a Mermaid-capable viewer.',
                    'No current-law applicability determination or independent validation of practitioner outcomes.'],
}
(P / 'verification-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=1))
