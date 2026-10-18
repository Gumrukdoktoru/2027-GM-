# İnce konu taksonomisi ve 500 sorunun konu eşlemesi
import json, csv, collections, sys
S = sys.argv[1]
# konu kimliği -> (ad, ders)
K = {
 'TANIM': ('Temel Tanımlar', 'GM'),
 'GENEL': ('Genel Hükümler (Kararlar, Bilgi, Süreler, Belge Saklama)', 'GM'),
 'KIYMET': ('Gümrük Kıymeti', 'GM'),
 'MENSE': ('Menşe (Tercihsiz)', 'GM'),
 'BTB': ('Bağlayıcı Bilgi (BTB/BMB)', 'GM'),
 'OZET': ('Özet Beyan ve Gümrüğe Sunma', 'GM'),
 'GDY': ('Geçici Depolama', 'GM'),
 'BEYAN': ('Gümrük Beyanı ve Basitleştirilmiş Usuller', 'GM'),
 'MUAYENE': ('Muayene, Uygunluk Denetimi ve Teslim', 'GM'),
 'SDG': ('Serbest Dolaşıma Giriş ve Nihai Kullanım', 'GM'),
 'TRANSIT': ('Transit', 'GM'),
 'ANTREPO': ('Antrepo', 'GM'),
 'DIR': ('Dahilde İşleme', 'GM'),
 'HIR': ('Hariçte İşleme, Geçici İhracat ve GKAİR', 'GM'),
 'GI': ('Geçici İthalat (ATA dahil)', 'GM'),
 'IHRG': ('İhracat (Gümrük İşlemleri)', 'GM'),
 'GERIGELEN': ('Geri Gelen Eşya', 'GM'),
 'MUAF': ('Muafiyetler', 'GM'),
 'POSTA': ('Posta ve Hızlı Kargo', 'GM'),
 'KUMANYA': ('Akaryakıt, Kumanya ve Dış Sefer', 'GM'),
 'YUKUM': ('Gümrük Yükümlülüğü', 'GM'),
 'TAHAKKUK': ('Tahakkuk, Tebliğ, Ödeme ve Zamanaşımı', 'GM'),
 'TEMINAT': ('Teminat ve Faiz', 'GM'),
 'GERIVERME': ('Geri Verme ve Kaldırma', 'GM'),
 'CEZA': ('Cezalar (GK 234–241)', 'GM'),
 'UZLASMA': ('Uzlaşma', 'GM'),
 'ITIRAZ': ('İtiraz', 'GM'),
 'YYS': ('Yetkilendirilmiş Yükümlü ve Yerinde Gümrükleme', 'GM'),
 'OKS': ('Onaylanmış Kişi Statüsü', 'GM'),
 'MUSAVIR': ('Gümrük Müşavirliği, Temsil ve Asgari Ücret', 'GM'),
 'YGM': ('Yetkilendirilmiş Gümrük Müşavirliği (YGM)', 'GM'),
 'SINIR': ('Sınır Ticareti', 'GM'),
 'GSM': ('Gümrüksüz Satış Mağazaları', 'GM'),
 'SB': ('Serbest Bölgeler ve Gümrük Statü Belgesi', 'GM'),
 'FSMH': ('Fikri ve Sınai Haklar', 'GM'),
 'TASFIYE': ('Tasfiye', 'GM'),
 'SONRADAN': ('Sonradan Kontrol', 'GM'),
 'TASIT': ('Taşıtların Giriş-Çıkışı', 'GM'),
 'KABOTAJ': ('Kabotaj', 'GM'),
 'SARTLI': ('Şartlı Muafiyet ve Ekonomik Etkili Rejimler (Genel)', 'GM'),
 'AKTRANSIT': ('Akaryakıt Transiti (Transit Seri No 3)', 'GM'),
 'TRBASIT': ('Denizyolu Transiti ve İzinli Gönderici (Transit Seri No 8, 14)', 'GM'),
 'ESIS': ('Varış Öncesi İşlemler, YKTS ve Elektronik Tebligat', 'GM'),
 'KACAK': ('Kaçakçılık (5607)', 'SAİR'),
 'KAMBIYO': ('Kambiyo', 'SAİR'),
 'KDV': ('KDV', 'SAİR'),
 'OTV': ('ÖTV', 'SAİR'),
 'KKDF': ('KKDF ve Fonlar (DFİF)', 'SAİR'),
 'DAMGA': ('Damga Vergisi', 'SAİR'),
 'IHRR': ('İhracat Rejimi ve İhracat Yönetmeliği', 'SAİR'),
 'ITHR': ('İthalat Rejimi Kararı ve İlave Gümrük Vergisi', 'SAİR'),
 'URUN': ('Ürün Güvenliği ve Teknik Düzenlemeler', 'SAİR'),
 'TPS': ('Ticaret Politikası Savunma Araçları', 'SAİR'),
 'MENSEBELGE': ('Tercihli Menşe İspat Belgeleri', 'SAİR'),
 'STA': ('STA/TTA ve Taraf Ülkeler', 'SAİR'),
 'GB': ('Gümrük Birliği (1/95 OKK, A.TR, INF)', 'SAİR'),
 'TESVIK': ('Yatırım Teşvik ve Yabancı Yatırım', 'SAİR'),
 'DTO': ('DTÖ, TFA, Transfer Fiyatlandırması ve Uluslararası Kuruluşlar', 'SAİR'),
 'INCO': ('Teslim Şekilleri (Incoterms)', 'SAİR'),
 'ODEME': ('Ödeme Şekilleri, Taşıma Belgeleri ve CISG', 'SAİR'),
 'TIR': ('TIR Sözleşmesi', 'SAİR'),
 'KOTA': ('Kota ve Tarife Kontenjanı', 'SAİR'),
 'TICHAK': ('Türkiye\'nin Ticari Haklarının Korunması', 'SAİR'),
 'IHRSAY': ('İhracat Sayılan Satış ve Teslimler, 99/13812 Vergi-Harç İstisnası', 'SAİR'),
 'EIHR': ('E-İhracat Destekleri ve Dış Ticaret Sermaye Şirketi', 'SAİR'),
 'ELMAS': ('Ham Elmas ve Nesli Tehlikedeki Türlerin (CITES) Dış Ticareti', 'SAİR'),
 'T_GYKK': ('Tarife – Genel Yorum Kuralları', 'TARİFE'),
 'T_HS22': ('Tarife – HS 2022 Değişiklikleri', 'TARİFE'),
 'T_YAPI': ('Tarife – Cetvel Yapısı, GTİP ve Tarife Hukuku', 'TARİFE'),
 'T_GIDA': ('Tarife – Hayvansal, Bitkisel ve Gıda Ürünleri (Fasıl 1–24)', 'TARİFE'),
 'T_KIMYA': ('Tarife – Mineral, Kimya, Plastik ve Kauçuk (Fasıl 25–40)', 'TARİFE'),
 'T_TEKSTIL': ('Tarife – Deri, Ahşap, Kâğıt ve Tekstil (Fasıl 41–63)', 'TARİFE'),
 'T_METAL': ('Tarife – Ayakkabı, Taş-Cam, Kıymetli Metal ve Metaller (Fasıl 64–83)', 'TARİFE'),
 'T_MAKINE': ('Tarife – Makine ve Elektrik (Fasıl 84–85)', 'TARİFE'),
 'T_TASIT': ('Tarife – Taşıtlar (Fasıl 86–89)', 'TARİFE'),
 'T_CESITLI': ('Tarife – Optik, Saat, Çalgı, Silah, Çeşitli ve Sanat Eşyası (Fasıl 90–97)', 'TARİFE'),
}
DEF = {'GM02':'KIYMET','GM03':'MENSE','GM06':'SDG','GM07':'TRANSIT','GM08':'ANTREPO','GM09':'DIR','GM10':'HIR','GM11':'GI',
 'GM12':'IHRG','GM13':'GERIGELEN','GM14':'MUAF','GM15':'POSTA','GM16':'KUMANYA','GM18':'GERIVERME','GM19':'CEZA','GM20':'YYS',
 'GM21':'MUSAVIR','GM23':'FSMH','GM24':'TASFIYE','SR01':'KACAK','SR02':'KAMBIYO','SR03':'KDV','SR04':'OTV','SR06':'IHRR',
 'SR07':'ITHR','SR08':'URUN','SR09':'TPS','SR10':'MENSEBELGE','SR11':'GB','SR12':'DIR','SR13':'TESVIK','SR14':'DTO','SR16':'TIR',
 'TR03':'T_GYKK'}
