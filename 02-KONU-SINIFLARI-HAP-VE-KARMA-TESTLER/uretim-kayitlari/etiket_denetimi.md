# Karma testler – `kaynak_tipi` etiket denetimi

Hiçbir soru dosyası değiştirilmedi. Öneriler `karma/etiket_denetimi.json` dosyasında (11 kayıt).

## Kapsam ve ölçüt

- 150 soru incelendi: 90 `beklenen` (K04-08 düzeltmesinden sonra), 60 `cikmis`. Esas alınan kaynak `karma/out/K*.json`.
- Her soru, kendi konusundaki ve komşu konulardaki 2021–2025 sorularıyla karşılaştırıldı (`konu/dosya/*.md`; bozuk metinler için `exams/20xx.txt`). Ayrıca anahtar ifadeler `soru_metinleri.json` içinde tarandı.
- Kullanılan ölçüt şu: doğru cevabı belirleyen bilgi daha önce doğru şık, çarpıtılmış şık ya da öncül olarak ölçülmüşse etiket `cikmis` olur. Bu bilgi olumsuz kökte yanlış ifadenin doğrusu, öncüllü sorularda ise ayırt edici öncüllerdir. Çıkmış bir soru yalnız tek bir çeldiriciye ya da öncüle dokunuyorsa bu bir sınır durumdur ve etiket `beklenen` olur.
- Sınır durumlarda mevcut etiket korundu ve düzeltme önerilmedi. Bunlar, aynı mevzuat listesinden başka bir kalemin sorulduğu ya da çeldiricilerin çoğunun çıkmış olduğu sorulardır.

## Öneriler

| Tür | Sayı | Soru |
|---|---|---|
| beklenen → cikmis | 1 | K02-07 (ref 2023/89: ihracatta işlemlerin yapıldığı idare = ihracat gümrük idaresi) |
| cikmis → beklenen | 4 | K03-07, K08-11, K09-10, K11-09 |
| Ref düzeltmesi (etiket aynı) | 6 | K03-12 (+2025/65), K11-05 (+2025/32, 2023/54, 2023/58), K08-06 (−2023/3), K01-04 (+2023/67), K01-08 (+2023/79), K04-05 (+2024/65) |

`cikmis` → `beklenen` önerilerinin dördünde de referans verilen sorular aynı maddenin başka bir hükmünü ölçüyor. Bu hüküm yalnız bir çeldiriciye karşılık geliyor:

| Soru | Referansın ölçtüğü | Sorunun ölçtüğü |
|---|---|---|
| K03-07 | 2023/90: boru hattında transit hükümlerinin uygulanmaya başladığı an | Rejimin sona ermesi |
| K08-11 | 2021/41, 2024/88: uygun olmayan akaryakıtın rafinericiye satılması | Hudut kapısında el konulan akaryakıttan numune alınması |
| K09-10 | 2024/17: ÖTVK 1/2 | GTİP sınıflandırmasında yetkili kurum |
| K11-09 | 2023/58: Form A, A.TR ve Malezya belgesinin süreleri | İran TTA belgesinin altı aylık süresi |

K08-06'daki 2023/3, md. 5/1'deki bilgi verme yoluyla etkin pişmanlığı ölçüyor. Bu sorunun anahtarı, karma sorusunun ölçtüğü 5/2–5/3 kapsamına zıt görünüyor.

## Öneri sonrası dağılım

| Test | cikmis | beklenen |
|---|---|---|
| 1 | 20 (değişmedi) | 30 |
| 2 | 17 (−1, K03-07) | 33 |
| 3 | 20 (+1 K02-07, −3 K08-11, K09-10, K11-09) | 30 |
| Toplam | 57 | 93 |

## Sınır durumlar: `beklenen` kalan sorular (düzeltme önerilmedi)

Bu sorularda çıkmış bir soru yalnız bir öncüle ya da çeldiriciye dokunuyor ya da aynı kavramı başka bir hükümle ölçüyor. Cevabı belirleyen bilgi yeni.

