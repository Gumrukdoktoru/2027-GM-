# KT5-H2 ortak veri seti: Türkiye tarafının yeniden kurulumu (B15-04 + B16-05)

- Yedek: `karma2/out_onceki_kt5/` (B15.json, B16.json, KT5-H2_ortak_veri.txt; değişiklikten önce alındı).
- Betik: `karma2/work_kt5/kt5_rebuild.py` (`apply` yedekten okur ve yazar; argümansız çalıştırılınca yalnız tarama yapar).
- Tarama çıktısı: `karma2/work_kt5/scan.txt` (GENEL: GEÇTİ). AD tutarı ön araması: `karma2/work_kt5/search_ad.py`.
- Değişen alanlar (v2 sonrası, yedekle karşılaştırıldı): B15-04 (`ortak_veri`, `aciklama`, `dayanak`, `kaynak`; `siklar` ve `tuzak` yedektekiyle aynı), B16-05 (`kok`, `siklar`, `aciklama`, `tuzak`, `dayanak`, `kaynak`, `kaynak_tipi`, `cikmis_ref`) ve B16-02 (yalnız `aciklama` son cümlesi, koordinatör talebi). Diğer 16 soru birebir aynı.
- v2 (koordinatör talebi): B15-04'te 3.600.000 (pompa tam bedel) şıkkı geri kondu, 3.670.000 çıkarıldı; B16-02 açıklamasının son cümlesi değişti. Ayrıntı §9. İlk sürümün betiği `work_kt5/kt5_rebuild_v1.py` olarak saklandı.

## 1. KDVK 21 unsurlarının önceki kullanımı

| Soru | KDVK 21 unsuru | Kurgu |
|---|---|---|
| İlk set K16-04 (T2, H2) | a; b (yalnız GV); c: tescil öncesi transit taşıma (KDV'siz), ardiyenin tescil öncesi/sonrası ayrımı, tescil sonrası fabrikaya taşıma | EXW kompresör seti; reklam kıymete girmez |
| İlk set K09-09 (T3, H3) | a; b (GV, İGV, ÖTV-IV); c: Mersin demurajı, ardiye ayrımı, KDV'li müşavirlik girmez | Parfüm; tescil öncesi giderler ÖTV matrahına da girer |
| İlk set K09-01 (T1) | ç: teminata esas ÖTV; KKDF yok (peşin) | Baz yağ |
| İlk set K09-07, K01-09, K01-14 | b: GV, ÖTV-III; c: tescil sonrası taşıma girmez | Şarap; FOB %10/%3; temettü ve dahili vergi |
| 1. deneme HS-A-01/02 (H2) | c: İzmir demurajı, ardiye ayrımı, KDV dahil müşavirlik, tescil sonrası nakliye, kurulum | CNC tezgâhı seti |
| 1. deneme HS-B-01, HS-B-03 | b: İGV, ÖTV-IV; ç: motorin teminatı | Klima; motorin |
| 2. deneme HS-A-07/08 (H2) | c: tahliye, memur yolluğu, ardiye ayrımı, tescil sonrası tahlil ve nakliye | Endüstriyel fırın seti |
| 2. deneme HS-B-07 | b: KKDF (mal mukabili); kur: tescil tarihi | Kompresör |
| 3. deneme HS-A-13/14 (H2) | c: Kapıkule–Halkalı taşıması, depolama ayrımı, tahliye, tescil sonrası nakliye, montaj | Boyama makinesi seti |
| 3. deneme HS-B-11, HS-B-12 | b: GV, İGV, ÖTV-IV; kur | Televizyon; cep telefonu |
| 3. deneme SR-A-33 (sözel) | c'deki "fiyat farkı, kur farkı" doğru ifade olarak şıkta; cevap 23/e (külçe altın) | — |
| İkinci set B09-03 (T5, sözel) | a ikinci cümlesi (CIF değeri) | — |
| İkinci set B15-08 (T6), B16-08 (T6) | a-b; c: tescil sonrası gider; beyanname başına tescil kesimi | Posta; antrepodan parça çekme |

Hesap sorularında hiç kullanılmayan unsurlar: 21/b'deki "her türlü vergi, resim, harç ve paylar"ın GV, İGV, ÖTV ve KKDF dışındaki kalemleri (ör. dampinge karşı vergi) ve 21/c'deki fiyat farkı ile kur farkı. 2021–2025 sınavlarında da dampinge karşı vergi yalnız sözel sorularda geçiyor (2021 TPS, 2022/21, 2024/43); KDV matrahında ölçülmedi.

## 2. Seçilen unsur ve gerekçe

**KDVK 21/b: "İthalat sırasında ödenen her türlü vergi, resim, harç ve paylar"; yeni kalem dampinge karşı vergi.** Kaynakta birebir görülenler:
- KDVK 21/b metni (`kaynak2/diger/SAİR MEVZUAT KİTABI.md`).
- 3577 sayılı Kanun md. 8: mükellef, malı ithal eden kişidir. Md. 9: vergi gümrük idarelerince, ithalde alınan diğer vergilerden ayrı olarak tahsil olunur.
- GK 28/f: eşyanın ithali veya satışı nedeniyle Türkiye'de ödenecek ithalat vergileri gümrük kıymetine dahil edilmez. GK 3/9-a: ithalat vergileri, ithalde ödenecek gümrük vergisi ile diğer eş etkili vergiler ve mali yüklerdir.

Böylece aynı kalem iki soruda iki ayrı kuralı ölçüyor. Kıymet sorusunda kıymete girmez (GK 28/f). KDV sorusunda matraha girer (21/b).

**Seçilmeyen: 21/c kur farkı (tescil öncesi/sonrası).** "Tescil tarihine kadar fatura ve benzeri vesikalarla belgelendirilen" ifadesi kaynak klasörlerinde yok; KDV Genel Uygulama Tebliğine ait olmalı ve tebliğ kaynaklarda bulunmuyor. Kanunun 21/c metninde tescil kesiminin kur farkına da uygulanıp uygulanmadığı açık değil. Mal bedeline bağlı bir kur farkı ya da fiyat farkı ayrıca fiilen ödenen fiyatı değiştirir (GK 24/3-a, 30); bu da 3.550.000'lik kıymeti bozar. Kural "açık yazılı" şartını karşılamıyor.

Kullanılmayan kurgular: demuraj, ardiye ayrımı, tahliye, fazla mesai, müşavirlik, iç taşıma (21/c kesimi). B10-04'ün (T6) konusu olan geçici önlem teminatı da kullanılmadı. 21/a'nın CIF cümlesi B09-03'te (T5) ölçüldüğü için kullanılmadı.

## 3. Yeni ortak veri (Türkiye tarafı)

Eski vii–xii bentleri ve "(vii, viii, ix ve x … KDV hesaplanmamıştır.)" notu çıkarıldı. i–vi bentleri, kur ve oranlar aynen kaldı. Yeni metin:

> vii) Eşyanın ithalinde, serbest dolaşıma giriş beyannamesi kapsamında gümrük vergisi ve ilave gümrük vergisinin yanı sıra araç başına 2.400 ABD Doları dampinge karşı vergi ödenmiştir.
> Eşyanın gümrük vergisi oranının %10, ilave gümrük vergisi oranının %15 ve dampinge karşı vergi tutarının yukarıda belirtildiği gibi olduğu varsayılmaktadır.
> (Döviz kuru: 1 ABD Doları = 10 TL alınacaktır. Hesaplamada sadece soruda yer verilen hususlar dikkate alınacaktır.)

