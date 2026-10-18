#!/usr/bin/env python3
"""Markdown → hap_docx.js blok listesi (katalog gibi uzun belgeler için).
Kullanım: python3 md2blok.py <girdi.md> <cikti.json> <kapak_baslik> <kapak_alt> <ust_bilgi>
# → atlanır (kapak), ## → h1, ### → h2, #### → h3, > → örnek kutusu, | → tablo, - → madde, ``` → mono
"""
import json, re, sys
src, out, kb, ka, ub = sys.argv[1:6]
L = open(src, encoding='utf-8').read().split('\n')
def un(s):
    s = re.sub(r'\\([\\`*_{}\[\]()#+\-.!|>])', r'\1', s)
    return s.rstrip('\\').rstrip()
B = [{'t': 'kapak', 'ust': 'GÜMRÜK MÜŞAVİRLİĞİ SINAVI', 'baslik': kb, 'alt': ka, 'hazirlik': 'Gümrük Müşavirliği Sınavına Hazırlık'}]
i, first_h1 = 0, True
para, madde, ornek, mono = [], [], [], None
def flush():
    global para, madde, ornek
    if para: B.append({'t': 'p', 'metin': un(' '.join(x.strip() for x in para))}); para = []
    if madde: B.append({'t': 'madde', 'maddeler': [un(m) for m in madde]}); madde = []
    if ornek: B.append({'t': 'ornek', 'satirlar': [un(o) for o in ornek]}); ornek = []
while i < len(L):
    l = L[i]
    if mono is not None:
        if l.startswith('```'): B.append({'t': 'mono', 'satirlar': mono}); mono = None
        else: mono.append(l)
        i += 1; continue
    if l.startswith('```'): flush(); mono = []; i += 1; continue
    m = re.match(r'^(#{1,4}) (.*)', l)
    if m:
        flush(); lvl, t = len(m.group(1)), un(m.group(2))
        if lvl == 1: pass
        elif lvl == 2: B.append({'t': 'h1', 'metin': t, 'yeni_sayfa': first_h1 or bool(re.match(r'^\d+\.', t))}); first_h1 = False
        elif lvl == 3: B.append({'t': 'h2', 'metin': t})
        else: B.append({'t': 'h3', 'metin': t})
        i += 1; continue
    if l.startswith('|'):
        flush(); rows = []
        while i < len(L) and L[i].startswith('|'):
            cells = [un(c.strip()) for c in re.split(r'(?<!\\)\|', L[i].strip().strip('|'))]
            if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells if c): rows.append(cells)
            i += 1
        n = max(len(r) for r in rows); rows = [r + [''] * (n - len(r)) for r in rows]
        w = [min(60, max(4, max(len(r[j]) for r in rows))) for j in range(n)]
        B.append({'t': 'tablo', 'basliklar': rows[0], 'satirlar': rows[1:], 'genislik': w})
        continue
    if l.startswith('>'):
        if para or madde: flush()
        ornek.append(l[1:].lstrip()); i += 1; continue
    if re.match(r'^\s*[-*] ', l):
        if para or ornek: flush()
        madde.append(re.sub(r'^\s*[-*] ', '', l)); i += 1
        while i < len(L) and L[i].startswith('  ') and L[i].strip() and not re.match(r'^\s*[-*] ', L[i]):
            madde[-1] += ' ' + L[i].strip(); i += 1
        continue
    if re.match(r'^-{3,}\s*$', l): flush(); i += 1; continue
    if not l.strip(): flush(); i += 1; continue
    if madde or ornek: flush()
    para.append(l); i += 1
flush()
json.dump({'meta': {'baslik': kb, 'ust_bilgi': ub, 'alt_bilgi': 'GM 2027 Hazırlık'}, 'bloklar': B}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'blok')
