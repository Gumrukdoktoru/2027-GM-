# GM Deneme 1–2 — Soru Yazarı Ortak Talimatı

Çalışma klasörü: /home/claude/2027-gm-/araclar/gm-deneme12
Marka: yalnızca "Gümrük Koçu - Ufuk Çetintaş". Kaynak metinlerde başka eğitim kurumu adı (ör. Altınsoy) geçse bile soruya, gerekçeye, kanıta taşıma (kanıt alıntısını o ibareyi içermeyen bir parçadan seç).

## Görev
Sana verilen KÜME için Gümrük Müşavirliği (GM) Deneme 1 ve Deneme 2 sorularını yaz. Kümenin set başına konu kontenjanı `kumeler.json` içinde; her set için bu kontenjanı AYNEN sağla (dict'te `set`: 1 veya 2, `konu`: kumeler.json'daki konu adı birebir). Toplam soru = 2 × kontenjan.
- Deneme 1 ile Deneme 2'de aynı çekirdek (aynı hüküm/bilgi) iki kez sorulmaz.
- Sorular, daha önce ürettiğimiz setlerden BAĞIMSIZ olacak: `/home/claude/2027-ye-haz-rl-k/sorular/hafiza/URETIM-HAFIZASI.md` içindeki çekirdekleri (kendi konunla ilgili satırları grep'le) tekrar etme. Aynı bilgi alanı mutlaka gerekiyorsa gerçekten farklı bir ölçme boyutu/hüküm seç.

## Kurallar (tamamını oku, harfiyen uygula)
1. `/home/claude/2027-ye-haz-rl-k/promptlar/prompt-3-nihai-soru-hazirlama-kurallari.md` — özellikle §5 bilgi türü→kurum kalıbı, §7 madde/fıkra/bent numarası kökte ve şıkta yok, §8 kök = MEVZUAT ADI + HÜKMÜN KONUSU + KALIP, §11–13 çeldirici ve önermeli standardı (en az 3, tercihen 4 önerme; doğru kombinasyonlar farklı; "hepsi doğru/hiçbiri" yok), §14 çıkmış bilgi alanı atlanmaz ama metin/şık/kurgu kopyalanmaz, §17 eski-yeni kurum adı rakip şık yapılmaz, §20 gerekçe.
2. Karar dayanaklı sorularda kök "4458 sayılı …" ile BAŞLAMAZ: `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …`. Kök, dayanağın türünü (Kanun/Karar/Yönetmelik/Tebliğ/Genelge/Anlaşma/Tarife Cetveli) baştan açıkça göstermeli.
3. KAYNAKTA YOKSA ÜRETME: tek bilgi kaynağı `metin/` klasörü (Grep ile ara). Web yok, hafıza yok. Doğru şık, çeldiricilerin yanlışlığı, olay verileri ve gerekçedeki her bilgi kaynakta olmalı.
4. GÜNCEL METİN ESAS: Kaynakta dipnotla değişmiş/mülga hükümler varsa güncel metne göre sor; mülga hükme dayanma. Çıkmış sorunun resmî cevabı güncel metinle çelişiyorsa güncel metne göre kur.
5. Her yıl yeniden değerlenen TL tutarlarını sorma; sorman gerekiyorsa tutarı kökte ver. Hesaplarda kur ve oranları kökte ver; hesabı Python ile doğrula.
6. Doğru şık sistematik olarak en uzun şık olmayacak (set başına kümendeki soruların en çok %20'si).
7. Tarife–mevzuat ayrımı: tarife/pozisyon/sınıflandırma sorusu yalnız T1 ve T2 kümelerinde yazılır ve tarife kaynaklarına (FASILxx, Tarife_Kitabi, TARİFENİNYORUMU…, genelge_*, gumruk_genel_tebligi_x1tarife-siniflandirma_*, siniflandirma_avi, 9-TAR.POZ.AYIRMA, izahname tebliği) dayanır. Diğer kümelerde GTİP/pozisyon sorusu yazılmaz.
8. Somut olaylarda firma/kişi etiketleri şık harfleriyle karışmasın: (K), (L), (M), (X), (Y) kullan.

## Çıkmış soru esaslı üretim
- `cikmis_envanter.tsv` (2021–2025 GM sınavları, 500 soru) sütunları: YIL, SORU_NO, KONU, ÖLÇÜLEN_BİLGİ, KALIP, KAYNAK_DOSYA, RESMI_CEVAP, DOGRU_SIK_METNI. `envanter/<YIL>_not.md` dosyalarında resmî cevabın güncel kaynakla çeliştiği sorular yazılı; bunlara dikkat et.
- Kümendeki konuların **2024 ve 2025** satırlarından KAYNAK_DOSYA≠YOK olanların EN AZ %75'inin bilgi alanı iki denemeden birinde ölçülsün (aynı hükmü kopyalamadan, farklı soru tekniğiyle). Kalan kontenjanı 2021–2023'te tekrar tekrar sorulan bilgi alanlarıyla ve kaynaktaki diğer sınavlık hükümlerle doldur.
- Ham sınav metinleri: `sinav/<YIL>_layout.txt` (iki sütun) ve `sinav/<YIL>.txt`. Kurumun soru dilini, kök yapılarını ve şık kurgusunu buradan gör. GM 2023–2025 kalıp dağılımı: ÖNERMELİ %15, KAPSAM_DIŞI %14, SINIFLANDIRMA %12 (tarife), YANLIŞ %11, HESAP %11, EŞLEŞTİRME %4, DOĞRU/TANIM/BOŞLUK/SÜRE %3'er, diğerleri az. Kümende çıkmış sorulardaki kalıp karışımına yakın kal; aynı kökü art arda kullanma.
- `cikmis` alanına karşıladığın çıkmış soruları yaz ("2025/41, 2024/12"); karşılamıyorsa boş bırak.

## Set başına zorluk
Kümendeki set başına soru sayısı n ise yaklaşık: ÇK %10, K %20, O %40, Z %20, ÇZ %10 (±1); O en kalabalık olsun.

## Format
Dosya: `batch_<KÜME>.py`, içinde `Q = [dict(...), ...]`. Biçim örneği: `/home/claude/2027-ye-haz-rl-k/araclar/gmy-deneme345/batch_G3.py` (ilk iki kaydı oku). Alanlar:
set (1/2), konu, kalip (TANIM KAVRAM KAPSAM KAPSAM_DIŞI DOĞRU YANLIŞ ÖNERMELİ SÜRE ORAN-TUTAR YETKİ BELGE ŞART HESAP BOŞLUK EŞLEŞTİRME MÜEYYİDE OLAY TABİ ZORUNLULUK MATRAH DAYANAK SONUÇ MUAFİYET KISA_AD SINIFLANDIRMA), z (ÇK/K/O/Z/ÇZ), madde (yalnız bu alanda; ör. "GK 241/1; GY 500" veya "Fasıl 85 Not 3; İzahname 85.17"), cek (≤25 kelime, ölçülen hüküm), kok (liste; önermeli ise "I. …" satırları ve son satır kökün devamı; paragraf/olay metni ayrı eleman olabilir), d (doğru şık), c (4 çeldirici), g (gerekçe §20; doğru şıkkı harfle değil şık metniyle an — örn. "… Bu nedenle doğru cevap 'I ve III' seçeneğidir." — harfi ben yerleştireceğim; sonu "(MD GK 24/3-b)" biçiminde), kanit ("dosya.txt | kaynaktan BİREBİR alıntı ≤40 kelime"; iki dosya gerekiyorsa "a.txt; b.txt | alıntı1 … alıntı2"; alıntı parçaları '…' ile ayrılabilir), cikmis.
- Önermeli şıklarında yalnız "I ve III", "Yalnız II", "II, III ve IV" gibi kombinasyonlar.
- Sayısal şıklar (süre, oran, tutar, yıl) küçükten büyüğe doğal sırada yazılabilir; ben harf dağılımında bunu koruyacağım.

## Denetim
1. `python3 kontrol_gm.py batch_<KÜME>.py` → "GENEL SONUÇ: TEMİZ" olana kadar düzelt. "??" benzer çekirdek uyarılarını tek tek incele; gerçekten aynı bilgiyse soruyu değiştir. Kanıt hatasında alıntıyı kaynaktan birebir kopyala (pdftotext çıktısında satır sonu tirelerine dikkat; tireli kelimeyi içermeyen bir parça seç).
2. Her soruda doğru şıkkın kaynağa göre KESİN doğru, diğer dört şıkkın KESİN yanlış olduğunu (olumsuz kökte tersini) kaynakla tek tek doğrula. İstisnaları, dipnotlu değişiklikleri, "mülga" ibarelerini oku.
3. Her soruyu `cikmis` alanındaki çıkmış soruyla karşılaştır: metin/şık/kurgu kopyası olmasın.

## Rapor (bitince kısa, ≤15 satır)
Set başına konu dağılımı; karşılanan 2024–2025 çıkmış soru numaraları; karşılanamayanlar ve nedeni; emin olmadığın noktalar. Git işlemi yapma, kendi batch dosyan dışında hiçbir dosyaya dokunma.
