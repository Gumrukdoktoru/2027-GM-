#!/usr/bin/env python3
"""Birleşik deneme verisini Word üreticisinin girdisine çevirir.
Kullanım: python3 deneme_hazirla.py <birlesik_dir> <derece_dir> <cikti_dir>
"""
import json, os, sys, collections

B, DER, OUT = sys.argv[1:4]
os.makedirs(OUT, exist_ok=True)
L = 'ABCDE'
DERS = {'GM': 'Gümrük Mevzuatı', 'SAİR': 'Sair Mevzuat', 'TARİFE': 'Tarife', 'HESAP': 'Hesaplama'}
KONU = {
 'GM02':'Gümrük Kıymeti','GM03':'Menşe, BTB/BMB','GM04':'Özet Beyan, Geçici Depolama','GM05':'Gümrük Beyanı, Muayene',
 'GM06':'Serbest Dolaşım, Nihai Kullanım','GM07':'Transit','GM08':'Antrepo','GM09':'Dahilde İşleme','GM10':'Hariçte İşleme / GKAİR',
 'GM11':'Geçici İthalat','GM12':'İhracat (gümrük)','GM13':'Geri Gelen Eşya','GM14':'Muafiyetler','GM15':'Posta ve Hızlı Kargo',
 'GM16':'Akaryakıt, Kumanya','GM17':'Yükümlülük, Teminat, Tecil','GM18':'Geri Verme – Kaldırma','GM19':'Cezalar, Uzlaşma, İtiraz',
 'GM20':'YYS, Onaylanmış Kişi','GM21':'Gümrük Müşavirliği, Temsil','GM22':'Gümrüksüz Satış, Sınır Ticareti, Serbest Bölge',
 'GM23':'Fikri ve Sınai Haklar','SR01':'Kaçakçılık (5607)','SR02':'Kambiyo','SR03':'KDV','SR04':'ÖTV','SR05':'Damga Vergisi, KKDF',
 'SR06':'İhracat Rejimi','SR07':'İthalat Rejimi','SR08':'Ürün Güvenliği, TAREKS','SR10':'Tercihli Ticaret, Menşe Belgeleri',
 'SR12':'Dahilde İşleme (Ticaret)','SR14':'DTÖ, TFA, DGÖ','SR15':'Incoterms, Ödeme Şekilleri','SR16':'TIR, ATA',
 'TR01':'Fasıl/Pozisyon Kapsamı','TR02':'Bölüm/Fasıl Notları','TR03':'GYKK','TR04':'Tanımı Verilen Eşya','TR05':'GTİP Yapısı, HS, 474',
 'HESAP':'Hesap'}
ROT = {('GM', 1): 'Genel Hükümler', ('GM', 2): 'Tasfiye', ('GM', 3): 'Genel Hükümler, Gümrük İdareleri',
       ('SAİR', 1): 'Yatırım Teşvik (2025/9903)', ('SAİR', 2): 'Ticaret Politikası Önlemleri', ('SAİR', 3): '1/95 OKK, Gümrük Birliği'}
MODEL = {1: '2025 sınavı', 2: '2022 sınavı', 3: '2023 sınavı'}

def blok_ad(qs):
    alan = {q['alan'] for q in qs}
    a, b = qs[0]['no'], qs[-1]['no']
    if alan == {'HESAP'}: ad = 'Hesaplama'
    elif alan == {'TARİFE'}: ad = 'Tarife'
    elif alan == {'SAİR'}: ad = 'Sair Mevzuat'
    elif alan == {'GM'}: ad = 'Gümrük Mevzuatı'
    else: ad = 'Gümrük Mevzuatı ve Sair Mevzuat'
    return f'{ad} ({a}–{b})'

