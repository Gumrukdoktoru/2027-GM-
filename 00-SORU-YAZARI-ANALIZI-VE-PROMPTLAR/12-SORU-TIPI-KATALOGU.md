# 12 — SORU TİPİ KATALOĞU

## Gümrük Müşavirliği Sınavı 2021–2025: 500 sorunun alt tip haritası

**Bu dosyada ne var?** 2021–2025 sınavlarındaki 500 sorunun her biri tek tek etiketlendi: bir **ana tip** (10 tip), bir **alt tip** (39 alt tip) ve dokuz **biçim bayrağı**. Bu dosya o etiketlerin sayımını verir. Her alt tip için gerçek sınavdan aynen alınmış bir örnek ve o tipte soru üretmenin tarifi de buradadır.

**Kimin işine yarar?**

- **Soru üreten** (insan ya da yapay zekâ): 02–06 numaralı soru promptlarındaki `ALT TİP` hedefleri bu dosyadaki kodlara dayanır.
- **Ders notu hazırlayan:** Bir konunun hangi tiple sorulduğunu bilir, "tuzak kutusu"nu o tipe göre yazar.
- **Öğrenci:** Soruyu görünce tipini tanır, o tipin adayı nerede yakaladığını bilir.

**Okuma kuralları**

- Tipi, kökün **son yüklemi** ve **şıkların biçimi** belirler. Kök "yanlıştır" dese bile şıklar bir listenin kısa öğeleriyse soru O1'dir, O2 değildir. Sınır durumlar Bölüm 4'te.
- "5 yıl" = 2021–2025 toplamı (500 soru). "24–25" = 2024 ve 2025 toplamı (200 soru); son eğilimi gösterir.
- Alanlar: **GM** Gümrük Mevzuatı (222 soru) · **SAİR** Sair Mevzuat (143) · **TARİFE** (76) · **HESAP** (59).
- Örnekler A kitapçığından **aynen** alındı; yalnız satır sonları birleştirildi. Doğru şık **kalın** yazıldı ve ✔ ile işaretlendi.
- Anahtarı tartışmalı sorular (2021/89-90, 2022/94, 2023/72-73, 2024/46, 2025/12, 2025/16) örnek olarak kullanılmadı.
- Ham veri (500 satırlık etiket tablosu, yıl yıl örnek dosyaları, etiket sözlüğü) `gmcikmislar/analiz/soru-tipi/` klasöründedir.

### Kod sözlüğü (özet)

| Ana tip | Alt tipler |
|---|---|
| **O** Olumsuz kök | O1 Liste dışı eleman · O2 Bozuk cümle · O3 Çift olumsuz / ters kurgu · O4 Tarife olumsuz |
| **D** Düz (tek bilgi) | D1 Tek değer · D2 Ad/kimlik · D3 Liste içi eleman · D4 Farklı olanı bul · D5 Yer tespiti · D6 Tek cevaplı usul/sonuç |
| **Ö** Öncüllü | Ö1 Hangileri doğrudur · Ö2 Hangileri yanlıştır · Ö3 Liste öncüllü · Ö4 Koşul öncüllü · Ö5 Vaka öncüllü |
| **G** "Hangisi doğrudur" | G1 Beş cümleden doğru · G2 Normatif güç merdiveni · G3 Ters kurgu · G4 Örnek seçme |
| **V** Vaka (hesapsız) | V1 Tarihli vaka · V2 Olaylı vaka · V3 Emsal/seçenek seçme · V4 Tarife tanım/görsel vakası |
| **K** Kavram | K1 Tanım → kavram |
| **B** Boşluk | B1 İki boşluk · B2 Üç-dört boşluk |
| **E** Eşleştirme | E1 Beş çiftten yanlış/doğru olan · E2 Tablo eşleştirme · E3 Doğru sıralama (permütasyon) |
| **S** Sıralama | S1 Süreç/öncelik sırası · S2 Numara/büyüklük sırası |
| **H** Hesap | H1 Kalem listeli kıymet · H2 Bağlı soru · H3 Vergi tutarı/zinciri · H4 Ceza/uzlaşma · H5 Kıymet yöntemi · H6 Özel kıymet durumu · H7 Hesapsız hesap · H8 Diğer sayısal |

| Bayrak | Anlamı |
|---|---|
| F_MATRIS | Şıklar iki ya da üç boyutun çapraz kombinasyonu ("Özel – 5 iş günü – 241/1") |
| F_MUTLAK | Doğru cevapta ya da kilit çeldiricide mutlak ifade (sadece, yalnızca, her türlü, istisnasız, hiçbir) |
| F_TUZAKVERI | Kökte kullanılmaması gereken veri (ödeme tarihi kuru, saha alanı, litre başı ÖTV, temettü…) |
| F_TUMU | Doğru cevap tüm öncüller ("I, II, III ve IV") |
| F_YALNIZ | Doğru cevap "Yalnız X" |
| F_DAYANAK | Kökte mevzuatın adı açıkça geçiyor |
| F_MADDENO | Kökte ya da şıkta madde/fıkra/bent numarası geçiyor |
| F_SERI | Önceki ya da sonraki soruyla aynı hükmün serisi ya da ortak veri seti |
| F_GUNCEL | O yıl veya bir önceki yıl yürürlüğe giren ya da yıllık güncellenen düzenlemeye dayanıyor (dar tanım) |

---

## 1. BÜYÜK RESİM

### 1.1 Ana tip × yıl

| Ana tip | 2021 | 2022 | 2023 | 2024 | 2025 | 5 yıl | Pay |
|---|---|---|---|---|---|---|---|
| O Olumsuz | 53 | 34 | 28 | 35 | 30 | 180 | %36 |
| D Düz | 23 | 21 | 21 | 23 | 17 | 105 | %21 |
| Ö Öncüllü | 4 | 15 | 16 | 15 | 17 | 67 | %13 |
| H Hesap | 10 | 13 | 16 | 11 | 9 | 59 | %12 |
| G Doğru | 4 | 12 | 5 | 4 | 9 | 34 | %7 |
| V Vaka | 1 | 1 | 6 | 2 | 5 | 15 | %3 |
| E Eşleştirme | 2 | 0 | 3 | 3 | 5 | 13 | %3 |
| K Kavram | 2 | 1 | 2 | 5 | 2 | 12 | %2 |
| B Boşluk | 0 | 3 | 2 | 2 | 5 | 12 | %2 |
| S Sıralama | 1 | 0 | 1 | 0 | 1 | 3 | %1 |

### 1.2 Alt tip × yıl × alan (500 sorunun tamamı)

| Alt tip | 2021 | 2022 | 2023 | 2024 | 2025 | 5 yıl | GM | SAİR | TARİFE | HESAP | 24–25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| O1 | 18 | 12 | 11 | 15 | 12 | 68 | 33 | 35 | 0 | 0 | 27 |
| O2 | 25 | 16 | 8 | 15 | 9 | 73 | 59 | 14 | 0 | 0 | 24 |
| O3 | 5 | 1 | 0 | 0 | 1 | 7 | 6 | 1 | 0 | 0 | 1 |
| O4 | 5 | 5 | 9 | 5 | 8 | 32 | 0 | 0 | 32 | 0 | 13 |
| D1 | 9 | 8 | 3 | 3 | 1 | 24 | 21 | 2 | 1 | 0 | 4 |
| D2 | 5 | 2 | 6 | 2 | 2 | 17 | 5 | 11 | 1 | 0 | 4 |
| D3 | 3 | 4 | 3 | 4 | 6 | 20 | 7 | 13 | 0 | 0 | 10 |
| D4 | 2 | 1 | 3 | 6 | 0 | 12 | 0 | 3 | 9 | 0 | 6 |
| D5 | 1 | 2 | 3 | 6 | 5 | 17 | 0 | 1 | 16 | 0 | 11 |
| D6 | 3 | 4 | 3 | 2 | 3 | 15 | 6 | 9 | 0 | 0 | 5 |
| Ö1 | 2 | 5 | 4 | 5 | 6 | 22 | 13 | 9 | 0 | 0 | 11 |
| Ö2 | 0 | 4 | 4 | 4 | 2 | 14 | 8 | 6 | 0 | 0 | 6 |
| Ö3 | 2 | 5 | 7 | 4 | 8 | 26 | 18 | 7 | 1 | 0 | 12 |
| Ö4 | 0 | 1 | 0 | 1 | 1 | 3 | 1 | 2 | 0 | 0 | 2 |
| Ö5 | 0 | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 | 0 | 1 |
| G1 | 2 | 9 | 4 | 4 | 6 | 25 | 17 | 6 | 2 | 0 | 10 |
| G2 | 0 | 2 | 0 | 0 | 2 | 4 | 1 | 2 | 1 | 0 | 2 |
| G3 | 1 | 1 | 1 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 |
| G4 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 2 | 0 | 1 |
| V1 | 0 | 0 | 1 | 0 | 1 | 2 | 2 | 0 | 0 | 0 | 1 |
| V2 | 0 | 0 | 1 | 1 | 1 | 3 | 3 | 0 | 0 | 0 | 2 |
| V3 | 0 | 0 | 2 | 0 | 1 | 3 | 2 | 1 | 0 | 0 | 1 |
| V4 | 1 | 1 | 2 | 1 | 2 | 7 | 0 | 0 | 7 | 0 | 3 |
| K1 | 2 | 1 | 2 | 5 | 2 | 12 | 5 | 7 | 0 | 0 | 7 |
| B1 | 0 | 1 | 1 | 2 | 3 | 7 | 3 | 4 | 0 | 0 | 5 |
| B2 | 0 | 2 | 1 | 0 | 2 | 5 | 3 | 1 | 1 | 0 | 2 |
| E1 | 2 | 0 | 3 | 3 | 3 | 11 | 3 | 6 | 2 | 0 | 6 |
| E2 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |
| E3 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 |
| S1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| S2 | 0 | 0 | 1 | 0 | 1 | 2 | 0 | 1 | 1 | 0 | 1 |
| H1 | 3 | 3 | 3 | 3 | 1 | 13 | 0 | 0 | 0 | 13 | 4 |
| H2 | 1 | 1 | 2 | 1 | 0 | 5 | 0 | 0 | 0 | 5 | 1 |
| H3 | 1 | 4 | 1 | 2 | 3 | 11 | 0 | 0 | 0 | 11 | 5 |
| H4 | 2 | 1 | 1 | 0 | 2 | 6 | 0 | 0 | 0 | 6 | 2 |
| H5 | 2 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
| H6 | 1 | 3 | 5 | 5 | 2 | 16 | 0 | 0 | 0 | 16 | 7 |
| H7 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 |
| H8 | 0 | 1 | 1 | 0 | 1 | 3 | 0 | 0 | 0 | 3 | 1 |

### 1.3 Her alanın tip imzası (alan içindeki pay; 5 yıl / 24–25)

| Alan | İlk beş alt tip | Bu beşin alan içindeki payı |
|---|---|---|
| **GM** (222) | O2 %27/26 · O1 %15/13 · Ö3 %8/10 · G1 %8/10 · D1 %9/5 | %67 |
| **SAİR** (143) | O1 %24/25 · O2 %10/5 · D3 %9/10 · D2 %8/6 · Ö1 %6/6 | %57 |
| **TARİFE** (76) | O4 %42/37 · D5 %21/29 · D4 %12/14 · V4 %9/9 · G4 %3/3 | %87 |
| **HESAP** (59) | H6 %27/35 · H1 %22/20 · H3 %19/25 · H4 %10/10 · H2 %8/5 | %86 |

**Okuma:** GM'nin dili **bozuk cümle** (O2), Sair'in dili **listede olmayanı bul** (O1). Tarife üç kalıpla sorulur: "yer almaz" (O4), "yer alır" (D5), "farklı olan" (D4). Hesapta "özel durum" (H6) 2023'ten beri klasik kalem listesini (H1) geçti.

### 1.4 Bayraklar × yıl

| Bayrak | 2021 | 2022 | 2023 | 2024 | 2025 | 5 yıl | 100 soruda ort. |
|---|---|---|---|---|---|---|---|
| F_DAYANAK | 56 | 54 | 58 | 65 | 73 | 306 | 61 (24–25: 69) |
| F_SERI | 12 | 8 | 45 | 23 | 47 | 135 | 27 (24–25: 35) |
| F_TUZAKVERI | 9 | 9 | 17 | 10 | 5 | 50 | 10 |
| F_MADDENO | 5 | 8 | 10 | 8 | 7 | 38 | 8 |
| F_MUTLAK | 5 | 8 | 6 | 9 | 6 | 34 | 7 |
| F_MATRIS | 2 | 8 | 8 | 3 | 9 | 30 | 6 |
| F_GUNCEL | 0 | 8 | 1 | 1 | 4 | 14 | 3 |
| F_YALNIZ | 0 | 3 | 1 | 5 | 4 | 13 | 3 |
| F_TUMU | 1 | 2 | 2 | 4 | 2 | 11 | 2 |

### 1.5 Biçimsel ölçümler (cevap anahtarının "parmak izi")

| Ölçü | Bulgu | Soru üretiminde karşılığı |
|---|---|---|
| Doğru harf (500 soru) | A 95 · B 94 · C 105 · D 106 · E 100 | Harf dağılımı N/5 ± 2 |
| Doğru şık uzunluğu, tüm cümle/eşleşme şıklı sorular (n=187) | orta %59 · en uzun %24 · en kısa %17 | Doğru şıkkı çoğunlukla orta uzunlukta yaz |
| **Olumsuz kökte bozuk şık** (O2 ve O3; n=78) | orta %59 · **en uzun %27** · en kısa %14 | Bozuk şık uzunlukla ele vermez; "kısa şık bozuktur" alışkanlığına düşme |
| **Olumlu kökte doğru şık** (G1–G4; n=33) | orta %64 · en uzun %27 · **en kısa %9** | En kısa şıkkı doğru yapmak nadir; en uzun eğilimi hafif |
| Öncüllü cevap (Ö1–Ö5 + E2; n=68) | ara kombinasyon 44 (%65) · "Yalnız X" 13 (%19) · tüm öncüller 11 (%16) | Bu oranlara yakın dağıt |
| Liste öncüllüde "hepsi" (Ö3; n=26) | 8 soru (%31); Ö3'te doğru harf E 11 kez | Ö3'te "tümü" cevabını kullan, ama E'ye sabitleme |
| Öncül sayısı (n=67) | 4 öncül 36 · 5 öncül 18 · 3 öncül 13 | Varsayılan 4 öncül |
| Hesapta doğru harf (n=59) | A 12 · B 14 · C 16 · D 14 · **E 3** | Şıklar çoğunlukla küçükten büyüğe dizili; en büyük tutar (çoğu kez "her kalemi katan" toplam) nadiren doğru. Denemede hesap cevabı en fazla 1 kez E |
| Tek değer (D1; n=24) | C 12 (%50) | Sıralı sayı şıklarında doğru değer ortaya yığılıyor; sen yığma |
| Mutlak ifade (F_MUTLAK; n=34) | O2'lerin yalnız 10'unda bozulmanın kendisi. 2021/63, 2022/30, 2023/35, 2023/50'de "yalnızca / hiçbir şekilde" içeren şık mevzuatın aynısı (doğru ifade); 2022/64'te mutlak ifadeli şık doğru cevap | "Mutlak = yanlış" sezgisini kıran soru da yaz |
| Madde numarası (F_MADDENO; n=38, ~%8) | Hemen hepsi kökte dayanak gösterimi ("… 244 üncü maddesinde düzenlenen …"). Numara yalnız 5–6 soruda şıkta ya da cevabın kendisinde (241/1–241/2, 234/1–234/3, 27/1-d, GYK 2-a, 84. fasıl 9 no.lu not) | Madde numarasını ezber sorusu yapma |
| Güncellik (F_GUNCEL, dar tanım; n=14) | 2021: 0 · 2022: 8 (HS 2022 ve 2022 tebliğleri) · 2023: 1 · 2024: 1 · 2025: 4 | Yeni nomenklatür ya da yeni tebliğ yılında güncel soru sıçrar (2027 = HS 2027) |

