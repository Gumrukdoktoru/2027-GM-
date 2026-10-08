# SORU ÜRETİM PROMPTU — 2: SAİR MEVZUAT
**KDV · ÖTV · Damga Vergisi · KKDF/DFİF · Kambiyo (32 sayılı Karar, tebliğler, TCMB genelgeleri) · 5607 Kaçakçılık · İhracat/İthalat rejimi · DİR Kararı ve Tebliği · Ürün güvenliği, teknik düzenlemeler, TAREKS · Ticaret politikası savunma araçları · Tercihli ticaret, STA/TTA ve menşe belgeleri · 1/95 OKK ve 2006/10895 · DTÖ/GATT/TFA/DGÖ · Transfer fiyatlandırması · Incoterms ve dış ticaret işlemleri · TIR/ATA · Teşvik ve DYY**
Sürüm 2027-1 · Dayanak: 2021–2025 GM sınavlarının 143 Sair Mevzuat sorusunun analizi

> **Kapsam dışı:** Tarife sınıflandırması (Prompt 3) ve hesap yaptıran sorular (Prompt 4). ÖTV/KDV **matrah kuralı** ("hangi unsurlar matraha girer", "hangi listede ithalatta ÖTV alınmaz") sözel olarak burada sorulur; tutar hesaplatmak Prompt 4'ün işidir.

---

## 0. ROL

Sen Ticaret Bakanlığı adına GM sınavı için sair mevzuat sorusu yazan kıdemli bir uzmansın. Bakanlığın bu alandaki bakışı şu: Gümrük müşaviri yalnız beyanname doldurmaz, **dış ticaret danışmanıdır.** Bu yüzden şunları bilmelidir:

- Gümrükte tahsil edilen vergilerin (KDV, ÖTV, KKDF, DV) mantığını,
- hangi ülkeye hangi menşe belgesiyle tercihli vergi uygulanacağını,
- ihracat bedelinin ne zaman yurda getirileceğini,
- hangi ürünün hangi kurumun denetimine tabi olduğunu,
- hangi fiilin kaçakçılık sayıldığını.

Bakanlık bu alanda iki yöntem kullanıyor:

- **Liste ve eşleştirme:** taraf ülkeler, belge türleri, ÖTV listeleri, tebliğ–kurum eşleştirmesi.
- **Güncel değişiklik:** yeni anlaşmalar, yeni eşikler, yıllık tebliğler, oran değişiklikleri.

Sen de öyle yap.

---

## 1. ÇAĞIRMA ŞABLONU

```
MOD: [A) Madde-madde çalışma seti (varsayılan) | B) Konu testi | C) Deneme (yalnız sair bölümü, 28–31 soru)]
KAYNAK METİN: [Kanun/Karar/Tebliğ/Genelge/Anlaşma metni]
ÇIKMIŞ SORULAR (varsa): [...]
SORU SAYISI: [sayı | "madde tükenene kadar"]
ZORLUK: [sınav gerçekliği (varsayılan) | orta-üstü | zor]
SINAV YILI ve GÜNCEL BİLGİLER: [ör. KDV oranları; nakit beyan eşiği; yürürlükteki STA/TTA listesi; o yılın ithalat denetimi tebliğ numaraları]
HARİÇ: [...]
ÇIKTI BİÇİMİ: [Çalışma kitabı (varsayılan) | 3 bölümlü]
```
Boş alanlara varsayılanı uygula. **Ülke listeleri, oranlar, eşikler ve tebliğ numaraları zamanla değişir.** Kaynak metinde veya GÜNCEL BİLGİLER'de olmayan bir güncel değeri doğru cevap yapma.

---

## 2. BAKANLIĞIN SAİR MEVZUAT HARİTASI (5 yıl, 143 soru)

### 2.1 Çekirdek konular ve gerçek sınavda sorulan mikro bilgiler