- **K01-07** – 2023/61 ve 2024/11, Gümrük Kıymeti Komitesinin hangi kuruluşta yer aldığını ve hangi anlaşmayla kurulduğunu ölçtü. Komitenin başkanını kendisinin seçmesi yeni.
- **K01-10** – Kurun tescil tarihine göre seçilmesi 2021/87'de var ve bir çeldiricide kullanılıyor. Kısmi miktarın oranlanması ve bir yıllık kusur düzeltmesi (GY 45/1-c, ç) yeni.
- **K01-11** – 2022/43, ilişkili taraflarda satış koşulları testlerini ölçtü. Emsal kıymetlere dayanarak satış bedelinin yerine kıymet konulamaması (GK 24/2-c) yeni.
- **K01-15** – 2021/89'da giriş yerinden sonraki nakliye faturada ayrı gösterilmişti. Navlunun mesafe oranıyla paylaştırılması (GY 51/6) yeni.
- **K01-16** – 2024/13 D şıkkı (royalti fiyata bağlıysa eşyayla ilgili sayılır) doğru şıkkın içeriğine dokunuyor. Ölçülen satış koşulu göstergeleri listesi (Seri 2 md. 7/3) yeni. Bu en güçlü aday; isterseniz 2024/13 ile `cikmis` yapılabilir.
- **K01-18** – Altı aylık süre ve teminat 2021/21 E'de var. 30 günlük uzatma ve idare amiri onayı yeni.
- **K02-01** – Antrepo için 2024/86 (devir, kapatma) ve 2022/67 (5 yıllık yasak) çıktı. Geçici depolama yerinde isteğe bağlı kapatmanın yasak dışında kalması yeni.
- **K02-05** – 2024/38 IV'te her kalemin ayrı beyanname gibi değerlendirilmesi (teslim, GK 73) var. Kalemler arasında mahsup yasağı (GK 67/2) yeni.
- **K03-05** – Makam dağılımı 2025/83 ve 2024/85'te soruldu. Antrepo dışında elleçlemeyi bölge müdürlüğünün sonuçlandırması yeni.
- **K03-08** – 2025/70'te ceza oranının genel basitleştirme ölçütü olduğu soruldu. Havayolu başvurusunda bu koşulun aranmaması (GY 237) yeni.
- **K05-02** – Diplomatik eşyanın devri 2021/27'de var. Çalınmanın ispatı (GY 442) yeni.
- **K05-05** – 2021/37'de konut satın alma ve bir yıl kiralama şartı var, IV. öncüle dokunuyor. Öğrenci muafiyeti, altı aylık dönüş süresi ve teminatlı geçici ithal yeni.
- **K05-07** – 2023/95 II'de vadesi geçmiş borç şartı gümrüksüz satış mağazaları için soruldu. Bunker bayilerinin şartları (GY 478) yeni.
- **K05-10** – 2024/21 IV'te 1600 cc sınırı yer alıyor. Engelli aracı şartları (Karar 104) yeni.
- **K05-14** – Kökteki 10 iş günlük süre 2021/17 ve 2024/31'de var. Teminatla teslimin hangi haklarda uygulandığı (GY 108) yeni.
- **K06-02** – Uzlaşma kapsamı 2024/12'de soruldu. Kısmi talep, iştirak, mülkiyetin kamuya geçirilmesi ve feragat hükümleri yeni.
- **K06-03** – C şıkkının kalıbı 2021/80 ve 2023/88'de var. GK 191/A'da ispat yükünün ilgili kişide olması yeni.
- **K06-05** – 2024/65 E (GK 207/1-b) ve 2025/19 (gecikme zammı hesabı) çıktı. GK 207/1-a'ya göre başlangıcın teminatın kabul tarihi olması yeni.
- **K06-06** – Kusurlu eşya (GK 212) 2024/98'de soruldu. Kusur fiyatta dikkate alınmışsa geri verme yapılmaması (GY 501/1-a) yeni.
- **K07-01** – E şıkkındaki ölçütler 2021/18 (onaylanmış kişi statüsünde 30 işçi) ve 2025/92 E'de (imalatçı olma) var. YYS temel koşulları yeni.
- **K08-02** – Canlı hayvan 2024/89'da kamuoyuna ilan listesinde soruldu. 5607 md. 3/10'daki ceza artırımı listesi yeni.
- **K08-07** – 2021/50'de sahte paranın TCMB'ye teslimi soruldu; bu aynı Yönetmelik 5/3 listesinde başka bir kalem. Hava taşıtlarının DHMİ'ye teslimi yeni.
- **K09-01** – Bileşenler 2025/15, 2022/55 ve 2021/87'de var. Belirleyici olan KDVK 21/ç (24.07.2025) ise yeni ve 2025/15 anahtarının tersi bir sonuç veriyor.
- **K09-05** – 2022/4 D ve 2023/40 eski 2012/3305 sayılı Karara göre soruldu. 2025/9903 md. 13/4'teki teminat süresinin başlangıcı yeni.
- **K11-03** – STA ile TTA ayrımı 2022/23 ve 2024/36'da soruldu. Maldivler TTA'sı yeni.
- **K11-06** – INF 4'ün işlevi 2025/96 ve 2023/48'de var. Dört aylık süre yeni.
- **K12-01** – 2021/67 ve 2023/64'te DDP'nin satıcıya en fazla yükümlülük getirdiği soruldu. DDP'de ithalat KDV'sinin satıcıya ait olması ve diğer kural ayrıntıları yeni.
- **K12-05** – 2022/40 IV (hane nakli) E şıkkına dokunuyor. 250.000 ABD Doları eşiği yeni.
- **K12-07** – Konsinye süreleri 2022/10 ve 2024/72'de var ve çeldiricilerde kullanılıyor. Fuar beyannamesinin 15 gün içinde gönderilmesi yeni.
- **K13-01** – HS 2022'de 05.09/05.11 değişikliği böcekler üzerinden 2022/79 ve 2024/2'de soruldu. Süngerler yeni.
- **K13-05** – Set ölçütleri 2021/94 ve 2025/42'de var. Teferruat kuralı yeni.
- **K13-06** – 2021/73 GK 16/1'i ölçtü. GK 15/4-5 ve 16/2 yeni.
- **K13-11** – Fasıl 9 ile 12.11 ayrımı 2021/96'da soruldu. Kebabe biberi yeni.

