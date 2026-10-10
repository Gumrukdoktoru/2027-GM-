# BAKANLIK SORU YAZARI ANALİZİ ve PROMPT SETİ (2027 GM sınavı için)

Bu klasör, 2021–2025 Gümrük Müşavirliği sınavlarının 500 sorusunun soru-soru analizine dayanır. Her soru tek tek incelendi; şu sorulara cevap arandı: Bakanlıkta soruyu hazırlayan kişi **neyi hedefledi, neden böyle sordu, adayı nerede yakalamak istedi?** Çıkan sonuçlar soru ve ders notu üretimi için promptlara dönüştürüldü.

## Dosyalar

| # | Dosya | Ne işe yarar |
|---|---|---|
| 01 | `01-ANALIZ_Bakanlik-Soru-Yazarinin-Zihni_2021-2025` | 5 yılın sentezi: sınav mimarisi, soru yazarının 12 kuralı, 45 konunun yıl yıl frekansı, tekrar eden bilgiler, alan alan hedefler, trendler, 2026-2027 çıkarımları, Bakanlığın kendi hatalarından dersler |
| 02 | `02-SORU-PROMPTU-0_GENEL` | **Tüm alanlar** için soru üretim promptu (deneme sınavı modu dahil) |
| 03 | `03-SORU-PROMPTU-1_GUMRUK-MEVZUATI` | Gümrük Kanunu, Yönetmelik, tebliğler, 2009/15481, GİKY, YGM |
| 04 | `04-SORU-PROMPTU-2_SAIR-MEVZUAT` | KDV/ÖTV/DV/KKDF, kambiyo, 5607, ihracat/ithalat rejimi, ürün güvenliği, tercihli ticaret, uluslararası anlaşmalar |
| 05 | `05-SORU-PROMPTU-3_TARIFE` | TGTC, notlar, izahname, GYKK, HS değişiklikleri |
| 06 | `06-SORU-PROMPTU-4_HESAPLAMA` | Kıymet, vergi zinciri, KDV matrahı, ceza-uzlaşma, kural kartları ve çeldirici algoritması |
| 07 | `07-DERS-NOTU-PROMPTU-0_GENEL` | **Tüm alanlar** için ders notu promptu (tam not, özet, tekrar kartı, karşılaştırma seti) |
| 08 | `08-DERS-NOTU-PROMPTU-1_GUMRUK-MEVZUATI` | Rejim kimlik kartı, tarih zinciri, rejimler arası matris, ceza haritası |
| 09 | `09-DERS-NOTU-PROMPTU-2_SAIR-MEVZUAT` | Kurum, liste, belge haritaları; ülke–anlaşma–belge matrisi; yıl damgalı güncel değerler |
| 10 | `10-DERS-NOTU-PROMPTU-3_TARIFE` | Fasıl kimlik kartı, notlar ve hariçler, şaşırtıcı içerenler/hariçler, karışan pozisyonlar, GYKK |
| 11 | `11-DERS-NOTU-PROMPTU-4_HESAPLAMA` | Kural kartları, kalem sözlüğü, vergi zinciri şeması, hata kataloğu, alıştırmalar |
| 12 | `12-SORU-TIPI-KATALOGU` | **500 sorunun 39 alt tipe ayrılmış haritası:** her alt tipin 5 yıllık sayısı, alanı, kök kalıpları, gerçek sınavdan aynen örneği (49 soru), doğru cevap ve çeldirici kurgusu, üretim tarifi; sınır durumlar; 100 soruluk deneme için alt tip reçetesi |

Her dosyanın `.md` (kopyala-yapıştır için) ve `.docx` (Word) sürümü vardır.

**Deneme sınavları:** Bu analizlere ve promptlara göre hazırlanmış, doğrulanmış 3 adet 100 soruluk deneme (soru kitapçığı, cevap anahtarı ve açıklamalı çözümler; PDF/Word) `../01-DENEME-SINAVLARI/` klasöründedir.

**Yıl yıl ayrıntılı analiz** (100'er satırlık soru tabloları, kök kalıpları, bütün hesap sorularının çözümleri, bütün tarife sorularının gerekçeleri, konu eşleme CSV'si) `gmcikmislar` deposunun `analiz/` klasöründedir. 500 sorunun alt tip etiketleri (CSV), yıl yıl örnek dosyaları ve etiket sözlüğü `analiz/soru-tipi/` klasöründedir.

## Nasıl kullanılır?

1. Promptu kopyala ve sohbetin başına yapıştır.
2. Promptun **"Çağırma şablonu"** bölümünü doldur: MOD, KAYNAK METİN, ÇIKMIŞ SORULAR, SORU SAYISI, SINAV YILI ve GÜNCEL TUTARLAR.
3. Mevzuat metnini **KAYNAK METİN** alanına yapıştır. Bu klasörün üst dizinindeki fasıl, tebliğ ve karar dosyaları doğrudan kullanılabilir.
4. Varsa o konunun çıkmış sorularını **ÇIKMIŞ SORULAR** alanına ekle. Promptlar çıkmış sorunun ölçtüğü bilgiyi mutlaka sorar ama kurguyu kopyalamaz.
5. İstersen **ALT TİP** alanını doldur (ör. `O2×3, Ö3×2, B2×1`). Boş bırakılırsa `OTOMATİK` uygulanır: katalogdaki deneme reçetesi. Belirli bir tipte zorlanıyorsan katalogdaki gerçek örneği KALİBRASYON için promptun sonuna yapıştır.

**Önerilen çalışma sırası (her konu için):**
`Ders notu promptu (Tam not)` → `Soru promptu (MOD A – madde madde)` → `Ders notu promptu (Son tekrar kartı)` → sınav öncesi `Genel soru promptu (MOD B – deneme)`

## Önemli uyarılar

- **Güncel rakamlar:** KDV oranı, ceza katı, götürü teminat tutarları, posta-hızlı kargo eşikleri, nakit beyan eşiği, asgari ücret tarifesi, yıllık ithalat denetimi tebliğleri her yıl değişebilir. Bunları **SINAV YILI ve GÜNCEL TUTARLAR / PARAMETRELER** alanına sen ver. Promptlar verilmeyen güncel değeri doğru cevap yapmamak üzere ayarlandı.
- **Önceki prompt dosyaların** (`0-Soru Hazırlama Kurgusu ve Kuralları.docx`, `gm MEVZUAT prompt.docx`, `SAİR MEVZUAT prompt.docx`) bu sete dahil edildi: madde numarası ezberi yasağı, gerekçe standardı, "(MD x)" referansı, 3 bölümlü deneme formatı korundu. Kök tipi payları, alt tip hedefleri, doğru şıkkın uzunluk kuralı ve öncüllü cevap dağılımı 5 yıllık gerçek veriyle güncellendi. Madde numarası ezberi yasağı korundu; gerçek sınavlarda numara ~%8 soruda yalnız dayanak olarak geçiyor.
- **Tartışmalı anahtarlar:** 2021/89-90, 2022/94, 2023/72-73, 2024/46 ve 2025/12-16'da Bakanlık anahtarı tartışmalı veya hatalı görünüyor. Ayrıntısı analiz raporunun 7. bölümünde.
