# DENEME SINAVI SORU ÜRETİMİ — ORTAK TALİMAT

Üç adet 100 soruluk Gümrük Müşavirliği deneme sınavı hazırlanıyor (Deneme 1, 2, 3). Her denemede 42 Gümrük Mevzuatı + 30 Sair Mevzuat + 17 Tarife + 11 Hesap sorusu var. İş, konu kümelerine bölündü; sen bir kümeden sorumlusun ve kümenin **üç denemedeki bütün sorularını** üretiyorsun. Slot listen (`slots/<KÜME>.md`) her sorunun denemesini, konusunu ve alt tipini verir.

Hedef: Bu sorular gerçek Bakanlık sınavının arasına konsa yabancı durmamalı. Her sorunun **tek ve tartışmasız** doğru cevabı olmalı ve bu cevap mevzuattan doğrulanabilmeli. Yanlış anahtarlı tek bir soru, setin güvenilirliğini bozar: emin olmadığın hükmü soru yapma.

Kısaltma: `S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`, `P=/home/user/2027-GM-/00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR`.

## 1. Önce oku (sırayla)

1. `$S/deneme/slots/<KÜME>.md` — senin slot listen.
2. `$P/02-SORU-PROMPTU-0_GENEL.md` — Bölüm 2.4 (12 kural), 4 (kök kalıpları), 5 (12 bozma tekniği), 6 (tipe özel standartlar), 7 (dil ve biçim), 8 (yasaklar). Bu kurallar bağlayıcıdır.
3. Alan promptun: GM → `$P/03-SORU-PROMPTU-1_GUMRUK-MEVZUATI.md` · Sair → `$P/04-SORU-PROMPTU-2_SAIR-MEVZUAT.md` · Tarife → `$P/05-SORU-PROMPTU-3_TARIFE.md` · Hesap → `$P/06-SORU-PROMPTU-4_HESAPLAMA.md` (kural kartları ve çeldirici algoritması zorunlu).
4. `$P/12-SORU-TIPI-KATALOGU.md` — yalnız slot listende geçen alt tiplerin kartları ("Kombinasyon şıkkı nasıl kuruluyor" bölümü dahil). Her alt tipi kartındaki gerçek örneğin biçimine uydur.

## 2. Kaynaklar

**Mevzuat metinleri:** `$S/kaynak/txt/` (UTF-8 düz metin; `grep -n` ile ara, büyük dosyayı baştan sona okuma).

