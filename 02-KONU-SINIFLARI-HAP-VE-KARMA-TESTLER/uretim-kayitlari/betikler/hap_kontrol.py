#!/usr/bin/env python3
"""Hap ajanlarının çıktılarını denetler.
Kullanım: python3 hap_kontrol.py <S> [küme ...]
- cikan/<K>.json: konu başına bütün çıkmış sorular haplarda geçiyor mu
- sorulmayan/<K>.json: kanıt kesitleri kaynak dosyada birebir var mı (boşluk/tırnak normalize)
Sonuç: hap/kontrol/<K>.json (geçersiz kanıtlı kayıtların listesi) ve ekrana özet.
"""
import json, os, re, sys, glob, unicodedata
S = sys.argv[1]
want = sys.argv[2:]
rows = {r['id']: r for r in json.load(open(f'{S}/konu/siniflar.json', encoding='utf-8'))}
kume = json.load(open(f'{S}/hap/kumeler.json', encoding='utf-8'))
os.makedirs(f'{S}/hap/kontrol', exist_ok=True)

def norm(s):
    s = unicodedata.normalize('NFC', s)
    s = s.replace('\\', '').replace('**', '').replace('__', '')
    s = re.sub(r'[’‘`´]', "'", s); s = re.sub(r'[“”«»]', '"', s); s = re.sub(r'[–—−]', '-', s)
    s = s.replace('­', '').replace(' ', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()
TRL = str.maketrans('İIÇĞÖŞÜ', 'iıçğöşü')
def low(s): return s.translate(TRL).lower()
_cache = {}
def text_of(path):
    if path not in _cache:
        try: _cache[path] = norm(open(path, encoding='utf-8', errors='replace').read())
        except Exception: _cache[path] = ''
    return _cache[path]
ALL = sorted(glob.glob(f'{S}/kaynak2/**/*.md', recursive=True) + glob.glob(f'{S}/kaynak/txt/*.txt'))
def resolve(k):
    if not k: return None
    k = k.split(' (')[0].split(' MADDE')[0].split(' md.')[0].strip().strip('`')
    for cand in (k, f'{S}/{k}', f'{S}/{k.lstrip("$S/")}'):
        if os.path.isfile(cand): return cand
    base = os.path.basename(k)
    for p in ALL:
        if os.path.basename(p) == base: return p
    return None
def kanit_ok(kanit, kaynak):
    n = norm(kanit or '')
    if len(n) < 12: return False, 'kısa'
    p = resolve(kaynak)
    if p:
        t = text_of(p)
        if n in t or low(n) in low(t): return True, p
    for q in ALL:  # dosya yanlış verilmiş olabilir
        t = text_of(q)
        if n in t or low(n) in low(t): return True, q
    return False, 'yok'

for kid, konular in kume.items():
    if want and kid not in want: continue
    rep = {'kume': kid}
    fc = f'{S}/hap/cikan/{kid}.json'
    if os.path.exists(fc):
        d = json.load(open(fc, encoding='utf-8'))
        byk = {k['konu']: k for k in d['konular']}
        eks = {}; nh = 0
        for k in konular:
            ids = set(rows[k]['sorular']); h = byk.get(k, {'haplar': []})['haplar']; nh += len(h)
            cov = set(i for x in h for i in x.get('sorular', []))
            if ids - cov: eks[k] = sorted(ids - cov)
            bos = [i for i, x in enumerate(h) if not x.get('metin', '').strip()]
            if bos: eks[k + '_bos'] = bos
        rep['cikan'] = {'hap': nh, 'eksik_soru': eks, 'konu_yok': [k for k in konular if k not in byk and rows[k]['toplam']]}
        print(kid, 'ÇIKAN hap', nh, 'eksik', eks or '-', 'konu yok', rep['cikan']['konu_yok'] or '-')
    fs = f'{S}/hap/sorulmayan/{kid}.json'
    if os.path.exists(fs):
        d = json.load(open(fs, encoding='utf-8'))
        bad = []; nsc = nb = 0; per = {}
        for k in d['konular']:
            c_sc = c_b = 0
            for a in k.get('alt_konular', []):
                for j, x in enumerate(a.get('sc', [])):
                    nsc += 1; ok, w = kanit_ok(x.get('kanit'), x.get('kaynak'))
                    if ok: c_sc += 1
                    else: bad.append({'konu': k['konu'], 'tur': 'sc', 'alt': a.get('ad'), 'i': j, 's': x.get('s', '')[:80], 'neden': w})
            for j, x in enumerate(k.get('beklenen', [])):
                nb += 1; ok, w = kanit_ok(x.get('kanit'), x.get('kaynak'))
                if ok: c_b += 1
                else: bad.append({'konu': k['konu'], 'tur': 'beklenen', 'i': j, 'metin': x.get('metin', '')[:80], 'neden': w})
            per[k['konu']] = (c_sc, c_b)
        rep['sorulmayan'] = {'sc': nsc, 'beklenen': nb, 'gecersiz': bad, 'konu_bazinda_gecerli': per,
                             'konu_yok': [k for k in konular if k not in {x['konu'] for x in d['konular']}]}
        print(kid, 'SORULMAYAN sc', nsc, 'beklenen', nb, 'geçersiz kanıt', len(bad), 'konu yok', rep['sorulmayan']['konu_yok'] or '-')
        print('   ', {k: v for k, v in per.items()})
    json.dump(rep, open(f'{S}/hap/kontrol/{kid}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
