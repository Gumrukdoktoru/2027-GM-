#!/usr/bin/env python3
"""Birleşik karma testi okunur md'ye döker (çapraz kontrol için).
Kullanım: python3 karma_md.py <S>  → $S/karma/birlesik/KARMA-TEST-<n>.md
"""
import json, sys
S = sys.argv[1]; L = 'ABCDE'
for t in (1, 2, 3):
    qs = json.load(open(f'{S}/karma/birlesik/test{t}.json', encoding='utf-8'))
    o = [f'# GM KARMA TEST {t}\n']
    for q in qs:
        o.append(f"## {q['no']}. ({q['id']} · {q['_blok']} · {q['_konu_ad']} · {q['_sinif']} · {q.get('kaynak_tipi')} {', '.join(q.get('cikmis_ref') or [])})\n")
        if q.get('ortak_veri'): o.append('ORTAK VERİ: ' + q['ortak_veri'] + '\n')
        if q.get('kok_on'): o.append(q['kok_on'] + '\n')
        for i, x in enumerate(q.get('onculler') or []): o.append(f'{["I","II","III","IV","V","VI"][i]}. {x}')
        if q.get('tablo'): o.append('TABLO: ' + json.dumps(q['tablo'], ensure_ascii=False))
        o.append('\n' + q['kok'] + '\n')
        for i, s in enumerate(q['siklar']): o.append(f'{L[i]}) {s}')
        o.append(f"\n**Cevap: {q['cevap']}**\n\nAçıklama: {q['aciklama']}\n\nTuzak: {q.get('tuzak','')}\n\nDayanak: {q.get('dayanak','')}\n")
    open(f'{S}/karma/birlesik/KARMA-TEST-{t}.md', 'w', encoding='utf-8').write('\n'.join(o))
    print(t, len(qs))
