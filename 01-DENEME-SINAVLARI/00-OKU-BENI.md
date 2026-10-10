# GÜMRÜK MÜŞAVİRLİĞİ SINAVI — 3 DENEME (2027 sınavına hazırlık)

Bu klasörde 100'er soruluk üç deneme sınavı var. Denemeler, 2021–2025 sınavlarının 500 sorusunun soru-soru analizine (`00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR/`) göre kuruldu: alan dağılımı, blok düzeni, konu ağırlıkları ve soru tipleri gerçek sınavı izliyor.

## Dosyalar

| Dosya | İçerik |
|---|---|
| `DENEME-1_SORU-KITAPCIGI` (.pdf / .docx / .md) | Deneme 1 — yalnız sorular; yazdırıp 150 dakikada çözmek için |
| `DENEME-1_CEVAP-ANAHTARI-VE-COZUMLER` (.pdf / .docx / .md) | Cevap anahtarı, denemenin yapısı ve 100 sorunun açıklamalı çözümü (gerekçe, tuzak, dayanak) |
| `DENEME-2_…`, `DENEME-3_…` | Aynı düzende Deneme 2 ve 3 |
| `veri/deneme1.json` … `deneme3.json` | Soruların makine verisi (no, cevap, alan, konu, alt tip, açıklama, dayanak) |
| `uretim-kayitlari/` | Plan, ajan talimatları, doğrulama ve çapraz kontrol raporları (denemelerin nasıl üretildiğinin kaydı) |

## Nasıl kullanılır?

1. Soru kitapçığının PDF'ini yazdır; 150 dakika süre tut. Gerçek sınavda olduğu gibi yanlışlar doğruları götürmez.
2. Bitirince cevap anahtarından puanla. Çözümler dosyasında her sorunun altında alanı, konusu ve soru tipi kodu (O1, O2, Ö3, H1… — açıklaması `12-SORU-TIPI-KATALOGU`) yazıyor.
3. Yanlışlarını konu ve tipe göre grupla: hangi konuda bilgi eksiğin, hangi tipte okuma hatan var, ayrı ayrı görürsün.
4. Denemeleri arayla çöz (ör. 1 → 2 hafta çalışma → 2 → …).

## Denemelerin yapısı

Her denemede: **42 Gümrük Mevzuatı · 30 Sair Mevzuat · 17 Tarife · 11 Hesap.** Her harf 20 kez doğru cevap; aynı harf en fazla 3 kez üst üste.

| | Deneme 1 | Deneme 2 | Deneme 3 |
|---|---|---|---|
| Blok düzeni (gerçek sınavlardan) | 2025 düzeni: 1–12 Sair · 13–23 Hesap · 24–38 karışık · 39–55 Tarife · 56–100 GM ağırlıklı | 2022 düzeni: 1–72 sözel · 73–89 Tarife · 90–100 Hesap | 2023 düzeni: 1–3 Kaçakçılık · 4–20 Tarife · 21–58 sözel · 59–69 Hesap · 70–100 sözel |
| Gümrük kıymeti (sözel + hesap) | 9 | 9 | 9 |
| Vergi zinciri, ceza, diğer hesaplar | 5 | 5 | 5 |
| Transit · Antrepo | 4 · 4 | 4 · 4 | 4 · 4 |
| Tercihli ticaret ve menşe belgeleri | 5 | 5 | 5 |
| Muafiyetler · 5607 · Kambiyo | 3 · 3 · 3 | 3 · 3 · 3 | 3 · 3 · 3 |
| Olumsuz kök · Öncüllü · Hesap | 33 · 15 · 11 | 34 · 15 · 11 | 33 · 16 · 11 |

Konu ağırlıkları 2021–2025 frekanslarından, soru tipleri katalogdaki deneme reçetesinden geldi. Küçük konular (tasfiye, yatırım teşvik, ticaret politikası önlemleri, 1/95 OKK, genel hükümler) denemeler arasında dönüşümlü dağıtıldı. Üç deneme arasında aynı bilginin tekrarı en aza indirildi (fark edilen iki küçük tekrar farklı denemelerde ve farklı kurguyla duruyor).

## Nasıl hazırlandı?

