#!/usr/bin/env python3
"""Hap dokümanlarının blok listelerini (hap_docx.js girdisi) üretir.
Kullanım: python3 hap_belgeler.py <S> <cikti_dir>
Üretir: konu_siniflari.json, beklenen.json, sorulmayan.json (+ veri/*.json ham birleşik veri)
"""
import json, os, sys, glob, collections, re

def iyelik(n):
    """Sayıya 3. tekil iyelik eki: 18'i, 16'sı, 43'ü, 100'ü."""
    n = int(n)
    if n == 0: return "0'ı"
    son = {1: "i", 2: "si", 3: "ü", 4: "ü", 5: "i", 6: "sı", 7: "si", 8: "i", 9: "u"}
    if n % 10: return f"{n}'{son[n % 10]}"
    on = {10: "u", 20: "si", 30: "u", 40: "ı", 50: "si", 60: "ı", 70: "i", 80: "i", 90: "ı"}
    if n % 100: return f"{n}'{on[n % 100]}"
    return f"{n}'ü" if n % 1000 else f"{n}'i"
S, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, f'{S}/scripts')
rows = json.load(open(f'{S}/konu/siniflar.json', encoding='utf-8'))
R = {r['id']: r for r in rows}
kume = json.load(open(f'{S}/hap/kumeler.json', encoding='utf-8'))
K2 = {k: kid for kid, ks in kume.items() for k in ks}
DERS = {'GM': 'Gümrük Mevzuatı', 'SAİR': 'Sair Mevzuat', 'TARİFE': 'Tarife'}
SIN = [('ÇOK', 'Çok çıkan konular (5 yılda 10 ve üzeri soru)'), ('ORTA', 'Orta çıkan konular (5 yılda 5–9 soru)'),
       ('AZ', 'Az çıkan konular (5 yılda 1–4 soru)'), ('HİÇ', 'Hiç çıkmayan konular (2021–2025)')]
KOTA = {'ÇOK': 30, 'ORTA': 13, 'AZ': 6, 'HİÇ': 1}
def idkey(s): y, n = s.split('/'); return (int(y), int(n))

# ---- veri topla -------------------------------------------------------------
cikan, sorulmayan = {}, {}
for f in sorted(glob.glob(f'{S}/hap/cikan/K*.json')):
    for k in json.load(open(f, encoding='utf-8'))['konular']: cikan[k['konu']] = k
gecersiz = set()
for f in sorted(glob.glob(f'{S}/hap/kontrol/K*.json')):
    rep = json.load(open(f, encoding='utf-8'))
    for b in rep.get('sorulmayan', {}).get('gecersiz', []):
        gecersiz.add((b['konu'], b['tur'], b.get('alt'), b['i']))
for f in sorted(glob.glob(f'{S}/hap/sorulmayan/K*.json')):
    for k in json.load(open(f, encoding='utf-8'))['konular']:
        for a in k.get('alt_konular', []):
            a['sc'] = [x for j, x in enumerate(a.get('sc', [])) if (k['konu'], 'sc', a.get('ad'), j) not in gecersiz]
        k['beklenen'] = [x for j, x in enumerate(k.get('beklenen', [])) if (k['konu'], 'beklenen', None, j) not in gecersiz]
        sorulmayan[k['konu']] = k
# elle çıkarılanlar (eskimiş ya da çelişkili bilgi; gerekçe hap/cikar.json'da)
_cik = json.load(open(f'{S}/hap/cikar.json', encoding='utf-8')) if os.path.exists(f'{S}/hap/cikar.json') else []
for c in _cik:
    k = sorulmayan.get(c['konu'])
    if not k: continue
    if c['tur'] == 'beklenen':
        k['beklenen'] = [x for x in k.get('beklenen', []) if c['icerir'] not in x['metin']]
    else:
        for a in k.get('alt_konular', []):
            a['sc'] = [x for x in a.get('sc', []) if c['icerir'] not in x['s'] + ' ' + x['c']]