---

## 2. KATALOGDAN ÇIKAN 12 BULGU

1. **On alt tip sınavın üçte ikisi.** O2 73, O1 68, O4 32, Ö3 26, G1 25, D1 24, Ö1 22, D3 20, D2 17, D5 17: toplam 324 soru (%65). Bir deneme bu on tipi doğru oranda içermiyorsa gerçek sınava benzemez.
2. **Olumsuz kök azaldı ama düşüş O2'den.** O tipi 53 → 30. O2 (bozuk cümle) 25 → 9'a indi; O1 (liste dışı eleman) 11–18 arasında sabit kaldı. Bakanlık uzun cümle tahrifini öncüllüye taşıdı: Ö1 + Ö2 2021'de 2, 2025'te 8.
3. **Öncüllünün yıldızı liste öncüllü (Ö3).** 26 soruyla öncüllülerin en büyüğü. Ö3'te doğru cevap üç soruda birinde "hepsi" (%31). Bakanlık adayın "biri mutlaka yanlıştır" önyargısını hedefliyor.
4. **Çıplak sayı sorusu eriyor, sayı başka kılığa giriyor.** D1: 9 → 8 → 3 → 3 → 1. Sayı bilgisi kaybolmadı: boşluk matrisinde (B1/B2: 0 → 5), "yalnız süresi değişen beş cümle"de (G1, 2025/94) ve eşleştirmede soruluyor.
5. **Matris şıklar yükselişte.** F_MATRIS 2 → 9. Boşluklu 12 sorunun 11'i matris: her boşluk bir boyut, şıklar boyutların kombinasyonu.
6. **Seri soru sınavın yarısına yaklaştı.** F_SERI 2023'te 45, 2025'te 47. Bir hüküm açılınca 2–6 soru arka arkaya geliyor (2025: transit 65–70, antrepo 78–83).
7. **Tarifede iki ana kalıp, bir yükselen.** O4 "yer almaz" (32) ve D5 "yer alır" (17). D5 son iki yılda 11 soruya çıktı; D4 "farklı olanı bul" 2024'te 6.
8. **Hesapta özel durum (H6) en büyük alt tip.** 16 soru: kullanılmış taşıt, royalti listesi, gözetim, serbest bölge, kendi kendini taşıyan eşya, dolaylı ödeme. 2023–2024'te her yıl 5.
9. **Tuzak veri hesapların imzası.** H1 ve H2'nin tamamında, H6'nın 10/16'sında, H3'ün 6/11'inde var. Hesap sorusu tuzak verisiz yazılmaz.
10. **Uzunluk ipucu yok.** Bozuk şık %59 orta, %27 en uzun, yalnız %14 en kısa. "Kısa ve mutlak şık bozuktur" genellemesi veride yok.
11. **Bakanlık kendi doğru şıkkını yeniden kullanıyor.** GYKK 3(b) "makarna + peynir + sos" seti 2021/94'te ve 2025/42'de doğru cevap. Kanıtlanmış doğru örnek dört yıl sonra yeni çeldiricilerle geri geliyor.
12. **Madde numarası dekor, güncellik dalga.** Numara 38 soruda geçiyor ama 5–6'sı dışında cevabı etkilemiyor. Dar anlamda güncel soru yeni nomenklatür ya da yeni tebliğ yılında sıçrıyor: 2022'de 8, diğer yıllar 0–4.

---

## 3. ALT TİP KARTLARI

Her kartta aynı başlıklar: **Tanım · Sayı · Kök kalıpları · Gerçek örnek · Doğru cevap nasıl kuruluyor · Çeldiriciler · Biçim verisi · Üretim tarifi · Kaçın.** Az kullanılan alt tiplerin kartları kısadır.

### O — OLUMSUZ KÖK (180 soru, %36)

#### O1 — Liste dışı eleman

**Sayı:** 68 (GM 33 · SAİR 35) · yıllar 18-12-11-15-12 · 24–25: 27. Sair Mevzuatın 1 numaralı tipi (%24).

**Tanım:** Şıklar bir listenin ya da kapsamın öğeleri: belge, ülke, eşya, kavram, kurum, liste adı, hâl başlığı. Dördü listede, biri değil.

**Kök kalıpları:** "… hâller arasında sayılmamıştır" · "… durumlardan biri değildir" · "… taraf ülkelerden biri değildir" · "… teslim şekillerinden değildir" · "… tanımlanan bir kavram değildir" · "… düzenlenmemiştir" · "… kapsamında değildir" · "… aranmaz".

**Gerçek örnek — 2025/5 (uydurma ad):**

> 5\. Aşağıdakilerden hangisi transfer fiyatlandırmasında uygulanacak yöntemlerden birisi değildir?\
> A) Karşılaştırılabilir fiyat yöntemi\
> **B) İndirgeme yöntemi** ✔\
> C) Maliyet artı yöntemi\
> D) Yeniden satış fiyatı yöntemi\
> E) Kâr bölüşüm yöntemi

**Gerçek örnek — 2025/90 (komşu listeden gerçek öğe):**

> 90\. Aşağıdakilerden hangisi yetkilendirilmiş yükümlü sertifikasının askıya alınmasını gerektiren durumlardan biri değildir?\
> A) Gümrük işlemlerinden doğan kesinleşmiş bir kamu alacağının süresi içinde ödenmediğinin gümrük idaresince tespit edilmesi\
> B) Ticaret unvanı değişikliği sonrası sertifikada değişiklik yapılması için sertifikanın düzenlendiği bölge müdürlüğüne süresi içinde başvuru yapılmaması\
> C) Transit işlemlerinde rejim hak sahibi olan sertifika sahibinin bilgisi dışında, kanun ve uluslararası anlaşmalarla ithali, ihracı veya transiti yasaklanmış eşyanın taşınması\
> **D) Sertifikanın sahte belgelere dayanılarak verildiğinin anlaşılması** ✔\
> E) ISO 9001 ve ISO 27001 belgelerinin süresi içinde Bölge Müdürlüğüne ibraz edilmemesi

**Doğru cevap nasıl kuruluyor? Yabancı öğenin yedi kaynağı** (en sıktan seyreğe):

| # | Kaynak | Gerçek örnekler |
|---|---|---|
| 1 | **Komşu listeden gerçek öğe** (aynı mevzuatın başka listesi ya da hükmü) | Askıya alma hâlleri arasına iptal sebebi (2025/90) · (IV) sayılı liste malları arasına başka listedeki sade gazoz (2024/16) · (B) cetveli solventleri arasına (A) cetvelinden uçak benzini (2025/7) · Kurul görevleri arasına Bakanlık biriminin görevi (2021/65) |
| 2 | **Minimal çift** (tek nitelik değişmiş öğe) | Brüt yerine net ağırlık (2023/92) · MRN yerine LRN (2023/86) · kıymetli taş listesine yarı değerli ametist (2023/49) · %5 eşiği %15 (2021/9) · eşik üstü değer (2022/72) |
| 3 | **Taraf olmayan ülke** | STA'lı ülkeler arasına İran (2022/23) · İİT anlaşmasına taraf olmayan Irak (2023/100) · 2025/71, 2025/97 |
| 4 | **Ters işlevli olay** | Sorumluluk doğuran hâller arasına sorumluluğu kaldıran özen (2021/33) · yükümlülük doğuranlar arasına yükümlülüğü sona erdiren izinli ihraç (2021/38) |
| 5 | **Uydurma ama inandırıcı terim veya şart** | "İndirgeme yöntemi" (2025/5) · "kiralama ödemesi" (2021/52) · uydurma teminat şartı (2025/92) · "reklam" çağrışımlı "reklamasyon" (2024/15) |
| 6 | **Başka hukuk dalından kavram** | Yönetmelik tanımları arasına CMK'dan "arama" (2021/42), TCK'dan "müsadere" (2021/49) |
| 7 | **Aynı ailede yanlış alt grup / yetkisiz birim** | Tüm taşıma türü Incoterms kuralları arasına deniz kuralı FAS/CFR (2022/65, 2024/1) · yetkili bölge müdürlükleri arasına yetkisiz Batı Marmara (2024/95) |

**Çeldiriciler:** Dördü listenin gerçek öğeleri ve mevzuattaki adlarıyla yazılmış. En iyi çeldirici, listede olduğu **beklenmeyen** gerçek öğedir: ruble ve rupi listede, gelişmiş ülke parası değil (2021/61).

**Biçim verisi:** Şıklar kısa 33, cümle 32 · Harf A16 B10 C14 D13 E15 · Cümle şıklılarda doğru şık orta 18, en kısa 10, en uzun 4 · Kökte dayanak 45/68.

**Dikkat:** Uzun hâl cümleleriyle kurulan O1'de yabancı öğe çoğu kez **en kısa** şık (32 sorunun 10'u, %31). Liste öğeleri mevzuattan uzun uzun aktarılırken uydurma ya da komşu öğe kısa kalıyor. Üretirken yabancı öğeyi ötekiler kadar ayrıntılı yaz.

**Üretim tarifi:**

1. Mevzuatta **kapalı** bir liste seç ("şunlardır", "aşağıda sayılan", ek liste). "Gibi" ile örneklenen açık listeden O1 yazma.
2. Listeden dört gerçek öğe al; mevzuattaki ifadeyi koru, uzunlukları dengele.
3. Yabancı öğeyi yukarıdaki yedi kaynaktan seç. En güçlüsü 1. ve 2. kaynak: aday "bunu bu listede gördüm" demeli.
4. Yabancı öğe ötekilerle aynı kategoride, aynı uzunlukta ve aynı üslupta olsun.
5. Kökte listenin adını ve dayanağını ver; olumsuz yüklemi **altı çizili ve kalın** yaz.

**Kaçın:** Yabancı öğenin açık bir kategoriye ("ve benzeri") girebilmesi · listede ikinci bir yabancı öğe kalması · listenin güncellenmiş olması (eski Karar listesi).

#### O2 — Bozuk cümle

**Sayı:** 73 (GM 59 · SAİR 14) · yıllar 25-16-8-15-9 · 24–25: 24. Gümrük Mevzuatının 1 numaralı tipi (%27).

**Tanım:** Şıklar tam cümle hükümler. Dördü mevzuattan neredeyse aynen alınmış, birinde tek unsur bozulmuş.

**Kök kalıpları:** "… ilişkin aşağıdaki ifadelerden hangisi yanlıştır?" (58) · "hangisi söylenemez?" (8) · "yanlış bir ifadedir" (3).

**Gerçek örnek — 2025/93:**

> 93\. Gümrük Yönetmeliğine göre teminata ilişkin aşağıdaki ifadelerden hangisi yanlıştır?\
> **A) Gümrük işlemleri sırasında teminat alınmasına gerek görülen hallerde bankalar tarafından verilen süreli teminat mektupları teminat olarak kabul edilir.** ✔\
> B) Toplu teminat takip edilebilir olması halinde diğer gümrük idarelerinde de geçerlidir.\
> C) Teminatı veren, verdiği teminatın, idare amirinin izniyle kısmen veya tamamen başka bir teminat ile değiştirilmesini isteyebilir.\
> D) Bir gümrük yükümlülüğü karşılığında alınan teminat mektubu, söz konusu yükümlülüğün yerine getirilmemesi halinde takibe alınır.\
> E) Gümrük yükümlülüğünün yerine getirilmemesi halinde teminat mektubunu veren hak sahibine yükümlülüğe ilişkin sürenin bitiminden yirmi gün önce tebligat yapılarak bu yükümlülüğünü yerine getirmemesi halinde teminat mektubunun nakde dönüştürüleceği belirtilir.

Kurgu: Dört şık Yönetmelik cümlesi aynen. Doğru cevapta "süresiz" teminat mektubu "süreli" yapılmış: tek kelimelik tahrif.

**Doğru cevap nasıl kuruluyor? Bozma tekniği dağılımı** (73 sorunun kurulum notlarından elle sınıflandırma; yaklaşık):

| Teknik | Soru | Pay | Gerçek örnekler |
|---|---|---|---|
| **Polarite tersi** (alınır → alınmaz, içinde → dışında, serbest → kotaya tabi, sayılır → sayılmaz) | 17 | %23 | 2021/15 teminat alınır → alınmaz · 2021/75 STM TGB dışında → içinde · 2025/31 ihracı serbest → "kotaya tabidir" · 2025/56 seferin devamı sayılır → sayılmaz |
| **Süre / sayı kaydırma** | 11 | %15 | 2021/17 üç iş günü → beş · 2021/36 150 gün → 100 · 2024/81 yurt dışında bulunma süresi iki katına (24 ay) |
| **Makam / kişi kaydırma** | 10 | %14 | 2021/73 TGTC'yi kabul eden Cumhurbaşkanı → Bakanlık · 2024/85-86 sonuçlandırma makamı → bölge müdürlüğü · 2021/80 son zilyet → ilk kullanıcı |
| **Uydurma şart ya da hüküm ekleme** | 7 | %10 | 2021/30 uydurma 15 günlük başvuru süresi · 2022/39 var olmayan "sözlü uyarı" yaptırımı · 2022/66 teminat iadesine 12 ay şartı |
| **Kapsam genişletme / daraltma, istisnayı kurala çevirme** | 7 | %10 | 2021/5 yalnız özel mahfazaya ait istisna genele çevrilmiş · 2024/75 kefillere "sigorta şirketleri" eklenmiş · 2025/75 binek otomobil istisnası muafiyet kuralına çevrilmiş |
| **Kavram / belge etiketi değiştirme** | 7 | %10 | 2021/70 genel antrepo → özel antrepo · 2023/87 gümrük statüsü → menşe · 2025/34 işlenmiş tarım ürününde A.TR → EUR.1 |
| **Mutlaklaştırma** (sadece, her türlü) | 6 | %8 | 2021/21 "sadece TCK hükümleri uygulanır" · 2024/92 "her türlü eşya" · 2024/78, 2024/84 kurala "sadece" eklenmiş |
| **Zaman / yer / sıra kaydırma** | 3 | %4 | 2021/25 akaryakıtın vergilendirildiği liman → "ilk" Türk limanı · 2022/47 kontrol zamanı TGB'ye girişten önceye |
| **Hükmü başka durum ya da rejime taşıma** | 3 | %4 | 2021/35 deniz yolu konteyner kuralı demir yolu/hava yoluna · 2022/20 örgüt artırımı üç kişi hâline |
| Diğer (usul ayrıntısı) | 2 | %3 | 2024/31, 2024/66 |