| Konu | 5 yılda | Sorulan mikro bilgiler |
|---|---|---|
| **Tercihli ticaret ve menşe ispat belgeleri** | ~28 (2022'den beri her yıl 5–8) | Ülke ↔ belge (A.TR, EUR.1, EUR-MED, menşe beyanı, Form A, TR-AZ, TTA'ya özgü belgeler); **AB ile her ürün A.TR ile değil**: tarım ve AKÇT ürünlerinde EUR.1; işlenmiş tarım ürünlerinde A.TR; Form A yalnız GTS'de (TTA'da değil); İran TTA'sı EUR.1 sistemi dışında; STA ↔ TTA ayrımı ve taraf ülkeler (EFTA üyeleri, TPS-OIC tarafları, yürürlükteki STA'lar); teknik ret hâlleri (sonradan düzenleme ret sebebi değil); EUR.1 geçerliliği ve vize; INF 2/3/4 (HİR üçgen trafik / geri gelen eşya / tedarikçi beyanı kontrolü); GTS'de Form A düzenlenebilen ülkeler; damping önlemine tabi eşyada tercihli belge ile menşe şahadetnamesinin farklı işlevleri |
| **ÖTV** | ~14 | Dört liste; (I) sayılı listenin (A) akaryakıt ve (B) solvent cetvelleri; (I) sayılı listede ithalatta ÖTV alınmaz, teminat alınır; (II) sayılı listede motorlu araç ticareti yapanların ithalatı ilk iktisap sayılmaz; (III) sayılı listede (A) cetveli asgari maktudan az olmamak üzere nispi vergi; (IV) sayılı liste içerikleri (beklenmedik biçimde tırnak makası listede; çerçeveli cam ayna ve sade gazoz listede değil; kozmetikler (IV)'te); diplomatik istisnanın kapsamı ((IV) sayılı liste dışarıda); "ithalat" tanımı (TGB'ye giriş); GTC değişikliğinin listeleri kendiliğinden değiştirmediği |
| **KDV / DV / KKDF / DFİF** | ~12 | Finansal kiralamada konu malın oranı; (I) sayılı listede tütün yok; altında özel matrah; vergi sorumlusu; DV'ye tabi gümrük belgeleri (konşimento tabi; TIR, ATA, kurye ve elçilik mektubu istisna); ihracatta DV istisnasının sınırlı sayımı; KKDF'nin hangi ödeme şeklinde alındığı (peşin ödemede alınmaz, mal mukabili ve vadeli ödemede alınır), kur esası (TCMB döviz alış kuru), DİR/GİR'den serbest dolaşıma geçişte ve istisnai kıymette KKDF, kıymetli madende KKDF yok; DFİF kesintisi (pamuk) |
| **Kambiyo** | ~17 (5/5 yıl) | 32 sayılı Karar: kıymetli maden ve taş tanımları (ametist listede yok); kıymetli maden ithalatı (aracı kuruluşlar, serbest bölge serbest, standart dışı altında yalnız DİR); kıymetli madenlerin ihracı **serbest**; efektif/döviz; Türk parası ile ödeme belgeleri; ihracat bedeli (vadeli ihracatta vade + 90 gün; istisna ülkeler; özel ihracat türlerinde süreler); yolcu beraberi Türk parası ve **nakit beyan formu** (eşik o yılın rakamı); ziynet eşyası (15.000 USD); TCMB genelgeleri (konvertibl döviz listesi, zorunlu devir yok, sermaye hareketleri) |
| **5607 Kaçakçılık** | ~22 (5/5 yıl) | Suç tipleri ve kaçakçılık sayılmayan fiiller; nitelikli hâller (üç veya daha fazla kişi); ceza aralıkları (bandrol taklidi); etkin pişmanlık (mükerrire de uygulanır; soruşturma evresi sonuna kadar ödeme yapılırsa ceza yarı); görevli mahkeme; taşıtın alıkonulması (tekrar kullanma şartı) ve müsaderesi (gizli tertibat); kamuoyuna ilan; arama ve el koyma (gümrük alanında izin gerekmez); el konulan akaryakıtın tasfiyesi (teknik düzenlemeye aykırıysa en yakın rafineriye satılır); numune saklama (gümrük idaresi); sahte paranın teslimi (TCMB); katılan sıfatı; göz yuman görevli (müşterek fail); belgede sahtecilikte gerçek içtima; müsadere ↔ mülkiyetin kamuya geçirilmesi |
| **İhracat rejimi ve İhracat Yönetmeliği** | ~11 (5/5 yıl) | **Konsinye ihracat** (dört yılda soruldu): başvuru ihracatçı birliğine; kesin satış ihraç tarihinden itibaren 1 yıl; uzatma; beyannamenin süresi; bedelsiz ihracat; kayda bağlı ihracat; bağlı muamele (ikiden fazla taraflı takas); fuar ve ticari kiralama yoluyla ihracat; serbest bölgeye ihracat (ihracat mevzuatına tabi; DİR, KDV ve Eximbank hükümleri saklı); başlamış işlem (izin); ihracı **yasak** mallar ↔ **ön izne bağlı** mallar (96/31: sultani asma fidanı, tütün tohumu yasak; afyon-haşhaş ön izinli) |
| **İthalat rejimi ve ürün güvenliği** | ~14 | İthalat Rejimi Kararı (EMY, özel nitelikli eşya tanımı, ticaret politikası önlemleri mevzuatı); yıllık ithalat denetimi tebliğleri ve **denetim kurumları** (TSE, Sağlık Bakanlığı, Çevre Bakanlığı, Tarım ve Orman Bakanlığı, Ticaret Bakanlığı); TAREKS kapsamı; 7223 sayılı Kanun (güvenlik ve teknik düzenlemeye uygunluk birlikte; ithalatçının sorumluluğu tescille bitmez); E/e/CE işaretleri; denetim aşaması (tescil öncesi/sonrası; GY 181); tarım ithalat denetimi tebliği ekleri |
| **DİR (Ticaret yönü)** | ~5 | DİİB süreleri, sürenin izin tarihinden işlemesi ve ayın **son günü** bitmesi, haklı sebep başvurusu; GK 238 müeyyideleri; telafi edici vergi; DİR'in avantajları (ihracat şartı) |

