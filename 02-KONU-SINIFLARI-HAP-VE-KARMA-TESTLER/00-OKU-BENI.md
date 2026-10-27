# GÜMRÜK MÜŞAVİRLİĞİ SINAVI — KONU SINIFLARI, HAP BİLGİLER VE KARMA TESTLER (2027 sınavına hazırlık)

Bu klasör, 2021–2025 Gümrük Müşavirliği sınavlarının 500 sorusunu konu konu sayarak 77 konuyu dört sınıfa ayırır: **çok çıkan**, **orta çıkan**, **az çıkan** ve **hiç çıkmayan**. Bu ayrıma dayanan dört çalışma dokümanı ve 50'şer soruluk üç karma test içerir. Dokümanlar örnek alınan "Konu Sınıfları ve Çıkan Sorular Hap", "Beklenen Konular Hap", "Sorulmayan Konular Soru–Cevap" ve "Soru Tipi Kataloğu" düzeninde hazırlandı.

## Dosyalar

| Dosya | İçerik |
|---|---|
| `01-KONU-SINIFLARI-VE-CIKAN-SORULAR-HAP` (.pdf / .docx, 71 sayfa) | Konu sınıfları tabloları (yıl yıl soru sayısı, son 2 yıl, eğilim) ve her konu için **çıkmış sorulardan hap bilgi**: 565 hap (Hesaplama bölümü kıymet, KDV matrahı, ceza, ÖTV, uzlaşma, antrepo teminatı, İGV/MIN-MAX ve diğer hesaplar diye gruplu), her biri hangi soruda çıktığıyla (ör. `2024/61`), tuzağıyla ve notuyla |
| `02-BEKLENEN-KONULAR-HAP` (.pdf / .docx, 67 sayfa) | Her konuda **henüz sorulmamış ama sorulma ihtimali yüksek** hükümler: 719 hap, 125'i değişiklik notu taşıyan hükümlerden (**[Yeni]** etiketli); sonda "Son Değişiklikler — Toplu Liste" |
| `03-SORULMAYAN-KONULAR-SORU-CEVAP` (.pdf / .docx, 333 sayfa) | Her konunun alt konuları SORULDU / KISMEN / SORULMADI diye işaretli; sorulmayan ve kısmen sorulan alt konular için **2.659 soru–cevap**, her cevap mevzuat dayanağıyla |
| `04-SORU-TIPI-KATALOGU` (.pdf / .docx, 36 sayfa) | 500 sorunun 39 alt tipe ve 9 biçim bayrağına ayrıldığı katalog (`00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR/12-SORU-TIPI-KATALOGU.md`'nin örnek düzeninde baskısı) |
| `KARMA-TEST-1` (.pdf / .docx) | **Tam test.** Kapak, Sınav Bilgileri, Bölüm A (soru kitapçığı), Cevap Anahtarı, Bölüm B (cevaplı ve gerekçeli sorular), Dağılım, Üretim Notu, Hafıza Güncellemesi |
| `KARMA-TEST-1_SORU-KITAPCIGI` (.pdf / .docx) | Yalnız sorular; yazdırıp 75 dakikada çözmek için |
| `KARMA-TEST-2…`, `KARMA-TEST-3…` | Aynı düzende Test 2 ve 3 |
| `KARMA-TEST-4…`, `KARMA-TEST-5…`, `KARMA-TEST-6…` | **İkinci set**, aynı düzende ve aynı dağılım kurallarıyla; Test 1–3'te ve üç denemede ölçülen hiçbir hükmü tekrar etmez (aşağıda "İkinci set") |
| `veri/` | Makine verisi: `konu_siniflari.json` (77 konu — Hesaplama dahil —, yıl yıl sayım, sınıf, eğilim, soru listesi), `soru_konu_eslesmesi.json` (500 sorunun alanı ve içerik konusu; `alan: HESAP` olanlar Hesaplama konusuna sayılır), `cikan_sorular_hap.json`, `beklenen_ve_sorulmayan.json`, `karma-test1..6.json` |
| `uretim-kayitlari/` | Ajan talimatları, konu kümeleri, test slotları, küme doğrulama raporları, çapraz kontrol yamaları ve betikler (dokümanların nasıl üretildiğinin kaydı); ikinci setinkiler `uretim-kayitlari/ikinci-set/` altında |

## Konu sınıfları (2021–2025, 500 soru)

Sayım, analizdeki alan ayrımıyla aynıdır (Gümrük Mevzuatı 222 · Sair Mevzuat 143 · Tarife 76 · Hesaplama 59). **Hesap soruları içerik konusuna değil ayrı "Hesaplama" konusuna sayıldı:** Gümrük Kıymeti, KDV, ÖTV, Cezalar gibi konuların sayıları yalnız sözel sorulardır (ör. Gümrük Kıymeti 15 sözel soru; kıymet hesabı 32 soru Hesaplama'da).

Sınıf sınırları: **çok çıkan** 5 yılda 10 ve üzeri soru · **orta** 5–9 · **az** 1–4 · **hiç çıkmayan** 0. Eğilim, son 2 yılın ortalamasının ilk 3 yılın ortalamasından en az 1 soru farklı olmasına göre "yükselen / azalan / sabit" olarak verildi.

| Sınıf | Konu | Toplam soru | Konular |
|---|---|---|---|
| Çok çıkan | 16 | 267 | **Hesaplama 59** (kıymet hesabı 32, KDV matrahı 9, ceza 5, ÖTV 4, uzlaşma 2, antrepo teminatı 2, İGV ve MIN/MAX 2, diğer 3) · Kaçakçılık (5607) 22 · Transit 21 · Tercihli Menşe İspat Belgeleri 17 · Muafiyetler 16 · Kambiyo 16 · Antrepo 15 · Gümrük Kıymeti 15 · Tarife Fasıl 1–24 12 · Dahilde İşleme 12 · İhracat Rejimi 12 · Geçici İthalat 10 · Tarife Fasıl 84–85 10 · ÖTV 10 · Tarife Cetvel Yapısı/GTİP 10 · Posta ve Hızlı Kargo 10 |
| Orta çıkan | 26 | 168 | YYS ve Yerinde Gümrükleme, Geri Gelen Eşya, Incoterms, TIR, STA/TTA, HS 2022, Gümrük Birliği, Fikri Haklar, Ürün Güvenliği, GYKK, Özet Beyan, Beyan, Müşavirlik, Tercihsiz Menşe, İhracat, Kumanya, DTÖ, Hariçte İşleme, Geri Verme, KKDF, İthalat Rejimi ve İGV, Genel Hükümler ve diğer tarife fasıl grupları |
| Az çıkan | 23 | 65 | Serbest Dolaşım ve Nihai Kullanım, **KDV (sözel 4)**, Tarife Taşıtlar, Teminat ve Faiz, Geçici Depolama, **Ticaret Politikası Savunma Araçları**, Ödeme Şekilleri, Tahakkuk-Tebliğ-Zamanaşımı, YGM, **Cezalar (sözel 3)**, Muayene, Onaylanmış Kişi, Sınır Ticareti, Tanımlar, Yatırım Teşvik, Damga Vergisi, Gümrüksüz Satış, BTB/BMB, Yükümlülük, Tasfiye, Serbest Bölgeler, Uzlaşma, İtiraz |
| Hiç çıkmayan | 12 | 0 | Akaryakıt Transiti · Denizyolu Transiti ve İzinli Gönderici · E-İhracat ve DTSŞ · Ham Elmas ve CITES · Kabotaj · Kota ve Tarife Kontenjanı · Sonradan Kontrol · Taşıtların Giriş-Çıkışı · Ticari Hakların Korunması · Varış Öncesi İşlemler, YKTS ve E-Tebligat · İhracat Sayılan Satış ve 99/13812 · Şartlı Muafiyet (Genel) |

Ayrıntılı tablo (yıl yıl sayılar ve eğilim) 01 numaralı dokümanın başında.

## Hap satırı nasıl okunur?

`★ Hap metni (dayanak · 2021/31, 2024/61) — Tuzak: … — Not: … ◇`

- **★** Hapın ölçtüğü bilgi en az iki farklı yılda soruldu.
- **(dayanak · yıl/soru)** Mevzuat maddesi ve bilginin çıktığı soru numaraları.
- **Tuzak** Sınavda bu bilginin hangi çarpıtmayla yanlış şık yapıldığı.
- **Not** Mevzuat değişikliği, resmî anahtarın tartışmalı olduğu durumlar, dikkat edilecek ayrım.
- **◇** Bilgi depodaki kaynak metinde yok; çıkmış sorunun doğrulanmış ifadesine ya da uluslararası metnin bilinen hükmüne dayanıyor.

Beklenen konular dokümanında **[Yeni]** etiketi, kaynak metinde değişiklik notu taşıyan hükmü gösterir (çoğu 2023–2026 değişiklikleri); değişiklik tarihi "Son Değişiklikler — Toplu Liste" tablosunda.

## Karma testler

Her testte **50 soru · 75 dakika**: **30 çok çıkan + 13 orta + 6 az + 1 hiç çıkmayan** konu sorusu. Çok çıkan konuların soru sayısı 5 yıllık sıklıklarıyla orantılı (yükselen konulara küçük ek ağırlık); her hiç çıkmayan konu en fazla 1 soruyla geldi. En çok çıkan konu olan **Hesaplama**dan (59 soru) her testte 6–7 hesap sorusu var (toplam 19: kıymet 10, KDV matrahı 3, ceza 2, ÖTV, KKDF, İGV/MIN-MAX ve antrepo teminatı birer).

| | Test 1 | Test 2 | Test 3 |
|---|---|---|---|
| Blok düzeni | 1–20 Gümrük Mevzuatı · 21–36 Sair · 37–43 Tarife · 44–50 Hesap | 1–22 GM · 23–37 Sair · 38–44 Tarife · 45–50 Hesap | 1–23 GM · 24–36 Sair · 37–44 Tarife · 45–50 Hesap |
| Hesap sorusu | 7 | 6 (48–49 ortak veriye bağlı kıymet → KDV matrahı) | 6 |
| Hiç çıkmayan konu sorusu | Kota ve Tarife Kontenjanı | Sonradan Kontrol | İhracat Sayılan Satış ve Teslimler (99/13812) |
| Çıkmış bilgi alanı / beklenen hüküm | 21 / 29 | 19 / 31 | 22 / 28 |
| Zorluk (kolay · orta · zor) | 11 · 26 · 13 | 9 · 32 · 9 | 14 · 20 · 16 |
| Konu sayısı | 36 | 36 | 36 |

- Her harf 10 kez doğru cevap; aynı harf en fazla 3 kez üst üste.
- Bölüm B'de her sorunun üstündeki italik satır: ders – konu · sınıfı (5 yıldaki soru sayısı) · bilgi kaynağı. "çıkmış bilgi: 2024/61" yazan soru, o çıkmış sorunun ölçtüğü bilgiyi (aynı hükmü ya da aynı mevzuat listesini) **yeni bir kurguyla** sorar; kopya değildir. "beklenen hüküm" yazan soru, cevabı belirleyen bilgisi 2021–2025'te hiç ölçülmemiş bir hükmü sorar. Üç testte toplam 62 çıkmış bilgi, 88 beklenen hüküm sorusu var.
- Gerekçe, doğru şıkkın neden doğru, diğerlerinin neden yanlış olduğunu açıklar ve "Bu nedenle doğru cevap X seçeneğidir. (MD …)" ile biter. Hesap sorularında her yanlış şıkkın hangi hatadan türediği yazılıdır.
- **Hafıza Güncellemesi:** her soru için tek satır `KT1-001 | ders | konu | sınıf | alt tip | zorluk | cevap | çıkmış ref | set`. Yanlışlarını konu ve sınıfa göre izlemek için.

### İkinci set: Test 4–6

Aynı kurallar: **50 soru · 75 dakika**, **30 çok çıkan + 13 orta + 6 az + 1 hiç çıkmayan** konu sorusu, Hesaplama ayrı konu. Fark: cevabı belirleyen bilgi olarak **Karma Test 1–3'te ya da önceki üç deneme sınavında ölçülen hiçbir hüküm tekrar edilmedi**; çeldiricilerde de aynı hüküm aynı kurguyla kullanılmadı. Bu yüzden ağırlık hiç sorulmamış hükümlerdedir; çıkmış bilgi alanı kullanılan sorularda ilk setin kullanmadığı çıkmış sorular seçildi. Hesap sorusu toplam 19: kıymet 10, KDV matrahı 3, ceza, uzlaşma, TPS gözetimi, ÖTV (sigara), İGV tavanı ve geçici ithalat faizi birer.

| | Test 4 | Test 5 | Test 6 |
|---|---|---|---|
| Blok düzeni | 1–23 GM · 24–36 Sair · 37–43 Tarife · 44–50 Hesap | 1–23 GM · 24–38 Sair · 39–44 Tarife · 45–50 Hesap | 1–20 GM · 21–35 Sair · 36–44 Tarife · 45–50 Hesap |
| Hesap sorusu | 7 | 6 (47–48 ortak veriye bağlı kıymet → KDV matrahı) | 6 |
| Hiç çıkmayan konu sorusu | Denizyolu Transiti ve İzinli Gönderici | E-İhracat Destekleri ve Dış Ticaret Sermaye Şirketi | Taşıtların Giriş-Çıkışı |
| Çıkmış bilgi alanı / beklenen hüküm | 5 / 45 | 9 / 41 | 8 / 42 |
| Zorluk (kolay · orta · zor) | 12 · 25 · 13 | 10 · 27 · 13 | 13 · 25 · 12 |
| Konu sayısı | 36 | 36 | 36 |

- Her harf 10 kez doğru cevap; aynı harf en fazla 3 kez üst üste.
- Metin benzerliği taramasında ikinci setin 150 sorusu ilk setle, üç denemeyle, 500 çıkmış soruyla ve kendi aralarında karşılaştırıldı; kopya ya da aynı hükmü aynı kurguyla ölçen soru kalmadı.

### Önerilen kullanım

1. Önce 01 numaralı dokümanda **çok çıkan** konuların haplarını, sonra **orta** ve **az** çıkanları çalış. ★ işaretli haplar birden fazla yılda sorulmuş bilgilerdir.
2. Her konuda 02 (beklenen) haplarına geç; **[Yeni]** etiketlileri ayrıca işaretle.
3. Test kitapçığını yazdır, 75 dakikada çöz; tam test dosyasının Cevap Anahtarı ile puanla, Bölüm B'den gerekçeleri oku.
4. Yanlış yaptığın sorunun konusunu 03 numaralı soru–cevap dokümanında bulup alt konuları tara.

## Nasıl hazırlandı?

1. **Konu eşleme:** 500 sorunun her biri 76 ince içerik konusundan birine atandı; analizdeki alan ayrımına uygun olarak 59 hesap sorusu ayrıca "Hesaplama" konusunda sayıldı (toplam 77 konu). Sorular, mevzuat dosyaları ve resmî anahtarlar konu dosyalarında toplandı.
2. **Çıkan sorulardan hap:** 76 içerik konusu 14 kümeye ayrıldı. Her kümede bütün çıkmış sorular hap satırlarına dönüştürüldü; hesap sorularının hapları Hesaplama bölümüne taşındı (hem hesap hem sözel soruya dayanan 6 hap iki yerde). Bir betik, her sorunun kendi konusunun haplarında geçtiğini denetledi (500/500).
3. **Beklenen ve sorulmayan:** Her konunun alt konuları kaynak metinle karşılaştırılıp SORULDU / KISMEN / SORULMADI diye işaretlendi. Soru–cevapların ve beklenen hapların her biri kaynak metinden birebir bir kesitle (kanıt) yazıldı; bir betik bu kesitleri kaynak dosyalarda aradı, bulunamayanlar elendi. Kümeler arası tekrarlar ve güncelliğini yitirmiş iki madde (Revize PEM 27.03.2026 yazısıyla) çıkarıldı.
4. **Karma testler:** 150 soru konu slotlarına bölündü ve 14 kümede yazıldı (8. adımdaki güncellemeyle 16 küme). Hesap soruları çıkmış hesap sorularının iskeleti üzerine kuruldu.
5. **Bağımsız doğrulama:** Her küme, soruyu cevaba bakmadan çözen ikinci bir uzman tarafından kaynakla karşılaştırıldı. 150 sorunun **133'ü değişmeden geçti, 17'si düzeltildi** (iki hatanın birlikte doğru cevabı verdiği hesaplar, belirsiz veri, önceki denemeyle tekrar). Hiçbir cevap harfi değişmedi. Hesap sorularının bütün şıkları ve 0–2 hatalı bütün yolları betikle yeniden hesaplandı.
6. **Test bazında çapraz kontrol:** Her test 50 sorusuyla baştan sona, anahtara bakmadan çözüldü. Anahtar hatası çıkmadı. 11 soruda test içi tekrar ya da sızıntı, şık konumuna kalmış atıf, vurgusuz olumsuz kök ve güncellik düzeltmesi yapıldı (1 soru yeniden yazıldı).
7. **Bilgi kaynağı etiketi denetimi:** 150 sorunun her birinin "çıkmış bilgi / beklenen hüküm" etiketi, cevabı belirleyen bilginin 2021–2025 sorularında ölçülüp ölçülmediğine bakılarak yeniden kontrol edildi. 6 sorunun etiketi değişti (2'si beklenen → çıkmış, 4'ü çıkmış → beklenen), 6 sorunun çıkmış soru referansı düzeltildi. Metin benzerliği taramasında testler kendi aralarında, önceki 3 denemeyle ve 500 çıkmış soruyla kopya ya da birbirine yakın soru çıkmadı.
8. **Hesaplamanın ayrı konu sayılması:** Analizdeki alan ayrımına uygun olarak 59 hesap sorusu ayrı "Hesaplama" konusuna sayılınca (Gümrük Kıymeti 47 → 15, KDV 13 → 4 vb.) test dağılımı yeniden hesaplandı. Hesap sorusu 14'ten 19'a çıktı; fazla kalan konulardan 9 soru çıkarıldı, yerine 5 hesap ve 4 sözel soru yazıldı (bir soru Test 3'ten Test 2'ye taşındı). Yeni soruların hepsi bağımsız doğrulamadan (4 sözelde 3, 5 hesapta 5 düzeltme; 1 hesap sorusu yeniden yazıldı) ve kendi testleriyle çapraz kontrolden geçti. Konu başına soru sayıları yeni sınıflamanın hedefleriyle birebir aynı.
9. **İkinci set (Test 4–6):** 150 yeni soru aynı slot dağılımıyla 16 kümede yazıldı; her yazar ilk setin 150 sorusunu ve üç denemeyi tarayıp aynı konunun sorulmamış alt başlıklarına gitti. Bağımsız küme doğrulamasında **118 soru değişmeden geçti, 32'si düzeltildi**; çoğu ilk setle ya da denemelerle çakışan bir çeldiricinin değiştirilmesiydi. 2 sorunun cevabı değişti: Revize PEM sonrası tartışmalı hâle gelen "doğrudan nakil" öncülü çıkarıldı; yalnız resmî anahtara dayanan "faiz KDV matrahına girer" kuralı hesaptan çıkarıldı. Test bazında çapraz kontrolde anahtar hatası çıkmadı; 11 soru düzeltildi (3'ü ilk setle ya da denemeyle kurgu tekrarı yüzünden yeniden yazıldı, 2'sinde art arda aynı kalıpla biten cevap düzeni bozuldu). Test 5'teki bağlı hesap setinin Türkiye giderleri, ilk setteki demuraj/ardiye kurgusunu tekrar etmesin diye dampinge karşı vergiyle yeniden kuruldu. Yeniden yazılan bütün sorular ayrıca bağımsız olarak çözüldü.

## Güncellik uyarıları

Dokümanlar ve testler depodaki mevzuat metinlerinin son hâline göre hazırlandı. Bazı çıkmış soruların anahtarı bugün farklı çıkar; ilgili haplarda **Not** satırında yazılı:

- **GK 241/1:** Anayasa Mahkemesinin 26.03.2026 tarihli kararıyla (E.2025/269, K.2026/72) yalnız "ikincil düzenlemelere aykırılık" ibaresi iptal edildi; 241/1'deki miktar ve 241/3–6 katları yürürlükte.
- **GY 94 ve 130/1:** Danıştay 12.08.2026 kararıyla iptal.
- **KDV Kanunu md. 21/1-ç (24.07.2025):** (I) sayılı listede teminata esas ÖTV ithalde KDV matrahına girer; 2025/15'in resmî anahtarı eski kurala dayanır.
- **2009/15481 sayılı Karar md. 62/1** (07.01.2026 tarihli Cumhurbaşkanı Kararı ile değişik, yürürlük 06.02.2026: posta ve hızlı kargoda gerçek kişiye gelen eşyada tek ve maktu vergi yalnız reçeteli ilaç ve takviye edici gıdaya uygulanır) ve **TIR Tebliği** (04.07.2026; md. 20/1'deki sayı sınırı sekiz) değişiklikleri.
- **2025/9903 sayılı Karar** 2012/3305'in yerini aldı (yatırım teşvik).
- **Revize PEM menşe kuralları** (27.03.2026 yazısı): tam kümülasyona ilişkin eski bilgiler çıkarıldı.
- **Resmî anahtarı tartışmalı sorular** (2021/89-90, 2022/94, 2023/57, 2023/72-73, 2023/82, 2023/98, 2024/46, 2025/12, 2025/15, 2025/16, 2025/82): haplarda resmî anahtar ve tartışma birlikte verildi; testlerde bu sorular iskelet olarak kullanılmadı.
- **Yalnız resmî anahtara dayanan kurallar:** "önceki işlemlerden kazanılmış indirim fiyattan düşülmez" (2023/79) ve antrepo götürü teminatında "açık + kapalı alan toplamı" (2022/41, 2024/83) Kanun ve Yönetmelik metninde açıkça yazmaz; testlerde bu kurallara dayanan veri kullanılmadı.

## Sınırlılıklar

- Gümrük Kanunu'nun 1–107. maddeleri, Gümrük Yönetmeliği'nin kıymet/özet beyan/beyan/transit-antrepo genel hükümleri, 5607 sayılı Kanun, DTÖ Kıymet Anlaşması, TFA ve TIR Sözleşmesi metinleri depoda yok. Bu konulardaki haplar ◇ işaretli; dayanakları çıkmış soruların doğrulanmış ifadeleri.
- Mevzuat durumu, depodaki kaynak dosyalardaki hâldir (son görülen değişiklik Ağustos 2026). Sınavdan önce yürürlüğe girecek değişiklikler dokümanlarda yok.
- Yıllık güncellenen tutarlar (ceza, teminat, ücret tarifesi) testlerde doğru cevap yapılmadı; gerektiğinde soruda veri olarak verildi.
- Tarife soruları HS 2022 nomenklatürüne göre.