**Çeldiriciler:** Dört doğru cümle. Bakanlık iki ek hile kullanıyor: (1) **ikiz şık** — doğru cümlenin hemen yanında, tek kelimesi farklı bozuk ikizi (2022/47: A şıkkındaki "girişinde" ile cevaptaki "girmeden önce"). Seri sorularda bir önceki sorunun doğru cümlesi bozulup sonraki soruya konuyor (2024/74 → 2024/75: kefil cümlesine "sigorta şirketleri" eklenmiş); (2) **mutlak kelimeli doğru cümle** — "yalnızca / hiçbir şekilde" içeren ama mevzuatın aynısı olan şık (2021/63, 2022/30, 2023/35, 2023/50). İkincisi "mutlak ifade bozuktur" diyen adayı yakalar.

**Biçim verisi:** Harf A9 B16 C16 D14 E18 · Bozuk şık orta 43, en uzun 19, en kısa 11 · F_MUTLAK 10 · Kökte dayanak 48/73.

**Üretim tarifi:**

1. Tek bir hükümden ya da aynı maddenin fıkralarından beş cümle çıkar.
2. Bozulacak cümleyi seç; tabloda tek bir teknik uygula. Bir sette hiçbir teknik O2'lerin %30'unu geçmesin.
3. Bozulmuş unsur **gerçek bir komşu** olsun: aynı mevzuatta geçen başka süre, başka makam, başka belge.
4. Diğer dört cümleyi mevzuattan aynen al. Birine bilerek bir "yalnızca/sadece" bırak, ama mevzuatta varsa.
5. Bozuk şıkkın uzunluğunu öteki şıkların ortasına koy.

**Kaçın:** İki unsuru birden bozmak (iki itiraz yolu açar) · bozulmanın yorumla tartışılabilmesi · doğru cümlelerden birinin başka bir hükümle çelişmesi.

#### O3 — Çift olumsuz / ters kurgu

**Sayı:** 7 (GM 6 · SAİR 1) · yıllar 5-1-0-0-1. **Bakanlık bu tipi 2022'den sonra neredeyse bıraktı.**

**Tanım:** Kök zaten olumsuz bir kavramın (dâhil edilmeyen, istisna, geçerliliğini kaybetme) olumsuzunu sorar.

**Kök kalıpları:** "… gümrük kıymetine dâhil edilmeyen giderler arasında değildir" · "… geçerliliğini kaybetmez" · "… istisnası değildir" · "… fiyatın ilişkiden etkilenmediğini göstermez".

**Gerçek örnek — 2021/16:**

> 16\. 4458 sayılı Gümrük Kanunu'na göre, aşağıdaki durumlardan hangisinde "bağlayıcı tarife bilgisi" geçerliliğini kaybetmez?\
> A) Türk Gümrük Tarife Cetveli'nde değişiklik yapılması ve verilen bilginin söz konusu değişiklikle getirilen hükümlere uymaması hâlinde\
> **B) Dünya Ticaret Örgütünün uymakla yükümlü bulunduğumuz Menşe Kuralları Anlaşması'na ve bu anlaşmaya ilişkin izahname ve kararlardaki bir değişikliğe uymaması hâlinde** ✔\
> C) Bağlayıcı tarife bilgisinin iptal edildiğinin bilgi verilen kişiye tebliğ edilmesi hâlinde\
> D) Bağlayıcı tarife bilgisinin değiştirildiğinin bilgi verilen kişiye tebliğ edilmesi hâlinde\
> E) Dünya Gümrük Örgütünün uymakla yükümlü bulunduğumuz nomanklatür, izahname, tarife pozisyonlarına ilişkin kararlarındaki bir değişikliğe uymaması hâlinde

Kurgu: Dört şık BTB'nin geçerliliğini kaybettiği hâller. Doğru cevap bağlayıcı **menşe** bilgisine ait DTÖ değişikliği. DGÖ/DTÖ ikiz şıkları ters kurguyu destekliyor.

**Doğru cevap nasıl kuruluyor?** Bir istisna ya da hariç listesi alınır. Dördü listeden aynen, beşincisi **karşı listeden** (dâhil olan, geçerli kalan, başka kurumun) bir öğe olur. 2025/8'de ÖTV listeleri arasında diplomatik istisnanın dışında kalan (IV) sayılı liste cevaptır.

**Üretim tarifi:** Denemede en fazla 1 soru. Yalnız gerçekten ters okuma disiplini ölçülecekse yaz. Kökteki iki olumsuzu da altı çizili ve kalın yaz.

**Kaçın:** Üç olumsuz (kök + kavram + şık) · olumsuzluğun yalnız ekte kalması ("-mez") ve vurgulanmaması.

#### O4 — Tarife olumsuz

**Sayı:** 32 (TARİFE) · yıllar 5-5-9-5-8 · 24–25: 13. Tarifenin 1 numaralı tipi (%42).

**Tanım:** "Şu fasılda/pozisyonda hangisi yer almaz", "hangisi sınıflandırılmaz", "bu GTİP için hangisi söylenemez".

**Kök kalıpları:** "… X'inci fasılda yer almaz?" · "… sınıflandırılmamaktadır?" · "… XX.XX tarife pozisyonunda sınıflandırılamaz?" · "… GTİP'indeki eşya için hangisi söylenemez?" · "… tümü aynı fasılda sınıflandırılmaz?"

**Gerçek örnek — 2025/45 (HS değişikliği):**

> 45\. Türk Gümrük Tarife Cetveline göre aşağıdakilerden hangisi 84 üncü fasılda yer almaz?\
> A) Mekanik salmastralar\
> B) Merkezi yağlama sistemleri\
> C) Tav ocakları\
> **D) Sıcak izostatik presler** ✔\
> E) Volanlar

Kurgu: Dört çeldirici adı makineyi çağrıştırmayan ama 84'te kalan eşya. Cevap, adı 84'ü çağrıştıran ama HS 2022 ile 85.14'e taşınan pres.

**Gerçek örnek — 2025/44 (GTİP yapısı okuma):**

> 44\. Türk Gümrük Tarife Cetveline göre 64.06.90.90.10.00 GTİP'indeki eşya için aşağıdakilerden hangisi söylenemez?\
> **A) Eşya TGTC 11. Bölüm kapsamındadır.** ✔\
> B) İstatistik amaçlı açılım yapılmamıştır.\
> C) Kombine Nomanklatür açılımı yapılmıştır.\
> D) Milli alt açılım yapılmıştır.\
> E) Ayakkabı aksamıdır.

**Doğru cevap nasıl kuruluyor? Altı kaynak:**

| Kaynak | Gerçek örnekler |
|---|---|
| Fasıl/bölüm notuyla hariç tutulan eşya | Güneş saati 91'de değil (2025/40) · bebek bezi 63.07'den 96.19'a (2021/93) · dişçilik tornası fırçası 90.18'e (2021/95) · 64.06 aksam tanımından hariç bağcıklar (2025/41) |
| HS değişikliğiyle taşınan eşya | Sıcak izostatik pres 85.14 (2025/45) · 24.04 yeni nesil ürünler arasında yakılarak içilen ürün (2025/52) |
| Ada/kelimeye aldanma | Isı pompası 84.18, ısı değiştirici 84.19 (2023/21) · platin grubu metaller arasında kadmiyum (2021/99) |
| Numara kaydırma | Pamuk 52 → 53 (2022/80) · 64. fasıl XII. bölümde, "11. Bölüm" yazılmış (2025/44) |
| Komşu pozisyon | 09.09 tohumları arasına 09.10 baharatı (2025/50) · 20.08 kriterleri arasına 20.09'un Brix kriteri (2023/5) |
| Homojen grubun içine başka fasıl | Balıklar arasına memeli balina (2022/83) · kesici silahlar arasına 95. fasıl ok ve yay (2021/92) |

**Biçim verisi:** Şıklar kısa 20, cümle 8, kod 4 · Harf D 13 kez (%41; rastlantı olabilir) · Kökte dayanak ("Türk Gümrük Tarife Cetveline göre") 27/32.

**Üretim tarifi:**

1. Fasıl/bölüm notlarından ve izahnameden **hariç** cümlesini bul.
2. Hariç tutulan eşyayı, adı o fasla en çok yakışan biçimde yaz (cevap).
3. Dört çeldiriciyi o fasılda kalan ama adı başka yeri çağrıştıran eşyalardan seç.
4. HS 2027 yılında taşınan eşyaları ayrıca işaretle (2027 sınavının güçlü adayı).

**Kaçın:** Eşya adının iki pozisyona da girebilecek kadar genel olması (2024/46 "kahve" tartışması) · malzemesi belirtilmemiş eşya.

### D — DÜZ (105 soru, %21)

#### D1 — Tek değer

**Sayı:** 24 (GM 21) · yıllar **9-8-3-3-1** · 24–25: 4. **Hızla eriyen tip.**

**Tanım:** Cevap bir sayı, süre, oran, tutar, kat ya da kod.

**Kök kalıpları:** "… kaç iş günü süresince …" · "… ne kadar süre içinde …" · "… yüzde (%) kaçı olarak tespit edilir?" · "… hangi vergi oranı uygulanır?" · "… usul kodlarından hangisi beyan edilir?"

**Gerçek örnek — 2025/25:**

> 25\. Gümrük Genel Tebliği (Serbest Dolaşıma Giriş) (Seri No: 16) kapsamında, deniz yolu ile sıvı halde Türkiye Gümrük Bölgesine getirilen ve gümrük gözetimi altında gaz haline dönüştürülerek limanda boru hattına verilen sıvılaştırılmış doğal gazın (LNG) serbest dolaşıma girişine ilişkin gümrük beyannamesinde aşağıda belirtilen basitleştirilmiş usul kodlarından hangisi beyan edilir?\
> A) BS-18\
> **B) BS-19** ✔\
> C) BS-20\
> D) BS-21\
> E) BS-22

**Doğru cevap ve çeldiriciler:** Çeldiriciler sayı komşuları ya da aynı mevzuatta başka hükümde geçen gerçek değerler (hafta/gün/ay komşuları, 2022/77). Sıralı şıklarda doğru cevap 24 sorunun 12'sinde C.

**Biçim verisi:** Şıklar sayı 21 · Harf A2 B6 **C12** D1 E3.

**Üretim tarifi:** Denemede GM'de en fazla 2. Sayıyı tek başına sormak yerine B1/B2 matrisine ya da G1 cümlesine taşı (Bölüm 2, bulgu 4). Yazarsan beş değeri sırala ama doğru değeri her seferinde ortaya koyma. Her çeldirici mevzuatta gerçekten geçen bir değer olsun.

**Kaçın:** Yeniden değerlemeyle her yıl değişen tutarı yıl belirtmeden sormak.

#### D2 — Ad/kimlik

**Sayı:** 17 (SAİR 11 · GM 5) · 24–25: 4.

**Tanım:** Cevap bir makam, kurum, belge, mahkeme, kanun, yöntem, işaret ya da kuruluş adı.

**Kök kalıpları:** "… belgenin adı nedir?" · "… hangisinin görevidir?" · "… hangi kanun hükümlerine tabidir?" · "… ispatlayan belge aşağıdakilerden hangisidir?"

**Gerçek örnek — 2025/36:**

> 36\. Türkiye Cumhuriyeti ile Özbekistan Cumhuriyeti arasındaki tercihli ticaret anlaşması çerçevesinde eşyanın tercihli menşeini ispatlayan belge aşağıdakilerden hangisidir?\
> A) TR-OZB Menşe Şahadetnamesi\
> B) TR-AZ Menşe İspat Belgesi\
> **C) EUR.1 Dolaşım Belgesi** ✔\
> D) TR-OZB Menşe İspat Belgesi\
> E) TR-UAE Menşe İspat Belgesi

**Doğru cevap ve çeldiriciler:** Bakanlığın dört hilesi: (1) **anlaşma adından türetilmiş uydurma belge** (TR-OZB, 2025/36); (2) **ikiz kavram** (büyük harf "E İşareti" / küçük harf "e işareti", 2022/16); (3) **ad benzerliği** (DGÖ Teknik Komitesi / DTÖ, 2023/61); (4) **kurum kaydırma** (numuneyi saklayan idare, sahte paranın teslim edildiği TCMB şubeleri, 2021/47 ve 2021/50).

**Üretim tarifi:** Doğru ad mevzuattaki tam adıyla. Çeldiricilerden en az biri gerçek ama başka yerde geçerli ad, en az biri inandırıcı uydurma olsun.

#### D3 — Liste içi eleman (olumlu)

**Sayı:** 20 (SAİR 13 · GM 7) · yıllar 3-4-3-4-**6** · 24–25: 10.

**Tanım:** O1'in aynası. Dört öğe listede **değil**, biri listede: "hangisi … tabidir / yasaktır / taraftır / ön izne bağlıdır".

**Gerçek örnek — 2025/1:**

> 1\. Gümrük idaresine verilen aşağıdaki belgelerden hangisi damga vergisine tabidir?\
> A) Elçilik Mektubu\
> B) Kurye Mektubu\
> **C) Konşimento** ✔\
> D) TIR Karnesi\
> E) ATA Karnesi

**Gerçek örnek — 2025/76 (miktarlı liste):**

> 76\. 2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre aşağıdakilerden hangisi Yolcu Beraberi Kişisel Eşya Listesi uyarınca muafiyet kapsamındadır?\
> A) 2 kg çay\
> B) 600 gr pipo tütünü\
> C) Alkol derecesi % 22'yi geçen üç litre alkol ve alkollü içki\
> D) 5 adet elde taşınabilir müzik aleti\
> **E) 5 adet cilt bakım ürünü ve makyaj malzemesi** ✔

**Doğru cevap nasıl kuruluyor?** Dört istisna arasında tek tabi olan (2025/1) · AB üyeleri arasında tek EFTA üyesi (2025/26) · sınırı aşmayan tek kalem (2025/76) · vizeye tabi tek belge EUR.1 (2024/33) · kesintiye tabi tek ürün pamuk (2024/64).

**Üretim tarifi:** Kapalı listeyi ve onun **karşı listesini** (istisnalar, muaflar, yasaklılar) yan yana koy. Dört çeldiriciyi karşı listeden, cevabı listeden al. Miktarlı listede çeldiricileri aynı kalemlerin sınırı aşan miktarlarıyla kur.

#### D4 — Farklı olanı bul / grup dışı

