# Konu sınıfları, eğilim ve karma test kontenjanı
import json, collections, sys
S = sys.argv[1]
d = json.load(open(f'{S}/konu/eslesme.json', encoding='utf-8'))
K, Q = d['konular'], d['sorular']
# Analizdeki alan ayrımı: hesap soruları (alan HESAP) içerik konusuna değil ayrı 'Hesaplama' konusuna sayılır
K = dict(K); K['HESAP'] = ['Hesaplama (Kıymet, Vergi ve Ceza Hesapları)', 'HESAP']
def konu_of(q): return 'HESAP' if q['alan'] == 'HESAP' else q['konu']
YIL = range(2021, 2026)
yc = {k: collections.Counter() for k in K}
for q in Q: yc[konu_of(q)][q['yil']] += 1
def sinif(n): return 'ÇOK' if n >= 10 else 'ORTA' if n >= 5 else 'AZ' if n >= 1 else 'HİÇ'
def egilim(c):
    if sum(c.values()) == 0: return '—'
    a = (c[2021] + c[2022] + c[2023]) / 3; b = (c[2024] + c[2025]) / 2
    return '↑ yükselen' if b - a >= 1 else '↓ azalan' if a - b >= 1 else '→ sabit'
rows = []
for k, (ad, ders) in K.items():
    c = yc[k]; n = sum(c.values())
    rows.append({'id': k, 'ad': ad, 'ders': ders, 'yillar': [c[y] for y in YIL], 'toplam': n, 'son2': c[2024] + c[2025],
                 'egilim': egilim(c), 'sinif': sinif(n), 'sorular': sorted([q['id'] for q in Q if konu_of(q) == k], key=lambda s: (int(s[:4]), int(s[5:])))})
rows.sort(key=lambda r: (-r['toplam'], -r['son2'], r['ad']))
by = collections.defaultdict(list)
for r in rows: by[r['sinif']].append(r)
KOTA = {'ÇOK': 30, 'ORTA': 13, 'AZ': 6, 'HİÇ': 1}
def larem(items, total, w):
    tw = sum(w(i) for i in items); raw = [total * w(i) / tw for i in items]
    base = [int(x) for x in raw]; rem = total - sum(base)
    for j in sorted(range(len(items)), key=lambda j: -(raw[j] - base[j]))[:rem]: base[j] += 1
    return base
alloc = {}
# ÇOK: 90 slot, toplam ile orantılı; yükselen konuya +%15 ağırlık
cok = by['ÇOK']; n = larem(cok, 90, lambda r: r['toplam'] * (1.15 if r['egilim'].startswith('↑') else 1))
for r, x in zip(cok, n): alloc[r['id']] = x
# ORTA: her konuya 1, kalan 10 slot toplam+son2 ile
orta = by['ORTA']; extra = larem(orta, 39 - len(orta), lambda r: r['toplam'] + r['son2'])
for r, x in zip(orta, extra): alloc[r['id']] = 1 + x
# AZ: 18 slot, öncelik son2, toplam
az = sorted(by['AZ'], key=lambda r: (-r['son2'], -r['toplam']))
for i, r in enumerate(az): alloc[r['id']] = 1 if i < 18 else 0
HIC_SECIM = ['SONRADAN', 'KOTA', 'IHRSAY']
for r in by['HİÇ']: alloc[r['id']] = 1 if r['id'] in HIC_SECIM else 0
# testlere dağıt: her sınıf için test başı kotayı tutturacak şekilde
tests = {r['id']: [0, 0, 0] for r in rows}
for s, q in KOTA.items():
    load = [0, 0, 0]
    items = sorted([r for r in by[s] if alloc[r['id']]], key=lambda r: -alloc[r['id']])
    for r in items:
        for _ in range(alloc[r['id']]):
            # en az yüklü ve bu konudan en az sorusu olan test
            t = min(range(3), key=lambda t: (load[t] >= q, tests[r['id']][t], load[t]))
            tests[r['id']][t] += 1; load[t] += 1
    assert load == [q] * 3, (s, load)
for r in rows: r['test'] = tests[r['id']]; r['karma_toplam'] = sum(tests[r['id']])
json.dump(rows, open(f'{S}/konu/siniflar.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for s in KOTA:
    L = by[s]; print(f"{s}: {len(L)} konu, {sum(r['toplam'] for r in L)} soru, karma {sum(sum(tests[r['id']]) for r in L)}")
for r in rows: print(f"{r['sinif']:4s} {r['toplam']:3d} {r['son2']:2d} {r['egilim']:11s} {r['test']} {r['ders']:6s} {r['ad']}")
ders = collections.Counter()
for r in rows:
    for t in range(3): ders[(t, r['ders'])] += r['test'][t]
print(sorted(ders.items()))
