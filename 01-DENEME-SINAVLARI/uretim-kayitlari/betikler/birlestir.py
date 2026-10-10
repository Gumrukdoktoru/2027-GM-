#!/usr/bin/env python3
"""Deneme sınavlarını küme çıktılarından birleştirir.
Kullanım: python3 birlestir.py <out_dir> <hedef_dir>
"""
import json, os, sys, re, random, collections, glob

OUT, HEDEF = sys.argv[1], sys.argv[2]
os.makedirs(HEDEF, exist_ok=True)
random.seed(20270)
L = 'ABCDE'

KONU_ADI = {
 'GM02':'Gümrük kıymeti','GM03':'Menşe, BTB/BMB','GM04':'Özet beyan, geçici depolama','GM05':'Gümrük beyanı, muayene',
 'GM06':'Serbest dolaşım, nihai kullanım','GM07':'Transit','GM08':'Antrepo','GM09':'Dahilde işleme','GM10':'Hariçte işleme / GKAİR',
 'GM11':'Geçici ithalat','GM12':'İhracat (gümrük)','GM13':'Geri gelen eşya','GM14':'Muafiyetler','GM15':'Posta ve hızlı kargo',
 'GM16':'Akaryakıt, kumanya','GM17':'Yükümlülük, teminat, tecil','GM18':'Geri verme – kaldırma','GM19':'Cezalar, uzlaşma, itiraz',
 'GM20':'YYS, yerinde gümrükleme','GM21':'Gümrük müşavirliği, temsil','GM22':'GSM, sınır ticareti, serbest bölge','GM23':'Fikri ve sınai haklar',
 'GM01':'Genel hükümler','GM24':'Tasfiye',
 'SR01':'5607 Kaçakçılık','SR02':'Kambiyo','SR03':'KDV','SR04':'ÖTV','SR05':'Damga vergisi, KKDF','SR06':'İhracat rejimi',
 'SR07':'İthalat rejimi','SR08':'Ürün güvenliği, TAREKS','SR10':'Tercihli ticaret, menşe belgeleri','SR12':'DİR (Ticaret)',
 'SR14':'DTÖ, TFA, DGÖ','SR15':'Incoterms, ödeme şekilleri','SR16':'TIR, ATA','SR09':'Ticaret politikası önlemleri',
 'SR11':'1/95 OKK, Gümrük Birliği','SR13':'Yatırım teşvik',
 'TR01':'Tarife – fasıl/pozisyon kapsamı','TR02':'Tarife – notlar, izahname','TR03':'Tarife – GYKK','TR04':'Tarife – tanımı verilen eşya',
 'TR05':'Tarife – GTİP yapısı, HS, 474','HESAP':'Hesap'}

