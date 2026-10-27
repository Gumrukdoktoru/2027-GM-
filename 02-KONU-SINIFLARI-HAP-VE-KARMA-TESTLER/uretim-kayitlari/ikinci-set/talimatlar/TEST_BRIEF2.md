# KARMA TEST — İKİNCİ SET (Test 4–6) ÜRETİM TALİMATI

Temel talimat `$S/karma/TEST_BRIEF.md`'dir (`S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`). Onu baştan sona oku ve uygula; **aşağıdaki farklar onun önüne geçer.**

## Farklar

1. **Set ve yollar:** Testler 4, 5, 6 (`test` alanı 4/5/6). Slot listen `$S/karma2/slots/<KÜME>.md` (küme adları B01…B16). Çıktı `$S/karma2/out/<KÜME>.json`, betikler `$S/karma2/work_<KÜME>/`. Malzeme dosyaları ilk setteki küme adlarıyla: B03 için `$S/hap/cikan/K03.json`, `$S/hap/sorulmayan/K03.json`, `$S/hap/girdi/K03.md` (slot dosyasının sonunda yazılı).

2. **Hesaplama ayrı konu:** 2021–2025'in 59 hesap sorusu ayrı "Hesaplama" konusuna sayılır. Hesap soruları yalnız B15 ve B16 kümelerinde yazılır (`alan: "HESAP"`, `konu` = hesap türünün konu kodu, ör. KIYMET, KDV). **B01–B14 kümelerinde hesap sorusu yazma** (TEST_BRIEF §3'teki "kıymet slotlarında 3 hesap + 2 sözel" ve "K09'da 1 hesap" kuralları bu sette geçersiz); bu kümelerin bütün slotları sözeldir. Gümrük Kıymeti, KDV, ÖTV, Cezalar gibi konuların sınıfı yalnız sözel sorularına göredir (slot dosyasındaki sınıf ve sayı).

3. **Tekrar yasağı (en önemli kural):** İlk set (Test 1–3, 150 soru) ve önceki 3 deneme yayımlandı. Senin sorunun **cevabını belirleyen hüküm** bunlardan hiçbirinde ölçülmüş olmamalı; çeldiricilerde de aynı hükmü aynı kurguyla kullanma.
   - İlk set: `$S/karma/out/K*.json` (konu kodunla ve anahtar sözcükle tara; `kok`, `onculler`, `siklar`, `aciklama`, `dayanak` alanları).
   - Denemeler: `/home/user/2027-GM-/01-DENEME-SINAVLARI/veri/deneme{1,2,3}.json`.
   - Aynı konunun **başka alt başlıklarına** ve **sorulmamış hükümlerine** git: `$S/hap/sorulmayan/<K>.json` içindeki `alt_konular` (durum SORULMADI / KISMEN) ve `beklenen` listeleri ana kaynağındır.
   - İkinci setin diğer kümeleri seninle eşzamanlı yazılıyor; komşu konulara (ör. transit–TIR, menşe–STA) taşma, kendi slot konunda kal.

4. **Kaynak tipi etiketi:** `kaynak_tipi: "cikmis"` yalnız **cevabı belirleyen bilgi** 2021–2025'te bir soruda (doğru şık, çarpıtılmış yanlış şık ya da öncül olarak) ölçüldüyse; `cikmis_ref` o soruların listesi. Aynı maddenin başka bir fıkrası ya da aynı listenin başka bir kalemi ölçüldüyse **"beklenen"**. Bu sette çok çıkan slotlarda da ağırlık beklenen hükümlerde olsun (ilk set çıkmış bilgi alanlarını büyük ölçüde kullandı); çıkmış bilgi alanı kullanırsan ilk setin kullanmadığı çıkmış sorulardan seç.

5. **Hiç çıkmayan konular:** B03'teki TRBASIT (Test 4), B12'deki EIHR (Test 5), B02'deki TASIT (Test 6) — beklenen hap ve sorulmayan hükümlerden, kaynakta birebir doğrulanmış.

6. **Güncellik:** Şu değişikliklere aykırı doğru cevap ya da açıklama yazma: AYM 26.03.2026 (GK 241/1'de yalnız "ikincil düzenlemelere aykırılık" ibaresi iptal; miktar ve 241/3–6 katları yürürlükte); Danıştay 12.08.2026 (GY 94 ve 130/1 iptal); KDVK 21/1-ç (24.07.2025; (I) sayılı listede teminata esas ÖTV KDV matrahına girer); 2009/15481 sayılı Karar md. 62/1 (07.01.2026 CK, yürürlük 06.02.2026); TIR Tebliği 04.07.2026 değişikliği; 2025/9903 sayılı Karar 2012/3305'in yerini aldı; Revize PEM menşe kuralları (27.03.2026; tam kümülasyon bilgisini kullanma). Kaynak dosyalarındaki dipnotlara bak; mülga/iptal hükmü doğru cevap yapma.

7. **Hesap soruları (B15, B16):**
   - Her şık tek bir adlandırılmış hatadan türesin; açıklamada beş şıkkın türetimini yaz. Betikle 0–2 hatalı bütün yolları tara: iki farklı tek hata aynı sayıyı vermesin, hiçbir hatalı yol doğru cevabı vermesin.
   - Yalnız kaynakta açık kurala dayan. Yalnız resmî anahtara dayanan kuralları kullanma: "önceki işlemlerden kazanılmış indirim fiyattan düşülmez" (2023/79), antrepo götürü teminatında "açık + kapalı alan" ölçütü, kullanılmış taşıt indirim oranı.
   - Yıllık değişen tutar ve oranlar (İGV, MIN/MAX, ceza katı, faiz, kur, ÖTV tutarı) kökte veri olarak verilsin ("… olduğu varsayılmaktadır").
   - Ceza hesabında matraha girecek vergileri kökte açıkça yaz (GK 234/1'in güncel metninde KDV'nin matrahta olup olmadığı tartışmalı).
   - Ortak veri seti (B15'teki Test 5 H2 slotu + B16'daki Test 5 H2 slotu, `ortak_veri_id: "KT5-H2"`): `ortak_veri` metni yalnız ilk soruda (B15), ikincide `null`; ikinci sorunun kökü ilkinin cevabını vermesin. B15 ve B16 ayrı ajanlarca yazılıyor: **B15 yazarı ortak veri metnini ve kıymet sorusunu yazar ve metni `$S/karma2/KT5-H2_ortak_veri.txt` dosyasına da kaydeder; B16 yazarı bu dosya oluşana kadar diğer slotlarını yazar, sonra aynı veriden KDV matrahı sorusunu kurar.**
   - İlk setin hesap kurgularını (Test 1–3: 91.02 saat MIN/MAX+İGV, 234/1-b kıymet farkı + EMY, EXW kompresör → KDV matrahı seti, KKDF kabul kredili/mal mukabili, şarap ÖTV, parfüm demuraj/ardiye, (I) liste baz yağ 21/ç, tarife farkı + kendiliğinden bildirim + DİR yarısı) ve deneme hesaplarını tekrar etme.

8. **Rapor:** TEST_BRIEF §6'ya ek olarak, ilk setle ya da denemelerle yakın bulduğun ve bilerek ayrıştırdığın her soruyu bir satırla yaz.