1. **Plan:** 300 soru, konu × alt tip slotlarına bölündü ve 12 konu kümesine ayrıldı (transit-antrepo, rejimler, kıymet-muafiyet, usul-yükümlülük, YYS-müşavirlik-ceza, vergi-kambiyo-5607, menşe-Incoterms-DTÖ, ihracat-ithalat rejimi, iki tarife, iki hesap kümesi).
2. **Üretim:** Her küme, depodaki mevzuat dosyalarına (Kanun/Yönetmelik bölümleri, tebliğler, Sair Mevzuat Kitabı, 97 fasıl dosyası, sınıflandırma kararları) ve çıkmış soruların doğrulanmış ifadelerine dayanılarak yazıldı. Hesap soruları, çıkmış hesap sorularının iskeleti üzerine sayılar ve kalemler değiştirilerek kuruldu; her şıkkın hangi hatadan türediği çözümde yazılı.
3. **Bağımsız doğrulama:** Her küme, soruyu cevaba bakmadan çözen ikinci bir uzman tarafından kaynakla karşılaştırıldı. 300 sorunun 244'ü değişmeden geçti, 47'si düzeltildi (belirsiz şık, eksik koşul, ipucu veren uzunluk), 9'u kaynakta doğrulanamadığı ya da başka soruyla çakıştığı için yeniden yazıldı. Hesap sorularının bütün şıkları yeniden hesaplandı.
4. **Deneme bazında çapraz kontrol:** Her deneme 100 sorusuyla baştan sona çözüldü. Anahtar hatası çıkmadı; 25 sorunda deneme içi sızıntı (bir sorunun başka sorunun cevabını vermesi), tekrar ya da biçim sorunu giderildi, 2 soru yeniden yazıldı.

## Güncellik uyarıları (denemeler hazırlanırken kaynak dosyalarda görülen değişiklikler)

Bu değişiklikler çıkmış soruların bazı anahtarlarını bugün farklı kılar; çalışırken dikkat:

- **GK 241/1:** Anayasa Mahkemesinin 26.03.2026 tarihli kararıyla (E.2025/269, K.2026/72) ikincil düzenlemelere aykırılık için usulsüzlük cezasına dayanak olan ibare iptal edildi. 241/1'e dayanan eski soru kalıplarını (ör. 2025/81) bu gözle oku.
- **KDV Kanunu md. 21/ç (24.07.2025):** (I) sayılı listede teminata bağlanan ÖTV ithalde KDV matrahına giriyor. 2025/15'in anahtarı bugünkü hükümle farklı çıkar (Deneme 1, hesap bloğu).
- **Posta ve hızlı kargo:** 2026/4 Genelgesi (06.02.2026) ve posta tebliğindeki 2026 değişiklikleri; eski eşik ve basitleştirilmiş beyan kalıplarını kullanmadan önce güncel metne bak.
- **Antrepo yatırım izni:** asgari faaliyet süresi 22.08.2025 değişikliğiyle üç yıl (2024/85'te iki yıl doğruydu); işleticiye yıllık fiyat tarifesi yükümlülüğü getirildi (GY 525/11).
- **Konsinye ihracat:** kesin satış bildirim süresi 06.05.2025 değişikliğiyle 120 gün.
- **99/13812 sayılı Karar:** taahhüt hesabı kapatma işlemine itiraz süresi 19.12.2025'ten itibaren 60 gün.
- **Geçici ithalat:** YYS sahibine dokuz ay süre uzatımı (GY 380/5, 09.01.2024).
- **Kambiyo:** çekili kıymetli maden tanımı (15.03.2025); taşıt satış sözleşmesinin dövizle kararlaştırılamaması (06.03.2025).
- **İthalatta ilave gümrük vergisi Kararı md. 4/6:** 11.07.2026 tarihli 11508 sayılı Kararla değişti.
- **Antrepo götürü teminat tutarları:** güncel GY 527/2 tutarlarıyla 2023/99'un resmî anahtarı tutmuyor; denemedeki götürü teminat sorusunda tutarlar soruda veri olarak verildi.
- **Nakit beyan TL eşiği:** kaynaklarda çelişkili değerler var (185.000 TL / 25.000 TL); bu yüzden denemelerde doğru cevap yapılmadı.

## Sınırlılıklar

- Gümrük Kanunu'nun 1–107. maddeleri, Gümrük Yönetmeliği'nin kıymet/özet beyan/beyan/transit-antrepo genel hükümleri, 5607 sayılı Kanun ile DTÖ Kıymet Anlaşması, TFA ve TIR Sözleşmesi metinleri depoda yok. Bu konulardaki sorular çıkmış soruların doğrulanmış ifadelerine ve uluslararası metinlerin bilinen hükümlerine dayanıyor; doğrulayıcılar tek tek kontrol etti. Metni depoda olmayan bir hükme doğrudan dayanan **16 soru** var; kendi kaynağından teyit etmeni öneririm:
  - Deneme 1: 3, 4, 27, 29, 36
  - Deneme 2: 38, 39, 41
  - Deneme 3: 49, 50, 54, 55, 56, 57, 78, 79
- Mevzuat durumu, depodaki kaynak dosyalardaki hâldir (son görülen değişiklik Temmuz 2026). Sınavdan önce yürürlüğe girecek değişiklikler sorularda yok.
- Yıllık güncellenen tutarlar (asgari ücret tarifesi, yeniden değerleme tutarları, tecil eşikleri) doğru cevap yapılmadı; gerektiğinde tutar soruda veri olarak verildi.
- HS 2027 değişikliklerinin metni depoda olmadığı için tarife soruları HS 2022 nomenklatürüne göre.