def load():
    qs = []
    for f in sorted(glob.glob(os.path.join(OUT, '*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        for q in d:
            q['_kume'] = os.path.basename(f)[:-5]
            qs.append(q)
    return qs

def check(q):
    err = []
    if len(q.get('siklar', [])) != 5: err.append('şık sayısı')
    if not isinstance(q.get('dogru'), int) or not 0 <= q['dogru'] <= 4: err.append('dogru')
    if len(set(s.strip() for s in q.get('siklar', []))) != 5: err.append('tekrarlı şık')
    for k in ('id','deneme','alan','konu','alt_tip','kok','aciklama'):
        if not q.get(k) and q.get(k) != 0: err.append('eksik '+k)
    return err

def rot_konu(q):
    k = q['konu']
    if k != 'ROT': return k
    if q['alan'] == 'GM': return {1:'GM01', 2:'GM24', 3:'GM01'}[q['deneme']]
    return {1:'SR13', 2:'SR09', 3:'SR11'}[q['deneme']]

def fasil_key(q):
    m = re.search(r'\b(\d{2})\.(\d{2})\b', (q.get('dayanak') or '') + ' ' + ' '.join(q['siklar']))
    if q['konu'] == 'TR05': return (0, 0)
    if q['konu'] == 'TR03': return (1, 0)
    if m: return (2, int(m.group(1)) * 100 + int(m.group(2)))
    m = re.search(r'(\d{1,2})\s*(?:\.|ıncı|inci|uncu|üncü|nci|ncı|ncu|ncü)?\s*[Ff]as[ıi]l', q['kok'] + ' ' + (q.get('dayanak') or ''))
    if m: return (2, int(m.group(1)) * 100)
    return (3, 0)

def group_by_konu(qs):
    g = collections.OrderedDict()
    for q in sorted(qs, key=lambda q: (q.get('seri') or 'zz', q['id'])):
        g.setdefault(q['_konu'], []).append(q)
    return g

def hesap_order(qs):
    pri = {'H3':0,'H4':1,'H7':2,'H5':3,'H6':4,'H1':5,'H2':6,'H8':7}
    sets = collections.OrderedDict(); singles = []
    for q in qs:
        if q.get('ortak_veri_id'): sets.setdefault(q['ortak_veri_id'], []).append(q)
        else: singles.append(q)
    singles.sort(key=lambda q: (pri.get(q['alt_tip'], 9), q['id']))
    out = []
    # H3/H4/H7 önce, sonra kıymet tekilleri, sonra set, sonra H8
    head = [q for q in singles if q['alt_tip'] in ('H3','H4','H7')]
    mid = [q for q in singles if q['alt_tip'] in ('H5','H6','H1')]
    tail = [q for q in singles if q['alt_tip'] not in ('H3','H4','H7','H5','H6','H1')]
    out = head + mid
    for k, v in sets.items():
        v.sort(key=lambda q: (0 if q.get('ortak_veri') else 1, q['alt_tip'] != 'H1', q['id']))
        out += v
    return out + tail

LAYOUT = {
 1: [('sozel', ['SR05','SR14','SR04','SR03','SR15','SR02']),
     ('hesap', None),
     ('sozel', ['SR10:3','GM02','GM14','GM03','GM18','SR16','SR07','SR12']),
     ('tarife', None),
     ('sozel', ['GM01','GM04','GM05','GM17','GM06','GM07','GM08','GM11','GM09','GM10','GM12','GM13','GM16','GM22',
                'SR06','SR08','SR13','GM15','GM23','SR10','GM20','GM21','SR01','GM19'])],
 2: [('sozel', ['GM04','GM05','GM06','GM07','GM08','SR10:3','SR15','GM11','GM09','GM10','GM12','SR06','SR07','SR12',
                'GM13','GM14','GM02','GM03','SR14','SR16','GM15','GM16','GM22','SR02','SR03','SR04','SR05',
                'GM17','GM18','GM19','GM24','SR10','SR01','GM20','GM21','GM23','SR08','SR09']),
     ('tarife', None), ('hesap', None)],
 3: [('sozel', ['SR01']), ('tarife', None),
     ('sozel', ['GM01','GM04','GM05','GM17','GM07','GM08','GM11','GM09','GM10','GM06','GM12','GM13','SR10:3','SR15',
                'SR14','GM14','GM02','GM03','GM18']),
     ('hesap', None),
     ('sozel', ['SR06','SR07','SR12','SR11','SR08','SR16','SR10','GM16','GM22','GM15','GM20','GM21','GM23','GM19',
                'SR02','SR03','SR04','SR05'])],
}

def order_deneme(d, qs):
    by_alan = collections.defaultdict(list)
    for q in qs: by_alan[q['alan']].append(q)
    sozel = group_by_konu([q for q in qs if q['alan'] in ('GM','SAİR')])
    used = set(); seq = []
    for kind, konular in LAYOUT[d]:
        if kind == 'hesap': seq += hesap_order(by_alan['HESAP'])
        elif kind == 'tarife': seq += sorted(by_alan['TARİFE'], key=lambda q: (fasil_key(q), q['id']))
        else:
            for k in konular:
                kod, _, n = k.partition(':')
                if kod in sozel and sozel[kod]:
                    take = len(sozel[kod]) if not n else int(n)
                    seq += sozel[kod][:take]; sozel[kod] = sozel[kod][take:]; used.add(kod)
    # planda olmayan konu kaldıysa sona ekle (olmamalı)
    for k, v in sozel.items():
        if v: seq += v; print(f'UYARI D{d}: {k} yerleşimde yok, sona eklendi', file=sys.stderr)
    return seq

def balance_letters(seq):
    cnt = collections.Counter(); last = []
    fixed_letters = collections.Counter(q['dogru'] for q in seq if q.get('sira_sabit'))
    target = len(seq) / 5
    for q in seq:
        if q.get('sira_sabit'):
            pos = q['dogru']
        else:
            def ok(p):
                return not (len(last) >= 3 and all(x == p for x in last[-3:]))
            # kalan sabitleri de hesaba kat
            rem_fixed = collections.Counter(x['dogru'] for x in seq[seq.index(q):] if x.get('sira_sabit'))
            cands = [p for p in range(5) if ok(p)]
            pos = min(cands, key=lambda p: (cnt[p] + rem_fixed[p], random.random()))
            sik = q['siklar']; c = sik[q['dogru']]
            others = [s for i, s in enumerate(sik) if i != q['dogru']]
            if q['alt_tip'] in ('O1','D3','D2','K1','O4','D5','D4','E1') and not re.match(r'^\d', others[0].strip()):
                random.shuffle(others)
            new = others[:pos] + [c] + others[pos:]
            q['siklar'] = new; q['dogru'] = pos
        cnt[pos] += 1; last.append(pos)
    return cnt

def esc_line(s):
    s = s.strip()
    m = re.match(r'^(\()?([A-Za-zÇĞİÖŞÜçğıöşü]{1,5}|\d{1,3})([.)])(\s|$)', s)
    if m:
        s = ('\\(' if m.group(1) else '') + m.group(2) + '\\' + m.group(3) + s[m.end(3):]
    s = re.sub(r'^([-*+#>]) ', lambda mm: '\\' + mm.group(0), s)
    return s

def lines_block(text):
    parts = [esc_line(x) for x in text.split('\n') if x.strip()]
    return '\\\n'.join(parts)

ROMA = ['I','II','III','IV','V','VI','VII','VIII','IX']

def render_q(n, q, ortak_baslik=None):
    out = []
    if ortak_baslik:
        out.append(f'**{ortak_baslik}**\n')
        out.append(lines_block(q['ortak_veri']) + '\n')
    kok_on = (q.get('kok_on') or '').strip()
    onc = q.get('onculler') or []
    first = True
    def num(txt):
        nonlocal first
        if first:
            first = False
            return f'**{n}.** ' + txt
        return txt
    if kok_on:
        out.append(num(lines_block(kok_on)) + '\n')
    if onc:
        ol = [f'{ROMA[i]}\\. {esc_line(o)}' for i, o in enumerate(onc)]
        out.append(num('\\\n'.join(ol)) + '\n')
    if q.get('tablo'):
        t = q['tablo']
        if first:
            out.append(f'**{n}.**\n'); first = False
        hdr = t[0]; out.append('| ' + ' | '.join(hdr) + ' |')
        out.append('|' + '---|' * len(hdr))
        for r in t[1:]: out.append('| ' + ' | '.join(r) + ' |')
        out.append('')
    out.append(num(lines_block(q['kok'])) + '\n')
    sik = [f'{L[i]}\\) {s.strip()}' for i, s in enumerate(q['siklar'])]
    out.append('\\\n'.join(sik) + '\n')
    return '\n'.join(out)

KAPAK = """# T.C. TİCARET BAKANLIĞI GÜMRÜK MÜŞAVİRLİĞİ SINAVI

## DENEME {d}

**GENEL AÇIKLAMALAR**

1. Bu kitapçıkta 100 soru bulunmaktadır.
2. Her sorunun yalnız bir doğru cevabı vardır.
3. Sınav süresi 150 dakikadır.
4. Değerlendirme yalnız doğru cevap sayısı üzerinden yapılır; yanlış cevaplar doğruları götürmez.

> Bu deneme, 2021–2025 Gümrük Müşavirliği sınavlarının soru-soru analizine dayanılarak gerçek sınavın alan dağılımı (42 Gümrük Mevzuatı, 30 Sair Mevzuat, 17 Tarife, 11 Hesap), blok düzeni ve soru tipi dağılımıyla hazırlanmıştır. Cevap anahtarı ve açıklamalı çözümler ayrı dosyadadır.

---
"""

def main():
    qs = load()
    bad = [(q['id'], check(q)) for q in qs if check(q)]
    if bad:
        for b in bad: print('HATA', b, file=sys.stderr)
    for q in qs: q['_konu'] = rot_konu(q)
    rapor = []
    for d in (1, 2, 3):
        dq = [q for q in qs if q['deneme'] == d]
        seq = order_deneme(d, dq)
        cnt = balance_letters(seq)
        alan = collections.Counter(q['alan'] for q in seq)
        rapor.append(f'Deneme {d}: {len(seq)} soru · ' + ' '.join(f'{k} {v}' for k, v in alan.items()) + ' · harf ' + ' '.join(f'{L[i]} {cnt[i]}' for i in range(5)))
        # numara ve ortak veri başlıkları
        num = {q['id']: i + 1 for i, q in enumerate(seq)}
        sets = collections.defaultdict(list)
        for q in seq:
            if q.get('ortak_veri_id'): sets[q['ortak_veri_id']].append(num[q['id']])
        # KİTAPÇIK
        K = [KAPAK.format(d=d)]
        blok_onceki = None
        for i, q in enumerate(seq, 1):
            ob = None
            if q.get('ortak_veri'):
                ns = sorted(sets[q['ortak_veri_id']])
                ob = f'{ns[0]} ve {ns[-1]} numaralı soruları aşağıdaki verilere göre cevaplayınız.' if len(ns) == 2 else f'{ns[0]}–{ns[-1]} numaralı soruları aşağıdaki verilere göre cevaplayınız.'
            K.append(render_q(i, q, ob))
        K.append('\n---\n\n*Deneme bitti. Cevaplarınızı kontrol ediniz.*\n')
        open(os.path.join(HEDEF, f'DENEME-{d}_SORU-KITAPCIGI.md'), 'w', encoding='utf-8').write('\n'.join(K))
        # CEVAP ANAHTARI + ÇÖZÜMLER
        C = [f'# GÜMRÜK MÜŞAVİRLİĞİ SINAVI — DENEME {d}\n\n## CEVAP ANAHTARI VE AÇIKLAMALI ÇÖZÜMLER\n']
        C.append('### 1. Cevap anahtarı\n')
        C.append('| No | Cevap | No | Cevap | No | Cevap | No | Cevap | No | Cevap |')
        C.append('|---|---|---|---|---|---|---|---|---|---|')
        nrow = (len(seq) + 4) // 5
        for r in range(nrow):
            cells = []
            for c in range(5):
                i = c * nrow + r
                cells += [str(i + 1), L[seq[i]['dogru']]] if i < len(seq) else ['', '']
            C.append('| ' + ' | '.join(cells) + ' |')
        C.append('')
        C.append('Harf dağılımı: ' + ' · '.join(f'{L[i]} {cnt[i]}' for i in range(5)) + '\n')
        # dağılım tabloları
        C.append('### 2. Denemenin yapısı\n')
        bl = []
        cur = None; start = 1
        for i, q in enumerate(seq, 1):
            a = 'Sözel (GM + Sair)' if q['alan'] in ('GM', 'SAİR') else {'TARİFE': 'Tarife', 'HESAP': 'Hesap'}[q['alan']]
            if a != cur:
                if cur: bl.append((start, i - 1, cur))
                cur = a; start = i
        bl.append((start, len(seq), cur))
        C.append('**Blok düzeni:** ' + ' · '.join(f'{s}–{e} {a}' for s, e, a in bl) + '\n')
        at = collections.Counter(q['alt_tip'] for q in seq)
        C.append('**Alt tip dağılımı:** ' + ' · '.join(f'{k} {v}' for k, v in sorted(at.items(), key=lambda x: -x[1])) + '\n')
        kc = collections.Counter(q['_konu'] for q in seq)
        C.append('**Konu dağılımı:** ' + ' · '.join(f'{KONU_ADI.get(k, k)} {v}' for k, v in sorted(kc.items(), key=lambda x: -x[1])) + '\n')
        C.append('Alt tip kodları için: `00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR/12-SORU-TIPI-KATALOGU`.\n')
        C.append('### 3. Açıklamalı çözümler\n')
        for i, q in enumerate(seq, 1):
            C.append(f'#### {i}. soru — Cevap: {L[q["dogru"]]}\n')
            C.append(f'*{q["alan"]} · {KONU_ADI.get(q["_konu"], q["_konu"])} · {q["alt_tip"]}*\n')
            C.append(f'**Doğru şık:** {L[q["dogru"]]}) {q["siklar"][q["dogru"]]}\n')
            ac = q['aciklama'].strip()
            C.append(ac + '\n')
            if q.get('tuzak'): C.append(f'**Tuzak:** {q["tuzak"].strip()}\n')
            if q.get('dayanak'): C.append(f'**Dayanak:** {q["dayanak"].strip()}\n')
        open(os.path.join(HEDEF, f'DENEME-{d}_CEVAP-ANAHTARI-VE-COZUMLER.md'), 'w', encoding='utf-8').write('\n'.join(C))
        # makine verisi
        json.dump([{k: v for k, v in q.items() if not k.startswith('_')} | {'no': i + 1, 'cevap': L[q['dogru']]} for i, q in enumerate(seq)],
                  open(os.path.join(HEDEF, f'deneme{d}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('\n'.join(rapor))

if __name__ == '__main__':
    main()