**Sayı:** 12 (TARİFE 9 · SAİR 3) · yıllar 2-1-3-**6**-0.

**Tanım:** "Hangisi farklı pozisyonda yer alır", "grubun dışında kalır", "hangi şıktaki ülkelerin tamamı ile … bulunmaktadır".

**Gerçek örnek — 2024/54:**

> 54\. Türk Gümrük Tarife Cetveline göre aşağıdakilerden hangisi 8 inci fasılda diğerlerinden farklı bir pozisyonda sınıflandırılır?\
> A) Taze fındık\
> **B) Taze kaju cevizi** ✔\
> C) Taze kestane\
> D) Taze pekan cevizi\
> E) Taze kola cevizi

**Gerçek örnek — 2024/36 (üçlü şık):**

> 36\. Aşağıda yer alan seçeneklerden hangisinde verilen ülkelerin tamamı ile Türkiye arasında "Serbest Ticaret Anlaşması" bulunmaktadır?\
> A) Birleşik Krallık, Mısır, Azerbaycan\
> B) Şili, Singapur, Özbekistan\
> **C) Güney Kore, Malezya, Bosna Hersek** ✔\
> D) Mısır, İran, Birleşik Krallık\
> E) Güney Kore, İran, Pakistan

**Doğru cevap nasıl kuruluyor?** Tekli şıkta: dört eşya aynı pozisyon, farklı olan **egzotik görünmeyen** eşya (egzotik kola ve pekan cevizi aynı pozisyonda, kaju ayrı). Üçlü şıkta: her yanlış üçlüye tek bir yabancı gizlenir (TTA ülkesi Azerbaycan, Özbekistan, İran, Pakistan).

**Üretim tarifi:** Üçlü şık kalıbı Sair'de güçlü: dört yanlış üçlünün her birinde **yalnız bir** yabancı olsun, yabancılar birbirinden farklı olsun, doğru üçlüdeki ülkeler başka şıklarda da geçsin.

#### D5 — Yer tespiti

**Sayı:** 17 (TARİFE 16) · yıllar 1-2-3-**6-5** · 24–25: 11. **Tarifede yükselen tip.**

**Tanım:** Kısa eşya adı verilir, "hangi pozisyonda / hangi fasılda yer alır" sorulur; ya da fasıl verilir, "hangisi bu fasılda yer alır" sorulur.

**Gerçek örnek — 2025/55 (şıklar eşya):**

> 55\. Türk Gümrük Tarife Cetveline göre aşağıdaki eşyalardan hangisi 40 ıncı fasılda yer alır?\
> A) Banyo başlığı\
> **B) Uçak lastiği** ✔\
> C) Sandalye\
> D) Oyuncak bebek\
> E) Lamba gövdesi

**Gerçek örnek — 2025/54 (şıklar kod):**

> 54\. Türk Gümrük Tarife Cetveline göre, "Ahtapotlar (Octopus spp.)" aşağıdaki tarife pozisyonlarından hangisinde yer alır?\
> A) 03.05\
> B) 03.06\
> **C) 03.07** ✔\
> D) 03.08\
> E) 03.09

**Doğru cevap nasıl kuruluyor?** Şıklar eşyaysa: hepsi aynı malzemeden yapılabilir (kauçuk), ama yalnız biri malzeme faslında kalır; ötekiler kendi işlev fasıllarına gider. Şıklar kodsa: sayı komşuları, çağrışım pozisyonları ve **HS değişikliğinden önceki eski pozisyon** (yenilebilir böcekler 04.10 ile insan tüketimine uygun olmayan böcekler 05.11: 2022/79, 2024/2).

**Üretim tarifi:** Malzeme faslı (39, 40, 44, 48, 70, 73) seç ve "o malzemeden yapılmış ama başka fasla giden" eşyaları çeldirici yap. Kod şıklarında ardışık beş pozisyon kullan, ama bunu her seferinde yapma; bazen çağrışım pozisyonlarını karıştır (2025/49'daki gibi 33.01 / 39.23 / 76.15).

#### D6 — Tek cevaplı usul/sonuç

**Sayı:** 15 (SAİR 9 · GM 6).

**Tanım:** Vaka kurgusu olmadan "hangi usulle hesaplanır", "hangi tarih esas alınır", "kime aittir", "yapılması gereken işlem hangisidir".

**Gerçek örnek — 2025/86:**

> 86\. Gümrük Yönetmeliğine göre gümrük kontrolü altında işleme rejiminde değişmemiş eşyaya veya izinde öngörülene nazaran işlemin ara aşamalarından birinde bulunan ürünlere ilişkin bir gümrük yükümlülüğü doğduğunda, gümrük vergileri tutarı aşağıdaki usullerin hangisiyle hesaplanır?\
> **A) İthal eşyasının, gümrük kontrolü altında işleme rejimine tabi tutulduğu beyannamenin tescili sırasındaki yürürlükte bulunan vergi oranı ve diğer vergilendirme unsurlarına dayanılarak belirlenir.** ✔\
> B) İthal eşyasının, serbest dolaşıma girdiği tarihte yürürlükte bulunan vergi oranı ve diğer vergilendirme unsurlarına dayanılarak belirlenir.\
> C) İşlenmiş ürünün serbest dolaşıma girdiği tarihte yürürlükte bulunan vergi oranı ve diğer vergilendirme unsurlarına dayanılarak belirlenir.\
> D) İşlenmiş ürüne ilişkin gümrük yükümlülüğünün doğması sırasında yürürlükte bulunan vergi oranı ve diğer vergilendirme unsurlarına dayanılarak belirlenir.\
> E) İthal eşyasının Türkiye Gümrük Bölgesine girdiği tarihte yürürlükte bulunan vergi oranı ve diğer vergilendirme unsurlarına dayanılarak belirlenir.

**Doğru cevap ve çeldiriciler:** Beş şık **aynı kalıpta**; yalnız iki unsur (eşya: ithal eşyası / işlenmiş ürün; tarih: tescil / serbest dolaşım / giriş) değişir. 15 sorunun 4'ü matris. Süre başlangıcı sorularında çeldiriciler sürecin önceki aşamalarıdır (sözleşme, onay, tescil, yükleme; 2022/69).

**Üretim tarifi:** Sürecin bütün aşamalarını sırayla yaz; cevap olan aşamayı ve dört komşu aşamayı şık yap. Cümle kalıbını beş şıkta da birebir koru.

### Ö — ÖNCÜLLÜ (67 soru, %13)

**Ortak veriler:** Öncül sayısı 4 (36 soru) > 5 (18) > 3 (13). Cevap: ara kombinasyon %65 · "Yalnız X" %19 · tüm öncüller %16. Yıllar 4 → 15 → 16 → 15 → 17.

**Kombinasyon şıkkı nasıl kuruluyor?** (gerçek sınavlardan)

1. Beş şık, beş farklı küme. Doğru küme bir kez geçer.
2. Çeldiricilerin üç türü:
   - doğru kümeye **bir bozuk öncül eklenmiş** küme (2025/69: doğru "I ve II", çeldirici "I, II ve III" ve "I, II ve IV");
   - doğru kümeden **bir öğesi değiştirilmiş** küme ("II ve IV");
   - **en çekici bozuk öncülü** içeren küme.
3. Cevap "Yalnız X" ise şıklarda en az iki "Yalnız" bulunur (2025/85: Yalnız I / Yalnız II / Yalnız III). Böylece "Yalnız" kelimesi cevabı ele vermez.
4. Cevap "hepsi" ise "I, II, III ve IV" şıkkı tek başına en büyük küme olarak durur. Bakanlık bunu %16 oranında doğru cevap yapıyor; adayın "hepsi olamaz" refleksi hedef.
5. Bir öncül beş şıkkın hepsinde geçerse aday onu değerlendirmek zorunda kalmaz (2025/69'da II her şıkta). Bakanlık bunu yapıyor ama soruyu kolaylaştırır; bilinçli kullan.

#### Ö1 — Hangileri doğrudur

**Sayı:** 22 (GM 13 · SAİR 9) · yıllar 2-5-4-5-6 · 24–25: 11.

**Kök kalıpları:** "… yukarıdaki ifadelerden hangileri doğrudur?" (10) · "hangisi/hangileri doğrudur?" (6) · "hangisi ya da hangileri doğrudur?" (4).

**Gerçek örnek — 2025/69:**

> 69\. I. İthalat vergileri ve ticaret politikası önlemlerine tabi tutulmayan serbest dolaşıma girmemiş veya ihracatla ilgili gümrük işlemleri tamamlanmış eşya, gümrük gözetimi altında Türkiye Gümrük Bölgesi içindeki bir noktadan diğerine transit rejimi kapsamında taşınır.\
> II. Hareket gümrük idaresindeki bilgi ve belgeler ile varış gümrük idaresindeki bilgi ve belgelerin karşılaştırılması sonucunda, transit rejiminin usulüne uygun olarak sonlandırıldığının belirlenmesi halinde rejim ibra edilir.\
> III. Transit rejimine tabi tutulan eşya ve gerekli belgeler, rejimi düzenleyen hükümlere uygun olarak hareket gümrük idaresine sunulduğunda transit rejimi sona erer.\
> IV. Transit rejimine konu olan eşyanın, gümrük gözetimi altındaki antrepolarda veya gümrük idarelerince eşya konulmasına izin verilen yerlerde bir süre kalması veya bir taşıttan diğer bir taşıta aktarılması mümkün değildir.\
> 4458 sayılı Gümrük Kanununa göre transit rejimine ilişkin olarak yukarıdaki ifadelerden hangileri doğrudur?\
> **A) I ve II** ✔\
> B) II ve IV\
> C) I, II ve III\
> D) I, II ve IV\
> E) II, III ve IV

Kurgu: III'te "varış" yerine "hareket" (yer kaydırma), IV'te "mümkündür" yerine "mümkün değildir" (polarite tersi).

**Doğru cevap ve çeldiriciler:** Öncüller aynı hükmün cümleleri. 1–3 öncül, O2'deki bozma tekniklerinden biriyle bozulur. 22 sorunun 4'ünde cevap "Yalnız X", 1'inde "hepsi".

**Üretim tarifi:** Aynı maddeden 4 cümle al. 2'sini bozmak varsayılan; farklı iki teknik kullan (biri yer/süre kaydırma, biri polarite). Kombinasyon şıklarını yukarıdaki kurala göre kur.

#### Ö2 — Hangileri yanlıştır

**Sayı:** 14 (GM 8 · SAİR 6) · yıllar 0-4-4-4-2.

**Tanım:** Ö1'in tersi. "Yanlış / kullanılamaz / izin verilmez" olanlar sorulur.

**Gerçek örnek — 2025/63 (ikiz öncül):**

> 63\. Aşağıda dahilde işleme rejimi kapsamında telafi edici vergiye ilişkin bazı ifadeler verilmiştir:\
> I. Telafi edici vergi bir ithalat vergisidir.\
> II. Telafi edici vergi gümrük yükümlülüğü, söz konusu eşyanın ihracına ilişkin gümrük beyannamesinin gümrük idaresi tarafından tescil edildiği tarihte başlar.\
> III. Önceden ihracat durumunda telafi edici vergi önceden ihracata tekabül eden ithalatın yapılması esnasında ödenir.\
> IV. Telafi edici vergi, ithalata ilişkin beyannamenin tescili tarihindeki vergi oranı ve diğer vergilendirme unsurlarına göre hesaplanır.\
> V. Telafi edici vergi, ihracata ilişkin beyannamenin tescili tarihindeki vergi oranı ve diğer vergilendirme unsurlarına göre hesaplanır.\
> Bu ifadelerden hangisi/hangileri yanlıştır?\
> A) Yalnız I\
> **B) Yalnız IV** ✔\
> C) Yalnız V\
> D) III ve IV\
> E) I, II ve III

**Doğru cevap ve çeldiriciler:** Bakanlığın en sevdiği Ö2 hilesi **ikiz öncül**: aynı cümlenin iki hâli (IV ithalat, V ihracat beyannamesi). Aday ikisinden birinin doğru olduğunu bilir ama hangisi olduğunu bilmelidir. Uç cevaplar Ö2'de daha sık: "Yalnız X" 4, "hepsi yanlış" 2 (2022/58, 2023/96). 5 sorunun kilit unsuru mutlak ifade ("yalnızca", "her durumda", "istisnasız").

**Üretim tarifi:** Bir ikiz öncül çifti kur; birini doğru, birini yanlış bırak. "Hepsi yanlış" cevabını 10 Ö2'de en fazla 1–2 kez kullan.

#### Ö3 — Liste öncüllü

**Sayı:** 26 (GM 18 · SAİR 7 · TARİFE 1) · yıllar 2-5-7-4-**8** · 24–25: 12. **Öncüllülerin en büyüğü.**

**Tanım:** Öncüller **kısa** öğeler (eşya, belge, ülke, kurum, hâl başlığı); "hangileri … tabidir / kapsamındadır / değildir" sorulur. O1 ve D3'ün öncüllü hâli.

**Gerçek örnek — 2025/66:**

> 66\. I. Kapsamlı teminat\
> II. İzinli gönderici yetkisi\
> III. Elektronik taşıma belgesi ile taşıma\
> IV. Belirli taşıma şekillerine özgü basitleştirmeler\
> Gümrük Yönetmeliğine göre yukarıdakilerden hangileri transit rejimi kapsamında yer alan basitleştirmelerdendir?\
> A) II ve III\
> B) III ve IV\
> **C) I, II ve IV** ✔\
> D) I, III ve IV\
> E) I, II, III ve IV

**Gerçek örnek — 2025/38 ("Yalnız"):**

> 38\. I. Oyuncaklar\
> II. Tohum, fide, fidan ve çiçek soğanları gibi çoğaltım materyalleri\
> III. Kara yolu taşıt araçları\
> IV. Katı yakıtlar\
> Yukarıdaki eşya gruplarından hangisi/hangileri ithalatta Dış Ticarette Risk Esaslı Kontrol Sistemi (TAREKS) üzerinden uygunluk denetimine tabidir?\
> **A) Yalnız I** ✔\
> B) Yalnız III\
> C) I ve III\
> D) II ve IV\
> E) I, III ve IV

**Doğru cevap ve çeldiriciler:** O1'deki yedi kaynaktan biriyle yabancı öğe eklenir, ama aday **kaç tane** yabancı olduğunu bilmez: sıfır, bir ya da iki. Bu yüzden Ö3, O1'den zordur. 26 sorunun 8'inde cevap "hepsi" (2023/46 kurulum notu: "'hepsi olamaz' önyargısı hedefleniyor"), 2'sinde "Yalnız X".

**Biçim verisi:** Harf C7 D4 **E11** · Öncül sayısı 3: 8, 4: 11, 5: 7.

**Üretim tarifi:** Kapalı listeden 3–5 öğe. Yabancı öğe sayısını sorudan soruya değiştir (0–2). "Hepsi" cevabını Ö3'lerin yaklaşık üçte birinde kullan, ama her seferinde E'ye koyma.