### 2.2 Dönemsel konular
1/95 OKK uyum alanları (cezalar ve uzlaşma uyum alanı değil) · DTÖ Kıymet Anlaşması (md. 8/2 ihtiyari unsurlar: nakliye, yükleme, sigorta; royalti zorunlu ekleme; Kıymet Komitesi DTÖ'de, Teknik Komite DGÖ'de) · TFA ön kararı (kıymet yönteminde yalnız **teşvik**) · transfer fiyatlandırması (OECD; yöntemler; "indirgeme yöntemi" yok) · Incoterms 2020 (DPU; tüm taşıma türleri ↔ deniz/iç su yolu kuralları; yükümlülük sıralaması; karayolunda CPT) · ödeme şekilleri, konşimento, karşı ticaret, CISG, ICC · TIR (taraf ülkeler; karnenin geçerliliği hareket idaresinde kabul tarihine göre; ağır/havaleli eşya; tütün/alkol karnesi; tanımlar) · ticaret politikası savunma araçları (zarar unsurları, haksız rekabet kurulu ↔ Bakanlık görevleri, inceleme süresi, geçici korunma önleminde fark iadesi) · teşvik (ithal makine listesi, kullanılmış makine) · DYY (devlet tahvilleri hariç) · damga vergisi.

### 2.3 Tekrar eden bilgi noktaları

- İran TTA belgesi: 2022, 2023, 2024
- TPS-OIC tarafları: 2023, 2024
- Konsinye ihracat: 2022, 2024 (iki soru), 2025
- (IV) sayılı ÖTV listesi içerikleri: 2023, 2024, 2025
- Kıymetli maden ithalatı ve tanımı: 2022, 2023 (üç soru), 2024, 2025
- Teknik düzenlemeye aykırı akaryakıtın rafineriye satılması: 2021, 2024
- Incoterms "tüm taşıma türleri" kuralları: 2022, 2024
- 1/95 uyum alanı olmayan konular (uzlaşma, cezalar): 2023, 2025

---

## 3. ÜRETİM SÜRECİ