## Sınırda kalan `cikmis` sorular (etiket korundu)

Bu sorularda aynı mevzuat listesi ya da aynı ayrım daha önce ölçüldü, ancak doğru cevaptaki kalemin kendisi yeni. Katı okumayla `beklenen` sayılabilirler:

| Soru | Ölçülmüş olan | Yeni olan |
|---|---|---|
| K01-02 | Taşıyıcı ortam kuralı GY 54/1 | GY 54/2 istisnaları |
| K04-02 | %3 oranı (2021/71) | Tavan, teminat, mahsup |
| K05-01 | Karar 107/4 listesi | Engelli eşyası için 3 yıl |
| K05-04 | A, B ve E şıkları | 47/5'teki 5 yıl |
| K05-11 | A ve C şıkları | GY 459 |
| K07-03 | I. öncül (2025/90 D) | III. öncül |
| K08-03 | Altın eşiği | Gümüş eşiği |
| K08-08 | Müteahhitlik ve kredili ihracat süreleri | Konsinye ihracat süresi |
| K12-02 | Yasak/ön izin ayrımı | Yaban domuzu ve kurt |
| K13-07 | Fasıl 11 Not 1 | Kozmetik nişasta |
| K13-08 | Fasıl 33 Not 4 (2025/49) | Kontakt lens solüsyonu |
| K14-09 | 96.03 kapsamı | Yol süpürme makinesi fırçası |