for d in (1, 2, 3):
    qs = json.load(open(os.path.join(B, f'deneme{d}.json'), encoding='utf-8'))
    dp = os.path.join(DER, f'deneme{d}.json')
    der = {x['id']: x for x in json.load(open(dp, encoding='utf-8'))} if os.path.exists(dp) else {}
    # bloklar: sözel / hesap / tarife değişimlerinde böl
    kind = lambda q: 'S' if q['alan'] in ('GM', 'SAİR') else q['alan']
    groups = []
    for q in qs:
        if groups and kind(groups[-1][-1]) == kind(q): groups[-1].append(q)
        else: groups.append([q])
    for g in groups:
        ad = blok_ad(g)
        for q in g: q['_blok'] = ad
    # ortak veri başlıkları
    sets = collections.defaultdict(list)
    for q in qs:
        if q.get('ortak_veri_id'): sets[q['ortak_veri_id']].append(q['no'])
    for q in qs:
        if q.get('ortak_veri'):
            ns = sorted(sets[q['ortak_veri_id']])
            q['_ortak_baslik'] = f'{ns[0]} ve {ns[-1]} numaralı soruları aşağıdaki verilere göre cevaplayınız.' if len(ns) == 2 else f'{ns[0]}–{ns[-1]} numaralı soruları aşağıdaki verilere göre cevaplayınız.'
        konu = KONU.get(q['konu']) or ROT.get((q['alan'], d), q['konu'])
        x = der.get(q['id'], {})
        q['_ders'] = x.get('ders') or DERS[q['alan']]
        q['_konu'] = x.get('konu') or konu
        q['_etiket'] = q['_konu'] if q['_konu'].split(' – ')[0] == q['_ders'] else f"{q['_ders']} – {q['_konu']}"
    # bilgiler
    blok_txt = ' · '.join(f"{g[0]['no']}–{g[-1]['no']} {blok_ad(g).split(' (')[0]}" for g in groups)
    cik = sum(1 for q in qs if der.get(q['id'], {}).get('cikmis'))
    zc = collections.Counter(der[q['id']]['zorluk'] for q in qs if q['id'] in der)
    bilgiler = [
        ['Set', f'GM Deneme {d} (D{d})'],
        ['Model', f'2021–2025 Gümrük Müşavirliği sınavları esas (resmî cevap anahtarlarıyla); blok düzeni {MODEL[d]}'],
        ['Soru sayısı', '100 (42 Gümrük Mevzuatı + 30 Sair Mevzuat + 17 Tarife + 11 Hesaplama)'],
        ['Süre', '150 dakika'],
        ['Blok düzeni', blok_txt],
    ]
    if der:
        bilgiler.append(['Zorluk', ' · '.join(f'{k} {zc[k]}' for k in ('ÇK', 'K', 'O', 'Z', 'ÇZ'))])
        bilgiler.append(['Çıkmış bilgi alanı karşılayan soru', str(cik)])
    notlar = ['Her sorunun yalnız bir doğru cevabı vardır. Sorular 2021–2025 Gümrük Müşavirliği sınavlarında (resmî cevap anahtarlarıyla) ölçülen bilgi alanları ve Bakanlık soru dili esas alınarak özgün olarak hazırlanmıştır; çıkmış soruların kopyası değildir.']
    # dağılım
    hc = collections.Counter(L[q['dogru']] for q in qs)
    dag = [['Doğru cevap harfi', list(L), [str(hc[c]) for c in L]]]
    if der:
        dag.append(['Zorluk', ['ÇK', 'K', 'O', 'Z', 'ÇZ'], [str(zc[k]) for k in ('ÇK', 'K', 'O', 'Z', 'ÇZ')]])
        kc = collections.Counter(der[q['id']]['kalip'] for q in qs if q['id'] in der)
        ks = [k for k, _ in kc.most_common()]
        dag.append(['Soru kalıbı', ks, [str(kc[k]) for k in ks]])
    konu_c = collections.Counter(q['_konu'] for q in qs)
    konu_tablo = [[k, str(v)] for k, v in sorted(konu_c.items(), key=lambda x: (-x[1], x[0]))]
    uretim = [
        f'Deneme, 2021–2025 Gümrük Müşavirliği sınavlarının 500 sorusunun soru-soru analizine dayanır: alan dağılımı (42/30/17/11), {MODEL[d]}nın blok düzeni, 5 yıllık konu frekansları ve soru tipi reçetesi (00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR/12-SORU-TIPI-KATALOGU).',
        '2021–2025 sınavlarının resmî cevap anahtarları, cevaplı kitapçıklardaki kırmızı işaretlerden çıkarılmış ve çıkmış soru analizinde esas alınmıştır. Çıkmış sorunun ölçtüğü bilgi yeni bir kurguyla sorulmuş; metin, şık ve kurgu kopyalanmamıştır.',
        'Sorular depodaki mevzuat dosyalarına (Kanun ve Yönetmelik bölümleri, tebliğler, Sair Mevzuat Kitabı, tarife fasılları ve izahname, sınıflandırma kararları) ve çıkmış soruların doğrulanmış ifadelerine dayanır.',
        'Hesap soruları çıkmış hesap sorularının iskeleti üzerine sayılar ve kalemler değiştirilerek kurulmuştur; her şıkkın hangi hatadan türediği gerekçede yazılıdır.',
        'Her soru, cevaba bakmadan çözen bağımsız bir doğrulamadan, ardından denemenin bütünü üzerinden çapraz kontrolden (sızıntı, çelişki, tekrar) geçirilmiştir.',
        'Kaynak metin resmî bir çıkmış soru cevabından farklıysa soru güncel kaynak metne göre kurulmuştur (ör. KDV Kanunu md. 21/ç, 24.07.2025).',
        'GK 241/1’e ilişkin AYM 26.03.2026 tarihli kararından etkilenen ibare (ikincil düzenlemelere aykırılık) doğru cevap ya da doğru ifade olarak kullanılmamıştır.',
        'Yıllık güncellenen tutarlar (asgari ücret tarifesi, yeniden değerleme tutarları, tecil eşikleri) doğru cevap yapılmamış; gerektiğinde tutar soruda veri olarak verilmiştir.',
        f'Doğru cevap dağılımı: her harf {hc["A"]} kez; aynı harf en fazla üç kez üst üste.',
    ]
    if der: uretim.insert(5, 'Zorluk dereceleri göreli olarak verilmiştir: deneme içindeki 100 soru kolaydan zora sıralanıp 10 ÇK, 20 K, 40 O, 20 Z, 10 ÇZ dağıtılmıştır.')
    hafiza = []
    for q in qs:
        x = der.get(q['id'])
        if not x: continue
        hafiza.append(f"GM{d}-{q['no']:03d} | {q['_ders']} | {q['_konu']} | {x.get('ozet','').strip()} | {x.get('kalip','')} | {x.get('zorluk','')} | {L[q['dogru']]} | GM-D{d}")
    meta = {'ust_baslik': 'GÜMRÜK MÜŞAVİRLİĞİ SINAVI', 'baslik': f'GM DENEME SINAVI {d}',
            'alt_baslik': '100 Soru · 150 Dakika · 2021–2025 Sınavları Esas', 'hazirlik': 'Gümrük Müşavirliği Sınavına Hazırlık',
            'ust_bilgi': f'GM Deneme Sınavı {d}', 'alt_bilgi': f'GM Deneme {d}', 'bilgiler': bilgiler, 'notlar': notlar}
    json.dump({'meta': meta, 'sorular': qs, 'dagilim': dag, 'konu_tablo': konu_tablo, 'uretim_notu': uretim, 'hafiza': hafiza},
              open(os.path.join(OUT, f'deneme{d}_docx.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(d, 'derece' if der else 'derecesiz', len(qs), 'çıkmış', cik)