# kümeler arası tekrar: aynı kanıt kesitine dayanan soru–cevap/hap yalnız ilk konuda kalır
import unicodedata
def _n(x): return re.sub(r'\s+', ' ', unicodedata.normalize('NFC', x or '')).strip().lower()
seen_sc, seen_b, dup = set(), set(), 0
for r in rows:
    k = sorulmayan.get(r['id'])
    if not k: continue
    for a in k.get('alt_konular', []):
        keep = []
        for x in a.get('sc', []):
            key = _n(x.get('kanit')) + '|' + _n(x.get('s'))[:60]
            if _n(x.get('kanit')) in seen_sc: dup += 1; continue
            seen_sc.add(_n(x.get('kanit'))); keep.append(x)
        a['sc'] = keep
    keep = []
    for x in k.get('beklenen', []):
        if _n(x.get('kanit')) in seen_b: dup += 1; continue
        seen_b.add(_n(x.get('kanit'))); keep.append(x)
    k['beklenen'] = keep
print('kümeler arası tekrar çıkarıldı:', dup)
os.makedirs(f'{OUT}/veri', exist_ok=True)
json.dump(cikan, open(f'{OUT}/veri/cikan_haplar.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(sorulmayan, open(f'{OUT}/veri/sorulmayan.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def kapak(baslik, alt, boyut=56):
    return {'t': 'kapak', 'ust': 'GÜMRÜK MÜŞAVİRLİĞİ SINAVI', 'baslik': baslik, 'alt': alt, 'hazirlik': 'Gümrük Müşavirliği Sınavına Hazırlık', 'boyut': boyut}
def yil_tablo(L, hic=False):
    return {'t': 'tablo', 'basliklar': ['Konu', 'Ders', '21', '22', '23', '24', '25', 'Top.', 'Son 2', 'Eğilim'],
            'genislik': [35.5, 8.5, 5, 5, 5, 5, 5, 7, 9, 15],
            'satirlar': [[r['ad'], DERS[r['ders']].replace('Gümrük Mevzuatı', 'GM').replace('Sair Mevzuat', 'Sair')] + [str(x) for x in r['yillar']] + [str(r['toplam']), str(r['son2']), r['egilim']] for r in L]}
by = collections.defaultdict(list)
for r in rows: by[r['sinif']].append(r)

# ---- 1. KONU SINIFLARI VE ÇIKAN SORULARDAN HAP -----------------------------
def hap_satir(h):
    ids = sorted(set(h.get('sorular', [])), key=idkey)
    yil = {i.split('/')[0] for i in ids}
    star = '★ ' if len(yil) >= 2 else ''
    ref = ' · '.join(x for x in [h.get('dayanak', '').strip(), ', '.join(ids)] if x)
    s = f"{star}{h['metin'].strip()} ({ref})"
    if h.get('tuzak', '').strip(): s += f" — Tuzak: {h['tuzak'].strip()}"
    if h.get('not', '').strip(): s += f" — Not: {h['not'].strip()}"
    if h.get('kaynak_disi'): s += ' ◇'
    return s, len(yil) >= 2
B = [kapak('ÇIKAN SORULARDAN HAP BİLGİ', 'Konu Sınıfları · GM 2021–2025 Çıkmış Soruların Hap Bilgisi')]
B.append({'t': 'h1', 'metin': 'Konu Sınıfları ve Çıkan Sorulardan Hap Bilgi (GM 2021–2025)', 'yeni_sayfa': True})
nkonu = len(rows); nhap = sum(len(cikan.get(r['id'], {}).get('haplar', [])) for r in rows)
B.append({'t': 'kutu', 'paragraflar': [
    f"2021–2025 Gümrük Müşavirliği sınavlarının **500 sorusu** (Gümrük Mevzuatı, Sair Mevzuat ve Tarife; hesap soruları ölçtükleri konuya göre) {nkonu} konuya ayrıldı ve konular dört sınıfa bölündü: **çok çıkan** (5 yılda 10 ve üzeri), **orta çıkan** (5–9), **az çıkan** (1–4), **hiç çıkmayan** (0).",
    "Hap bilgiler çıkmış soruların ölçtüğü bilgiden, **resmî cevap anahtarına** göre yazıldı; birden çok yılda sorulan bilgi tek satırda birleştirildi (★). Bilgisi depodaki mevzuat metinlerinde bulunmayan haplar yalnız soru ve resmî cevaptan kuruldu (◇). Sınav tarihinden sonra değişen hükümler \"Not\" ile gösterildi. Parantez içinde dayanak ve sorunun yılı/numarası yer alır.",
    f"Toplam {nhap} hap. Konu sınıfları üç adet 50 soruluk karma testin dağılımına da esas alındı: test başına {KOTA['ÇOK']} çok çıkan, {KOTA['ORTA']} orta, {KOTA['AZ']} az çıkan ve {KOTA['HİÇ']} hiç çıkmayan konu sorusu."]})
B.append({'t': 'h1', 'metin': '1. KONU SINIFLARI'})
B.append({'t': 'tablo', 'basliklar': ['Sınıf', 'Konu sayısı', '5 yılda soru', 'Karma testte (test başına)'], 'genislik': [40, 18, 18, 24],
          'satirlar': [[ad.split(' (')[0], str(len(by[s])), str(sum(r['toplam'] for r in by[s])), str(KOTA[s])] for s, ad in SIN]})
for s, ad in SIN:
    B.append({'t': 'h2', 'metin': ad}); B.append(yil_tablo(by[s]))
B.append({'t': 'kutu', 'paragraflar': ['21–25: 2021–2025 sınav yılları; Son 2: 2024 ve 2025 toplamı. Eğilim: son iki yılın (2024–2025) yıllık ortalaması ilk üç yılın ortalamasından en az 1 soru fazlaysa yükselen, en az 1 soru azsa azalan. Ders: GM Gümrük Mevzuatı, Sair Sair Mevzuat.']})
B.append({'t': 'h1', 'metin': '2. ÇIKAN SORULARDAN HAP BİLGİ', 'yeni_sayfa': True})
star_n = 0
for s, ad in SIN[:3]:
    B.append({'t': 'h1', 'metin': ad})
    for r in by[s]:
        k = cikan.get(r['id'])
        B.append({'t': 'h2', 'metin': f"{r['ad']} — {r['toplam']} soru ({r['egilim']})"})
        if not k or not k.get('haplar'):
            B.append({'t': 'p', 'metin': '(hap hazırlanmadı)'}); continue
        if k.get('ozet'): B.append({'t': 'etiket', 'metin': k['ozet']})
        L = []
        for h in k['haplar']:
            t, st = hap_satir(h); L.append(t); star_n += st
        B.append({'t': 'madde', 'maddeler': L})
B.append({'t': 'h1', 'metin': 'Hiç çıkmayan konular'})
B.append({'t': 'p', 'metin': 'Aşağıdaki konulardan 2021–2025 sınavlarında soru gelmedi; sorulmamış hükümlerinin hapları **Beklenen Konular Hap Bilgi** dokümanında, soru–cevapları **Sorulmayan Konular Soru–Cevap** dokümanındadır: ' + ', '.join(r['ad'] for r in by['HİÇ']) + '.'})
json.dump({'meta': {'baslik': 'Çıkan Sorulardan Hap Bilgi', 'ust_bilgi': 'GM Çıkan Sorulardan Hap Bilgi', 'alt_bilgi': 'GM 2027 Hazırlık'}, 'bloklar': B},
          open(f'{OUT}/konu_siniflari.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('konu_siniflari', nhap, 'hap', star_n, '★')

# ---- 2. BEKLENEN KONULAR HAP -------------------------------------------------
B = [kapak('BEKLENEN KONULAR HAP BİLGİ', "2021–2025'te Sorulmamış Hükümler · Son Değişiklikler")]
B.append({'t': 'h1', 'metin': 'Çıkması Beklenen Konulardan Hap Bilgi (GM 2027 hazırlık)', 'yeni_sayfa': True})
B.append({'t': 'kutu', 'paragraflar': [
    "Hap bilgiler 2021–2025 GM sınavlarında **hiç sorulmamış hükümlerden** seçildi. Öncelik sırası: (1) çok ve orta çıkan konuların sorulmamış sayı, süre, oran, makam ve şart hükümleri; (2) kaynak metinde yakın tarihli değişiklik notu taşıyan hükümler (**[Yeni]**); (3) son iki yılda yükselen konuların sorulmamış alt başlıkları; (4) çıkmış soruların komşu hükümleri.",
    "Her hap kaynak metindeki karşılığıyla (birebir kesit) doğrulandı; çıkmış sorulardaki bilgi burada tekrarlanmadı. Parantez içinde dayanak madde yer alır."]})
B.append({'t': 'h1', 'metin': '1. ÖNCELİK TABLOSU'})
B.append({'t': 'tablo', 'basliklar': ['Konu', 'Sınıf', '5 yılda', '2024–25', 'Eğilim', 'Hap'], 'genislik': [48, 9, 10, 10, 15, 8],
          'satirlar': [[r['ad'], r['sinif'], str(r['toplam']), str(r['son2']), r['egilim'], str(len(sorulmayan.get(r['id'], {}).get('beklenen', [])))] for r in rows]})
degisen = []
for i, (s, ad) in enumerate(SIN):
    B.append({'t': 'h1', 'metin': f'{i + 2}. {ad}', 'yeni_sayfa': i == 0})
    for r in by[s]:
        k = sorulmayan.get(r['id'])
        B.append({'t': 'h2', 'metin': r['ad']})
        if not k: B.append({'t': 'p', 'metin': '(hazırlanmadı)'}); continue
        if k.get('ozet'): B.append({'t': 'kutu', 'paragraflar': [k['ozet']]})
        L = []
        for h in k.get('beklenen', []):
            yeni = ' **[Yeni]**' if h.get('degisiklik', '').strip() else ''
            L.append(f"{h['metin'].strip()}{yeni} ({h.get('dayanak', '').strip()})")
            if yeni: degisen.append([r['ad'], re.sub(r'\*\*', '', h['metin'].strip()), h.get('dayanak', ''), h['degisiklik']])
        if L: B.append({'t': 'madde', 'maddeler': L})
B.append({'t': 'h1', 'metin': '6. SON DEĞİŞİKLİKLER — TOPLU LİSTE', 'yeni_sayfa': True})
B.append({'t': 'kutu', 'paragraflar': ['Kaynak metinde yakın tarihli değişiklik notu taşıyan hükümler (**[Yeni]**).']})
B.append({'t': 'tablo', 'basliklar': ['Konu', 'Hap', 'Dayanak', 'Değişiklik'], 'genislik': [14, 50, 17, 19], 'satirlar': degisen})
nb = sum(len(k.get('beklenen', [])) for k in sorulmayan.values())
json.dump({'meta': {'baslik': 'Beklenen Konular Hap Bilgi', 'ust_bilgi': 'GM Beklenen Konular Hap Bilgi', 'alt_bilgi': 'GM 2027 Hazırlık'}, 'bloklar': B},
          open(f'{OUT}/beklenen.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('beklenen', nb, 'hap', len(degisen), 'yeni')

# ---- 3. SORULMAYAN KONULAR SORU–CEVAP ---------------------------------------
sira = [r for d in ('GM', 'SAİR', 'TARİFE') for r in rows if r['ders'] == d]
def say(k):
    c = collections.Counter(a.get('durum') for a in k.get('alt_konular', []))
    return c['SORULDU'], c['KISMEN'], c['SORULMADI'], sum(len(a.get('sc', [])) for a in k.get('alt_konular', []))
toplam_sc = sum(say(sorulmayan[r['id']])[3] for r in sira if r['id'] in sorulmayan)
B = [kapak('SORULMAYAN KONULAR', f'2021–2025 GM Çıkmış Sorularında Ölçülmeyen Hükümler · {toplam_sc} Soru–Cevap')]
B.append({'t': 'h1', 'metin': 'Karşılaştırma Özeti', 'yeni_sayfa': True})
B.append({'t': 'madde', 'maddeler': [
    "2021–2025 GM sınavlarının 500 sorusu konu konu sınıflandırıldı; her sorunun ölçtüğü bilgi noktası kitapçık metni ve resmî cevap anahtarıyla kayıt altına alındı.",
    "Her kaynak mevzuat dosyası okunup sınav değeri taşıyan **alt konulara** (hüküm gruplarına) ayrıldı; her alt konu çıkmış sorularla karşılaştırılarak **SORULDU / KISMEN / SORULMADI** olarak işaretlendi.",
    "KISMEN: maddenin bir ayrıntısı sorulmuş, sınav değeri taşıyan diğer ayrıntıları sorulmamış demektir; bu ayrıntılar da soru–cevaba alındı.",
    "Soru–cevaplar yalnızca sorulmamış hükümlerden ve yalnızca depodaki mevzuat metninden üretildi; her cevabın dayanağı kaynak metinden **birebir kesitle** otomatik olarak doğrulandı, doğrulanamayan çiftler setten çıkarıldı.",
    "Şekli maddeler (amaç, yürürlük, yürütme, mülga hükümler) alt konu sayılmadı."]})
B.append({'t': 'h2', 'metin': 'Konu bazında çıkmış soru sayısı ve sorulmayan hükümler'})
T = []
for i, r in enumerate(sira, 1):
    k = sorulmayan.get(r['id'], {}); a, b_, c, n = say(k) if k else (0, 0, 0, 0)
    T.append([str(i), r['ad']] + [str(x) for x in r['yillar']] + [str(r['toplam']), f'{a} / {b_} / {c}', str(n)])
B.append({'t': 'tablo', 'basliklar': ['#', 'Konu', '21', '22', '23', '24', '25', 'Top.', 'Sorulan / Kısmen / Sorulmayan alt konu', 'S–C'],
          'genislik': [5.5, 32, 4.5, 4.5, 4.5, 4.5, 4.5, 7, 19, 6], 'satirlar': T})
B.append({'t': 'dipnot', 'metin': 'Top.: o konuda 2021–2025 sınavlarında sorulan soru sayısı (her soru tek konuya sayıldı; hesap soruları ölçtükleri konuda).'})
B.append({'t': 'h2', 'metin': 'Beş yılda hiç sorulmayan konular'})
B.append({'t': 'madde', 'maddeler': [f"**{r['ad']}** ({sorulmayan.get(r['id'], {}).get('kaynak_ozeti', '')}) — {say(sorulmayan[r['id']])[3] if r['id'] in sorulmayan else 0} soru–cevap" for r in by['HİÇ']]})
B.append({'t': 'h2', 'metin': 'Az sorulan konular (1–4 soru)'})
B.append({'t': 'madde', 'maddeler': [f"**{r['ad']}** — {r['toplam']} soru ({', '.join(r['sorular'])})" for r in by['AZ']]})
gozlem = []
for r in by['ÇOK'][:5]:
    if r['id'] in sorulmayan:
        a, b_, c, n = say(sorulmayan[r['id']]); t = a + b_ + c
        if t: gozlem.append(f"{r['ad']}: {t} alt konunun {iyelik(c)} hiç, {iyelik(b_)} kısmen sorulmuştur ({r['toplam']} soruya rağmen).")
if gozlem:
    B.append({'t': 'h2', 'metin': 'Gözlemler'})
    B.append({'t': 'madde', 'maddeler': ['En çok sorulan konularda bile sorulmamış alan geniştir. ' + ' '.join(gozlem)] +
              [f"Son iki yılda yükselen konular: {', '.join(r['ad'] for r in rows if r['egilim'].startswith('↑'))}."]})
B.append({'t': 'h1', 'metin': 'Sorulmayan Konular — Soru–Cevap', 'yeni_sayfa': True})
B.append({'t': 'p', 'metin': 'Sorular açık uçludur; cevabı kapatıp kendinizi deneyin. Her cevabın sonunda dayanak madde yer alır. Çıkmış sorularda ölçülen bilgi noktaları bu bölümde tekrar edilmemiştir.'})
for i, r in enumerate(sira, 1):
    k = sorulmayan.get(r['id'])
    if not k: continue
    n = say(k)[3]
    if not n: continue
    B.append({'t': 'h1', 'metin': f"{i}. {r['ad']}"})
    B.append({'t': 'etiket', 'metin': f"{r['ad']} · {k.get('kaynak_ozeti', '')} · Beş yılda {r['toplam']} soru · {n} soru–cevap"})
    no = 0
    for a in k.get('alt_konular', []):
        if not a.get('sc'): continue
        B.append({'t': 'h2', 'metin': a['ad']})
        for x in a['sc']:
            no += 1; B.append({'t': 'sc', 'no': no, 's': x['s'].strip(), 'c': x['c'].strip(), 'dayanak': x.get('dayanak', '').strip()})
json.dump({'meta': {'baslik': 'Sorulmayan Konular', 'ust_bilgi': 'GM Sorulmayan Konular Soru–Cevap', 'alt_bilgi': 'GM 2027 Hazırlık'}, 'bloklar': B},
          open(f'{OUT}/sorulmayan.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('sorulmayan', toplam_sc, 'soru–cevap')