#### Ö4 — Koşul öncüllü

**Sayı:** 3 (SAİR 2 · GM 1) · 2022, 2024, 2025'te birer.

**Gerçek örnek — 2025/85:**

> 85\. 5607 sayılı Kaçakçılıkla Mücadele Kanununa göre kaçakçılık suçunun işlenmesinde kullanılarak elkonulan taşıtın elkoyan mercilerce alıkonulması için;\
> I. Soruşturma ve kovuşturma devam ederken, kaçakçılık suçunun işlenmesinde tekrar kullanılması,\
> II. Kaçak eşyanın, taşıma aracı yüküne göre miktar veya hacim bakımından tamamını veya ağırlıklı bölümünü oluşturması veya naklinin, bu aracın kullanılmasını gerekli kılması,\
> III. Taşıma aracındaki kaçak eşyanın, Türkiye'ye girmesi veya Türkiye'den çıkması yasak veya toplum veya çevre sağlığı açısından zararlı maddelerden olması\
> koşullarından hangisinin/hangilerinin gerçekleşmesi gerekir?\
> **A) Yalnız I** ✔\
> B) Yalnız II\
> C) Yalnız III\
> D) I ve II\
> E) I, II ve III

**Doğru cevap ve çeldiriciler:** II ve III kanunun taşıtlarla ilgili hükümlerinde geçen, kanun diliyle yazılmış gerçek ifadeler; ama alıkoymanın koşulu değil. Aday "kanunda bunu okudum" der, hangi sonuç için olduğunu karıştırır. 3 sorunun 2'sinde cevap "Yalnız I".

**Üretim tarifi:** Aynı kanunda farklı sonuçlara bağlanan koşulları bul (alıkoyma, müsadere, iade gibi). Birinin koşulunu sor, öbürlerinin koşullarını öncül olarak karıştır. Her öncül kanun dilinde yazılsın.

#### Ö5 — Vaka öncüllü

**Sayı:** 2 (2023/28, 2024/43).

**Gerçek örnek — 2023/28:**

> 28\. Aşağıdaki durumlardan hangisinde/hangilerinde Gümrük Kanunu'nun 176'ncı maddesi uyarınca vergisiz yakıt kullanılamaz?\
> I) İstanbul-Ankara iç seferinden sonra ihraç yükü almak üzere Adnan Menderes Havalimanına boş olarak yapılan seferde,\
> II) Fransa'dan hareketle İstanbul Havalimanına gelen ve yükünün bir kısmını burada boşaltarak hiç dahili yük almadan Esenboğa Havalimanına yükün kalan kısmını boşaltmak üzere yapılan seferde,\
> III) İspanya'dan hareketle İstanbul Havalimanına gelip tüm yükünü boşaltan bir uçağın buradan Adnan Menderes Havalimanına ihraç yükü almak üzere kısmen ihraç yükü almış olarak veya boş olarak yaptığı seferde,\
> IV) Almanya'dan hareketle Esenboğa Havalimanına gelip tüm yükünü boşaltan bir uçağın buradan iç hat yükü alıp İstanbul Havalimanına yaptığı seferde,\
> A) Yalnız IV\
> B) I ve III\
> C) II ve III\
> **D) I ve IV** ✔\
> E) I, III ve IV

**Üretim tarifi:** Bir kuralın ayırdığı iki grubu bul (dış seferin devamı / iç sefer). Her gruptan iki somut senaryo yaz; senaryoları birbirine çok benzet, tek bir olgu (yük alıp almama, nereden gelme) farklı olsun.

### G — "HANGİSİ DOĞRUDUR" (34 soru, %7)

#### G1 — Beş cümleden doğru

**Sayı:** 25 (GM 17 · SAİR 6 · TARİFE 2) · yıllar 2-9-4-4-6 · 24–25: 10.

**Tanım:** O2'nin tersi: dört tahrifli, bir doğru cümle.

**Kök kalıpları:** "… ilişkin aşağıdaki ifadelerden hangisi doğrudur?" (21) · "hangi seçenekte doğru belirtilmiştir?" · "hangisinde doğru olarak verilmiştir?"

**Gerçek örnek — 2025/95:**

> 95\. 4458 sayılı Gümrük Kanununa göre, yapılan kontrol sonucunda noksan alındığı tespit edilen ve yükümlüye tebliğ edilen gümrük vergileri ile ilgili olarak aşağıdaki ifadelerden hangisi doğrudur?\
> **A) Noksan alınan gümrük vergilerinin yükümlüye tebliğ edildiği tarihten itibaren on beş gün içinde ödenmesi zorunludur.** ✔\
> B) Noksan alınan gümrük vergilerine ilişkin ödeme süresinin bitiminden önce ilgilinin yazılı istemde bulunması ve teminat alınması şartıyla ödeme süresi 3 ay daha uzatılabilir.\
> C) Noksan alınan gümrük vergilerine ilişkin ödeme süresinin uzatılması durumunda ayrıca tecil faizi alınmaz.\
> D) Yükümlünün noksan alınan gümrük vergilerinin tutarının bir kısmını verilen sürenin bitimini beklemeksizin ödemesi durumunda kalan kısmını 6 ay içinde ödeyebilir.\
> E) Noksan alınan gümrük vergilerine ilişkin ilgilinin talebi halinde teminat alınmadan ödeme süresi otuz gün daha uzatılabilir.

**Doğru cevap ve çeldiriciler:** Dört çeldirici aynı hükmün **farklı unsurlarını** tahrif eder (uzatma süresi, teminat şartı, tecil faizi, kısmi ödeme). Üç G1 varyantı öne çıkıyor:

- **Yalnız süresi değişen beş cümle** (2025/94): D1'in cümleye taşınmış hâli.
- **Matris cümle** (5 soru): "gecikme faizi/zammı × 241/1, 234/1, ceza yok" (2022/49).
- **Mutlak ifadeli doğru cevap** (2022/64: "herhangi bir süre kısıtı bulunmaksızın"; 2023/3'te "yalnızca/gerekir/uygulanmaz" ile daraltılmış dört cümleye karşı kapsamı açan hüküm).

**Biçim verisi:** Harf A6 B7 C2 D4 E6 · Doğru şık orta 18, en uzun 5, en kısa 2 · F_MUTLAK 7.

**Üretim tarifi:** Bir hükmün 4–5 unsurunu çıkar; her çeldiricide **farklı** bir unsuru boz. Doğru şıkkı en uzun yapma alışkanlığına düşme (25'te yalnız 5).

#### G2 — Normatif güç merdiveni

**Sayı:** 4 (2022'de 2, 2025'te 2).

**Tanım:** Şıklar aynı konunun farklı hukuki gücü: zorunlu / teşvik / yasak / karşılıklılık / düzenleme yok; ya da "%100'e kadar / yalnızca %10 / yetkisi yok".

**Gerçek örnek — 2025/6:**

> 6\. Ticaretin Kolaylaştırılması Anlaşması kapsamında "ön karar" mekanizması ile ilgili olarak, gümrük kıymetinin tespitinde kullanılacak uygun yöntem ve kriterlere ilişkin aşağıdakilerden hangisi doğrudur?\
> A) Üyelerin bu konuda ön karar vermeleri zorunludur.\
> B) Anlaşmada bu konuda düzenleme bulunmaz.\
> C) Bu konu, ön karar verilmemesi gereken başlıklar arasındadır.\
> D) Ön karar verilmesi karşılıklılık şartıyla mümkündür.\
> **E) Üyeler bu konuda ön karar vermeleri için teşvik edilir.** ✔

**Gerçek örnek — 2025/53 (yetki merdiveni):**

> 53\. 474 sayılı Gümrük Giriş Tarife Cetveli Hakkında Kanuna göre Cumhurbaşkanının tarife cetvelindeki gümrük vergisi oranlarında değişiklik yapmasına ilişkin aşağıdaki ifadelerden hangisi doğrudur?\
> A) Vergi oranlarını %100'e kadar yükseltebilir ve sabitleyebilir.\
> **B) Vergi oranlarını 50'ye kadar yükseltebilir, sıfıra kadar indirebilir veya bu Cetveldeki had ve nispetleri %50'sine kadar artırabilir.** ✔\
> C) Vergi oranlarını yalnızca %10 oranında azaltabilir.\
> D) Vergi oranlarını yalnızca %10 oranında artırabilir.\
> E) Vergi oranlarını değiştirme yetkisi yoktur.

**Üretim tarifi:** Uluslararası anlaşmalar (TFA, GATT, DTÖ) ve yetki kanunları için ideal. Beş basamağın beşi de dil olarak mümkün olsun; doğru basamak metinde açıkça yazsın ("teşvik edilir", "zorunludur").

#### G3 — Ters kurgu (olumlu kök, olumsuz mantık)

**Sayı:** 3 (2021, 2022, 2023'te birer; 2024–25'te yok).

**Gerçek örnek — 2023/24:**

> 24\. Tam muafiyet suretiyle geçici ithalata konu aşağıdaki eşyalardan hangisinde ithalat vergilerini karşılayacak tutarda teminat aranmaktadır?\
> A) Türkiye Gümrük Bölgesinde meydana gelen kriz hali nedeniyle bir kamu kuruluşu adına veya kamu kuruluşları tarafından yetkili kılınan kuruluşlar adına gönderilen yardım malzemeleri\
> B) Hava, deniz veya demiryolu şirketlerine veya posta idarelerine ait olan ve bunlar tarafından uluslararası trafikte kullanılmak üzere üzerleri ayırt edici biçimde işaretlenmiş malzeme\
> **C) Test, deneme veya tanıtıma tabi tutulmak amacıyla gönderilen eşya** ✔\
> D) Uluslararası deniz trafiğine kayıtlı bir gemide kullanılmak üzere getirilen gemi adamlarının ihtiyaç malzemesi\
> E) Türkiye Gümrük Bölgesi dışında yerleşik radyo ve televizyon kuruluşları temsilcilerinin mesleki teçhizat kapsamında getirdikleri radyo ve televizyon prodüksiyon ve yayın teçhizatı, bu amaçla kullanım için özel olarak uyarlanmış taşıtlar ve bunların teçhizatı

**Üretim tarifi:** Dört şıkkı istisna listesinden (teminat aranmayanlar), cevabı genel kurala tabi bir öğeden seç. D3'ten farkı: kök kuralı değil istisnanın tersini çağırır.

#### G4 — Örnek seçme

**Sayı:** 2 (TARİFE; 2021/94, 2025/42).

**Gerçek örnek — 2025/42:**

> 42\. Tarifenin Yorumuna İlişkin Genel Kural 3(b) uyarınca, perakende satılacak hale getirilmiş takım halinde bulunan eşya, takımın içindeki mümeyyiz eşyanın GTİP'ine göre sınıflandırılır. Aşağıdakilerden hangisi, bu kuralın uygulanmasına örnektir?\
> A) Tek bir kutu içinde paketlenmiş; az miktarda dezenfektan, az miktarda gazlı bez, bir adet tıbbi plaster, bir çift kauçuk eldiven, küçük bir makas içeren ilk yardım çantası 30.06 tarife pozisyonunda sınıflandırılmıştır.\
> **B) Tek bir kutu içinde paketlenmiş; bir poşet makarna ve üzerine dökmek için bir poşet rendelenmiş peynir ile bir poşet domates sosu (tüm ürünler sadece bir porsiyon makarna hazırlamaya yetecek gramajdadır) 19.02 tarife pozisyonunda sınıflandırılmıştır.** ✔\
> C) Paslanmaz çelikten mamul 18 parça çatal-kaşık-bıçak takımı (takımdaki her bir eşya tipi 6 adettir) 82.15 tarife pozisyonunda sınıflandırılmıştır.\
> D) Plastik tek bir ambalaj içindeki dekoratif amaçlı seramik semaver ve 50 gr çay içeren kutu ayrı ayrı sırasıyla 69.12 ve 09.02 tarife pozisyonlarında sınıflandırılmıştır.\
> E) Plastik bir ambalaj içinde birlikte paketlenmiş iki adet far ve bir adet göz kalemi 33.04 tarife pozisyonunda sınıflandırılmıştır.

**Dikkat:** Aynı makarna seti 2021/94'te de doğru cevaptı. Bakanlık izahnamedeki **kanıtlanmış örneği** yeniden kullanıyor; çeldiriciler değişiyor. Çeldiriciler pozisyon metniyle (GYK 1) çözülen setler (ilk yardım çantası 30.06, sofra takımı 82.15), set sayılmayan paketler (semaver + çay) ya da aynı pozisyonlu kozmetiktir.

**Üretim tarifi:** İzahnamenin GYK örneklerini kullan. Doğru örneği izahnameden, çeldiricileri "set gibi görünen ama başka kuralla çözülen" paketlerden kur.

### V — VAKA (hesapsız; 15 soru, %3)

#### V1 — Tarihli vaka

**Sayı:** 2 (2023/25, 2025/88) · ikisi de F_MATRIS ve F_TUZAKVERI.

**Gerçek örnek — 2025/88:**

> 88\. 01.01.2025 tarihli geçici ithalat beyannamesi ile kısmi muafiyet suretiyle geçici ithal edilen eşya için 30.06.2025 tarihine kadar geçici ithalat izin süresi alınmış, sonrasında 16.04.2025 tarihli serbest dolaşıma giriş beyannamesi ile geçici ithalat kati ithalata dönüştürülmek istenmiştir. 4458 sayılı Gümrük Kanununa göre bu durumda uygulanacak vergi oranları ve gecikme zammı oranında faiz tahsilatına ilişkin aşağıda yer alan ifadelerden hangisi doğrudur?\
> A) 01.01.2025 tarihindeki vergi oranları ve diğer vergilendirme unsurlarına göre gümrük vergileri tutarı tespit edilir, faiz tahsil edilmez.\
> B) 16.04.2025 tarihindeki vergi oranları ve diğer vergilendirme unsurlarına göre gümrük vergileri tutarı tespit edilir, faiz tahsil edilmez.\
> **C) 01.01.2025 tarihindeki vergi oranları ve diğer vergilendirme unsurlarına göre gümrük vergileri tutarı tespit edilir, 01.01.2025 tarihinden başlamak üzere faiz tahsil edilir.** ✔\
> D) 16.04.2025 tarihindeki vergi oranları ve diğer vergilendirme unsurlarına göre gümrük vergileri tutarı tespit edilir, 01.01.2025 tarihinden başlamak üzere faiz tahsil edilir.\
> E) 30.06.2025 tarihindeki vergi oranları ve diğer vergilendirme unsurlarına göre gümrük vergileri tutarı tespit edilir, 01.01.2025 tarihinden başlamak üzere faiz tahsil edilir.

**Üretim tarifi:** Üç tarih ver (beyan, dönüşüm, izin bitişi); biri tuzak olsun. Şıkları "tarih × faiz var/yok" matrisi olarak kur. Tarihleri sınav yılına göre seç.

#### V2 — Olaylı vaka