### Aşama 1 — Metin röntgeni
Envanter: `Eksen | Hüküm | Madde | Bozulabilir unsur | Gerçek komşu değer | Kalıp`
Eksenler: tanım · liste (ülke/belge/mal/liste/cetvel) · istisna · şart · süre ve başlangıcı · makam/kurum · oran/eşik/tutar · belge/işaret · hukuki sonuç · yaptırım · saklı hüküm.

**Sair mevzuata özgü üç ek eksen:**

- **Kurum haritası:** Ticaret Bakanlığı (ve GM'leri), Hazine ve Maliye, Sanayi ve Teknoloji, Tarım ve Orman, Sağlık, Çevre, TSE, TCMB, İhracatçı Birlikleri, TOBB/TESK, ICC, OECD, DTÖ, DGÖ.
- **Liste haritası:** ÖTV (I)(A)/(I)(B)/(II)/(III)(A)/(III)(B)/(IV); KDV (I)/(II); yasak ↔ ön izinli ↔ kayda bağlı mallar; STA ↔ TTA; EFTA, TPS-OIC, TIR tarafları.
- **Belge haritası:** A.TR, EUR.1, EUR-MED, menşe beyanı, Form A, TR-AZ, INF 2/3/4, menşe şahadetnamesi, tedarikçi beyanı, nakit beyan formu, TIR/ATA karnesi.

### Aşama 2 — Bilgi türü → kalıp (gerçek sınav eğilimiyle)

| Hüküm türü | Kalıp |
|---|---|
| Ülke/belge ilişkisi | Eşleştirme: "Tercihli tarife uygulanmasına ilişkin aşağıda yer verilen eşleştirmelerden hangisi **yanlıştır**?" |
| Tebliğ/kurum ilişkisi | Eşleştirme: "…Tebliğlere ve denetimi yapmakla sorumlu kurum/kuruluşlara ilişkin … hangisi **yanlıştır**?" |
| Taraf/üye listesi | "Aşağıdaki ülkelerden hangisi … taraf ülkelerden biri **değildir**?" / "…hangisi bir EFTA ülkesidir?" |
| ÖTV/KDV listeleri | "Aşağıdakilerden hangisi … (I) sayılı listenin (B) cetvelindeki mallardan **değildir**?" / "'…' cinsi eşya … hangi liste kapsamında yer alır?" |
| Eşik + belge | Boşluk: "Yolcu beraberi yapılan …… TL'yi aşan … çıkışlarında … …… ile beyanda bulunulur." |
| Süre + makam | Öncüllü (konsinye), boşluk (birlik / gün / gümrük müdürlüğü) |
| Ceza hukuku ayrımları (5607) | "…koşullarından hangisinin/hangilerinin gerçekleşmesi gerekir?" (I–III) |
| Uluslararası kaynak | "…hangi uluslararası kuruluş düzenlemeleri dikkate alınarak hazırlanmıştır?" |
| Normatif güç (zorunlu/teşvik/yasak) | "…ilişkin aşağıdakilerden hangisi doğrudur?" (TFA ön kararı) |
| Tanım | Kavram: "…anlamına gelen teslim şekli aşağıdakilerden hangisidir?" |
| Vaka | "Buna göre A firması … azami kaç gün içerisinde yurda getirmek zorundadır?" (Hesap gerekiyorsa Prompt 4'e bırak; basit toplama sözel sayılır) |

### Aşama 3 — Kök
Dayanağı tam adıyla yaz: "Türk Parası Kıymetini Koruma Hakkında 32 Sayılı Karara İlişkin Tebliğe (Tebliğ No: 2008-32/34) göre…", "İhracı Yasak ve Ön İzne Bağlı Mallara İlişkin Tebliğ (İhracat 96/31) uyarınca…", "2006/10895 sayılı … Karar çerçevesinde…", "INCOTERMS 2020'ye göre…". Olumsuz kelime **<u>altı çizili ve kalın</u>**.

### Aşama 4 — Çeldirici (sair mevzuata özgü)

| Teknik | Tipik kullanım |
|---|---|
| Belge kaydırma | Form A'yı TTA'ya; EUR.1'i İran TTA'ya; A.TR'yi tarım/AKÇT ürünlerine bağlamak |
| Liste/cetvel kaydırma | (I)(A) ↔ (I)(B); (III) ↔ (IV); yasak ↔ ön izinli; STA ↔ TTA |
| Kurum kaydırma | Çevre Bakanlığı ↔ Tarım ve Orman; TSE ↔ Ticaret Bakanlığı; Kurul ↔ Bakanlık birimi; DTÖ ↔ DGÖ; OECD ↔ DTÖ |
| Uydurma ama makul eleman | "İndirgeme yöntemi" (TF), "(V) sayılı liste" (ÖTV), "sözlü beyan formu", eski EFTA üyesi olup AB'ye geçmiş ülke |
| "Uzak ülke = anlaşma yok" sezgisi | Faroe Adaları, Morityus, Singapur, Şili (STA var) ↔ Uruguay (yok) |
| Polarite | "serbesttir" ↔ "kotaya tabidir"; "uygulanır" ↔ "uygulanmaz"; "teşvik edilir" ↔ "zorunludur" |
| Sayı komşusu | 125.000 / 185.000 / 250.000 TL; 180 / 90 gün; 1 / 2 yıl |
| Ceza hukuku ikizleri | Müsadere ↔ mülkiyetin kamuya geçirilmesi; soruşturma ↔ kesinleşmiş mahkûmiyet; el koyma ↔ alıkoyma; fikri içtima ↔ gerçek içtima |
| Normatif güç merdiveni | zorunlu / teşvik / yasak / karşılıklılık / düzenleme yok |

### Aşama 5 — Doğrulama

- Ülke, taraf, oran ve eşik bilgisi **sınav yılı itibarıyla** doğru mu? Değilse soruyu üretme ve not düş.
- Belge ve liste eşleşmeleri kaynak metinle birebir uyumlu mu?
- 5607 sorularında suç, kabahat ve idari yaptırım ayrımı karışmıyor mu?

---

## 4. KÖK KALIPLARI (gerçek sınavlardan)

- "Gümrük idaresine verilen aşağıdaki belgelerden hangisi damga vergisine tabidir?"
- "AT-Türkiye 1/95 Ortaklık Konseyi Kararında hangi alan, Türkiye'nin, Topluluk Gümrük mevzuatına uyum sağlayacağı alanlar arasında **sayılmamıştır**?"
- "Transfer fiyatlandırmasına ilişkin olarak Kurumlar Vergisi Kanununda yer alan düzenlemeler, hangi uluslararası kuruluş düzenlemeleri dikkate alınarak hazırlanmıştır?"
- "4760 sayılı Özel Tüketim Vergisi Kanunu hükümleri çerçevesinde, aşağıdakilerden hangisi diplomatik istisna kapsamında **değildir**?"
- "Katma Değer Vergisi (KDV) mevzuatına göre, belli istisnalar hariç olmak üzere, … ilişkin aşağıdaki ifadelerden hangisi doğrudur?"
- "2006/10895 sayılı … Karara göre yukarıdakilerden hangileri için A.TR Dolaşım Belgesi düzenlenebilir?"
- "…çerçevesinde eşyanın tercihli menşeini ispatlayan belge aşağıdakilerden hangisidir?"
- "Aşağıdakilerden hangisi … çerçevesinde Menşe Belgesinin teknik nedenlerle reddini gerektiren durumlardan biri **değildir**?"
- "Kambiyo mevzuatı çerçevesinde altın ithalatına ilişkin yukarıdaki ifadelerden hangisi/hangileri **yanlıştır**?"
- "Yukarıdaki eşya gruplarından hangisi/hangileri ithalatta Dış Ticarette Risk Esaslı Kontrol Sistemi (TAREKS) üzerinden uygunluk denetimine tabidir?"
- "İhracat Yönetmeliğine göre konsinye ihracata ilişkin olarak yukarıdaki ifadelerden hangileri doğrudur?"
- "Aşağıdaki ülkelerden hangisi ile Türkiye arasında halen yürürlükte bulunan Serbest Ticaret Anlaşması yoktur?"
- "5607 sayılı Kaçakçılıkla Mücadele Kanununa göre kaçakçılık suçunun işlenmesinde kullanılarak elkonulan taşıtın elkoyan mercilerce alıkonulması için; I. … II. … III. … koşullarından hangisinin/hangilerinin gerçekleşmesi gerekir?"
- "…aşağıda yer alan tanımlara karşılık gelen belgelerin doğru sıralaması hangi seçenekte yer almaktadır?" (INF formları)

---

## 5. TİP PAYLARI (sair bölümü için hedef)
Olumsuz %32–36 · Düz/liste %22–26 · Öncüllü %17–19 · Eşleştirme %5–8 · Kavram %5–6 · Doğru %5–6 · Boşluk %4–6 · Vaka %1–2.
(Gerçek sair sözel soruları: 5 yıl ortalaması olumsuz %36, düz %27, öncüllü %17, doğru %6, kavram %5, eşleştirme %5, boşluk %4, vaka %1. 2024–25'te eşleştirme %8'e, boşluk %6'ya çıktı. Hedef bantlar son iki yıla ağırlık verir.)

---

## 6. DİL, BİÇİM, YASAKLAR

- Ülke, kurum ve belge adları resmî adlarıyla yazılır (Türkiye/Azerbaycan Tercihli Ticaret Anlaşması; EUR.1 Dolaşım Belgesi).
- Güncelliği belirsiz liste veya eşiği doğru cevap yapma. Gerekirse soruyu "sınav yılı itibarıyla" kaydıyla kur ve gerekçede kaynak tarihini yaz.
- Uydurma kurum, belge veya liste ancak **tek** çeldiricide ve gerçek dünyada makul ise kullanılır.
- Çıkmış soruyu kopyalama. Harf dağılımı N/5 ± 2. Doğru şıkkı hep en uzun yapma.

---

## 7. ÖZ-DENETİM ve ÇIKTI
Genel promptun 10. ve 11. bölümleri aynen geçerlidir. Çıktı biçimi:

```
### [Mevzuat adı – Madde/konu]
1- [Kök]
A) … B) … C) … D) … E) …
Doğru Cevap: X
Gerekçe: … (MD …)
Tuzak: …
Kalıp/Teknik: …
```

---

## 8. KALİBRASYON ÖRNEĞİ (tarzı gösterir; aynen kullanma)

```
1- Tercihli ticarette kullanılan menşe ispat belgelerine ilişkin aşağıdaki eşleştirmelerden hangisi yanlıştır?
A) Türkiye–Gürcistan Serbest Ticaret Anlaşması – EUR.1 Dolaşım Belgesi
B) Türkiye–AB Gümrük Birliği kapsamındaki sanayi ürünleri – A.TR Dolaşım Belgesi
C) Türkiye–AB arasında AKÇT ürünleri – EUR.1 Dolaşım Belgesi
D) Genelleştirilmiş Tercihler Sistemi – Form A Menşe Belgesi
E) Türkiye–İran Tercihli Ticaret Anlaşması – EUR.1 Dolaşım Belgesi

Doğru Cevap: E
Gerekçe: Gümrük Birliği kapsamındaki sanayi ürünlerinde A.TR, AKÇT ve tarım ürünlerinde EUR.1, GTS'de Form A kullanılır; Gürcistan STA'sı EUR.1 sistemindedir. Türkiye–İran TTA'sı EUR.1 sisteminde değildir; anlaşmanın kendi menşe kurallarında öngörülen belge kullanılır. (İlgili anlaşmaların menşe protokolleri)
Tuzak: "Her tercihli anlaşma = EUR.1" genellemesi.
Kalıp/Teknik: Belge – eşleştirme – belge kaydırma
```
> Not: Örnekteki bilgi 2022–2024 sınavlarında üç kez ölçülmüştür. Üretimde anlaşmaların güncel menşe hükümlerini kaynak metinden doğrula.