Yıllık değişen tutarlar (GV, İGV, AD, kur) kökte veri olarak verildi. KDV oranı gerekmediği için verilmedi.

Türkiye tarafı bilerek tek bentte tutuldu. Yasak kurgulara girmeyen ikinci bir Türkiye kalemi denendi ama hepsi elendi:
- Tescil öncesi ya da sonrası her gider 21/c kesimine dayanıyor.
- Sözleşme damga vergisi ve trafik harcı, zamanlama belirsizliğiyle 21/c'ye kayıyor.
- Geçici önlem teminatı B10-04'ün hükmü.

Seçilen AD tutarı 2.400 ABD Doları/araç (toplam 120.000 TL). Ön aramada bu tutar her iki soruda ve çapraz yollarda temiz çıkan değerlerden biri. 1.000 ABD Doları 3.600.000 ile, 2.000 ABD Doları ise satış komisyonu ile çakışıyordu.

`KT5-H2_ortak_veri.txt` güncellendi. Ortak veri kısmı JSON alanıyla birebir aynı; ayraçtan sonraki not yeni çözüme göre yeniden yazıldı.

## 4. B15-04 (kıymet) — v2 son hâli

- Doğru cevap **3.550.000** (değişmedi); anahtar D (indeks 3).
- Şıklar: 3.400.000 / 3.530.000 / 3.540.000 / **3.550.000** / 3.600.000 (yedekteki şıklarla aynı).
  - 3.400.000: pompa farkı eklenmemiş. 3.530.000: satış komisyonu eklenmemiş. 3.540.000: tesis–Şanghay taşıma ve yükleme eklenmemiş. 3.600.000: pompaların tam alış bedeli eklenmiş (üreticinin ödediği ve fiyata yansıyan 5.000 ABD Doları ikinci kez katılmış).
  - Eski ardiye ve müşavirlik kalemleri veride olmadığından 3.600.000'in tek türetimi artık pompa hatası. Eskiden "tescil öncesi ardiye + müşavirlik" iki hatalı yolu da bu sayıya düşüyordu; bu yol ortadan kalktı.