**Sayı:** 3 (GM; 2023/66, 2024/93, 2025/79).

**Gerçek örnek — 2025/79:**

> 79\. Esenboğa Havalimanı İşletmecisi A firması, havalimanındaki çıkış gümrüksüz satış mağazalarının işletilmesi için gümrüksüz satış mağazaları yönetmeliği uyarınca ihale gerçekleştirmiş ve ihaleyi X firması kazanmıştır. Havalimanında bulunan gümrüksüz satış mağazaları için tek işletmeci durumunda olan X firması ise yine Gümrüksüz Satış Mağazaları Yönetmeliği uyarınca Y firması ile alt işletme sözleşmesi yaparak işletme hakkı kendisinde olan gümrüksüz satış mağazalarından birini yine gümrüksüz satış mağazası işletmesi için Y firmasına kiralamıştır. Buna göre Gümrüksüz Satış Mağazaları Yönetmeliğinin tek işletmeci kuralı doğrultusunda aşağıdakilerden hangisi yanlıştır?\
> A) X firması gümrüksüz satış mağazalarında tütün ürünleri ve alkollü içecek satabilir.\
> **B) Y firması gümrüksüz satış mağazalarında tütün ürünü satabilir.** ✔\
> C) Y firması gümrüksüz satış mağazalarında parfüm satabilir.\
> D) X firmasının çıkışta mağaza açılabilmesi için, başvuru tarihinden önceki aydan başlamak üzere son on iki ay ya da bir önceki takvim yılı içinde toplam en az 10.000 yolcunun havalimanından çıkış yapmış olması gerekir.\
> E) Y firması gümrüksüz satış mağazasında alkollü içecek satamaz.

**Üretim tarifi:** İki ya da üç aktör (A, X, Y) ve bir kural. Şıklar her aktör için kuralın sonucu; biri tersine çevrilmiş. Vaka metni kuralı değil, olayı anlatsın.

#### V3 — Emsal/seçenek seçme

**Sayı:** 3 (2023'te 2, 2025/18).

**Gerçek örnek — 2025/18:**

> 18\. Gümrük kıymeti, benzer eşyanın satış bedeli yöntemine göre tespit edilecek XYZ markalı bir radyoya ilişkin olarak yapılan araştırmada aşağıdaki tespitler yapılmıştır. İthale konu XYZ markalı radyo Çin'de üretilmiş, orijinal ve kaliteli segmentte bir üründür. Gümrük kıymetinin tespitinde aşağıda verilen eşyalardan hangisi esas alınmalıdır?\
> I. XYZ markalı Japonya'da üretilmiş, aynı teknik özellikleri taşıyan radyo, birim kıymeti 5 TL\
> II. XYZ markalı Çin'de üretilen, radyo yanı sıra USB bağlantısıyla müzik çalma özelliği olan cihaz, birim kıymeti 3 TL\
> III. ABC markalı, görünüş ve teknik özellikleri aynı olan, Çin'de üretilen düşük kalite segmentinde ürün, birim kıymeti 1 TL\
> IV. DEF markalı, Japonya'da üretilen, teknik özellikleri dahil diğer hususlarda aynı olan, birim kıymeti 4 TL\
> V. DEF markalı Çin'de üretilen, teknik özellikleri ve fonksiyonları aynı olan ve aynı kalite segmentinde, birim kıymeti 2 TL\
> A) I\
> B) II\
> C) III\
> D) IV\
> **E) V** ✔

**Üretim tarifi:** Emsalliği belirleyen 3–4 boyut seç (ülke, kalite, işlev, marka). Her yanlış adayı **tek bir** boyutta boz; doğru aday "önemsiz" görünen boyutta (marka) farklı olsun.

#### V4 — Tarife tanım/görsel vakası

**Sayı:** 7 (TARİFE) · her yıl 1–2.

**Gerçek örnek — 2025/49:**

> 49\. Dış çapı yaklaşık 4 cm ve iç çapı yaklaşık 2 cm olan plastik halka. Halkanın dış ve iç kısmında iki küçük açıklığı vardır. Koku verici maddelerle emprenye edilmiş, dokunmamış kumaştan bir şerit içerir. Ürün, su içerken solunan ortam havasını aromatize etmek amacıyla özel üretilmiş su şişelerinin ağız kısmına yerleştirilir. Aromatize edilmiş hava retronazal olarak (ağız boşluğunun içinden) algılanır ve tüketiciye aromalı bir içecek tükettiği izlenimini verir. Ürünün farklı kokuları mevcuttur ve koku üretimi için aroma kapsülleri şeklinde alüminyum kompozit folyo torbalarda perakende satışa yönelik olarak paketlenmiştir. Yukarıda tanımı yapılan eşya Türk Gümrük Tarife Cetvelinde hangi tarife pozisyonunda sınıflandırılır?\
> A) 33.01\
> **B) 33.07** ✔\
> C) 39.23\
> D) 39.26\
> E) 76.15

**Doğru cevap ve çeldiriciler:** Çeldiriciler tanımdaki **malzeme kelimelerinden** (plastik → 39.23, 39.26; alüminyum → 76.15) ve **çağrışım kelimesinden** (koku → 33.01) türetilir. Cevap işleve göre.

**Üretim tarifi:** DGÖ sınıflandırma görüşlerinden ya da BTB kararlarından gerçek bir ürün tanımı al. Tanıma iki malzeme ve bir çağrışım kelimesi yerleştir; her biri bir çeldirici olsun.

### K — KAVRAM (12 soru)

#### K1 — Tanım → kavram

**Sayı:** 12 (SAİR 7 · GM 5) · yıllar 2-1-2-**5**-2.

**Gerçek örnek — 2025/89:**

> 89\. 4458 Sayılı Gümrük Kanunu kapsamında, Türkiye Gümrük Bölgesi dışında tamir edilmek istenen eşyanın yerine, tamir işlemi tamamlanarak gümrük bölgesine geri getirilinceye kadar geçen süre içerisinde kullanılmak üzere, serbest dolaşımda olmayan eşyanın geçici olarak ithal edilerek kullanılması usulü aşağıdakilerden hangisidir?\
> A) Eşdeğer eşya sistemi\
> B) Değişmemiş eşya sistemi\
> C) Bağlayıcı menşe sistemi\
> **D) Standart değişim sistemi** ✔\
> E) Sabit değişim sistemi

**Gerçek örnek — 2025/11:**

> 11\. Dış ticarette kullanılan teslim şekillerine ilişkin kuralların belirlendiği INCOTERMS 2020'ye göre aşağıdakilerden hangisi "belirlenen yerde boşaltılmış olarak teslim" anlamına gelen teslim şeklidir?\
> A) FCA\
> B) CPT\
> C) CIP\
> D) DDP\
> **E) DPU** ✔

**Doğru cevap ve çeldiriciler:** Üç çeldirici ailesi: (1) **komşu gerçek kavramlar** (LRN/MRN/GRN/TAD/NCTS, 2024/73; döviz/efektif/konvertibl, 2021/62 ve 2024/37); (2) **kalıba uydurulmuş sahte adlar** ("Sabit değişim sistemi", "Değişmemiş eşya sistemi"); (3) **ters yönlü K1**: kavram verilir, tanım sorulur (GRN, 2022/61).

**Üretim tarifi:** Tanımı mevzuattan aynen al ama kavramın adını tanımın içinde geçirme. Çeldiricilerin en az ikisi gerçek ve aynı aileden olsun.

### B — BOŞLUK (12 soru)

#### B1 — İki boşluk · B2 — Üç ya da dört boşluk

**Sayı:** B1 7 (SAİR 4 · GM 3) · B2 5 · yıllar 0-3-2-2-**5**. **12 sorunun 11'i matris; güncel tutarlar sık sık boşlukta.**

**Gerçek örnek — B1, 2025/59:**

> 59\. Yolcu beraberi yapılan …… TL'yi aşan Türk parası ve Türk parası ile ödemeyi sağlayan belge çıkışlarında gümrük idarelerine Ticaret Bakanlığı tarafından yayımlanan …… ile beyanda bulunulur. Türk Parası Kıymetini Koruma Hakkında 32 Sayılı Karara İlişkin Tebliğe (Tebliğ No: 2008-32/34) göre yukarıdaki boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?\
> A) 125.000 / nakit beyan formu\
> B) 125.000 / sözlü beyan formu\
> **C) 185.000 / nakit beyan formu** ✔\
> D) 185.000 / sözlü beyan formu\
> E) 250.000 / sözlü beyan formu

**Gerçek örnek — B2, 2025/81:**

> 81\. ….. antrepoda bulunan eşyanın devrine ilişkin talepler, eşyanın devrini müteakip .…. içinde gümrükçe onaylanmış yeni bir işlem veya kullanıma tabi tutulmak suretiyle antrepodan çıkarılması şartıyla kabul edilir. Belirtilen süre içinde eşyanın antrepodan çıkarılmaması halinde bu sürenin aşıldığı tarihten itibaren antrepo işleticisine ve devralana ayrı ayrı olmak üzere, aşılan her gün için .…. uyarınca işlem yapılır. Gümrük Yönetmeliği uyarınca yukarıda yer alan boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?\
> A) Genel-5 iş günü–Gümrük Kanunu 241/1\
> B) Genel-10 iş günü–Gümrük Kanunu 241/2\
> **C) Özel- 5 iş günü–Gümrük Kanunu 241/1** ✔\
> D) Özel-10 iş günü–Gümrük Kanunu 241/2\
> E) Genel- 5 iş günü–Gümrük Kanunu 241/2

**Doğru cevap ve çeldiriciler:** Her boşluk bir boyut. Her boyutta 2–3 değer (genel/özel × 5/10 iş günü × 241/1-241/2). Çeldiriciler bir ya da iki boyutu bozuk kombinasyonlar. Bir çeldirici **uydurma ama inandırıcı** değer taşır ("sözlü beyan formu"); bir çeldirici **eski değer** taşır (posta eşiğinde %18 eski oran, 2025/77).

**Üretim tarifi:**

1. Cümlede 2–3 kritik unsur seç (nitelik, süre, yaptırım fıkrası; eşik, oran, form adı).
2. Her unsur için 1 doğru + 1–2 komşu değer belirle.
3. Beş kombinasyon kur: doğru olanı ve her boyutu en az bir kez bozan dört çeldirici.
4. Güncel eşik/oran kullanıyorsan çağırma şablonundaki GÜNCEL TUTARLAR'dan al ve yılı not et.

### E — EŞLEŞTİRME (13 soru)

#### E1 — Beş çiftten yanlış/doğru olan

**Sayı:** 11 (SAİR 6 · GM 3 · TARİFE 2) · yıllar 2-0-3-3-3.

**Kök kalıpları:** "… eşleştirmelerden hangisi yanlıştır?" (8) · "doğru eşleştirilmemiştir" · "yanlış gösterilmiştir".

**Gerçek örnek — 2025/33:**

> 33\. Tercihli tarife uygulanmasına ilişkin aşağıda yer verilen eşleştirmelerden hangisi yanlıştır?\
> A) Türkiye /Bolivarcı Venezuela Cumhuriyeti Ticaretin Geliştirilmesi Anlaşması-EUR.1 Dolaşım Belgesi\
> **B) Türkiye/Azerbaycan Tercihli Ticaret Anlaşması- Form A Menşe Belgesi** ✔\
> C) Türkiye/Gürcistan Serbest Ticaret Anlaşması-EUR.1 Dolaşım Belgesi\
> D) Genelleştirilmiş Tercihler Sistemi-Form A Menşe Belgesi\
> E) Türkiye/ Şili Serbest Ticaret Anlaşması-EUR.1 Dolaşım Belgesi

**Doğru cevap ve çeldiriciler:** Yanlış çiftte sağ taraf **başka bir çiftin gerçek sağ tarafı** (Form A, GTS'nin belgesi). Bakanlık farkı bazen ortak bir sabitin arkasına saklıyor: 2023/57'de her çiftte "10 Ay" yazıyor, fark belge-ülke eşleşmesinde. Konular: anlaşma–belge (2023/47, 2024/35, 2024/41, 2025/33), tebliğ–denetim kurumu (2025/30), kod–işlem (2021/31, 2025/98), eşya–pozisyon (2024/51), örnek–GYK (2021/97).

**Üretim tarifi:** Beş çiftin sağ tarafları gerçek bir kümeden gelsin; yanlış çiftte sağ tarafı kümenin başka bir elemanıyla değiştir. Sağ tarafın aynı değeri iki çiftte birden geçebilsin, yoksa eleme ile bulunur.

#### E2 — Tablo eşleştirme · E3 — Doğru sıralama (permütasyon)

**Sayı:** 1'er (ikisi de 2025'te ilk kez). **Yeni biçimler; 2026–27'de tekrar beklenir.**

**Gerçek örnek — E2, 2025/83:**

> 83\. Gümrük Yönetmeliği kapsamında aşağıdaki tabloda yer verilen eşleştirmelerden hangisi/hangileri doğrudur?

| | İşlem / durum | Sonuç / makam |
|---|---|---|
| I | Geçici depolama yerinde plan değişikliği gerektirmeyen talep | Gümrük Müdürlüğünce sonuçlandırılır. |
| II | Akaryakıt antreposuna tank ilavesi talebi | Bakanlıkça sonuçlandırılır. |
| III | Elleçleme | Geçici depolama yerinde yapılamaz. |
| IV | Antrepo şartlarına ilişkin hafif kusur tespit edilmişse | Bir ay süre verilerek, bu sürede antrepoya eşya girişine izin verilir. |

> Şıklar: A) Yalnız I · **B) Yalnız II** ✔ · C) I ve III · D) II ve IV · E) III ve IV

**Gerçek örnek — E3, 2025/96 (kısaltılmış):** Gümrük Birliği Kararı'ndaki üç belge tanımı (I geri gelen eşyada muafiyet için ihracatçı idaresinin düzenlediği belge; II üçgen trafikte hariçte işleme izni veren idarenin belgesi; III tedarikçi beyanının doğrulanması için düzenlenen belge) verilir. Şıklar INF 2 / INF 3 / INF 4'ün beş permütasyonu; doğru sıra **A) INF 3 – INF 2 – INF 4** ✔.

**Üretim tarifi:** E2 için 4 satırlık tablo; 1–2 satır doğru, ötekilerde makam ya da sonuç kaydırılmış. E3 için adları birbirine çok benzeyen 3 belge/kavram seç (INF, form, karne), tanımlarını sırala, beş permütasyon yaz.

### S — SIRALAMA (3 soru)

#### S1 — Süreç/öncelik sırası · S2 — Numara/büyüklük sırası

**Sayı:** S1 1 (2021/51) · S2 2 (2023/64, 2025/46).

**Gerçek örnek — S1, 2021/51:**

