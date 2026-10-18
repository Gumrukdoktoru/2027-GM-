# GÜMRÜK MÜŞAVİRLİĞİ SINAVI — KONU SINIFLARI, HAP BİLGİLER VE KARMA TESTLER (2027 sınavına hazırlık)

Bu klasör, 2021–2025 Gümrük Müşavirliği sınavlarının 500 sorusunu konu konu sayarak 76 konuyu dört sınıfa ayırır: **çok çıkan**, **orta çıkan**, **az çıkan** ve **hiç çıkmayan**. Bu ayrıma dayanan dört çalışma dokümanı ve 50'şer soruluk üç karma test içerir. Dokümanlar örnek alınan "Konu Sınıfları ve Çıkan Sorular Hap", "Beklenen Konular Hap", "Sorulmayan Konular Soru–Cevap" ve "Soru Tipi Kataloğu" düzeninde hazırlandı.

## Dosyalar

| Dosya | İçerik |
|---|---|
| `01-KONU-SINIFLARI-VE-CIKAN-SORULAR-HAP` (.pdf / .docx, 69 sayfa) | Konu sınıfları tabloları (yıl yıl soru sayısı, son 2 yıl, eğilim) ve her konu için **çıkmış sorulardan hap bilgi**: 559 hap, her biri hangi soruda çıktığıyla (ör. `2024/61`), tuzağıyla ve notuyla |
| `02-BEKLENEN-KONULAR-HAP` (.pdf / .docx, 67 sayfa) | Her konuda **henüz sorulmamış ama sorulma ihtimali yüksek** hükümler: 719 hap, 125'i değişiklik notu taşıyan hükümlerden (**[Yeni]** etiketli); sonda "Son Değişiklikler — Toplu Liste" |
| `03-SORULMAYAN-KONULAR-SORU-CEVAP` (.pdf / .docx, 332 sayfa) | Her konunun alt konuları SORULDU / KISMEN / SORULMADI diye işaretli; sorulmayan ve kısmen sorulan alt konular için **2.659 soru–cevap**, her cevap mevzuat dayanağıyla |
| `04-SORU-TIPI-KATALOGU` (.pdf / .docx, 36 sayfa) | 500 sorunun 39 alt tipe ve 9 biçim bayrağına ayrıldığı katalog (`00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR/12-SORU-TIPI-KATALOGU.md`'nin örnek düzeninde baskısı) |
| `KARMA-TEST-1` (.pdf / .docx) | **Tam test.** Kapak, Sınav Bilgileri, Bölüm A (soru kitapçığı), Cevap Anahtarı, Bölüm B (cevaplı ve gerekçeli sorular), Dağılım, Üretim Notu, Hafıza Güncellemesi |
| `KARMA-TEST-1_SORU-KITAPCIGI` (.pdf / .docx) | Yalnız sorular; yazdırıp 75 dakikada çözmek için |
| `KARMA-TEST-2…`, `KARMA-TEST-3…` | Aynı düzende Test 2 ve 3 |
| `veri/` | Makine verisi: `konu_siniflari.json` (76 konu, yıl yıl sayım, sınıf, eğilim, soru listesi), `soru_konu_eslesmesi.json` (500 sorunun konu kodu), `cikan_sorular_hap.json`, `beklenen_ve_sorulmayan.json`, `karma-test1..3.json` |
| `uretim-kayitlari/` | Ajan talimatları, konu kümeleri, test slotları, küme doğrulama raporları, çapraz kontrol yamaları ve betikler (dokümanların nasıl üretildiğinin kaydı) |

## Konu sınıfları (2021–2025, 500 soru)

Sınıf sınırları: **çok çıkan** 5 yılda 10 ve üzeri soru · **orta** 5–9 · **az** 1–4 · **hiç çıkmayan** 0. Eğilim, son 2 yılın ortalamasının ilk 3 yılın ortalamasından en az 1 soru farklı olmasına göre "yükselen / azalan / sabit" olarak verildi.

| Sınıf | Konu | Toplam soru | Konular |
|---|---|---|---|
| Çok çıkan | 16 | 261 | Gümrük Kıymeti 47 · Kaçakçılık (5607) 22 · Transit 21 · Antrepo 17 · Tercihli Menşe İspat Belgeleri 17 · Kambiyo 17 · Muafiyetler 16 · ÖTV 14 · KDV 13 · Tarife Fasıl 1–24 12 · Dahilde İşleme 12 · İhracat Rejimi 12 · Geçici İthalat 11 · Tarife Fasıl 84–85 10 · Tarife Cetvel Yapısı/GTİP 10 · Posta ve Hızlı Kargo 10 |
| Orta çıkan | 28 | 183 | YYS ve Yerinde Gümrükleme, Cezalar, Geri Gelen Eşya, Incoterms, TIR, STA/TTA, HS 2022, Gümrük Birliği, İthalat Rejimi ve İGV, Fikri Haklar, Ürün Güvenliği, GYKK, Özet Beyan, Beyan, Müşavirlik, Tercihsiz Menşe, Kumanya, DTÖ, Hariçte İşleme, Geri Verme, KKDF ve diğer tarife fasıl grupları |
| Az çıkan | 20 | 56 | Serbest Dolaşım ve Nihai Kullanım, Teminat ve Faiz, Geçici Depolama, Ödeme Şekilleri, Tahakkuk-Tebliğ-Zamanaşımı, YGM, Muayene, Onaylanmış Kişi, Uzlaşma, Sınır Ticareti, Yatırım Teşvik, Damga Vergisi, Gümrüksüz Satış, BTB/BMB, Yükümlülük, Tasfiye, Serbest Bölgeler, İtiraz… |
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

Her testte **50 soru · 75 dakika**: **30 çok çıkan + 13 orta + 6 az + 1 hiç çıkmayan** konu sorusu. Çok çıkan konuların soru sayısı 5 yıllık sıklıklarıyla orantılı (yükselen konulara küçük ek ağırlık); her hiç çıkmayan konu en fazla 1 soruyla geldi.

| | Test 1 | Test 2 | Test 3 |
|---|---|---|---|
| Blok düzeni | 1–20 Gümrük Mevzuatı · 21–38 Sair · 39–45 Tarife · 46–50 Hesap | 1–23 GM · 24–39 Sair · 40–46 Tarife · 47–50 Hesap | 1–24 GM · 25–37 Sair · 38–45 Tarife · 46–50 Hesap |
| Hiç çıkmayan konu sorusu | Kota ve Tarife Kontenjanı | Sonradan Kontrol | İhracat Sayılan Satış ve Teslimler (99/13812) |
| Çıkmış bilgi alanı / beklenen hüküm | 20 / 30 | 17 / 33 | 22 / 28 |
| Zorluk (kolay · orta · zor) | 11 · 26 · 13 | 9 · 31 · 10 | 15 · 19 · 16 |
| Konu sayısı | 36 | 36 | 36 |

- Her harf 10 kez doğru cevap; aynı harf en fazla 3 kez üst üste.
- Bölüm B'de her sorunun üstündeki italik satır: ders – konu · sınıfı (5 yıldaki soru sayısı) · bilgi kaynağı. "çıkmış bilgi: 2024/61" yazan soru, o çıkmış sorunun ölçtüğü bilgiyi **yeni bir kurguyla** sorar (kopya değildir); "beklenen hüküm" yazan soru, 2021–2025'te hiç sorulmamış ve 02 numaralı dokümanda yer alan bir hükmü sorar.
- Gerekçe, doğru şıkkın neden doğru, diğerlerinin neden yanlış olduğunu açıklar ve "Bu nedenle doğru cevap X seçeneğidir. (MD …)" ile biter. Hesap sorularında her yanlış şıkkın hangi hatadan türediği yazılıdır.
- **Hafıza Güncellemesi:** her soru için tek satır `KT1-001 | ders | konu | sınıf | alt tip | zorluk | cevap | çıkmış ref | set`. Yanlışlarını konu ve sınıfa göre izlemek için.

### Önerilen kullanım

1. Önce 01 numaralı dokümanda **çok çıkan** konuların haplarını, sonra **orta** ve **az** çıkanları çalış. ★ işaretli haplar birden fazla yılda sorulmuş bilgilerdir.
2. Her konuda 02 (beklenen) haplarına geç; **[Yeni]** etiketlileri ayrıca işaretle.
3. Test kitapçığını yazdır, 75 dakikada çöz; tam test dosyasının Cevap Anahtarı ile puanla, Bölüm B'den gerekçeleri oku.
4. Yanlış yaptığın sorunun konusunu 03 numaralı soru–cevap dokümanında bulup alt konuları tara.

## Nasıl hazırlandı?

1. **Konu eşleme:** 500 sorunun her biri 76 ince konudan birine atandı. Sorular, mevzuat dosyaları ve resmî anahtarlar konu dosyalarında toplandı.
2. **Çıkan sorulardan hap:** 76 konu 14 kümeye ayrıldı. Her kümede bütün çıkmış sorular hap satırlarına dönüştürüldü; bir betik, her sorunun en az bir hapta geçtiğini denetledi (500/500).
3. **Beklenen ve sorulmayan:** Her konunun alt konuları kaynak metinle karşılaştırılıp SORULDU / KISMEN / SORULMADI diye işaretlendi. Soru–cevapların ve beklenen hapların her biri kaynak metinden birebir bir kesitle (kanıt) yazıldı; bir betik bu kesitleri kaynak dosyalarda aradı, bulunamayanlar elendi. Kümeler arası tekrarlar ve güncelliğini yitirmiş iki madde (Revize PEM 27.03.2026 yazısıyla) çıkarıldı.
4. **Karma testler:** 150 soru konu slotlarına bölündü ve 14 kümede yazıldı. Hesap soruları çıkmış hesap sorularının iskeleti üzerine kuruldu.
5. **Bağımsız doğrulama:** Her küme, soruyu cevaba bakmadan çözen ikinci bir uzman tarafından kaynakla karşılaştırıldı. 150 sorunun **133'ü değişmeden geçti, 17'si düzeltildi** (iki hatanın birlikte doğru cevabı verdiği hesaplar, belirsiz veri, önceki denemeyle tekrar). Hiçbir cevap harfi değişmedi. Hesap sorularının bütün şıkları ve 0–2 hatalı bütün yolları betikle yeniden hesaplandı.
6. **Test bazında çapraz kontrol:** Her test 50 sorusuyla baştan sona, anahtara bakmadan çözüldü. Anahtar hatası çıkmadı. 11 soruda test içi tekrar ya da sızıntı, şık konumuna kalmış atıf, vurgusuz olumsuz kök ve güncellik düzeltmesi yapıldı (1 soru yeniden yazıldı).

## Güncellik uyarıları

Dokümanlar ve testler depodaki mevzuat metinlerinin son hâline göre hazırlandı. Bazı çıkmış soruların anahtarı bugün farklı çıkar; ilgili haplarda **Not** satırında yazılı:

- **GK 241/1:** Anayasa Mahkemesinin 26.03.2026 tarihli kararıyla (E.2025/269, K.2026/72) yalnız "ikincil düzenlemelere aykırılık" ibaresi iptal edildi; 241/1'deki miktar ve 241/3–6 katları yürürlükte.
- **GY 94 ve 130/1:** Danıştay 12.08.2026 kararıyla iptal.
- **KDV Kanunu md. 21/1-ç (24.07.2025):** (I) sayılı listede teminata esas ÖTV ithalde KDV matrahına girer; 2025/15'in resmî anahtarı eski kurala dayanır.
- **İthalat Rejimi Kararı md. 62/1** (07.01.2026) ve **TIR Tebliği** (04.07.2026; md. 20/1'deki sayı sınırı sekiz) değişiklikleri.
- **2025/9903 sayılı Karar** 2012/3305'in yerini aldı (yatırım teşvik).
- **Revize PEM menşe kuralları** (27.03.2026 yazısı): tam kümülasyona ilişkin eski bilgiler çıkarıldı.
- **Resmî anahtarı tartışmalı sorular** (2021/89-90, 2022/94, 2023/57, 2023/72-73, 2023/82, 2023/98, 2024/46, 2025/12, 2025/15, 2025/16, 2025/82): haplarda resmî anahtar ve tartışma birlikte verildi; testlerde bu sorular iskelet olarak kullanılmadı.
- **Yalnız resmî anahtara dayanan kurallar:** "önceki işlemlerden kazanılmış indirim fiyattan düşülmez" (2023/79) ve antrepo götürü teminatında "açık + kapalı alan toplamı" (2022/41, 2024/83) Kanun ve Yönetmelik metninde açıkça yazmaz; testlerde bu kurallara dayanan veri kullanılmadı.

## Sınırlılıklar

- Gümrük Kanunu'nun 1–107. maddeleri, Gümrük Yönetmeliği'nin kıymet/özet beyan/beyan/transit-antrepo genel hükümleri, 5607 sayılı Kanun, DTÖ Kıymet Anlaşması, TFA ve TIR Sözleşmesi metinleri depoda yok. Bu konulardaki haplar ◇ işaretli; dayanakları çıkmış soruların doğrulanmış ifadeleri.
- Mevzuat durumu, depodaki kaynak dosyalardaki hâldir (son görülen değişiklik Ağustos 2026). Sınavdan önce yürürlüğe girecek değişiklikler dokümanlarda yok.
- Yıllık güncellenen tutarlar (ceza, teminat, ücret tarifesi) testlerde doğru cevap yapılmadı; gerektiğinde soruda veri olarak verildi.
- Tarife soruları HS 2022 nomenklatürüne göre.
