#!/usr/bin/env python3
"""Çapraz kontrol yamalarını küme JSON dosyalarına uygular.
Kullanım: python3 yama_uygula.py <out_dir> <yama.json> [<yama2.json> ...]
Şık eşlemesi içerikle yapılır (birleştirmede şıklar karıştırıldığı için indeks kullanılmaz).
"""
import json, sys, glob, os, difflib

OUT = sys.argv[1]
files = {}
index = {}
for f in glob.glob(os.path.join(OUT, '*.json')):
    d = json.load(open(f, encoding='utf-8'))
    files[f] = d
    for i, q in enumerate(d):
        index[q['id']] = (f, i)

def best(lst, s):
    if s in lst: return lst.index(s)
    for i, x in enumerate(lst):
        if s.strip() and (s.strip() in x or x.strip() in s): return i
    m = difflib.get_close_matches(s, lst, n=1, cutoff=0.6)
    return lst.index(m[0]) if m else None

ok = fail = 0
log = []
for yf in sys.argv[2:]:
    for p in json.load(open(yf, encoding='utf-8')):
        pid = p.get('id')
        if pid not in index:
            log.append(f'BULUNAMADI {pid}'); fail += 1; continue
        f, i = index[pid]; q = files[f][i]
        alan = p.get('alan'); eski = p.get('eski'); yeni = p.get('yeni')
        try:
            if alan == 'yeniden_yaz':
                yeni = dict(yeni); yeni['id'] = pid
                for k in ('deneme', 'alan', 'konu', 'alt_tip'):
                    yeni.setdefault(k, q[k])
                assert len(yeni['siklar']) == 5 and 0 <= yeni['dogru'] <= 4
                files[f][i] = yeni
            elif alan in ('kok', 'kok_on', 'aciklama', 'tuzak', 'dayanak', 'ortak_veri'):
                cur = q.get(alan) or ''
                if eski and eski in cur:
                    q[alan] = cur.replace(eski, yeni, 1)
                elif not eski:
                    q[alan] = yeni
                else:
                    raise ValueError(f'eski metin bulunamadı ({alan})')
            elif alan in ('siklar', 'onculler'):
                lst = q[alan]
                j = best(lst, eski) if eski else None
                if j is None: raise ValueError(f'eski {alan} öğesi bulunamadı')
                if eski in lst[j] and eski != lst[j]:
                    lst[j] = lst[j].replace(eski, yeni, 1)
                else:
                    lst[j] = yeni
            elif alan == 'dogru_icerik':
                j = best(q['siklar'], yeni)
                if j is None: raise ValueError('doğru şık metni bulunamadı')
                q['dogru'] = j
            else:
                raise ValueError(f'bilinmeyen alan {alan}')
            ok += 1; log.append(f'UYGULANDI {pid} {alan}')
        except Exception as e:
            fail += 1; log.append(f'HATA {pid} {alan}: {e}')
for f, d in files.items():
    for q in d:
        assert len(q['siklar']) == 5 and len(set(q['siklar'])) == 5, q['id']
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(log)); print(f'uygulandı {ok}, hata {fail}')
