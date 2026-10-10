#!/usr/bin/env python3
"""Zorluk etiketlerini denetler: 100 nesne, id/no eşleşmesi, 10/20/40/20/10, geçerli kalıp."""
import json, sys, collections
B, DER = sys.argv[1:3]
KAL = set('HESAP OLAY KAPSAM_DIŞI YANLIŞ ÖNERMELİ EŞLEŞTİRME DOĞRU SÜRE BOŞLUK KAVRAM KAPSAM BELGE ZORUNLULUK YETKİ ORAN-TUTAR MUAFİYET TANIM SONUÇ SIRALAMA'.split())
ok = True
for d in (1, 2, 3):
    qs = json.load(open(f'{B}/deneme{d}.json', encoding='utf-8'))
    try: der = json.load(open(f'{DER}/deneme{d}.json', encoding='utf-8'))
    except Exception as e: print(d, 'YOK', e); ok = False; continue
    m = {x['id']: x for x in der}
    err = []
    if len(der) != 100: err.append(f'{len(der)} nesne')
    for q in qs:
        x = m.get(q['id'])
        if not x: err.append(f"eksik {q['id']}"); continue
        if x.get('no') != q['no']: err.append(f"no {q['id']} {x.get('no')}≠{q['no']}")
        if x.get('kalip') not in KAL: err.append(f"kalıp {q['no']} {x.get('kalip')}")
        if not (x.get('ozet') or '').strip(): err.append(f"özet boş {q['no']}")
        if len(x.get('ozet') or '') > 260: err.append(f"özet uzun {q['no']} {len(x['ozet'])}")
    zc = collections.Counter(x.get('zorluk') for x in der)
    if [zc[k] for k in ('ÇK', 'K', 'O', 'Z', 'ÇZ')] != [10, 20, 40, 20, 10]: err.append(f'zorluk {dict(zc)}')
    cik = sum(1 for x in der if x.get('cikmis'))
    print(d, 'TAMAM' if not err else 'HATA', f'çıkmış {cik}', dict(collections.Counter(x.get('kalip') for x in der).most_common(6)), err[:10])
    ok &= not err
sys.exit(0 if ok else 1)
