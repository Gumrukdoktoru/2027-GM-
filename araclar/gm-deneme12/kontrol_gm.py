"""GM Deneme 1-2 batch denetimi. Kullanım: python3 kontrol_gm.py batch_<KÜME>.py
- Her soru dict'inde set (1 veya 2) ve konu alanı; küme kontenjanı kumeler.json'dan.
- Prompt 3 biçim denetimi (kontrol3.py), kontenjan, zorluk, en uzun doğru şık, kanıt alıntısının metin/ içinde birebir bulunması,
  küme içi / diğer kümelerle / önceki setlerle (URETIM-HAFIZASI) çekirdek benzerliği."""
import sys, subprocess, tempfile, os, re, collections, json, unicodedata, pathlib, glob
here = os.path.dirname(os.path.abspath(__file__))
path = sys.argv[1]; kume = re.search(r'batch_(\w+)\.py', path).group(1)
ns = {}; exec(open(path).read(), ns); Q = ns['Q']
K = json.load(open(os.path.join(here, 'kumeler.json')))[kume]['konular']
err = 0
norm = lambda s: re.sub(r'\s+', ' ', unicodedata.normalize('NFC', s).replace('­', '').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip().lower()
CORPUS = {f.name: norm(f.read_text(errors='replace')) for f in pathlib.Path(here, 'metin').glob('*.txt')}
def kanit_ok(k):
    if '|' not in k: return False, 'biçim'
    dosyalar, body = k.split('|', 1)
    adlar = [d.strip() for d in re.split(r';', dosyalar) if d.strip()]
    for a in adlar:
        if not a.endswith('.txt'): a += '.txt'
        if a not in CORPUS: return False, f'dosya yok: {a}'
    metin = ' '.join(CORPUS[a if a.endswith('.txt') else a + '.txt'] for a in adlar)
    parts = [p.strip(' .…;,"\'') for p in re.split(r'\.\.\.|…|\[\.\.\.\]|\n', norm(body)) if len(p.strip()) > 12]
    eks = [p for p in parts if p not in metin]
    return (not eks and bool(parts)), ('bulunamadı: ' + eks[0][:70]) if eks else ''
for s in (1, 2):
    sub = [q for q in Q if q.get('set') == s]
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as f: f.write('Q=' + repr(sub)); tmp = f.name
    out = subprocess.run([sys.executable, os.path.join(here, 'kontrol3.py'), tmp], capture_output=True, text=True).stdout
    os.unlink(tmp)
    print(f'--- SET {s} ---'); print(out.strip())
    if 'Hatalı: 0' not in out: err += 1
    kc = collections.Counter(q['konu'] for q in sub)
    if dict(kc) != K: print(f'!! set {s}: konu kontenjanı {K} olmalı -> {dict(kc)}'); err += 1
    n = len(sub); z = collections.Counter(q['z'] for q in sub)
    hedef = {'ÇK': round(n * .1), 'K': round(n * .2), 'Z': round(n * .2), 'ÇZ': max(1, round(n * .1))}
    for k, v in hedef.items():
        if abs(z.get(k, 0) - v) > 1: print(f'!! set {s}: zorluk {k}={z.get(k,0)} (hedef ≈{v}); O en kalabalık olmalı'); err += 1
    if z and z.get('O', 0) < max(z.values()): print(f'!! set {s}: O en kalabalık zorluk olmalı'); err += 1
    lg = sum(len(q['d']) > max(map(len, q['c'])) for q in sub)
    if lg > max(1, round(n * .2)): print(f'!! set {s}: doğru şık en uzun {lg} (≤{max(1,round(n*.2))})'); err += 1
bad = []
for i, q in enumerate(Q, 1):
    ok, why = kanit_ok(q.get('kanit', ''))
    if not ok: bad.append(f'{i}: {why}')
if bad: print('!! kanıt alıntısı kaynakta birebir yok:\n   ' + '\n   '.join(bad)); err += 1
miss = [i + 1 for i, q in enumerate(Q) if q.get('set') not in (1, 2)]
if miss: print('!! set alanı eksik:', miss); err += 1
# çekirdek benzerliği
def tok(s):
    s = s.replace('İ', 'i').replace('I', 'ı').lower()
    return set(w for w in re.findall(r'\w+', s) if len(w) > 3)
jac = lambda a, b: len(a & b) / max(1, len(a | b))
for i in range(len(Q)):
    for j in range(i + 1, len(Q)):
        if jac(tok(Q[i]['cek']), tok(Q[j]['cek'])) >= 0.4: print(f'?? küme içi benzer çekirdek {i+1} ↔ {j+1}: {Q[i]["cek"][:70]} | {Q[j]["cek"][:70]}')
for f in sorted(glob.glob(os.path.join(here, 'batch_*.py'))):
    if os.path.abspath(f) == os.path.abspath(path): continue
    try:
        n2 = {}; exec(open(f).read(), n2)
    except Exception: continue
    for i, q in enumerate(Q, 1):
        for j, r in enumerate(n2.get('Q', []), 1):
            if jac(tok(q['cek']), tok(r.get('cek', ''))) >= 0.4: print(f'?? başka kümeyle benzer ({os.path.basename(f)}#{j}) ↔ {i}: {q["cek"][:60]} | {r["cek"][:60]}')
eski = []
for hf in ('/home/claude/2027-ye-haz-rl-k/sorular/hafiza/URETIM-HAFIZASI.md', os.path.join(here, '../../sorular/hafiza/URETIM-HAFIZASI.md')):
    if os.path.exists(hf):
        for l in open(hf):
            p = [x.strip() for x in l.split('|')]
            if len(p) >= 8 and re.match(r'[A-ZÇĞİÖŞÜ]+\d*-', p[0]): eski.append((p[0], p[3]))
for i, q in enumerate(Q, 1):
    for e in eski:
        if jac(tok(q['cek']), tok(e[1])) >= 0.4: print(f'?? önceki setle benzer ({e[0]}) ↔ {i}: {q["cek"][:60]} | {e[1][:60]}')
print('GENEL SONUÇ:', 'TEMİZ' if err == 0 else f'{err} sorun', '| "??" satırlarını tek tek incele: aynı bilgi ise soruyu değiştir.')