> 51\. Süresi içinde kendilerine gümrükçe onaylanmış bir işlem veya kullanım tayini için gerekli işlemlere başlanmamış eşyanın tasfiyesi hâlinde eşyanın satış bedelinden aşağıda sayılanlar, ayrılarak hak sahiplerine dağıtılır.\
> I. Hizmet karşılığı alacaklar ve yapılmış masraflar\
> II. Gümrük vergileri\
> III. Satış için yapılmış masraflar\
> IV. Para cezaları\
> 4458 sayılı Gümrük Kanunu'na göre yukarıda sayılanların eşyanın satış bedelinden ayrılma sırası aşağıdaki seçeneklerden hangisinde doğru biçimde belirtilmiştir?\
> **A) I, II, III ve IV** ✔\
> B) II, I, III ve IV\
> C) III, I, II ve IV\
> D) IV, III, II ve I\
> E) IV, I, II ve III

**Gerçek örnek — S2, 2025/46:**

> 46\. Türk Gümrük Tarife Cetveline göre aşağıdakilerden hangisinde eşyaların 85 inci fasıldaki sıralanışı pozisyon numarasına göre küçükten büyüğe doğru şekilde belirtilmiştir?\
> A) LED ampul – fotodiyot – mikrodalga yükselteç- sigorta\
> B) Akümülatör- ütü - radar cihazı-redresör\
> C) Pil kömürleri- elektrik kablosu- magnetron- radyo\
> D) Televizyon – rezistans - mıktanıs- invertör\
> **E) Tıraş makinası – akıllı kart – kondansatör - röle** ✔

**Dikkat:** 2021/51'de öncüller **doğru sırayla** verilmiş ve cevap "I, II, III ve IV". Aday "bu kadar kolay olamaz" diye düşünür. Bakanlığın "hepsi doğru" hilesinin sıralama versiyonu.

**Üretim tarifi:** Mevzuatta açık bir sıra (tasfiye bedelinden ayırma, itiraz aşamaları, pozisyon numarası) seç. Çeldiricilerde yalnız 1–2 öğenin yeri bozuk olsun.

### H — HESAP (59 soru, %12)

**Ortak veriler:** Şıklar hep sayı ve çoğunlukla küçükten büyüğe dizili. Doğru harf A 12 · B 14 · C 16 · D 14 · **E 3**. Tuzak veri 59 sorunun 44'ünde. Çeldiriciler "merdiven": her basamak tek bir kalemin yanlış tarafa konmasıyla elde ediliyor. Kural kartları ve çeldirici algoritması `06-SORU-PROMPTU-4_HESAPLAMA` dosyasındadır.

#### H1 — Kalem listeli kıymet

**Sayı:** 13 · yıllar 3-3-3-3-1 · **13 sorunun 13'ünde tuzak veri.**

**Kök kalıpları:** "… gümrük kıymeti kaç TL'dir?" · "… gümrük kıymetini ₺ olarak hesaplayınız." · "… ABD doları cinsinden ne kadardır?"

**Gerçek örnek — 2025/20:**

> 20\. I. Türkiye'de yerleşik (A) firması Çin'de yerleşik (X) firmasından 200 adet sınai makine ithal etmektedir. Makinaların birim fiyatı 100 TL, teslim şekli CIF Mersin olarak belirlenmiştir.\
> II. Söz konusu eşyalar ile ilgili olarak satış sözleşmesine göre, ithal ürünlere ilişkin olarak satıcı tarafından sağlanan garanti nedeniyle toplam 1.500 TL ödenmiştir.\
> III. İthal ürünler ile ilgili lisans bedelleri nedeniyle, sözleşme hükümleri uyarınca, 400 TL net lisans ücreti ödenmiş olup, bu ödemeye ilişkin sorumlu sıfatıyla yapılmış olan % 20 kurumlar vergisi stopajı da ilgili vergi dairesine yatırılmıştır.\
> IV. İthal ürünler, Türkiye'de ithalattan önce üniversitede ekspertize tabi tutulmuş, bunun için 1.000 TL KDV dahil ödeme yapılmıştır.\
> V. Gümrük işlemlerinin ivedilikle sonuçlanmasını teminen gümrük beyannamesinin tescilinden sonra gümrük idaresinde yapılan fazla mesai ile ilgili olarak 1.000 TL ödenmiştir.\
> VI. İthal eşyasına ilişkin ardiye gideri olarak 1.500 TL ödenmiş olup bunun 1.000 TL'lik kısmı serbest dolaşıma giriş beyannamesinin tescil tarihinden önce, 500 TL'si ise sonraki döneme ait bulunmaktadır.\
> VII. Mal bedelinin 10.000 TL'lik kısmının peşin ödemesinin gerçekleştirilebilmesi için ithalatın finansmanı için finansmanı sağlayan kuruma yazılı finansman anlaşması uyarınca, bankacılık düzenlemelerine uygun olarak piyasa koşulları çerçevesinde 1.000 TL faiz ödenmiş, söz konusu işlem ile ilgili olarak da 50 TL BSMV ödenmiştir.\
> VIII. Akreditif işlemi ile ilgili olarak, ithalatçı bankası ile yaptığı görüşme sonucunda, ithalat bedelinin transferi ile ilgili olarak 1.000 TL teyit komisyonu ödenmiştir.\
> Yukarıdaki veriler çerçevesinde, söz konusu eşyanın gümrük kıymeti kaç TL'dir?\
> A) 20.000\
> B) 21.500\
> C) 21.900\
> **D) 22.000** ✔\
> E) 23.000

**Çözüm ve şık türetimi:** CIF 20.000 + satıcıya ödenen garanti 1.500 + stopajla brüte çevrilen lisans 500 = **22.000**. Ekspertiz, tescil sonrası mesai, ardiye, faiz/BSMV ve teyit komisyonu hariç. Çeldiriciler: 20.000 (yalnız CIF) · 21.500 (lisans unutulmuş) · 21.900 (lisans net 400 alınmış) · 23.000 (bir hariç kalem daha eklenmiş).

**Üretim tarifi:**

1. 6–9 kalem; yarısı dahil, yarısı hariç. En az bir kalem "yarısı tescilden önce, yarısı sonra" (ardiye), en az bir kalem "brüte çevirme" (stopaj) ya da "ayıklama" (KDV dahil tutar) gerektirsin.
2. Her çeldirici tek ve adlandırılabilir bir hatanın sonucu olsun; çözümde beş şıkkın türetimini yaz.
3. Teslim şeklini ve giriş yerini açıkça yaz (2021/89-90'daki belirsizliği tekrarlama).

#### H2 — Bağlı soru (çoğunlukla KDV matrahı)

**Sayı:** 5 · yıllar 1-1-2-1-0. 2025'te bağlı soru yok, ama 2021–2024'te her yıl en az bir set var.

**Gerçek örnek — 2024/9 ve 2024/10 (ortak veri seti):**

> 9 ve 10 numaralı soruları aşağıdaki verilere göre cevaplayınız.\
> i) Türkiye'de yerleşik (A) firması Çin'de yerleşik (X) firmasından ticari marka taşıyan el çantaları satın almaktadır. 1.000 adet el çantası için tanesi 50 ABD Doları üzerinden anlaşılmıştır. Eşyalar üretici firmanın Çin'de bulunan fabrikasında teslim alınacaktır.\
> ii) Eşyaların satıcının Çin'de bulunan fabrikasından, ithalatçının Ankara'da bulunan deposuna kadar taşınması işi için bir nakliye firması ile anlaşılmıştır. Firma, Çin'de bulunan fabrikadan ihraç limanına kadar nakliye için 250 ABD Doları, Çin İhraç Limanı - Mersin Limanı deniz taşımacılığı için sigorta dahil 500 ABD Doları, Mersin - Ankara kara taşıması için de 250 TL ücret almaktadır.\
> iii) İthal eşyasının Türkiye'ye kadar nakliyesi ile ilgili olarak ihraç ülkesi limanındaki gecikme için 500 ABD Doları, Türkiye'deki giriş limanına gelişten sonraki gecikme için ise 600 ABD Doları demuraj ödenmiştir.\
> iv) Satıcı firma adına çalışan komisyoncuya 500 ABD Doları komisyon ödemesi yapılmıştır.\
> v) Söz konusu ürünler tüketiciye özel kılıf içinde takdim edilmekte olup, bu kılıflar (A) firması tarafından Çin'de bulunan (Y) firmasından temin edilerek (X) firmasına bedelsiz olarak gönderilmiştir. Bu kılıflar için (Y) firmasına adet başına 2 ABD Doları ödenmiştir.\
> vi) Ticari marka altında pazarlanan el çantaları ile ilgili olarak, satış sözleşmesi hükümleri uyarınca, hak sahibi ABD'de yerleşik (Z) firmasına adet başına 1 ABD Doları lisans ücreti ödenmesi gerekmekte olup ödeme (A) firması tarafından gerçekleştirilmiştir.\
> vii) İthalat ile ilgili olarak Gümrük Laboratuvarında yapılan tahliller nedeniyle, Gümrük Yönetmeliğinin 24 nolu ekinde yer alan tarifeye göre 3.000 TL tahlil ücreti ödenmiştir.\
> viii) Beyannamenin tescilinden önce ithal eşyasının tahliyesi için ödenen ücret 1.000 TL tutarındadır.\
> ix) İthal eşyasının ardiye gideri olarak 3.000 TL ödenmiş olup bunun 1.000 TL'lik kısmı serbest dolaşıma giriş beyannamesinin tescil tarihinden önce, 2.000 TL'si ise sonraki döneme ilişik bulunmaktadır.\
> Döviz kuru: 1 ABD Doları = 1 TL\
> 9\. Yukarıdaki veriler çerçevesinde, ticari işleme ilişkin gümrük kıymeti kaç TL'dir?\
> A) 51.000 · B) 52.750 · C) 54.000 · **D) 54.750** ✔ · E) 55.000\
> 10\. Yukarıda yer alan veriler dikkate alındığında (diğer vergiler ihmal edilmiştir) ithalatta KDV matrahı kaç TL'dir?\
> **A) 57.350** ✔ · B) 58.250 · C) 59.100 · D) 61.000 · E) 61.850

**Çözüm:** Kıymet = 50.000 + fabrika–liman nakliyesi 250 + deniz navlunu ve sigorta 500 + ihraç limanı demurajı 500 + satıcı komisyonu 500 + bedelsiz kılıf 2.000 + lisans 1.000 = **54.750**. KDV matrahı = 54.750 + gelişten sonraki demuraj 600 + tescil öncesi tahliye 1.000 + tescil öncesi ardiye 1.000 = **57.350**. Tahlil ücreti, Mersin–Ankara taşıması ve tescil sonrası ardiye dışarıda.

**Bakanlığın kurgusu:** Bir kalem kıymete girmez ama KDV matrahına girer (giriş yerine varıştan sonraki demuraj, tescil öncesi tahliye ve ardiye). İlk soruda dışarıda bırakılan kalemin ikinci soruda içeri alınması, iki soruyu ayrı ayrı ölçer.

**Üretim tarifi:** Veri setine en az iki "kıymete girmez ama KDV matrahına girer" kalemi koy. İkinci sorunun çeldiricilerinden biri, birinci sorunun yanlış cevabı üzerine kurulmuş olsun (hata taşıma).

#### H3 — Vergi tutarı / zinciri

**Sayı:** 11 · yıllar 1-4-1-2-3 · 24–25: 5.

**Gerçek örnek — 2025/15 (tuzak veri):**

> 15\. Yükümlü (A), ÖTV Kanunu eki (I) sayılı listenin (A) cetvelinde bulunan CIF kıymeti 10.000 TL olan, 1.000 litre eşya ithali yapmaktadır. ÖTV Kanunu eki (I) sayılı listede eşyanın litre başına vergisi 15 TL olarak yer almaktadır. Eşyanın gümrük vergisi oranı %10, KDV oranı %20'dir. Söz konusu eşya için serbest dolaşıma giriş beyannamesi kapsamında, ithalata ilişkin olarak gümrük idaresince tahsil edilecek gümrük vergileri tutarı kaç TL'dir?\
> A) 3.000\
> **B) 3.200** ✔\
> C) 4.500\
> D) 13.200\
> E) 21.000

Kurgu (Bakanlık anahtarına göre): Litre başı ÖTV verisi tuzak; gümrük idaresinin tahsil ettiği tutara girmiyor. GV 1.000 + KDV %20 × 11.000 = 2.200 → 3.200. Çeldiriciler ÖTV'yi bir biçimde katan toplamlar.

**Konu yelpazesi:** MIN/MAX'lı gümrük vergisi (2022/99, 2024/24) · nispi ÖTV ile asgari maktu karşılaştırması (2022/93, 2022/97) · KKDF'nin ÖTV ve KDV matrahına girmesi (2021/87) · motorlu araç ticareti yapanın ithalatında ÖTV doğmaması (2023/78) · faizin KDV etkisi (2025/19).

**Üretim tarifi:** Zincirin her halkasını (GV → İGV → ÖTV → KDV matrahı) ayrı bir çeldiriciyle sına: biri ÖTV'yi KDV matrahına katmaz, biri İGV'yi unutur, biri tuzak veriyi kullanır.

#### H4 — Ceza / uzlaşma / zamanaşımı tutarı

**Sayı:** 6 · yıllar 2-1-1-0-2.

**Gerçek örnek — 2025/13:**

> 13\. Yükümlü (A) firmasının yaptığı serbest dolaşıma giriş rejimi kapsamı bir ithalat ile ilgili olarak, idarece tespit edilen noksan kıymet beyanı nedeniyle tahsili gereken gümrük vergisi tutarı 1.250 TL, ek mali yükümlülük tutarı 1.250 TL, KDV tutarı 500 TL olarak hesaplanmıştır. Yukarıda yer verilen olay kapsamında yükümlü (A) firmasına uygulanacak para cezası kaç TL'dir?\
> A) 5.250\
> B) 6.000\
> C) 7.750\
> **D) 9.000** ✔\
> E) 9.900

**Çözüm:** (1.250 + 1.250 + 500) × 3 = **9.000**. Çeldiriciler bir vergi kalemini dışlayan ya da farklı kat uygulayan tutarlar.

**Üretim tarifi:** Ceza fıkrasını (234/1–234/3, 241/1–241/2) ve kendiliğinden bildirim, uzlaşma, peşin ödeme indirimi gibi hâlleri kombinasyon olarak kullan. Her çeldirici yanlış fıkra, yanlış kat ya da yanlış matrah olsun. Bu soruyu yıllık güncellenen tutarlara bağlayacaksan yılı yaz.

#### H5 — Kıymet yöntemi