| Konu | Dosya |
|---|---|
| Transit (Gümrük Genel Tebliği Transit Rejimi Seri No: 14) | `27-seri no 14.txt` |
| Antrepo ve geçici depolama yeri açma/işletme (GY 518 vd.) | `29-iŞLETİCİLER.txt` |
| Gümrüksüz satış mağazaları | `30-Güm.Sat.Mağazaları.txt` |
| Yetkilendirilmiş gümrük müşaviri, tespit | `31-YGM.txt` |
| Dahilde işleme (GK/GY) · DİR Kararı ve Tebliği · TEV | `32-DAHİLDE İŞLEME.txt`, `dahilde_isleme_rejimi_karari_sayisi_2005-8391.txt`, `dahilde_isleme_rejimi_tebligi_ihracat_2006_12.txt`, `dtm_2008-02_...txt` |
| Gümrük kontrolü altında işleme · Geçici ithalat · Hariçte işleme | `33-GKAİR.txt`, `34-GEÇİCİ İTHALAT.txt`, `35- hir.txt` |
| İhracat rejimi (GK/GY) · Geri gelen eşya · Serbest bölgeler · Muafiyetler (GK 167-168, 2009/15481) | `36-ihracat.txt`, `37-geri gelen eşya.txt`, `38-serbest bölge.txt`, `39-muafiyetler.txt` |
| Posta ve hızlı kargo · Sınır ticareti · Akaryakıt-kumanya · Tasfiye | `40-posta ve hızlı kargo.txt` (+ `posta_ve_hizli_kargo_...seri_no_1.txt`), `41-sınır ticareti.txt`, `42-kumanya.txt`, `43-tasfiye.txt` (+ tasfiye tebliğleri) |
| Yükümlülük · Tebliğ/tahakkuk · Teminat ve faiz · Geri verme-kaldırma | `44-yükümlülük.txt`, `45-tebliğ.txt`, `46-teminat ve faiz.txt`, `47-geri verme kaldırma.txt` |
| Cezalar · İtirazlar · Uzlaşma · Disiplin | `48-cezalar.txt`, `49-itirazlar.txt`, `50-uzlaşma.txt`, `51-disiplin cezaları.txt` |
| Varış öncesi işlemler · Yükümlü kayıt (YKTS) · Gümrük gözetiminde teslim · e-tebligat | `gumruk_genel_tebligi_x1varis_oncesi...`, `...yukumlu_kayit...`, `g_g_tebligi_x1gumruk_islerix2_seri_no_16...`, `elektronik_tebligat...` |
| Sair (KDV, ÖTV, 1567/32 sayılı Karar ve tebliğleri, ithalat genelgesi, DYY, 9903 teşvik, haksız rekabet, korunma, gözetim, ödeme şekilleri, teknik düzenlemeler, ürün güvenliği tebliğleri, 2006/10895 GB Kararı, serbest bölgeler uygulama, KKDF, onaylanmış kişi, TIR…) | `SAİR MEVZUAT KİTABI.txt` (18.500 satır; grep ile) |
| ÖTV listeleri | `ozel_tuketim_vergisi_*_liste_uygulama_genel_tebligi.txt` |
| İhracat (Ticaret yönü) | `ihracat_rejim_karari_...txt`, `ihracat_yonetmeligi_2006.txt`, `ihraci_yasak_ve_on_izne_bagli_...txt`, `ihraci_kayda_bagli_...txt`, `bedelsiz_ihracata_...txt`, `ihracat_sayilan_satis_...txt`, `dis_ticaret_sermaye_sirketi_...2025-07.txt`, `ck_2022-05986_e-ihracat...txt`, `ihracata_yonelik_devlet_yardimlari...txt` |
| İthalat (Ticaret yönü) · Teknik düzenlemeler · Fuar | `ithalatta_ilave_gumruk_vergisi_...txt`, `4 - TEKNİK DÜZENLEMELER.txt`, `2026-01_yurt_icinde_..._fuarlara...txt`, `nesli_tehlike_...txt`, `ham_elmas_...txt` |
| Menşe, STA, kümülasyon, GTS, uluslararası anlaşmalar | `STA ve KÜMÜLASYONLAR.txt`, `gumruk_genel_tebligi_x1genellestirilmis_tercihler_sistemix2_seri_no_5.txt`, `gumruk_genel_tebligi_x1uluslararasi_anlasmalarx2_seri_no_7.txt`, `27.03.2026_..._revize_pem_...txt` |
| Yatırım teşvik (2025/9903) | `7cbc2aad-101e-4f65-99e4-41b836e5bde2.txt` (sunum) + `SAİR MEVZUAT KİTABI.txt` |
| Tarife | `FASIL01.txt` … `FASIL97.txt` (pozisyonlar + bölüm/fasıl notları), `TARİFENİNYORUMU İLE İLGİLİ GENEL KURALLAR 2017.txt`, `gumruk_genel_tebligi_x1gumruk_tarife_cetveli_izahnamesix2_seri_no_4.txt`, sınıflandırma kararı tebliğleri, `genelge_*.txt`, `siniflandirma_avi.txt` |

**Çıkmış sorular (2021–2025, 500 soru):**

- Kitapçık metni, doğru şık «…» içinde: `$S/exams/<yıl>_red.txt`
- Konu dizini (her sorunun konu kodu): `$S/analysis/konu_eslesme.csv` (sütunlar: yil,no,alan,kod,hesap_mi,kok_tipi,bilgi_turu,kisa_konu). Kendi konu kodlarının satırlarını çıkar, o soruları kitapçıktan oku.
- Yıl yıl soru-soru analiz (hesap ve tarife sorularının tam metni ve adım adım çözümü dahil): `$S/analysis/<yıl>.md`
- Alt tip etiketleri ve "doğru cevap nasıl kurulmuş" notları: `$S/tipoloji/<yıl>_tipler.csv`, `$S/tipoloji/<yıl>_ornekler.md`

**Doğrulanmış ifade kaynağı olarak çıkmış sorular:** Bir O2 sorusunun cevap olmayan dört şıkkı ve bir G1 sorusunun doğru şıkkı Bakanlığın mevzuattan aynen aldığı cümlelerdir. Bunları doğrulanmış hüküm olarak kullanabilirsin (sonradan değişmiş olabileceğini aklında tut). Anahtarı tartışmalı sorular: 2021/89-90, 2022/94, 2023/72-73, 2024/46, 2025/12, 2025/16 — bunları kaynak olarak kullanma.