O = {}
def put(k, ids):
    for i in ids.split(): O[i] = k
put('TANIM', '21/2 21/13 21/72'); put('GENEL', '21/1 21/3 21/6 22/25 22/54')
put('BTB', '21/16 22/84')
put('OZET', '21/7 21/8 21/10 21/23 21/30 21/36 24/71'); put('GDY', '21/35 22/58 22/59 23/96')
put('BEYAN', '21/20 23/43 23/46 25/23 25/25 25/29'); put('MUAYENE', '22/47 22/77 24/38')
put('YUKUM', '21/38 21/80'); put('TAHAKKUK', '22/3 25/95 24/99'); put('ITIRAZ', '23/41'); put('TEMINAT', '21/39 21/77 22/6 25/93')
put('DIR', '21/32 24/68'); put('UZLASMA', '21/82 23/68 24/12')
put('HIR', '22/8 23/22'); put('GI', '24/92')
put('OKS', '21/18 22/62 25/91'); put('YGM', '21/31 25/98 25/100')
put('SINIR', '21/75 22/30 23/31'); put('GSM', '23/95 25/79'); put('SB', '25/24')
put('KKDF', '22/2 22/5 23/52 24/14 24/64'); put('DAMGA', '24/20 25/1')
put('IHRR', '21/68'); put('KIYMET', '25/3')
put('STA', '22/23 22/34 23/100 24/36 24/40 25/26 25/97'); put('GB', '22/37 23/55 25/27 25/96')
put('INCO', '21/67 22/29 22/65 23/64 23/65 23/71 24/1 25/11'); put('ODEME', '21/52 21/60 21/64 23/62')
put('T_HS22', '22/76 22/79 22/86 24/2 24/56 25/45 25/52')
put('T_YAPI', '21/5 21/59 21/73 22/82 24/46 25/44 25/48 25/53 22/80 23/15')
put('T_GIDA', '21/96 22/83 23/5 23/20 24/51 24/54 25/39 25/50 25/51 24/53 25/43 25/54')
put('T_KIMYA', '21/91 22/78 24/44 25/55 21/98 24/52 25/49')
put('T_TEKSTIL', '23/4 23/14 24/55 21/93 22/75 23/8')
put('T_METAL', '22/85 23/6 23/7 24/48 25/41 21/99 24/58 23/16')
put('T_MAKINE', '23/13 23/21 24/47 24/60 25/46 23/10 23/11 23/17 24/59 24/45')
put('T_TASIT', '23/18 23/19 24/57 25/47')
put('T_CESITLI', '21/92 21/95 22/87 23/9 24/49 25/40 24/50')
r = json.load(open(f'{S}/scripts_topics/rows.json', encoding='utf-8'))
kod = {(int(x['yil']), int(x['no'])): x['kod'] for x in csv.DictReader(open(f'{S}/analysis/konu_eslesme.csv', encoding='utf-8'))}
out = []; miss = []
for x in r:
    qid = f"{x['yil']%100}/{x['no']}"
    k = O.get(qid) or DEF.get(kod[(x['yil'], x['no'])])
    if not k: miss.append((qid, kod[(x['yil'], x['no'])], x['alt'][:60])); continue
    out.append({'id': f"{x['yil']}/{x['no']}", 'yil': x['yil'], 'no': x['no'], 'alan': x['alan'], 'kod': kod[(x['yil'], x['no'])],
                'konu': k, 'alt': x['alt'], 'dayanak': x['dayanak'], 'kok': x['kok'], 'dogru': x['dogru'], 'celdirici': x['celdirici'], 'hedef': x['hedef']})
print('eksik', miss)
json.dump({'konular': K, 'sorular': out}, open(f'{S}/konu/eslesme.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
c = collections.Counter(q['konu'] for q in out)
yc = collections.defaultdict(lambda: collections.Counter())
for q in out: yc[q['konu']][q['yil']] += 1
print(len(out), 'soru', len(K), 'konu', sum(1 for k in K if c[k]), 'çıkan')
for k, n in c.most_common(): print(f'{n:3d} {k:11s} {K[k][0]} ', [yc[k][y] for y in range(2021, 2026)])
print('HİÇ:', [K[k][0] for k in K if not c[k]])
