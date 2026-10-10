# TR-A doğrulama raporu (30 tarife sorusu)

Denetlenen dosya: `deneme/out/TR-A.json` · Özgün kopya: `deneme/out/orig/TR-A.json` · Betik: `deneme/work_verify_TR-A/fix.py`

Yöntem: Her soru önce anahtara bakmadan çözüldü. Sonra doğru şık ve dört çeldiricinin her biri ilgili `FASILxx.txt` dosyasında aranıp doğrulandı (pozisyon metni, bölüm/fasıl notu, izahname). Alt tip, kök kalıbı, olumsuz yüklem biçimi, şık sayısı/tekrarı, `sira_sabit` ve şık uzunluğu ipucu da denetlendi.

| id | Karar | Ne değişti / neden (kaynak) |
|---|---|---|
| TR-A-01 | TAMAM | Düdüklü tencere ve çelik yünü 73.23 (7323.10), odun sobası 73.21, paslanmaz evye 7324.10, kaşık ise 82.15'tir. 73.23 hariçler (e) kaşıkları dışarıda bırakır (FASIL73 s.921-967; FASIL82 82.15). |
| TR-A-02 | TAMAM | Soya sosu 2103.10, ketçap 2103.20, hardal unu 2103.30'dur; mayonez 21.03 (A) örneklerinde sayılır. Salça 20.02'dedir; 20.02 açıklama notunda "domates püresi, salçası veya konsantresi" geçer (FASIL20 s.68). |
| TR-A-03 | TAMAM | 87.02'nin ölçütü "on veya daha fazla kişi (sürücü dahil)"dir. Kar taşıtı ve golf arabası 8703.10'da, ambulans ve motorlu karavan 87.03 açıklama notu (b)-(c)'dedir. |
| TR-A-04 | DÜZELT (açıklama) | Anahtar (19.04) doğru: 1904.30 "Bulgur", 19.04 (C), 11. Fasıl GA hariçler (e) ve 11.04 hariçler (c). Açıklamadaki "11.03'teki küçük parçalar pişirilmemiş tanelerden elde edilir" cümlesi kaynakta yok; 11.03 ısıl işlemle prejelatinize kaba unları da kapsar. Bu cümle kaldırıldı. Yerine 11. Fasıl Not 3'teki "(bulgur)" ibaresinin yalnız elek kriterini tanımladığı ve pişirilmiş bulguru 11.03'e getirmediği yazıldı. Dayanak ve kaynak güncellendi. |
| TR-A-05 | DÜZELT (şık) | "Teknik çizim kalemi" Rotring tipi stilo olarak okunabilir; o zaman 9608.30 ("stilolar") ile 96. fasla girer ve ikinci doğru cevap çıkar. Şık "Teknik çizim kalemi (tirlin)" olarak netleştirildi; tirlin 90.17 açıklama notu (A)(3)'teki "çizgi çizmeye mahsus mürekkepli kalem"dir, 96.08 hariçler (c) ve 96. Fasıl Not 1(f) bunu 90.17'ye verir. Açıklama, tuzak, dayanak ve kaynak güncellendi. Tripod 96.20; göz kalemi Not 1(a); şemsiye sapı 66.03 (3); taklit küpe 71.17. |
| TR-A-06 | TAMAM | Saç kesme makinesi 8510.20; saç kurutucu 8516.31, saç kıvırma cihazı 8516.32, el kurutma cihazı 8516.33, ütü 8516.40. |
| TR-A-07 | TAMAM | 84.23 pozisyon metni, hassasiyeti 5 cg veya daha iyi olan terazileri hariç tutar. 1 mg terazi 90.16'dır (90.16 (1) analitik teraziler); diğer dördü 84.23 açıklama notunda (1), (3), (4), (6) olarak sayılır. |
| TR-A-08 | TAMAM | 84. Fasıl Not 1(b): seramik pompa 69.09 (2) "tulumbalar"dır. XVI. Bölüm GA (B): tamamı plastik pompa 84.13'te kalır. Püskürtücü 84.24, bulaşık makinesi 84.22, kazan 84.03. |
| TR-A-09 | TAMAM | 63. Fasıl Not 3 (a)(i)-(iv), (b) ve iki şart doğrulandı; 57.01-57.05'teki halılar not dışındadır. |
| TR-A-10 | DÜZELT (biçim) | İçerik doğru: 70.18 metni, Not 1(h) ve 70.18 (F). Doğru şık (65 karakter) diğerlerinin iki katı uzunluktaydı ve ipucu veriyordu. İki çeldirici kaynak ifadesiyle uzatıldı: "İnsanlarda kullanılmak üzere camdan imal edilmiş protez göz" (90.21) ve "Noel ağacına takılan, üfleme yoluyla yapılmış ince camdan süs küresi" (95; 70.18 hariçler (ij)). |
| TR-A-11 | TAMAM | 61. Fasıl Not 2(a): 62.12 örülmüş olsun olmasın sütyeni kapsar. Kazak 61.10, külotlu çorap 61.15, eldiven 61.16, bebek tulumu 61.11 (Not 6(a), 86 cm). |
| TR-A-12 | TAMAM | 94. Fasıl Not 1(b): boy aynası 70.09'dur. Not 2(a): duvar tipi kitap dolabı 94.03'tür. Hasta karyolası 94.02, şilte 94.04, prefabrik bina 94.06 (Not 4). |
| TR-A-13 | TAMAM | 97. Fasıl Not 1(a): tedavüldeki kullanılmamış pul 49.07'dir. İlk gün zarfı 97.04 (GA (B)), litograf 97.02 (Not 3), fosil koleksiyonu 97.05, antika saat 97.06 (12). |
| TR-A-14 | TAMAM | Katmanlı üretim 84.85 / 8485.20'dir; 84. Fasıl Not 10 öncelik kuralını koyar, ekstrüzyon nozullu makine 84.85 açıklama notu (4)'tedir. Kod şıkları sıralı (`sira_sabit` true). |
| TR-A-15 | TAMAM | Ayçiçeği küspesi 2306.30'dur; 12. Fasıl Not 2, 23.04-23.06'daki artıkları 12.08 dışında bırakır. Genelge 2016/03 EK-1 sıra 1 de 2306.30 der. |
| TR-A-16 | TAMAM | Tabii bal 04.09'dur (suni bal 17.02'ye gider, FASIL04 s.285). 17.02 metninde "suni bal… karamel" geçer; melas 1703.10, beyaz çikolata 17.04 (6) (FASIL18 Not 1(b)). "Karamel" şekerleme olarak okunsa bile 17.04'e, yani yine 17. fasla girer; cevap değişmez. |
| TR-A-17 | TAMAM | 71. Fasıl Not 9(a)-(b): yüzük, kol düğmesi, pudra kutusu ve tesbih 71.13'tür. Not 10: sofra eşyası 71.14'tür. |
| TR-A-18 | TAMAM | 85. Fasıl Not 4: aspiratörlü davlumbaz 84.14'tür. Cilalama makinesi ağırlıktan bağımsız 85.09'dadır (A)(1). Diş fırçası (B)(7) ve nemlendirici (B)(8), 20 kg sınırıyla 85.09'dadır. |
| TR-A-19 | TAMAM | 42. Fasıl Not 4: 91.13'teki saat kayışları hariçtir. Eldiven ve kemer 42.03, tasma 42.01, evrak çantası 42.02. |
| TR-A-20 | TAMAM | 10. Fasıl Not 1(B): işlenmiş pirinç (kırık dahil) 10.06'da kalır. Not 2: tatlı mısır 7. fasıldadır. Yulaf 11.04, malt 11.07, pirinç unu 11.02. |
| TR-A-21 | TAMAM | 69. Fasıl Not 2(g): takma diş 90.21'dir. Lavabo 69.10, porselen tabak 69.11, heykelcik 69.13, havan 69.09 (1). |
| TR-A-22 | TAMAM | 7. Fasıl Not 4: öğütülmüş Capsicum 09.04'tür. "Teneke kutulardaki soğan tozu" 7. Fasıl GA'da aynen geçer (07.12). Zeytin ve biber Not 2 ile 07.09'da, nohut 07.13'tedir. |
| TR-A-23 | DÜZELT (biçim) | Üreticinin işaret ettiği nokta doğrulandı: 95. Fasıl Not 5 evcil hayvan oyuncaklarını 95.03 dışında bırakır. Oyun çadırı 95.03 (D)(xxiii) ile açıkça kapsamdadır (Not 1(y)'deki çadırlar kamp eşyasıdır). Motorlu çocuk arabası (A)(7), tren (D)(iv) ve salıncaklı at (D)(v) de 95.03'tedir. Belirgin biçimde en uzun olan doğru şık kısaltıldı: "Münhasıran köpekler için tasarlanmış kauçuk çiğneme oyuncağı". |
| TR-A-24 | TAMAM | 43. Fasıl Not 4: kürk astarlı manto 43.03'tür. Not 2(a): kuş derisi 05.05/67.01; Not 2(c): deri-kürk eldiven 42.03; Not 2(e): başlık 65. fasıl; Not 5: örme taklit kürk 60.01. |
| TR-A-25 | TAMAM | 92.08 metni "düdükler… ağızla işaret verme aletleri"dir (95. Fasıl Not 1(s) ile de tutarlı). Not 1(c)-(d): oyuncak ksilofon 95.03, temizleme fırçası 96.03. GA hariçler (a): müzik modülü 85.43. 92.08 hariçler (a): bisiklet zili 83.06 veya 85.31. |
| TR-A-26 | TAMAM | Klozet kapağı 3922.20'dir. Kasa 3923.10, çöp torbası 3923.21 (açıklama (a) "çöp torbaları dahil"), damacana 3923.30, şişe kapağı 3923.50. |
| TR-A-27 | TAMAM | Pozisyonlar tek tek doğrulandı: 84.02, 84.08, 84.14, 84.15, 84.18, 84.25 (krikolar), 84.26 (kule vinç 8426.20), 84.28, 84.33, 84.34, 84.46, 84.47, 84.50, 84.52, 84.58, 84.70, 84.71, 84.81, 84.82, 84.83. Yalnız "dizel motor – kompresör – kriko – kule vinç" sıralaması doğrudur. Diğer dört şıkta tek bir yer değişikliği vardır. |
| TR-A-28 | DÜZELT (şık + açıklama) | Açıklamada XV. Bölüm Not 2(c) yanlış aktarılmıştı: not 83.06'nın tamamını değil, yalnız "83.06'daki adi metalden çerçeve ve aynaları" kapsar; düzeltildi. Doğru şık notun (b) bendi ifadesine uyduruldu: "Adi metalden saat zemberekleri" (91.14; 91. Fasıl Not 1(c)). Bu, tek kısa şık olma ipucunu da kaldırdı. Civata/somun 73.18, yay yaprağı 73.20, asma kilit 83.01, menteşe 8302.10. |
| TR-A-29 | TAMAM | 12. Fasıl Not 3 ve (c): hububat 12.09 dışındadır, makarnalık buğday tohumu 1001.11 "Tohum"dur. Pancar 1209.10, çim 1209.25, süs çiçeği 1209.30, orman ağacı tohumu 12.09 açıklama notundadır. |
| TR-A-30 | TAMAM | Yağlı radyatör 85.16 açıklama notu (B)(3)'tedir; alt pozisyonu 8516.29'dur, 8516.21 depolu radyatörlere aittir ve soru fasıl düzeyinde sorduğu için sonucu etkilemez. 85. Fasıl Not 1(a), (d), (e) ve 85.16 hariçler (f): ısıtıcılı servis masası 94. fasıldadır. |

## Özet

- TAMAM: 25 · DÜZELT: 5 (04, 05, 10, 23, 28; 04 yalnız açıklama) · YENİDEN YAZ: 0.
- Anahtarı değişen soru yok. Soru sayısı 30, JSON geçerli. Doğru cevap dağılımı her konumda 6 olarak dengeli.
- Üreticinin işaret ettiği noktalar:
  - Bulgur (04): 19.04 doğru, açıklama düzeltildi.
  - 95. Fasıl Not 5 (23): doğru.
  - Kule vinç (27): 8426.20 doğru.
  - Yağlı radyatör (30): 85.16 / 8516.29 doğru.
  - Saat zembereği (28): 91.14 doğru, açıklamadaki not aktarımı düzeltildi.
- Hâlâ küçük itiraz riski taşıyanlar:
  - TR-A-23: Not 1(y) "çadırlar" ile 95.03 (D)(xxiii) "oyun çadırları" arasında görünür gerilim var. İzahname açık, anahtar sağlam.
  - TR-A-04: Türkçe 11. Fasıl Not 3'teki "(bulgur)" ibaresine dayanan itiraz gelebilir. Kökteki ön pişirme tanımı ve 1904.30 bunu karşılar.