**Eksik kaynak uyarısı:** Gümrük Kanunu'nun 1–107. maddeleri ve Gümrük Yönetmeliği'nin kıymet, özet beyan, gümrük beyanı, transit (genel), antrepo (genel), BTB/menşe hükümleri bu klasörde **yok**; 5607 sayılı Kanun'un metni de yok. Bu konularda (1) çıkmış soruların doğru ifadelerine, (2) analiz dosyalarındaki açıklamalara, (3) kesin bildiğin hükümlere dayan. Bilgin kesin değilse o hükmü kullanma; aynı slotu aynı konunun doğrulayabildiğin başka bir hükmüyle doldur.

**İnternet:** Resmî mevzuat siteleri bu ortamdan erişilemiyor; deneme.

## 3. Güncellik

- Sınav hedefi 2027. Kaynak metinlerdeki yürürlükteki hükmü esas al (dipnotlarda "değişik", "mülga" ibarelerine dikkat et; mülga hükmü soru yapma).
- Her yıl değişen tutarları (asgari ücret tarifesi, yeniden değerleme ile güncellenen ceza ve teminat tutarları, tecilde teminat eşiği) doğru cevap yapma. Gerekirse tutarı soruda veri olarak ver ("… tutarın … TL olduğu varsayılmaktadır").
- Kaynakta tarihi belli bir eşik ya da oran kullanıyorsan açıklamada tarihini yaz.
- KDV genel oranı %20.

## 4. Yazım kuralları (özet; ayrıntı 02 ve alan promptunda)

- Slot listendeki **alt tipe uy.** Uyamıyorsan aynı ana tipten en yakın alt tipi kullan ve raporda gerekçesini yaz.
- Bakanlık dili: resmî, kısa, mevzuat merkezli. Kökte dayanak çoğu kez açıkça yazılır ("Gümrük Yönetmeliğine göre…", "4458 sayılı Gümrük Kanununa göre…").
- Olumsuz ya da kritik yüklem kökte **kalın ve altı çizili** yazılır: `**<u>değildir</u>**`, `**<u>yanlıştır</u>**`, `**<u>söylenemez</u>**`, `**<u>yer almaz</u>**`.
- Madde numarası ezberi sorma. Numara yalnız dayanak göstermek için kökte geçebilir.
- Her soru 5 şıklı. Çeldiriciler aynı kategoriden, gerçek komşu değerlerden (aynı mevzuatta geçen başka süre, makam, belge, liste öğesi). Bariz yanlış, komik ya da kategori dışı çeldirici yok. "Hepsi", "Hiçbiri" şıkkı yok.
- Bozuk şıkta tek bir unsur bozulur. İki unsuru birden bozma.
- Doğru şıkkı alışkanlıkla en uzun ya da en kısa yapma; çoğunlukla orta uzunlukta olsun.
- Öncüllü sorularda cevap dağılımı (kümen genelinde): ~%65 ara kombinasyon, ~%20 "Yalnız X", ~%15 tüm öncüller. Cevap "Yalnız X" ise şıklarda en az iki "Yalnız" bulunsun.
- Çıkmış soruyu aynen ya da şık yapısıyla kopyalama. Çıkmış sorunun **ölçtüğü bilgiyi** yeni bir kurguyla sorabilirsin (Bakanlık da yapıyor). **Hesap sorularında** çıkmış sorunun iskeletini kullanıp sayıları, kalem karmasını ve sırasını değiştirebilirsin; bütün şıkları yeniden türet.
- Aynı hükmü ya da aynı bilgiyi kümende iki kez sorma (üç deneme arasında da). Üç denemeye konu içindeki farklı alt başlıkları yay; 01 analiz §3.3'teki "mikro konular" ve çıkmış soruların ölçtüğü bilgiler öncelikli.
- Bir sorunun kökü ya da doğru öncülü başka bir sorunun cevabını vermesin.
- Bağlı seri kurabilirsin: aynı denemede aynı hükümden 2–3 soru (kural → öncüllü → vaka). Seri içindeki soruların alt tipi farklı olsun.
- **Açıklamada şık harfi kullanma** ("A şıkkı" yazma). Şıklara içeriğiyle atıf yap ("'süreli teminat mektubu' ifadesi …"). Harfler birleştirme aşamasında atanacak ve şıklar karıştırılabilecek.

## 5. Çıktı

