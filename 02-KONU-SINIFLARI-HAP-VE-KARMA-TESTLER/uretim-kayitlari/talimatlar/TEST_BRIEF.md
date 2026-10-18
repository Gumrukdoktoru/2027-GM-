# KARMA TEST SORU ÜRETİMİ — ORTAK TALİMAT

Gümrük Müşavirliği (GM) sınavı için **üç adet 50 soruluk karma test** hazırlanıyor. 2021–2025 sınavlarının 500 sorusu konu konu sayıldı; konular dört sınıfa ayrıldı (çok çıkan ≥10 soru, orta 5–9, az 1–4, hiç çıkmayan 0). Her testte **30 çok çıkan, 13 orta, 6 az, 1 hiç çıkmayan** konu sorusu var: son 5 yılda çok sorulan konu testte çok, hiç sorulmayan konu en fazla 1 soruyla temsil ediliyor. İş konu kümelerine bölündü; sen bir kümenin **üç testteki bütün sorularını** yazıyorsun.

Hedef: Sorular gerçek Bakanlık sınavının arasına konsa yabancı durmamalı. Her sorunun **tek ve tartışmasız** doğru cevabı olmalı, cevap kaynaktan doğrulanabilmeli. Emin olmadığın hükmü soru yapma.

Kısaltma: `S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`, `P=/home/user/2027-GM-/00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR`.

## 1. Önce oku

1. `$S/karma/slots/<KÜME>.md`: slot listen (test, konu, sınıf).
2. `$S/deneme/BRIEF.md`: önceki deneme üretiminin ortak talimatı. **§4 yazım kuralları, §5 JSON şeması ve §6 öz-denetim aynen geçerlidir** (§2'deki "eksik kaynak uyarısı" artık geçerli değil: GK/GY metinleri `$S/kaynak2/gm/` altında var).
3. `$P/02-SORU-PROMPTU-0_GENEL.md` §2.4, 4, 5, 6, 7, 8 ve alan promptun (GM `03`, Sair `04`, Tarife `05`, Hesap `06`).
4. `$P/12-SORU-TIPI-KATALOGU.md`: kullandığın alt tiplerin kartları.

## 2. Malzeme (sorunun bilgisini buradan seç)

- **Çıkmış sorular:** `$S/konu/dosya/<KONU>.md` (konu konu, kitapçık metni ve resmî cevap).
- **Çıkan sorulardan haplar:** `$S/hap/cikan/<KÜME>.json` (konu konu; `sorular` alanı çıkmış soru kimlikleri).
- **Beklenen haplar ve sorulmayan hükümler:** `$S/hap/sorulmayan/<KÜME>.json` (`beklenen` = sorulma ihtimali yüksek, hiç sorulmamış hükümler; `alt_konular[].sc` = sorulmamış hükümlerden soru–cevaplar; her birinde `kanit` ve `kaynak`).
- **Kaynak mevzuat:** `$S/hap/girdi/<KÜME>.md` dosyasındaki yollar. Doğru cevabı ve çeldiricilerin yanlışlığını **kaynak metinde gör**.

Bir slotun bilgisini şöyle seç:

| Sınıf | Seçim |
|---|---|
| Çok çıkan | Yaklaşık yarısı **çıkmış bilgi alanından** (★ işaretli çok yıllı haplar öncelikli; Bakanlık bu bilgileri tekrar soruyor), yarısı **beklenen haplardan**. Çıkmış bilgiyi **yeni kurguyla** sor: farklı kök, farklı alt tip, farklı çeldiriciler; çıkmış sorunun şıklarını kopyalama. |
| Orta çıkan | Çoğunlukla beklenen haplardan; kalanı çıkmış bilgi alanından yeni kurguyla. |
| Az çıkan / hiç çıkmayan | Beklenen haplardan ve sorulmayan hükümlerden. |

Her soruya `kaynak_tipi` ("cikmis" | "beklenen") ve `cikmis_ref` (çıkmış bilgi alanıysa ölçülen çıkmış soru kimlikleri, ör. ["2024/74", "2022/66"]; beklenense []) alanı ekle.

## 3. Karma teste özgü kurallar

- **Hesap soruları:** Kıymet slotlarında her testte **3 hesap + 2 sözel** soru olsun (hesap: H1 kalem listeli kıymet, H3 vergi tutarı, H5/H6; iskelet çıkmış hesap sorularından, sayılar ve kalemler değiştirilerek; `$S/konu/dosya/KIYMET.md` ve `$P/06-SORU-PROMPTU-4_HESAPLAMA.md`). K09 kümesinde her testte KDV ya da ÖTV slotlarından **1 hesap** sorusu (ithalatta KDV/ÖTV matrahı). K06 kümesinde ceza slotlarından birinde hesap kullanabilirsin (GK 234). Hesap sorularında `alan: "HESAP"` yaz; `konu` alanı yine konu kodu (ör. KIYMET).
- **Alt tip dağılımı (kümende):** ~%35 olumsuz kök (O1 liste dışı, O2 bozuk cümle), ~%15 öncüllü (Ö1–Ö3), ~%10 eşleştirme / vaka / "hangisi doğrudur" (E1, V2, G1), kalanı düz bilgi (D1–D6). Tarife kümelerinde katalogdaki tarife kalıpları (eşya → pozisyon, fasıl kapsamı, not hükmü, GYKK).
- **Bir test içinde** aynı konudan gelen sorular farklı alt başlıkları ölçsün; **üç test arasında** aynı hükmü iki kez sorma.
- **Önceki 3 GM denemesiyle tekrar:** `$S/deneme/birlesik/deneme{1,2,3}.json` dosyalarında aynı konudaki soruları (`konu` alanı eski kodlarla: GM02 kıymet, GM07 transit, SR01 kaçakçılık… — kök metinlerinde anahtar sözcükle grep et) gözden geçir; aynı hükmü aynı kurguyla tekrar etme.
- Testlerin süresi 75 dakika (50 soru); soru uzunluğu gerçek sınavdaki gibi olsun.

## 4. Çıktı

Dosya: `$S/karma/out/<KÜME>.json`. JSON dizi; şema `$S/deneme/BRIEF.md` §5 ile aynı, şu farklarla:

- `id`: slot kimliği ("K03-07"), `deneme` yerine `test` (1, 2, 3).
- `konu`: slot listesindeki konu kodu (TRANSIT, KIYMET, T_MAKINE …).
- Ek alanlar: `kaynak_tipi`, `cikmis_ref` (yukarıda), `zorluk` ("K" kolay, "O" orta, "Z" zor; kümende yaklaşık 1/4 K, 1/2 O, 1/4 Z).

Betiği `$S/karma/work_<KÜME>/` altında tut; `json.dump(..., ensure_ascii=False, indent=1)`.

## 5. Öz-denetim
`$S/deneme/BRIEF.md` §6'daki altı madde + şunlar:
7. Slot listesindeki her slot için tam bir soru var mı (id'ler birebir)?
8. `kaynak_tipi` dağılımı §2'deki tabloya uyuyor mu?
9. Açıklamada şık harfi yok; `aciklama` doğru cevabın gerekçesini ve çeldiricilerin neden yanlış olduğunu söylüyor.

## 6. Son rapor (en fazla 20 satır)
Test başına soru sayısı, hesap soruları, `kaynak_tipi` dağılımı, `guven: orta` sorular (id + neden), slottan sapmalar.
