#!/usr/bin/env python3
"""Birleşik karma test verisini deneme_docx.js girdisine çevirir.
Kullanım: python3 karma_hazirla.py <S> <cikti_dir>
"""
import json, os, sys, collections
S, OUT = sys.argv[1:3]
KD = sys.argv[3] if len(sys.argv) > 3 else 'karma'
import glob, re
os.makedirs(OUT, exist_ok=True)
L = 'ABCDE'
R = {r['id']: r for r in json.load(open(f'{S}/konu/siniflar.json', encoding='utf-8'))}
SIN_AD = {'ÇOK': 'Çok çıkan', 'ORTA': 'Orta çıkan', 'AZ': 'Az çıkan', 'HİÇ': 'Hiç çıkmayan'}
ZOR = {'K': 'Kolay', 'O': 'Orta', 'Z': 'Zor'}
for t in sorted(int(re.search(r'test(\d+)', f).group(1)) for f in glob.glob(f'{S}/{KD}/birlesik/test*.json')):
    qs = json.load(open(f'{S}/{KD}/birlesik/test{t}.json', encoding='utf-8'))
    # blok başlıkları (numara aralığıyla)
    groups = collections.OrderedDict()
    for q in qs: groups.setdefault(q['_blok'], []).append(q)
    for ad, g in groups.items():
        for q in g: q['_blok'] = f"{ad} ({g[0]['no']}–{g[-1]['no']})"
    sets = collections.defaultdict(list)
    for q in qs:
        if q.get('ortak_veri_id'): sets[q['ortak_veri_id']].append(q['no'])
    for q in qs:
        if q.get('ortak_veri'):
            ns = sorted(sets[q['ortak_veri_id']])
            q['_ortak_baslik'] = f'{ns[0]} ve {ns[-1]} numaralı soruları aşağıdaki verilere göre cevaplayınız.' if len(ns) == 2 else f'{ns[0]}–{ns[-1]} numaralı soruları aşağıdaki verilere göre cevaplayınız.'
        r = R['HESAP' if q['alan'] == 'HESAP' else q['konu']]
        ek = f" · {SIN_AD[r['sinif']]} ({r['toplam']} soru)"
        if q.get('kaynak_tipi') == 'cikmis' and q.get('cikmis_ref'): ek += ' · çıkmış bilgi: ' + ', '.join(q['cikmis_ref'])
        elif q.get('kaynak_tipi') == 'beklenen': ek += ' · beklenen hüküm'
        if q['alan'] == 'HESAP': konu_ad = f"Hesaplama – {q['_hesap_turu']}"
        else: konu_ad = r['ad'] if r['ad'].split(' – ')[0] == q['_ders'] else f"{q['_ders']} – {r['ad']}"
        q['_etiket'] = konu_ad + ek
    sc = collections.Counter(q['_sinif'] for q in qs)
    dc = collections.Counter(q['_ders'] for q in qs if q['alan'] != 'HESAP'); h = sum(1 for q in qs if q['alan'] == 'HESAP')
    zc = collections.Counter(q.get('zorluk', 'O') for q in qs)
    kc = collections.Counter(q.get('kaynak_tipi') for q in qs)
    blok_txt = ' · '.join(f"{g[0]['no']}–{g[-1]['no']} {ad}" for ad, g in groups.items())
    bilgiler = [
        ['Set', f'GM Karma Test {t} (KT{t})'],
        ['Model', '2021–2025 Gümrük Müşavirliği sınavlarının konu sınıfları: çok çıkan konular çok, hiç çıkmayan konular en fazla 1 soruyla'],
        ['Soru sayısı', f"50 ({sc['ÇOK']} çok çıkan + {sc['ORTA']} orta + {sc['AZ']} az + {sc['HİÇ']} hiç çıkmayan konu)"],
        ['Ders dağılımı', ' · '.join(f'{k} {v}' for k, v in dc.items()) + f' · Hesaplama {h}'],
        ['Süre', '75 dakika'],
        ['Blok düzeni', blok_txt],
        ['Zorluk', ' · '.join(f'{ZOR[k]} {zc[k]}' for k in 'KOZ')],
        ['Bilgi kaynağı', f"Çıkmış bilgi alanı {kc['cikmis']} · Beklenen (hiç sorulmamış) hüküm {kc['beklenen']}"],
    ]
    notlar = ['Her sorunun yalnız bir doğru cevabı vardır. Sorular 2021–2025 Gümrük Müşavirliği sınavlarının konu sınıflarına göre dağıtılmış ve özgün olarak hazırlanmıştır; çıkmış soruların kopyası değildir. Bölüm B\'de her sorunun üstünde konusu, sınıfı ve bilgi kaynağı yazılıdır.']
    hc = collections.Counter(L[q['dogru']] for q in qs)
    dag = [['Doğru cevap harfi', list(L), [str(hc[c]) for c in L]],
           ['Konu sınıfı', [SIN_AD[k] for k in ('ÇOK', 'ORTA', 'AZ', 'HİÇ')], [str(sc[k]) for k in ('ÇOK', 'ORTA', 'AZ', 'HİÇ')]],
           ['Zorluk', [ZOR[k] for k in 'KOZ'], [str(zc[k]) for k in 'KOZ']],
           ['Ders', list(dc.keys()) + ['Hesaplama'], [str(v) for v in dc.values()] + [str(h)]]]
    konu_c = collections.Counter((q['_konu_ad'], SIN_AD[q['_sinif']]) for q in qs)
    konu_tablo = [[f'{k} ({s})', str(v)] for (k, s), v in sorted(konu_c.items(), key=lambda x: (-x[1], x[0]))]
    uretim = [
        'Konu sınıfları 2021–2025 GM sınavlarının 500 sorusunun konu konu sayımına dayanır: çok çıkan (5 yılda 10 ve üzeri soru), orta (5–9), az (1–4), hiç çıkmayan (0). Analizdeki alan ayrımına uygun olarak 59 hesap sorusu ayrı Hesaplama konusuna sayıldı (çok çıkan; kıymet, KDV, ceza gibi konuların sayıları yalnız sözel sorulardır). Ayrıntı: Konu Sınıfları ve Çıkan Sorulardan Hap Bilgi dokümanı.',
        'Her testte 30 çok çıkan, 13 orta, 6 az ve 1 hiç çıkmayan konu sorusu var; çok çıkan konuların soru sayısı 5 yıllık sıklıklarıyla orantılıdır (yükselen konulara küçük ek ağırlık). En çok çıkan konu olan Hesaplamadan (59 soru) her testte 6–7 soru var.',
        ('Çok çıkan konulardaki soruların yaklaşık yarısı çıkmış soruların ölçtüğü bilgi alanını yeni bir kurguyla sorar (çıkmış soru numarası Bölüm B etiketinde yazılı); diğerleri hiç sorulmamış ama sorulma ihtimali yüksek hükümlerdendir (Beklenen Konular Hap Bilgi).' if KD == 'karma' else
         'Bu ikinci sette (Test 4–6) ağırlık hiç sorulmamış ama sorulma ihtimali yüksek hükümlerdedir (Beklenen Konular Hap Bilgi). Karma Test 1–3\'te ve üç deneme sınavında cevabı belirleyen bilgi olarak ölçülen hiçbir hüküm burada tekrar edilmemiştir; çıkmış bilgi alanı kullanılan sorularda ilk setin kullanmadığı çıkmış sorular seçilmiştir (çıkmış soru numarası Bölüm B etiketinde yazılı).'),
        'Hesap soruları çıkmış hesap sorularının iskeleti üzerine sayılar ve kalemler değiştirilerek kurulmuştur; her şıkkın hangi hatadan türediği gerekçede yazılıdır.',
        'Sorular depodaki mevzuat metinlerine (Gümrük Kanunu ve Yönetmeliği bölümleri, tebliğler, Sair Mevzuat Kitabı, tarife fasılları) dayanır; her soru cevaba bakmadan çözen bağımsız bir doğrulamadan geçirilmiştir.',
        'Yıllık güncellenen tutarlar (ceza, teminat, ücret tarifesi) doğru cevap yapılmamış; gerektiğinde soruda veri olarak verilmiştir.',
        f'Doğru cevap dağılımı: her harf {hc["A"]} kez; aynı harf en fazla üç kez üst üste.']
    hafiza = [f"KT{t}-{q['no']:03d} | {q['_ders']} | {q['_konu_ad']} | {SIN_AD[q['_sinif']]} | {q.get('alt_tip', '')} | {ZOR.get(q.get('zorluk', 'O'), 'Orta')} | {L[q['dogru']]} | {', '.join(q.get('cikmis_ref') or []) or 'beklenen'} | GM-KT{t}" for q in qs]
    meta = {'ust_baslik': 'GÜMRÜK MÜŞAVİRLİĞİ SINAVI', 'baslik': f'GM KARMA TEST {t}', 'alt_baslik': '50 Soru · 75 Dakika · Konu Sınıflarına Göre Karma',
            'hazirlik': 'Gümrük Müşavirliği Sınavına Hazırlık', 'ust_bilgi': f'GM Karma Test {t}', 'alt_bilgi': f'GM Karma Test {t}', 'bilgiler': bilgiler, 'notlar': notlar}
    json.dump({'meta': meta, 'sorular': qs, 'dagilim': dag, 'konu_tablo': konu_tablo, 'uretim_notu': uretim, 'hafiza': hafiza},
              open(f'{OUT}/test{t}_docx.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(t, len(qs), dict(sc))