Dosya: `$S/deneme/out/<KÜME>.json` — JSON dizi. JSON'u elle değil, bir Python betiğiyle `json.dump(..., ensure_ascii=False, indent=1)` kullanarak yaz; betiği `$S/deneme/work_<KÜME>/` altında tut. Her soru bir nesne:

```json
{
  "id": "GM-A1-07",                 // <KÜME>-<slot no, iki hane>
  "deneme": 2,
  "alan": "GM",                     // GM | SAİR | TARİFE | HESAP
  "konu": "GM07",                   // slot listesindeki kod (HESAP için "HESAP")
  "alt_tip": "O2",
  "seri": "D2-transit-teminat",     // isteğe bağlı: aynı denemede yan yana durması gereken sorular aynı değeri taşır
  "ortak_veri_id": null,            // H1+H2 setinde iki soru aynı kimliği taşır, ör. "D1-HS-A"
  "ortak_veri": null,               // yalnız setin İLK sorusunda: "X ve Y numaralı soruları…" cümlesi YAZMADAN, veri metni (satır sonları \n)
  "kok_on": "",                     // öncüllerden ÖNCE gelen metin (öncüllü değilse "")
  "onculler": [],                   // öncül metinleri, numarasız ("I." yazma; birleştirmede eklenir)
  "tablo": null,                    // E2 için: [["", "İşlem", "Sonuç"], ["I", "...", "..."], ...]
  "kok": "Gümrük Yönetmeliğine göre … hangisi **<u>yanlıştır</u>**?",
  "siklar": ["…", "…", "…", "…", "…"],   // harfsiz, 5 adet
  "dogru": 3,                       // 0 tabanlı indeks
  "sira_sabit": false,              // true: sayı/kod sıralı, kombinasyon, permütasyon, sıralama şıkları; false: serbestçe karıştırılabilir
  "aciklama": "2–4 cümle: doğru cevabın mevzuat gerekçesi + çeldiricilerin neden yanlış olduğu (harfsiz)",
  "tuzak": "Adayın hangi yanlış inançla hangi çeldiriciye kayacağı (tek cümle)",
  "dayanak": "Mevzuat adı ve madde (ör. Gümrük Yönetmeliği md. 519)",
  "kaynak": "Doğrulamada kullandığın dosya ve yer ya da çıkmış soru (ör. 29-iŞLETİCİLER.txt 'MADDE 524' bölümü; 2024/74 doğru ifade)",
  "guven": "yüksek"                 // yüksek | orta  (orta = kaynakta birebir göremedin, bilgine dayandı)
}
```

- `sira_sabit: true` olan sorularda doğru şıkkın konumunu kümen içinde çeşitlendir (hep C olmasın). Hesap şıkları küçükten büyüğe dizilir; en büyük tutar nadiren doğru cevap olsun.
- Hesap sorularında `aciklama` alanına çözüm tablosunu ve **beş şıkkın türetimini** yaz (her çeldirici tek bir hatadan; ör. "… → 21.900: lisans net tutarla alınmış"). Bu alan uzun olabilir.
- Tarife sorularında `dayanak` alanına pozisyon/not/GYKK ve her çeldiricinin gittiği pozisyonu yaz.

## 6. Öz-denetim (bitirmeden önce her soru için)

1. Doğru cevap kaynaktan birebir doğrulandı mı? Diğer dört şıkkın her biri kesin olarak yanlış mı (olumsuz kökte: dördü kesin doğru mu)?
2. Yorumla ikinci bir doğru cevap çıkabilir mi? Çıkıyorsa kökü ya da şıkkı netleştir.
3. Alt tip slotla uyumlu mu? Kök kalıbı katalogdaki gerçek örneğe benziyor mu?
4. Aynı bilgi kümende ikinci kez soruldu mu?
5. Hesapta beş şıkkın türetimi tutuyor mu (aritmetiği bir kez daha yap)? İki farklı hata aynı sayıyı veriyor mu?
6. JSON geçerli mi: `python3 -c "import json;d=json.load(open('<dosya>'));print(len(d))"` slot sayına eşit mi; her nesnede 5 şık ve 0–4 arası `dogru` var mı?

## 7. Son rapor (kısa; en fazla 25 satır)

- Üretilen soru sayısı (deneme bazında) ve dosya yolu.
- Slottan sapmalar ve gerekçesi.
- `guven: orta` işaretli sorular (id + kısa neden).
- Kaynakta doğrulanamadığı için değiştirdiğin ya da kullanmadığın konular.
