# HS-A doğrulama raporu (18 hesap sorusu)

Yöntem: Her soru kör olarak yeniden çözüldü ve beş şıkkın türetimi bağımsız bir betikle yeniden hesaplandı (`work_verify_HS-A/recompute.py`). Kural kaynağı: 06-HESAPLAMA K1–K8 ve çeldirici algoritması (§4). Karşılaştırılan çıkmış sorular: 2021/85, 87, 88 · 2022/89-90, 96, 98, 100 · 2023/74, 75, 76, 80, 81-82, 83 · 2024/9-10, 18, 19, 26, 27 · 2025/17, 20. Kaynak metin: `38-serbest bölge.txt` GK md. 161/1. Özgün dosya `out/orig/HS-A.json` olarak saklandı, düzeltmeler `work_verify_HS-A/fix.py` ile uygulandı.

**Sonuç:** 18 sorunun hepsinde anahtar ilk hâliyle de aritmetik ve kural yönünden doğruydu. Düzeltmeler çeldirici algoritmasına uyum, iki hatanın aynı sayıyı verdiği şık ve harf dağılımı içindir.

| id | Karar | Ne değişti / neden (kaynak) |
|---|---|---|
| HS-A-01 | TAMAM | Kıymet 311.500 ABD Doları × 10 = 3.115.000. FOB Yokohama, giriş yeri İzmir ve tescil kuru tek anlamlı. Faturada ayrıca gösterilen ve alıcı lehine düzeltilen dahili vergi fiyattan düşülmüş; bu K3 ve 2022/89 anahtarıyla aynı. Satış komisyonu dahil. Kurulum, İzmir demurajı, ardiye, müşavirlik ve Manisa nakliyesi hariç. Dört çeldiricinin her biri tek hatadan çıkıyor. |
| HS-A-02 | TAMAM | KDV matrahı 3.115.000 + İzmir demurajı 8.000 + tescil öncesi ardiye 15.000 = 3.138.000. Matraha alınan giderlerin üçü de tescilden önce. Taşınan hata çeldiricisi (3.198.000) tek hatadan çıkıyor: birinci sorunun 3.175.000 şıkkı + 23.000. Müşavirlik, tescil sonrası ardiye ve nakliye hariç (2022/90, 2024/10). |
| HS-A-03 | TAMAM | EXW: fabrika–liman taşıması, ihraç limanı demurajı, assist ve ayrıca faturalanan ambalaj dahil. Alım komisyonu, Türkiye'de yapılan tasarım, Mersin demurajı ve reklam hariç. Sonuç 133.700 (2021/85, 2024/9). Şıkların hepsi türetiliyor. |
| HS-A-04 | TAMAM | 500.000 + marka 40.000 + brüt patent 30.000 (24.000 / 0,80) = 570.000. Çoğaltma hakkı ve satış şartı olmayan dağıtım hakkı hariç (2025/20, 2025/17, 2022/100). |
| HS-A-05 | DÜZELT | Anahtar ve şıklar aynı kaldı (41.600). "GY hükmü klasörde yok" denilen dayanak kaynakta bulundu: **GK md. 161/1** (`38-serbest bölge.txt` satır 67). Serbest bölgedeki depolama ve muhafaza masrafları fiyattan ayrı gösterilmişse kıymete girmez. Dayanak, kaynak ve açıklama buna göre düzeltildi; 33.100 şıkkının türetimi "(S)'nin edinme maliyeti esas alınmış" diye netleştirildi; `guven` yüksek yapıldı. Soru 2023/75 anahtarının mantığını aynen izliyor. Eklenen satış komisyonu (dahil) ve alıcının pazarlama gideri (hariç) yeni bir belirsizlik yaratmıyor. |
| HS-A-06 | TAMAM | 60.000 + dolaylı ödeme 8.000 = 68.000. Mahsup bir ödeme şeklidir, fiyatı azaltmaz. Temettü, başka eşyaya yapılan transfer ve fuar gideri hariç (2024/18). |
| HS-A-07 | DÜZELT | Doğru cevap en küçük şıktı (A) ve dört çeldiricinin dördü de fazla kalemle kurulmuştu; bu 06 §4/3'e aykırı. Tahliyeyle aynı kuralı ölçen 12.388.000 (memur yolluğu) ve 12.580.000 (bakım) çıkarıldı. Yerlerine iki eksik kalem çeldiricisi kondu: **12.140.000** (garanti bedeli eklenmemiş) ve **12.240.000** (patent eklenmemiş; bu sayı ikinci sorudaki taşınan hata çeldiricisinin tabanı). Anahtar A→C. Avro ve ABD Doları ayrı kurla çevriliyor ve tek anlamlı. |
| HS-A-08 | DÜZELT | Yalnız açıklama değişti: 12.354.000'in birinci sorunun 12.240.000 çeldiricisinden taşındığı belirtildi. Hesap 12.380.000 + tahliye 56.000 + memur yolluğu 8.000 + tescil öncesi ardiye 50.000 = 12.494.000 ve doğru. Matraha alınan giderlerin hepsi tescilden önce. Tahlil ücretinin tescilden sonra olduğu açıkça yazılı (2023/82, 2024/10). |
| HS-A-09 | DÜZELT | Doğru cevap en küçük şıktı (A) ve bütün çeldiriciler fazla kalemle kurulmuştu. 1.997.000 (teyit komisyonu) ve 2.025.000 (teknik yardım) çıkarıldı. Yerlerine **1.895.000** (Almanya'da yaptırılan tasarım eklenmemiş) ve **1.960.000** (üretimde tüketilen vernikler eklenmemiş) kondu. Faiz ve Türkiye'de geliştirilen yazılım çeldiricileri kaldı. Anahtar A→C; kıymet 1.985.000 değişmedi (2023/77, 2025/20). |
| HS-A-10 | DÜZELT | 137.500 şıkkı iki ayrı hatadan çıkıyordu. Birincisi GV'nin KDV matrahına eklenmemesi: 100.000 + 12.500 + 25.000. İkincisi kökün yanlış okunup KDV matrahının (125.000 + 12.500) cevap sanılması. Bu çakışma, ödenen 100.000'in beyan edilen değerin tam 0,8'i olmasından kaynaklanıyordu. Navlun ve sigorta 1.000'den **1.500 ABD Dolarına** çıkarıldı; fiili CIF birim 21 olduğu için eşya yine gözetime tabi. Yeni şıklar 130.000 / 138.600 / 142.500 / **145.000** / 165.000, anahtar D'de kaldı. Soru 2023/76 anahtarının mantığını aynen izliyor: vergiler beyan edilen gözetim değeri üzerinden, ödemeler fiili bedel üzerinden. Kök "satıcıya, taşıyıcıya ve gümrük idaresine" dediği için FOB ile ayrı navlun yeni bir belirsizlik yaratmıyor. `guven` yüksek. |
| HS-A-11 | TAMAM | 120.000 + satış komisyonu 2.400 + simsarlık 1.000 = 123.400. Alım komisyonu, fiyata dahil satıcı primi ve bayi primi hariç. |
| HS-A-12 | TAMAM | Emsalin 300 adette 50 olması fiyat listesiyle tutarlı. 900 adet "801 ve üzeri" kademesine düşer: 900 × 40 = 36.000. Perakende fiyatı ticari düzey farkı nedeniyle dışlanır (2023/83, 2021/88). |
| HS-A-13 | TAMAM | Teslim DAP Kapıkule, giriş yeri Kapıkule: kesim noktası ile teslim yeri örtüşüyor ve giriş yerine kadar taşıma fiyatın içinde. Satıcıya ödenen kabul testi, kalıp ve kalıbın taşınması dahil. Kapıkule–Halkalı taşıması giriş yerinden sonra olduğu için hariç. Kıymet 1.026.000 × 20 = 20.520.000 (2022/96). |
| HS-A-14 | DÜZELT | Hesap doğru: 20.520.000 + Kapıkule–Halkalı 80.000 (tescilden önce, KDVK 21) + depolama 30.000 + tahliye 12.000 = 20.642.000. Ancak "taşınan hata" çeldiricisi 20.722.000 **iki hatadan** çıkıyordu: birinci sorudaki hata ve aynı giderin mükerrer eklenmesi. Birinci sorudaki hatayı tutarlı taşıyan aday zaten doğru sonuca, 20.642.000'e ulaşıyor. Ayrıca doğru cevap en küçük şıktı. Bu çeldirici **20.562.000** ile değiştirildi: kıymete girmeyen Kapıkule–Halkalı taşımasının KDV matrahına da girmeyeceğini sanma hatası. Anahtar A→B. |
| HS-A-15 | TAMAM | 808.000 × 32 = 25.856.000. Avans kuru (30) tuzak veri; CFR'de sigorta ekleniyor (2021/87, 2024/19). Şıkların hepsi tek hatadan. |
| HS-A-16 | TAMAM | Net kâr 120.000, satıcıya düşen pay %40 ile 48.000. Kıymet 200.000 + 30.000 + 48.000 = 278.000 (2023/80). |
| HS-A-17 | DÜZELT (şıklar yeniden kuruldu) | Doğru cevap en büyük şıktı (E) ve dört çeldiricinin dördü de eksik kalemden geliyordu; bu algoritmaya aykırı. Ayrıca D3 hesap bloğunda HS-B-11 ile birlikte ikinci E idi. Yeni şıklar 3.070.000 (mürettebat eklenmemiş) / 3.089.000 (sigorta eklenmemiş) / 3.091.000 (Valletta liman ücreti eklenmemiş) / **3.095.000** / **3.098.000**. Sonuncusu fazla kalem çeldiricisi: Türkiye'de, varıştan sonra ve tescilden önce ödenen Tuzla bağlama ücreti eklenmiş. Anahtar E→D. 2023/74 ile karşılaştırma: yakıt, personel ve liman giderleri dahil; anahtarın mantığı aynen izleniyor. Tartışmalı "yolculuk öncesi bakım" kalemi kullanılmamış. Eklenen sigorta (GK 27/1-e) ve Türkiye'deki giderler yeni bir belirsizlik yaratmıyor. `guven` yüksek. |
| HS-A-18 | DÜZELT | Hesap doğru: 200.000 + 8.000 + 12.000 = 220.000 (2022/98, 2024/27). D3'te C cevapları yığılıyordu: HS-A-15, 16, 18 ile HS-B-12 ve 15 birlikte 11 hesap sorusunun 5'i C idi. 225.000 (bağımsız yazılım lisansı) şıkkı yerine **200.000** kondu (hiçbir royalti ve lisans eklenmemiş). Yazılım lisansı kökte tuzak veri olarak kaldı. Anahtar C→D. |

## Ortak veri setleri

- **D1 (FOB Yokohama, giriş yeri İzmir, 1 ABD Doları = 10 TL):** Teslim şekli, giriş yeri, tescil kuru ve tescil öncesi/sonrası ayrımı tek anlamlı. Dahili vergi K3 kartına uygun işlenmiş (fiyattan düşülür).
- **D2 (CIF Mersin, 1 Avro = 40 TL, 1 ABD Doları = 35 TL):** İki döviz ayrı kurla verilmiş. Matraha alınan tahliye, memur yolluğu ve ardiye kalemlerinin hepsinin tescilden önce olduğu yazılı. Tahlil açıkça tescilden sonra.
- **D3 (DAP Kapıkule):** Teslim yeri giriş yeriyle aynı. Kapıkule–Halkalı taşıması kıymete girmiyor, tescilden önce ödendiği için KDV matrahına giriyor. Bu ayrım, birinci soruda 20.600.000, ikinci soruda 20.562.000 çeldiricisiyle karşılıklı ölçülüyor.

## Biçim

- Para yazımı her yerde Türk usulünde (12.500, 0,80); döviz kodu yok.
- Şıklar küçükten büyüğe sıralı, tekrar eden şık yok, `sira_sabit` true.
- Açıklamalarda şık harfi geçmiyor.

## Harf dağılımı (düzeltme sonrası)

| Deneme | HS-A | HS-A + HS-B |
|---|---|---|
| D1 | D B D C B C | A1 B3 C4 D3 |
| D2 | C D C D B B | A2 B2 C3 D4 |
| D3 | D B C C D D | B2 C4 D4 E1 |

Her D3 bloğunda yalnız bir E kaldı (HS-B-11).