**Sayı:** 3 (2021'de 2, 2023'te 1; 2024–25'te yok).

**Gerçek örnek — 2023/83:**

> 83\. (A) ithalatçısının yaptığı, tanesi 50 ABD Dolardan beyan edilen 300 adet mutfak cihazı ithalatında eşya kıymeti satış bedeli yöntemine göre belirlenememiştir. Gümrük idaresince yakın tarihli, aynı ticari düzeyde ithalat yapan (B) firmasının 200 adetlik aynı eşya ithalatında birim kıymetin 70 ABD Doları olduğu anlaşılmıştır. Gümrük idaresince aynı eşyanın satıcısının geçerli fiyat listesi temin edilmiş olup, buna göre satıcı: 1-100 adet satışlarda 80 ABD Doları, 101-200 adet satışta 70 ABD Doları, 201 adet ve üstü satışlarda 65 ABD Doları fiyatından satış yapmaktadır. Bu durumda, yukarıdaki verilere göre, ithale konu söz konusu eşyanın toplam gümrük kıymeti ABD Doları olarak ne kadardır?\
> A) 13.000\
> B) 15.000\
> **C) 19.500** ✔\
> D) 21.000\
> E) 24.000

**Çözüm:** Aynı eşya emsali, satıcının fiyat listesiyle 300 adetlik kademeye düzeltilir: 300 × 65 = **19.500**. Çeldiriciler beyan fiyatı (15.000), emsalin ham fiyatı (21.000) ve yanlış kademeler.

**Üretim tarifi:** Miktar ya da ticari düzey farkını belgeyle düzelttir. Denemede 3 setten birinde, H6 ya da H3 yerine.

#### H6 — Özel kıymet durumu

**Sayı:** 16 · yıllar 1-3-**5-5**-2 · 24–25: 7. **Hesabın en büyük alt tipi.**

**Tanım:** Az kalemli, ama tek bir özel kurala dayanan kıymet: kullanılmış taşıt, royalti/lisans listesi, gözetim, serbest bölgeden ithalat, kendi kendini taşıyan eşya, dolaylı ödeme ve temettü ayıklama, taşıyıcı ortam ve yazılım, diplomatik araç.

**Gerçek örnek — 2025/17:**

> 17\. (A) firması yurt dışında üretilen ileri teknoloji ürünü makineler ithal etmektedir. Bu makineler ile ilgili gayrı maddi haklar nedeniyle, satış sözleşmesinde yer alan koşullar gereğince, aşağıdaki royalti ve lisans ücretlerinin ödenmesi gerekmektedir.\
> \- Makinenin pazarlamasında kullanılan ticari marka için toplam 5.000 TL lisans ücreti\
> \- Eşyanın üretim sürecine ilişkin toplam 4.000 TL patent ücreti\
> \- İthal eşyasının Türkiye'de çoğaltılması hakkı için yapılan 3.000 TL royalti ücreti\
> \- Eşyanın taşıdığı teknolojiye ilişkin know-how için 2.000 TL\
> \- İthal eşyasının dağıtım ve tekrar satış hakları için 1.000 TL royalti ücreti\
> Yukarıda yer alan bilgilere göre gümrük kıymetine dahil edilmesi gereken royalti ve lisans ücreti toplamı tutarı kaç TL'dir?\
> A) 15.000\
> B) 14.000\
> **C) 12.000** ✔\
> D) 11.000\
> E) 10.000

**Çözüm:** Satış koşulu olan bütün royalti ve lisanslar dahil; yalnız **çoğaltma hakkı** (3.000) hariç → **12.000**. Aynı kural 2022/100 ve 2024/23'te de soruldu.

**Dikkat — kullanılmış taşıt:** Dört yılda dört soru (2022/91, 2023/84, 2024/22, 2025/16) ve her birinde indirim kuralı farklı uygulanmış görünüyor (model yılı mı, satın alma yılı mı; yıllık oran mı, tavan mı). 2025/16'nın anahtarı mevzuattan net izlenemiyor. Bu tipte soru üretirken kuralı **soru içinde açıkça** ver ya da yalnız tartışmasız kısmını sor.

**Üretim tarifi:** Tek bir özel kural seç; ona 1–2 tuzak veri ekle (ödeme tarihi kuru, model yılı, temettü). Çeldiriciler kuralın bir adımını atlayan ya da tuzak veriyi kullanan tutarlar.

#### H7 — Hesapsız hesap

**Sayı:** 2 (ikisi de 2023'te).

**Gerçek örnek — 2023/68:**

> 68\. Yükümlü, kendisine tatbik edilen idari para cezaları ile ilgili olarak Gümrük Uzlaşma Yönetmeliği hükümleri çerçevesinde uzlaşma talebinde bulunmuş, yapılan uzlaşma görüşmesi sonucunda 60.000 TL idari para cezası ödenmesi konusunda uzlaşmaya varılmıştır. Yükümlü ayrıca uzlaşılan tutar üzerinden, Kabahatler Kanunu hükümleri çerçevesinde peşin ödeme indirim yapılmasını talep etmiştir. Söz konusu uzlaşılan tutarlar ile ilgili olarak ödenecek tutar ne kadardır?\
> A) 6.000 TL\
> B) 18.000 TL\
> C) 40.000 TL\
> D) 45.000 TL\
> **E) 60.000 TL** ✔

**Kurgu:** Uzlaşılan tutara peşin ödeme indirimi uygulanmaz; cevap verilen tutarın kendisi. Çeldiriciler indirim uygulanmış hâller (45.000 = %25 indirim). 59 hesap sorusunda E'nin doğru olduğu üç sorudan biri.

**Üretim tarifi:** Bir hesap kuralının **uygulanmadığı** hâli seç (uzlaşmada indirim yok, mükerrer vergileme yok). Rakamları bol ver; aday hesaplamaya başlasın. Denemede 3 setten birinde 1 soru.

#### H8 — Diğer sayısal

**Sayı:** 3 (2022/41, 2023/99, 2025/62).

**Gerçek örnek — 2025/62:**

> 62\. Türkiye'de yerleşik A firması, Almanya'da yerleşik B firmasıyla beyaz eşya ihracatı konusunda anlaşmaya varmıştır. Taraflar, ihracat bedelinin ödenmesi için fiili ihracat tarihinden itibaren 200 günlük bir vade belirlemiştir. Buna göre A firması, ihracat bedellerini Merkez Bankası İhracat Genelgesi hükümleri uyarınca azami kaç gün içerisinde yurda getirmek zorundadır?\
> A) 270 gün\
> **B) 290 gün** ✔\
> C) 320 gün\
> D) 360 gün\
> E) 380 gün

**Konu yelpazesi:** İhracat bedelinin yurda getirilme süresi (vade + 90 gün) · antrepo götürü teminatı (2023/99: saha alanı tuzak, tank hacmi esas) · süre ve faiz hesapları.

**Üretim tarifi:** Süre ya da teminat kuralını sayıyla sor; bir tuzak veri ekle (saha alanı, fiili ihraç tarihi yerine sözleşme tarihi).

---

## 4. SINIR DURUMLAR: HANGİ TİP HANGİSİ?

Etiketlerken ve üretirken tereddüt edilen durumlar. Karar ölçütü her zaman **kökün son yüklemi + şıkların biçimi**dir.

| Tereddüt | Karar ölçütü | Örnek |
|---|---|---|
| O1 mi, O2 mi? | Şıklar bir listenin öğeleri ya da hâl başlıklarıysa O1. Her şık bağımsız bir hüküm cümlesiyse O2. Kök "yanlıştır" dese de şıklar liste öğesiyse O1. | 2025/92 (kök "yanlıştır", şıklar koşul öğeleri → O1) |
| O3 mü, O1 mi? | Kökteki kavramın kendisi olumsuz ya da istisnaysa ("dâhil edilmeyen", "istisna", "kaybetmez") O3. | 2025/8 |
| D1 mi, G1 mi? | Şıklar çıplak değerse D1. Değer cümle içindeyse ve kök "hangisi doğrudur" diyorsa G1. | 2025/94 (yalnız süresi değişen beş cümle → G1) |
| D6 mı, V1 mi? | Somut tarih ya da olay verilmişse V1. Genel kural soruluyorsa D6. | 2025/86 (D6) ve 2025/88 (V1) |
| D6 mı, G2 mi? | Şıklar aynı konunun farklı hukuki gücüyse G2. Farklı usul sonuçlarıysa ve kök "yapılması gereken işlem" diyorsa D6. | 2025/72 (D6) |
| D3 mü, Ö3 mü? | Tek cevap isteniyorsa D3. Öncül + kombinasyon şıkkı varsa Ö3. | 2025/1 (D3), 2025/38 (Ö3) |
| Ö3 mü, Ö1 mi? | Öncüller kısa öğe ya da başlıksa Ö3. Tam hüküm cümlesiyse Ö1/Ö2. | 2025/28 (uzun eşya tanımları; Ö1'e yakın Ö3) |
| Ö mü, V3 mü? | Şıklar kombinasyonsa Ö. Şıklar tek numaraysa V3. | 2025/18 (V3) |
| V4 mü, D5 mi? | Uzun teknik tanım ya da görsel varsa V4. Kısa eşya adıysa D5. | 2025/43 (ayran + tanım → V4) |
| H1 mi, H6 mı? | Karışık türde dört ve daha fazla kalemin dahil/hariç eleğiyse H1. Tek bir özel kurala dayanıyorsa H6 (royalti listesi, taşıt, gözetim). | 2025/17 (5 royalti kalemi → H6) |
| H3 mü, H8 mi? | Sorulan vergi toplamıysa H3. Süre, teminat ya da yalnız faizse H8. | 2025/19 (faizli ama vergi toplamı → H3) |

---

## 5. DENEME SINAVI ALT TİP REÇETESİ (100 soru)

Hedefler 5 yıllık pay (%40 ağırlık) ile 2024–25 payının (%60 ağırlık) birleşimidir. Alan toplamları `02-SORU-PROMPTU-0_GENEL` Bölüm 2.1'deki bantların ortasıdır.

### 5.1 Alan × alt tip

| Alan (soru) | Alt tip hedefi | Esnek kontenjan (birini seç) |
|---|---|---|
| **GM (42)** | O2 11 · O1 6 · Ö3 4 · G1 4 · Ö1 3 · D1 2 · Ö2 2 · D3 2 · D6 1 · K1 1 · V1/V2/V3 2 · B1/B2 2 · E1/E2 1 | 1: O3, D2 ya da G3 |
| **SAİR (30)** | O1 7 · D3 3 · D2 2 · O2 2 · Ö1 2 · Ö3 2 · K1 2 · E1 2 · B1 1 · D6 1 · G1 1 · Ö2 1 · Ö4 1 · D4 1 | 2: G2, E3, D5, O3, Ö5 |
| **TARİFE (17)** | O4 7 · D5 4 · D4 2 · V4 2 | 2: E1, G4, S2, G2 ya da B2 |
| **HESAP (11)** | H6 3 · H3 3 · H1 2 · H2 1 (H1'e bağlı) · H4 1 · H8 1 | Üç denemeden birinde H5 ya da H7, bir H6 ya da H3 yerine |

**Ana tip toplamı (yaklaşık):** O 33 · D 18 · Ö 15 · H 11 · G 6 · V 4 · K 3 · B 3 · E 3 · esnek 4. Bu, `02` Bölüm 2.2'deki kök tipi bantlarıyla uyumludur.

### 5.2 Bayrak hedefleri (100 soruluk deneme)

| Bayrak | Hedef | Not |
|---|---|---|
| F_DAYANAK | 60–70 | Kökte mevzuatın adı ("Gümrük Yönetmeliğine göre …") |
| F_SERI | 25–40 | 2–6 soruluk seri bloklar; seri içinde alt tip değişsin |
| F_TUZAKVERI | 8–10 | Bütün H1/H2, H6'ların yarısı, 1–2 vaka |
| F_MUTLAK | 6–8 | Bir kısmı doğru ifadede olsun ("mutlak = yanlış" sezgisini kırmak için) |
| F_MATRIS | 6–9 | B1/B2'nin hepsi, D6 ve V1'in bir kısmı |
| F_MADDENO | ≤ 8 | Yalnız dayanak gösterimi; numara cevap olmasın (241/1–2 ve 234/1–3 istisna) |
| F_YALNIZ | 3–5 | Öncüllülerin ~%20'si |
| F_TUMU | 2–4 | Öncüllülerin ~%15'i; çoğu Ö3'te |
| F_GUNCEL | 3–5 | Çağırma şablonundaki GÜNCEL TUTARLAR'dan; HS 2027 yılında artır |

### 5.3 Dağıtım kuralları

1. Aynı alt tip üst üste en fazla 3 kez. Seri blok içinde (aynı hüküm) alt tip değişmeli: önce kural (O2/G1), sonra öncüllü (Ö1), sonra vaka (V1/V2).
2. Öncüllülerde cevap: ~%65 ara kombinasyon, ~%20 "Yalnız X", ~%15 tüm öncüller.
3. Hesap sorularında doğru cevap en fazla 1 kez E.
4. O2'lerde hiçbir bozma tekniği %30'u geçmesin (Bölüm 3, O2 tablosu).
5. Tarife bloğunda O4 ve D5 dönüşümlü gelsin. Aynı fasıldan iki soru varsa alt tipleri farklı olsun.
6. Cümle şıklı sorularda doğru şık ~%60 orta uzunlukta. Bozuk şıkkı kısa, doğru şıkkı uzun yazma alışkanlığına düşme.

---

## 6. PROMPTLARDA KULLANIM

02–06 numaralı soru promptlarının çağırma şablonuna `ALT TİP` satırı eklendi:

```
ALT TİP: OTOMATİK          → Bölüm 5 reçetesi (alan promptunda o alanın satırı)
ALT TİP: O2×3, Ö3×2, B2×1  → Yalnız bu alt tiplerden, bu sayılarda
ALT TİP: KARMA-24-25       → 2024–25 paylarına göre (son eğilim)
```

Her üretilen sorunun altında `Kalıp/Teknik` satırı alt tip kodunu da verir; örneğin: `Kalıp: O2 – polarite tersi – Gümrük Yönetmeliği teminat hükmü`.

**Öneri:** Önce bu katalogdaki örnek soruyu promptun KALİBRASYON alanına yapıştır, sonra o alt tipte üretim iste. Model biçimi örnekten, mantığı karttan alır.

---

## 7. YÖNTEM NOTU

- 500 sorunun her biri, kitapçık metni ve kırmızıyla işaretli resmî cevap üzerinden tek tek etiketlendi. Etiket sözlüğü (`TIPOLOJI.md`) yıllar arasında aynı tutuldu.
- Her soru için ayrıca şık türü, öncül sayısı, doğru harf, doğru şıkkın uzunluk konumu, kökün son yüklemi ve "doğru cevap nasıl kurulmuş" notu kaydedildi.
- Tereddütlü etiketler, her yılın örnek dosyasının sonundaki "Sınır durumlar" bölümünde gerekçesiyle listelendi.
- O2 bozma tekniği dağılımı ve O1 yabancı öğe kaynakları, kurulum notlarından elle yapılmış sınıflandırmadır; sayılar yaklaşık kabul edilmelidir.
- Veri dosyaları: `gmcikmislar/analiz/soru-tipi/` → `2021…2025_tipler.csv` (500 satır), `2021…2025_ornekler.md` (her alt tip için aynen örnekler), `TIPOLOJI.md` (sözlük), `TOPLU.md` (bütün sayımlar ve her sorunun kurulum notu).
