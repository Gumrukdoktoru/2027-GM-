# Çapraz okuma sonrası bağımsız kontrol (B16-01, B16-02, B11-04, B03-17, B10-03, B13-04, B16-08)

Bu kontrolde hiçbir soru dosyası değiştirilmedi. Tarama betikleri: `$S/karma2/work_capraz_sonrasi/scan_b1601.py`, `scan_b1602.py`, `scan_b1608.py`.
Dosya sayıları değişmedi: B03 17, B10 4, B11 10, B13 13, B16 9.

## Özet

| id | Karar | Kısa gerekçe |
|---|---|---|
| B16-01 | TAMAM | Kör hesap 1.627.200 (E). Dört çeldirici dört ayrı tek hatadan geliyor. 0–2 hatalı hiçbir yol doğru tutarı vermiyor. Kur ve oran dilimi kökte veri olarak var. D3 HS-B-11'in kur tuzağı soruda artık yok. (Not: D2 HS-B-08'e yakınlık) |
| B16-02 | TAMAM (açıklamada küçük düzeltme önerisi) | Kör hesap 58.000 (C). 234/1-b, 234/4 (iki cümlesi) ve 234/6 güncel metinle uyumlu. AYM 26.03.2026 kararıyla da uyumlu. Ceza matrahı kökte tek tutar olarak veriliyor. Açıklamadaki "hiçbir iki hatanın birleşimi doğru tutarı vermez" ifadesi mutlak olarak doğru değil. |
| B11-04 | TAMAM | Seri No 7 md. 8/2 ile birebir. Dört çeldiricinin dördü de kesin yanlış. K07-05, D3 GM-C-22 ve D2 GM-C-12 ile tekrar yok. B07-02 ile ipucu yok. |
| B03-17 | TAMAM (tuzak cümlesinde küçük düzeltme önerisi) | I, III ve IV doğru, II yanlış (TIR Tebliği 34/2, 34/7, 34/6, 34/4). Cevap "I, III ve IV" ve tek. |
| B10-03 | TAMAM | I, II ve III doğru, IV yanlış (ÜGD 2026/23 md. 4/1, 4/3, 4/4, 9/1). Cevap "I, II ve III" ve tek. |
| B13-04 | TAMAM | Uzatılmış şık hâlâ 29.39'da (24.04 hariç (b)). Anlam değişmedi. Diğer dört şık 24.04'te. |
| B16-08 | TAMAM | Kör hesap 3.150.000 (D). Kökten peşin ödeme kuru çıkarılınca açıklama, tuzak ve şıklarda ondan iz kalmadı. Her şık tek bir hatadan geliyor ve tarama temiz. |

Anahtarı değişmesi gereken soru yok. Zorunlu düzeltme yok. Aşağıdaki iki metin önerisi isteğe bağlıdır.

---

## 1. B16-01 (Test 4, KDV/ÖTV hesabı): TAMAM

**Kör çözüm:**
- Kıymet: 20.000 × 45 = 900.000 TL.
- GV 90.000; İGV 180.000.
- ÖTV matrahı: 900.000 + 90.000 + 180.000 = 1.170.000 TL. Bu tutar 1.000.000 TL'yi aşıyor, bu yüzden matrahın tamamına %80 uygulanır: ÖTV 936.000.
- KDV matrahı 2.106.000; KDV 421.200.
- Toplam 1.627.200 TL. Anahtar (`dogru`: 4) bu tutarı gösteriyor.

**Kaynak:**
- `kaynak2/genelge/ozel_tuketim_vergisi_ii_sayili_liste_uygulama_genel_tebligi.md`, satır 1077–1089 ("İthalatta Matrah"): ithalat sırasında ödenen her türlü vergi matraha girer (ÖTV ve KDV hariç).
- Aynı dosya, satır 1107–1119 (B- ORAN): ÖTV, matraha listedeki oran uygulanarak hesaplanır. Cumhurbaşkanı "oranlara esas özel tüketim vergisi matrahlarının alt ve üst sınırlarını" belirlemeye yetkilidir. Yani oran dilimini ÖTV matrahı belirler ve oran matrahın tamamına uygulanır.
- Aynı dosya, satır 123–125, 209 ve 233: kullanılmak üzere ithalat ilk iktisaptır ve ÖTV ithalatta doğar. Motorlu araç ticareti yapanlar satmak üzere ithal ettiğinde bu aşamada ÖTV uygulanmaz. Kökteki "(A) motorlu araç ticareti ile uğraşmamaktadır" ifadesi bu ayrımı netleştiriyor.