- Çözümde tek cümle eklendi: Türkiye'de ödenen dampinge karşı vergi ithalat vergisi olduğundan kıymete dahil edilmez (GK 3/9-a, 28/f). Dampinge karşı verginin kıymete eklenmesi 3.670.000 verir; açıklamada "şıklarda yer almaz" listesine yazıldı.
- Tuzak alanı yedekteki hâliyle kaldı (3.400.000 ve 3.600.000 pompa tuzakları). Dayanak ve kaynakta GK 28/a çıkarıldı (Türkiye'de taşıma yok); GK 28/f ve 3/9-a eklendi. `kaynak_tipi` cikmis ["2024/26"] aynen kaldı.
- İlk sürümde (v1) beşinci şık 3.670.000 (dampinge karşı vergi kıymete eklenmiş) idi. Koordinatör, pompa hatasının sorunun asıl ölçtüğü noktadaki en güçlü çeldirici olduğu gerekçesiyle 3.600.000'in geri konmasını istedi.

## 5. B16-05 (KDV matrahı), baştan kuruldu

- Kök: "Yukarıdaki veriler dikkate alındığında (soruda yer verilmeyen vergi ve mali yükler ihmal edilmiştir; (v) numaralı bentteki komisyon için hesaplanan KDV, (A) firmasınca sorumlu sıfatıyla beyan edilerek ödenmiştir) ithalatta KDV matrahı kaç TL'dir?"
  - Eski kökteki "GV ve İGV dışındaki vergiler ihmal" ifadesi AD'yi dışlayacağı için kaldırıldı.
  - (v) notu korundu: alım komisyonu tescil öncesi vergilendirilmemiş ödeme sayılırsa 21/c'nin lafzi okumasıyla matraha girebilirdi (2023/73).
- Çözüm: 3.550.000 + GV 355.000 + İGV 532.500 (kıymet üzerinden) + AD 120.000 = **4.557.500**.
- Şıklar (artan, `sira_sabit` true, doğru indeks 2, C; eskisiyle aynı harf):

| Şık | Türetim (tek hata) |
|---|---|
| 4.370.000 | Kıymet sorusundaki pompa farkı hatası taşınmış (3.400.000 + 340.000 + 510.000 + 120.000) |
| 4.437.500 | AD, ithalat sırasında ödenen vergi olduğu hâlde matraha alınmamış (21/b) |
| **4.557.500** | Doğru |
| 4.572.500 | KDV'si sorumlu sıfatıyla ödenmiş alım komisyonu (15.000) matraha eklenmiş (21/c "vergilendirilmeyenler" şartı) |
| 4.587.500 | AD kıymete katılıp GV ve İGV de üzerinden hesaplanmış (3.670.000 + 367.000 + 550.500). Kıymet sorusunda bu hata şık değil (3.670.000); KDV sorusunda bağımsız, adlandırılmış tek hata olarak geçerli |

- Açıklama beş şıkkın türetimini yazıyor. Tuzak ve açıklamada konum atfı yok; "ortak veri setinin kıymet sorusu" deniyor (betik "ilk soru", "önceki soru" ve "bir önceki" ifadelerini aradı, bulmadı).
- Dayanak: KDVK 21/a-c ve md. 9; 3577 s. Kanun md. 8-9; GK 3/9-a, 28/e, 28/f.
- **`kaynak_tipi`: "beklenen", `cikmis_ref`: [].** AD'nin KDV matrahına girmesi 2021–2025'te ölçülmedi (`exams/*_red.txt` tarandı). Aynı bentteki GV ve İGV 2024/25'te ölçüldü; bu yüzden etiket TEST_BRIEF2 §4 gereği "beklenen".
- Zorluk K'de bırakıldı. B16'da K sayısı zaten 2/9; O'ya çekilirse 1/9'a düşerdi.

## 6. Tarama (betik: `kt5_rebuild.py`, çıktı: `scan.txt`; v2 sonrası yeniden çalıştırıldı)

- **B15-04:** 8 tek hata, 27 iki hatalı yol. Doğru tutar modelle uyumlu. Dört çeldiricinin her biri tam bir tek hatadan türüyor: pompa0, satkom_yok, fab_liman_yok, pompa_tam. İki tek hata aynı sayıyı vermiyor (pompa_tam 3.600.000, ad_kiymet 3.670.000). Hiçbir 1 ya da 2 hatalı yol 3.550.000 vermiyor. İki hatalı yollardan başka bir hatanın çeldiricisine düşen de yok; 3.600.000'e düşen iki hatalı yol yok.
- **B16-05:** 13 tek hata (B15'in 8 hatası taşınmış hâliyle + AD yok, alım komisyonu KDV'ye eklenmiş, GV yok, İGV yok, İGV kıymet + GV üzerinden), 74 iki hatalı yol. Çakışma ve doğru tutara düşen yol yok. 4.370.000 (pompa0 taşınmış) ve 4.587.500 (ad_kiymet) her biri tek bir hatadan türüyor; ikisi de geçerli.
- **Çapraz yol:** B15-04'teki 8 tek hatanın her biri (pompa_tam 3.600.000 dahil) B16-05'e taşındı ve üstüne B16'ya özgü 5 hatadan biri eklendi; hiçbir yol 4.557.500 vermiyor. Pompa tam bedel hatası taşınırsa 4.620.000 çıkar; şıklarda yok.
- **Kökler:** B16-05 kökü kıymeti (3.550.000) vermiyor. Ortak veri ve B15-04 kökü KDV matrahını vermiyor. B16-05'in `ortak_veri` alanı null.

## 7. Aynı testle (Test 5) çakışma ve ipucu kontrolü

- **B09-03** (21/a CIF cümlesi): B16-05 bu cümleyi kullanmıyor. Ortak veride muafiyet ya da kıymet esası dışı vergi yok. B09-03'ün şıkları 21/b'ye değinmiyor.
- **B16-07** (İGV tavanı, 2/3 ve 4/4): B16-05'te İGV kıymet üzerinden hesaplanıyor; B16-07'nin açıklamasıyla uyumlu. GV + İGV = %25, tavanın altında. İGV matrahına dayalı çeldirici bilerek kullanılmadı.
- **B16-06** (sigara ÖTV), **B15-05** (indirim ve kur), **B15-06** (ardıl satış; Mersin demurajı tuzak): çakışma yok. Eski ortak verideki Mersin demurajı Test 5'te B15-06 ile tekrar ediyordu; bu tekrar da kalktı.
- **B02-07** (gümrüklenmiş değer = CIF + gümrük vergileri): kavramsal komşuluk var ama KDV matrahını ya da tutarı vermiyor. Kabul edildi.
- **B10-04** (geçici önlem teminatı, 3577) Test 6'da. B16-05'te kesin vergi "ödenmiştir" diye geçiyor; teminat hükmü kullanılmadı.

## 8. Kalan riskler

- AD'nin GK 3/9-a anlamında "ithalat vergisi" sayılması "diğer eş etkili vergiler ve mali yükler" ifadesine dayanıyor. Kıymet tarafı için ayrıca GK 27/3 de aynı sonucu verir (ilave yalnız sayılan unsurlarla yapılır). B15-04'te risk düşük.
- Türkiye tarafı tek bent; gerçek H2 setlerinden daha sade. Bu, yasaklı 21/c kurgusundan uzak durmanın bedeli.
- 4.572.500 çeldiricisi, "vergilendirilmiş ödeme matraha girmez" hükmünü yeni bir kalemle (sorumlu sıfatıyla ödenen KDV) kullanıyor. Cevabı belirleyen unsur değil; müşavirlik kalemi kullanılmadı.

## 9. v2 değişiklikleri (koordinatör talebi)

1. **B15-04:** 3.670.000 şıkkı çıkarıldı, 3.600.000 geri kondu. Şıklar 3.400.000 / 3.530.000 / 3.540.000 / 3.550.000 / 3.600.000; doğru indeks 3. Açıklamada beş şıkkın türetimi buna göre yazıldı. Dampinge karşı verginin kıymete girmediği çözümde tek cümle (GK 3/9-a, 28/f). Tarama yeniden çalıştırıldı: GEÇTİ (§6). B16-05'in 4.370.000 ve 4.587.500 şıkları geçerliliğini koruyor; B16-05'te değişiklik gerekmedi.
2. **B16-02 açıklaması:** Son cümle "Tarama: tek hatalar birbirinden farklı sonuç verir; hiçbir iki hatanın birleşimi doğru tutarı vermez." B16-02'de **birebir** bulundu (açıklamanın son cümlesi). Yerine şu cümle kondu: "Dört çeldirici dört ayrı tek hatadan türer; II. bentte alt sınırın altında kalan her hesap alt sınırla 2.000 TL'ye tamamlandığından bu bentte ölçülen bilgi alt sınırın kendisidir." B16-02'nin başka alanına dokunulmadı.
3. `KT5-H2_ortak_veri.txt` içindeki ayraçlı not yeni şıklara göre güncellendi; ortak veri kısmı JSON alanıyla birebir aynı.

