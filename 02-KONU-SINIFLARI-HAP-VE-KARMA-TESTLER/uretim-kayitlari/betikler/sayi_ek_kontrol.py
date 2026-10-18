#!/usr/bin/env python3
"""Metindeki sayı+kesme işareti eklerini (18'i, 16'sı, 30'da…) ses uyumuna göre denetler.
Kullanım: python3 sayi_ek_kontrol.py <metin.txt> ...
"""
import re, sys
# sayının okunuşundaki son kelimenin son ünlüsü ve ünsüzle bitip bitmediği
SON = {0: ('ı', 0), 1: ('i', 0), 2: ('i', 1), 3: ('ü', 0), 4: ('ö', 0), 5: ('e', 0), 6: ('ı', 1), 7: ('i', 1), 8: ('i', 0), 9: ('u', 0)}
ONLAR = {10: ('o', 0), 20: ('i', 1), 30: ('u', 0), 40: ('ı', 0), 50: ('i', 1), 60: ('ı', 0), 70: ('i', 0), 80: ('e', 0), 90: ('a', 0)}
def son(n):
    if n % 10 or n == 0: return SON[n % 10]
    if n % 100: return ONLAR[n % 100]
    if n % 1000: return ('ü', 0)   # yüz
    return ('i', 0)                # bin
YUV = {'a': 'a', 'ı': 'a', 'o': 'a', 'u': 'a', 'e': 'e', 'i': 'e', 'ö': 'e', 'ü': 'e'}
DAR = {'a': 'ı', 'ı': 'ı', 'o': 'u', 'u': 'u', 'e': 'i', 'i': 'i', 'ö': 'ü', 'ü': 'ü'}
SERT = set('fstkçşhp')
def okunus_sert(n):
    """Okunuşun son harfi ünsüzse o ünsüz, ünlüyse boş dizi."""
    if n == 0: return 'r'                                   # sıfır
    d = {1: 'r', 2: '', 3: 'ç', 4: 't', 5: 'ş', 6: '', 7: '', 8: 'z', 9: 'z'}
    if n % 10: return d[n % 10]
    t = {10: 'n', 20: '', 30: 'z', 40: 'k', 50: '', 60: 'ş', 70: 'ş', 80: 'n', 90: 'n'}
    if n % 100: return t[n % 100]
    return 'z' if n % 1000 else 'n'
def beklenen(n, ek):
    v, unlu_bitis = son(n)
    unlu_bitis = okunus_sert(n) == ''
    s = okunus_sert(n)
    y, dar = YUV[v], DAR[v]
    ek0 = ek.lower()
    adaylar = {
        'iyelik': (('s' if unlu_bitis else '') + dar),
        'bulunma': ('t' if s in SERT else 'd') + ('a' if y == 'a' else 'e'),
        'ayrilma': ('t' if s in SERT else 'd') + ('a' if y == 'a' else 'e') + 'n',
        'yonelme': ('y' if unlu_bitis else '') + ('a' if y == 'a' else 'e'),
        'tamlayan': ('n' if unlu_bitis else '') + dar + 'n',
        'ile': ('l' if unlu_bitis else 'l') + ('a' if y == 'a' else 'e'),
    }
    tip = None
    if re.fullmatch(r's?[ıiuü]', ek0): tip = 'iyelik'
    elif re.fullmatch(r'[dt][ae]', ek0): tip = 'bulunma'
    elif re.fullmatch(r'[dt][ae]n', ek0): tip = 'ayrilma'
    elif re.fullmatch(r'y?[ae]', ek0): tip = 'yonelme'
    elif re.fullmatch(r'n?[ıiuü]n', ek0): tip = 'tamlayan'
    if not tip: return None
    return adaylar[tip]
bad = 0
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    for m in re.finditer(r"(?<![\d.,/])(\d{1,7})['’]([a-zçğıöşü]{1,3})\b", t):
        n = int(m.group(1)); ek = m.group(2)
        e = beklenen(n, ek)
        if e and e != ek.lower():
            bad += 1
            print(f"{f.split('/')[-1]}: {m.group(0)} → {n}'{e}  …{t[max(0,m.start()-40):m.end()+20].replace(chr(10),' ')}…")
print('hatalı', bad)