**Kökteki veriler:**
- Tek kur var: tescil tarihi kuru (45). GK md. 30 ile tutarlı.
- Oran dilimleri (1.000.000 TL'ye kadar %60, aşanlarda %80) ile GV, İGV ve KDV oranları "varsayılmaktadır" kaydıyla kökte veri olarak veriliyor.
- "Aşmayanlarda / aşanlarda" ifadesi aracı sınıflandırıyor, tutarı dilimlere bölmüyor. Dilimli (artan oranlı) okuma kaynakla da çelişiyor.

**0–2 hatalı yol taraması (12 hata türü):**

| Şık | Tek hata | Hesap |
|---|---|---|
| 1.216.800 | İGV ÖTV matrahına katılmamış | Matrah 990.000 → %60 |
| 1.346.400 | Oran dilimi gümrük kıymetine göre seçilmiş | |
| 1.387.200 | ÖTV dilimli (artan oranlı) hesaplanmış | |
| 1.440.000 | ÖTV KDV matrahına eklenmemiş | |

- Şıklarda olmayan tek hata sonuçları: GV ÖTV matrahına katılmamış 1.540.800; İGV KDV matrahına katılmamış 1.591.200; GV KDV matrahına katılmamış 1.609.200; ÖTV yalnız kıymet üzerinden 1.152.000; ÖTV gümrükte alınmamış 504.000; İGV kıymet + GV üzerinden 1.666.080.
- İki farklı tek hata aynı şıkkı vermiyor.
- 0–2 hatalı hiçbir yol 1.627.200'ü vermiyor.
- "İGV katılmamış" hatası dilimli hesap ya da kıymete göre dilim hatasıyla birleşince yine 1.216.800 çıkıyor. Bunun nedeni 990.000 TL'nin zaten alt dilimde kalması. Zararsız.

**Deneme 3 HS-B-11 ile karşılaştırma: artık aynı kurgu değil.**
- HS-B-11: (IV) sayılı listede televizyon; FOB'a navlun, sigorta ve satış şartı lisans eklenir; peşin ödeme kuru ile tescil kuru karşılaştırılır.
- B16-01'den peşin ödeme kuru ve buna dayanan çeldirici (1.699.520) çıkarıldı.
- Ortak kalan yalnız iki genel unsur var: "GV + İGV + ÖTV + KDV toplamı" biçimi ve her KDV hesabında görülen "ÖTV KDV matrahına eklenmemiş" çeldirici ailesi.

**Not (zorunlu düzeltme değil): Deneme 2 HS-B-08 ile yakınlık.**
- Ortam B16-01'e HS-B-11'den daha yakın: (II) sayılı liste, binek otomobil, motorlu araç ticareti yapmayan firmanın ithalatında ÖTV.
- Çeldiricilerin ikisi aynı hükümlere dokunuyor:
  - D2'deki 1.880.000 ("ÖTV yalnız kıymet üzerinden") ↔ B16-01'deki 1.216.800 ("İGV ÖTV matrahına katılmamış"); hüküm ÖTVK 11/3.
  - D2'deki 1.830.000 ↔ B16-01'deki 1.440.000 ("ÖTV KDV matrahına eklenmemiş"); hüküm KDVK 21.
- Cevabı belirleyen hüküm ise farklı: oran dilimi ÖTV matrahına göre seçilir ve oran matrahın tamamına uygulanır. Bu hüküm D2'de yok.
- Önceki doğrulama (`dogrulama/B16.md`, satır 25) bu yakınlığı kabul etmişti. Risk düşük.

---

## 2. B16-02 (Test 4, GK 234 ceza hesabı): TAMAM, açıklamada küçük düzeltme önerisi

**Kör çözüm:**
- I: 18.000 × 3 = 54.000 TL.
- II: 500 × 3 = 1.500 TL. 234/6'daki alt sınır nedeniyle ceza 2.000 TL olur.
- III: Belediyeye 234/4 uyarınca 234'teki cezalar uygulanmaz; 241/1'e göre 2.000 TL.
- Toplam 58.000 TL. Anahtar (`dogru`: 2) bu tutarı gösteriyor.

**Güncel metin (`kaynak/txt/48-cezalar.txt` satır 21–29; `kaynak2/gm/48_48-cezalar.md` satır 43–69):**
- 234/1-b: "noksanlığa ait ithalat vergilerinden başka vergi farkının üç katı".
- 234/4: "Genel yönetim kapsamındaki kamu idareleri için yukarıda belirtilen cezalara ilişkin hükümler uygulanmaz. Bu gibi hallerde, 241 inci maddenin birinci fıkra hükmüne göre işlem yapılır."
- 234/6: "Bir ila üçüncü fıkralara göre verilen cezalar 241 inci maddenin birinci fıkrasında belirtilen miktardan az olamaz."
- Üç hüküm de soruyla birebir uyumlu.

**AYM 26.03.2026 kararı ile uyum (`48-cezalar.txt` satır 106):**
- 241/1'in yürürlükteki metni "bu Kanuna (…) aykırı hareket edenlere … usulsüzlük cezası uygulanır" biçiminde. Yalnız ikincil düzenlemelere aykırılık ibaresi çıkmış.
- Usulsüzlük cezası miktarı yürürlükte. 234/4 ve 234/6'nın 241/1'e atfı da yürürlükte.
- Belediyenin aykırılığı Kanuna aykırılıktır (noksan kıymet) ve 241/1'in uygulanacağı 234/4'te açıkça yazılı. Bu nedenle karar soruyu etkilemiyor.

**Ceza matrahına giren vergiler kökte açık mı?**
- Kök her bent için tek bir "ithalat vergileri farkı" tutarı veriyor ve "Ceza hesabında yalnız yukarıda verilen vergi farkları esas alınacaktır" diyor.
- Aday vergileri ayrıştırmak zorunda kalmıyor. KDV'nin matrahta olup olmadığı tartışması hesaba girmiyor. TEST_BRIEF2 §7 karşılanıyor.
- Kat (3) ve 241/1 miktarı (2.000 TL) kökte veri olarak veriliyor.

**0–2 hatalı yol taraması:**

| Şık | Tek hata | Hesap |
|---|---|---|
| 56.000 | Belediyeye hiç ceza verilmemiş | |
| 57.500 | Alt sınır uygulanmamış | |
| 59.500 | Alt sınır hesaplanan cezaya ayrıca eklenmiş | 54.000 + 3.500 + 2.000 |
| 74.000 | Belediyeye üç kat ceza uygulanmış | |

Ancak açıklamadaki "Tarama: … hiçbir iki hatanın birleşimi doğru tutarı vermez" ifadesi mutlak olarak doğru değil:
- **II. bentte yarım ceza (234/1-c) uygulamak:** 250 TL çıkar, alt sınır onu 2.000 TL'ye tamamlar, sonuç yine 58.000 olur. Kökte maddi hesap hatası ya da miktar farkı geçmediği için bu doğal bir hata değil. Ayrıca alt sınır sorularında bu maskelenme kaçınılmaz.
- **Düşük olasılıklı iki çift hata da 58.000 veriyor:**
  - "II'ye hiç ceza yok" + "belediyeye 241/3 uyarınca iki kat (4.000)".
  - "II'de alt sınır iki kat (4.000)" + "belediyeye ceza yok".
- **56.000 ikinci bir yoldan da çıkıyor:** "II'ye hiç ceza verilmez" (500 TL'lik küçük fark) hatası. Bu hata şıkta yazılan "belediyeye ceza yok" türetiminden farklı ama aynı sayıyı veriyor. Olasılığı düşük.

**Önerilen açıklama düzeltmesi (isteğe bağlı):** son cümle olan "Tarama: tek hatalar birbirinden farklı sonuç verir; hiçbir iki hatanın birleşimi doğru tutarı vermez." yerine şu konsun:

> "Dört çeldirici dört ayrı tek hatadan türer; II. bentte alt sınırın altında kalan her hesap alt sınırla 2.000 TL'ye tamamlandığından bu bentte ölçülen bilgi alt sınırın kendisidir."

**Tekrar kontrolü:**
- **234/6 alt sınırı ilk kez ölçülüyor.** K06-07 açıklamasında ve D3 HS-B-14 dayanağında yalnız anılıyor, hiçbir şıkta ölçülmüyor.
- **234/4'ün ikinci cümlesi ilk kez ölçülüyor.** D1 GM-C-08'in IV. öncülünden 241/1 atfı çıkarılmıştı.
- **234/4'ün ilk cümlesi kısmen tekrar.** Bu cümle D1 GM-C-08'in IV. öncülünde doğru öncül olarak ölçüldü. B16-02'de 74.000 çeldiricisi ve III. bentin çözümü bu cümleye de dayanıyor. Kurgu farklı (sözel öncül yerine hesap). Belirleyici yeni unsurlar 234/6 ve 234/4'ün ikinci cümlesi. Kabul edilebilir.
- **Kısmi muafiyetli geçici ithalat ile tam muafiyetli geçici ithalat ayrımı (234/1–234/2) sorudan tamamen çıktı.** D1 GM-C-08 ve K06-07 ile örtüşme bu yüzden kalmadı.
- Aynı testte (Test 4) 234'ü ölçen başka soru yok. B06-02 GK 231, 232, 233 ve GY 579, 582'yi; B16-03 uzlaşmayı ölçüyor.

---

## 3. B11-04 (Test 5, Seri No 7 md. 8/2): TAMAM

**Kaynak:** `kaynak2/genelge/gumruk_genel_tebligi_x1uluslararasi_anlasmalarx2_seri_no_7.md`, satır 65: "Aranan belgelerden bir kısmının başvuru dosyasında yer almadığının tespit edilmesi halinde başvuru sahibine eksik belgelerin tamamlanması için yazılı olarak 1 aylık ek süre verilir. Başvuru sahibine bildirimin yapıldığı tarihten itibaren bu süre içinde eksiklikleri tamamlanmayan başvuru dosyaları kendilerine iade edilir." Doğru şık (A) bu metinle birebir aynı.

**Çeldiricilerin hepsi kesin yanlış:**
- Üç aylık ek süre: Tebliğde yok. "Üçer aylık" ifadesi yalnız 11/1-c'deki liste dönemleri için geçiyor.
- Altı aylık ek süre: Tebliğde yok. "Altı ay" 13/1'deki askı süresi.
- Bir ay + ret + bir yıl yeniden başvuru yasağı: Tebliğde ret ya da başvuru yasağı yok. "Bir yıl" 14/4'teki geri alma süresinin alt sınırı.
- Ek süresiz ret: 8/2 ile çelişiyor.

**Tekrar:**
- K07-05 (GY 26/5, OKS iptali geçmişe etkili, iki yıl yasak) ve D3 GM-C-22 (OKS Tebliği md. 59, iki uyarı sonra altı ay askı) md. 8/2'ye dokunmuyor. Yeni soruda iptal ya da askı kuralı ölçülmüyor; "altı ay" yalnız yanlış bir ek süre rakamı olarak geçiyor.
- D2 GM-C-12 (OKS Tebliği, eksik beyan usulünde "bir ay içinde ibraz") başka bir hüküm. Ortak olan yalnız "bir ay" rakamı.
- İlk sette, denemelerde ve ikinci sette Seri No 7 md. 8 başka hiçbir yerde yok.

**Aynı testte ipucu (Test 5):**
- B07-02 ihracatta yerinde gümrükleme iznini ölçüyor. Onaylanmış ihracatçı, eksik belge, ek süre ya da iade içeriği yok; ipucu yok.
- Test 5'in diğer sorularında da onaylanmış ihracatçı, fatura beyanı ya da başvuru ek süresi geçmiyor.

**Etiket:** `kaynak_tipi: beklenen` doğru. `hap/sorulmayan/K11.json`'a göre Seri No 7 2021–2025'te hiç sorulmadı.

---

## 4a. B03-17 (Test 6, TIR Tebliği md. 34): TAMAM, tuzak cümlesinde küçük öneri

**Kaynak:** `kaynak2/gm/21_21-TIR_SÖZLEŞMESİ.md`, satır 537–553.

**Öncüller tek tek:**
- **I doğru (34/2):** "nedeninin üç ay içinde belgelendirilmesi istenir … Üç aylık takibat süresi talep halinde … üç ay uzatılır. Haklı sebebin varlığı halinde … bir ay daha uzatılabilir."
- **II yanlış (34/4):** Kaynak "faslın **en yüksek** vergiye tabi pozisyonuna göre" diyor; öncülde "en düşük" yazıyor.
- **III doğru (34/7):** "Kap adedi olarak beyana uygun, ancak sayı, baş, ağırlık gibi ölçülerinde … eksiklik veya fazlalık olan eşya için takibat yapılmaz."
- **IV doğru (34/6 ikinci cümle):** "takibat ve varsa cezaî işlem, eksiklik veya fazlalığın tamamı için değil, bu oranları aşan kısmı için uygulanır." Yeni öncül bu cümleyle birebir uyumlu.

**Sonuç:**
- Doğru kombinasyon I, III ve IV. Şıklarda yalnız D ("I, III ve IV") buna uyuyor. Anahtar (`dogru`: 3) doğru.
- 04.07.2026 TIR değişikliği md. 20'ye dokunmuş, md. 34'e dokunmamış.
- Açıklama yeni anahtarla tutarlı.

**İsteğe bağlı düzeltme (tuzak alanı):** Mevcut cümle ilk yanılgıyı da "IV'ü yanlış saymak" sonucuna bağlıyor. Oysa en düşük vergili pozisyon yanılgısı II'yi doğru saydırır. Önerilen metin:

> "Pozisyonu belirlenemeyen eşyada yükümlü lehine en düşük vergili pozisyonun esas alınacağını sanıp II'yi doğru saymak ya da oran aşılınca eksikliğin tamamının takibe gireceğini sanıp IV'ü yanlış saymak."

**Komşu sorular (işlem gerekmez):**
- D3 GM-C-29'un B şıkkı GK 237/4'ü ölçüyor: dökme eşyada tolerans içindeki farklar için takibat yapılmaz. IV ise toleransı aşan kısmı ölçüyor (34/6 ikinci cümle). Farklı hüküm.
- B06-02 (Test 4) GY 582'yi ölçüyor ("en düşük vergi oranı"). Farklı test ve farklı hüküm.

---

## 4b. B10-03 (Test 6, ÜGD 2026/23): TAMAM

**Kaynak:** `kaynak2/diger/SAİR MEVZUAT KİTABI.md`, satır 16523–16592.

**Öncüller tek tek:**
- **I doğru (md. 4/1):** Metal Hurda İthalatçı Belgesi kaydı; ergiterek işlem yapan ya da ön işlem uygulayan; Geçici Faaliyet Belgesi ya da Çevre İzin ve Lisans Belgesine sahip sanayiciler.
- **II doğru (md. 4/3, satır 16536):** Belge "verildiği tarihten itibaren İKİ (2) YIL GEÇERLİDİR"; listesi Bakanlığın internet sayfasında ilan edilir.
- **III doğru (md. 4/4):** Ek-2'deki hurdaların serbest bölgeler dâhil Türkiye Gümrük Bölgesine girişi yasak. Transit geçişte izin yazısı sınır giriş gümrük idaresine ibraz edilir.
- **IV yanlış (md. 9/1):** Denetimi "ilgili gümrük idaresinin bulunduğu Çevre, Şehircilik ve İklim Değişikliği İl Müdürlüğü" yapar. Nükleer Düzenleme Kurumu md. 4/2 uyarınca yalnız radyasyon altyapısını değerlendirir.

**Sonuç:**
- Doğru kombinasyon I, II ve III. Şıklarda yalnız D ("I, II ve III") buna uyuyor. Anahtar (`dogru`: 3) doğru.
- Açıklama ve tuzak yeni anahtarla tutarlı.
- Tekrar yok. D1 SR-C-05 katı yakıt tebliğine ait.
- Test 6'da B11-07'nin cevabı da "I, II ve III". İki sorunun şık kümeleri farklı; sorun değil.

---

## 5. B13-04 (Test 4, olumsuz kök, 24.04): TAMAM

**Uzatılmış şık:** "Tütün yapraklarından ekstraksiyon yoluyla elde edilen nikotin (alkaloid)".

**Hâlâ 24.04 dışında:**
- `kaynak/txt/FASIL24.txt` satır 131, 24.04 hariç (b): "Nikotin, (tütünden ekstrakte edilen toksik alkaloid ile sentez yoluyla elde edilen alkaloid) (29.39 pozisyonu)".
- Aynı dosya, satır 91, 24.03 hariç (a) aynı sonucu veriyor.
- "Tütün yapraklarından ekstraksiyon yoluyla" eklemesi "tütünden ekstrakte edilen" anlamını değiştirmiyor; kapsamı da daraltmıyor.
- Aday şıkkı 24.03'teki tütün hülasası (satır 88) sansa bile eşya yine 24.04'te değil. Olumsuz kökün tek cevabı korunuyor.

**Diğer dört şık kesin olarak 24.04'te:**
- Tek kullanımlık e-sigara: (A)(5), satır 122.
- Elektrikle ısıtılan tütün sistemi çubukları: (A)(2), satır 119 (2404.11).
- Tütünsüz, ağız yoluyla kullanılan nikotinli ürünler: 2404.91.
- Transdermal nikotin bantları: 2404.92; ayrıca `FASIL30.txt` Not 1(b) bunları 24.04'e gönderiyor.

**Uzunluk:** Şık uzunlukları 196 / 108 / 85 / 89 / 72 karakter. Cevap şıkkı artık kısalığıyla göze batmıyor.

---

## 6. B16-08 (Test 6, KDV matrahı): TAMAM

**Kör çözüm:**
- Kıymet: 1.200 × 50 × 40 = 2.400.000 TL.
- GV 240.000; İGV 480.000.
- Ardiye: antrepoya giriş–10 Mart döneminden 1.200 adede isabet eden 12.000 TL ile 10 Mart–12 Mayıs dönemindeki 18.000 TL.
- KDV matrahı 3.150.000 TL. Anahtar (`dogru`: 3) bu tutarı gösteriyor.
- Dayanak: GK 30 ve GY 57 (kur); KDVK 21/c (tescil tarihine kadar yapılmış ve vergilendirilmemiş giderler).

**Peşin ödeme kuru çıkarıldıktan sonra:**
- Kökte yalnız iki tescil kuru (38 ve 40) kaldı.
- Açıklamada "ilk beyannamenin tescil kuru (38) bu beyanname için kullanılmaz" ifadesi var. 36 TL'lik kur ya da peşin ödeme hiçbir yerde (kök, açıklama, tuzak) geçmiyor.
- 2.994.000 çeldiricisi kökte hâlâ bulunan 38 TL'lik kurdan türetilebiliyor.

**0–2 hatalı yol taraması:**

| Şık | Tek hata |
|---|---|
| 2.994.000 | İlk beyannamenin kuru (38) kullanılmış |
| 3.132.000 | Kesim çizgisi ilk tescil tarihi alınmış |
| 3.138.000 | Yalnız 18.000 TL'lik ardiye eklenmiş |
| 3.158.000 | 800 adede isabet eden 8.000 TL de eklenmiş |

- İki farklı tek hata aynı şıkkı vermiyor.
- 0–2 hatalı hiçbir yol 3.150.000'i vermiyor. Ek olarak taranan hatalar: ardiyenin kıymete katılması, İGV'nin kıymet + GV üzerinden hesaplanması, GV ya da İGV'nin KDV matrahına katılmaması, 2.000 adedin tamamının bu beyannameye alınması.

**Etiket:**
- 2021/87 (ödeme günü kuru değil, tescil kuru) bağı peşin kur çıkınca zayıfladı. "Her beyanname kendi tescil kuruyla" bilgisi aynı kurala (GK 30) dayandığı için bu atıf savunulabilir.
- `cikmis` etiketini asıl 2023/82 (21/c: tescile kadar yapılan giderler) taşıyor.
- K09-09 (ilk set) tescil öncesi ve sonrası ardiye ayrımını ölçmüştü. B16-08'in yeni unsuru, antrepodan parça parça çekilen eşyada her beyannamenin kendi kesim tarihi ve kendi kuru. Önceki doğrulama bu yakınlığı kabul etmişti (`dogrulama/B16.md`, satır 24).
