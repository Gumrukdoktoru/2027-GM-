# SORULMAYAN HÜKÜMLER: BEKLENEN KONULAR HAP + SORU–CEVAP — ORTAK TALİMAT

Gümrük Müşavirliği (GM) sınavına hazırlanan adaylar için iki doküman hazırlanıyor:

1. **"Beklenen Konular Hap Bilgi"**: 2021–2025 GM sınavlarında **hiç sorulmamış** ama sorulma ihtimali yüksek hükümlerden tek satırlık haplar.
2. **"Sorulmayan Konular Soru–Cevap"**: Kaynak mevzuatın sınav değeri taşıyan ama sorulmamış hükümlerinden açık uçlu soru–cevaplar.

Sen bir **konu kümesinden** sorumlusun. Kümendeki her konunun kaynak metnini oku, alt konulara ayır, çıkmış sorularla karşılaştır ve sorulmamış hükümlerden bu iki içeriği üret.

Kısaltma: `S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`

## 1. Girdiler

- `$S/hap/girdi/<KÜME>.md`: konular (kod, ad, sınıf, 5 yıllık sayı, eğilim), hedef sayılar ve kaynak dosyalar.
- `$S/konu/dosya/<KONU>.md`: o konunun **bütün çıkmış soruları** (kitapçık metni, doğru şık «…» içinde). Bir hükmün sorulup sorulmadığını buna göre belirle. Yalnız doğru şık değil, **soru kökü ve şıklarda doğru bilgi olarak geçen hükümler de "sorulmuş"** sayılır (olumsuz kökte doğru olan dört şık da sorulmuş bilgidir). Gerekirse tüm sınavları da tara: `$S/exams/<yıl>_red.txt` (bir hüküm başka konu altında sorulmuş olabilir; `grep -i` ile anahtar sözcüğü ara).
- Kaynak mevzuat: girdi dosyasındaki yollar. `SAİR MEVZUAT KİTABI.md` 366 sayfadır; ilgili bölümü başlıkla grep et ve yalnız o bölümü oku. Kendi konularının kaynak bölümlerini **baştan sona** oku (şekli maddeler hariç).

## 2. Yöntem

### 2.1 Alt konular
Her konunun kaynak metnini sınav değeri taşıyan **alt konulara** (hüküm gruplarına) ayır: bir madde ya da birbirine bağlı birkaç fıkra = bir alt konu (ör. "Kapsamlı teminatta indirim ve teminattan vazgeçme", "Kefilin yükümlülükleri", "Transit beyanının düzenlenmesi"). Amaç, yürürlük, yürütme, mülga hükümler ve salt atıf maddeleri alt konu değildir. Her alt konuya durum ver:

- `SORULDU`: alt konunun sınav değeri taşıyan bilgisi çıkmış soruda ölçülmüş.
- `KISMEN`: bir ayrıntısı sorulmuş, diğer ayrıntıları sorulmamış.
- `SORULMADI`: hiç ölçülmemiş.

`cikmis` alanına ilgili çıkmış soru kimliklerini ("2024/74") yaz.

### 2.2 Soru–cevap (SORULMADI ve KISMEN alt konular)
Her SORULMADI alt konudan 1–3, her KISMEN alt konunun **sorulmamış ayrıntılarından** 1–2 soru–cevap yaz. Konu başına hedef, girdi dosyasındaki aralıktır (kaynak az ise alt sınırın altında kalabilirsin; şişirme).

Örnek (başka sınavın aynı dokümanından):

> **S.** 4458 sayılı Gümrük Kanununa göre tüzel kişi veya kişiler ortaklığının Türkiye Cumhuriyeti Gümrük Bölgesinde yerleşik kişi sayılması için ne gerekir?
> **Cevap:** Bu bölgede kayıtlı işyeri, kanuni iş merkezi veya şubesinin bulunması gerekir. Gerçek kişilerde ölçüt ise bu bölgede yerleşim yerinin bulunmasıdır. *(GK md. 3/4-b)*

Kurallar:
- Soru açık uçlu, tek bir hükmü sorar ve dayanağı (kanun/yönetmelik/tebliğ adı) söyler. "Ne kadardır, kimdir, hangi şartla, hangi hallerde, ne olur" türü.
- Cevap 1–2 cümle; ilk cümle doğrudan cevap. İkinci cümle gerekirse **karıştırılan komşu hükmü** ayırt eder (örnekteki gibi).
- Cevabın dayanağı (madde/fıkra) yazılır.
- **Yalnız kaynak metinde bulunan hükümler.** Her soru–cevaba `kanit` alanında kaynak metinden **birebir kesit** (15–200 karakter, kaynak dosyada aynen geçen; satır sonunu boşlukla birleştirebilirsin) ve `kaynak` alanında dosya yolu ver. Birleştirme betiği kesiti dosyada arayacak; bulunamayan çift setten çıkar.
- Çıkmış sorularda ölçülmüş bilgiyi soru–cevaba **alma**.
- Mülga ve yürürlükten kalkmış hükümleri alma. Yıllık değişen tutarlarda (ceza, teminat, ücret tarifesi tutarları) kaynakta yazan tutarı yılıyla ver ("2026 için …").

### 2.3 Beklenen hap (konu başına hedef: girdi dosyasında)
Sorulmamış hükümlerden **sorulma ihtimali en yüksek** olanları seç ve tek cümlelik hap yaz. Öncelik sırası:
1. Çok ve orta çıkan konuların sorulmamış **sayı, süre, oran, makam, belge, şart ve istisna** hükümleri (Bakanlığın en sevdiği unsurlar).
2. Kaynak metinde **yakın tarihli değişiklik** notu taşıyan hükümler (2023 ve sonrası; "(Değişik: …/…/2025-…)", "(Ek: …)" ibareleri). Bunlarda `degisiklik` alanına tarihi ve kısa açıklamayı yaz ("22.08.2025", "14.08.2026 (33340 R.G., Seri No 9 Tebliğ)").
3. Son iki yılda yükselen konuların sorulmamış alt başlıkları.
4. Çıkmış bir sorunun **komşu** hükmü (aynı maddenin sorulmamış fıkrası; aynı listenin sorulmamış öğesi; aynı sürenin istisnası).

Örnek haplar:

> Her iki firmanın oy hakkı veren hisse veya sermaye paylarının **en az %5'i** doğrudan ya da dolaylı aynı kişilere aitse alıcı ile satıcı **ilişkili** sayılır. (GY 55/1-ç)

> El konulan taşıt gizli tertibat, Türkiye'de **sicile kayıtsızlık** veya soruşturma sürerken **tekrar kullanılma** hâlinde alıkonulur; değeri kadar teminat **otuz gün** içinde verilmezse derhal tasfiye edilir. (5607 md. 10/2)

Kurallar: tek cümle, en fazla ~45 kelime; sınavda sorulacak unsur `**kalın**` (2–4 öbek); dayanak ayrı alanda (metne yazılmaz). Haplar soru–cevaplardan seçilebilir (aynı hükmün hap hâli). Her hapa da `kanit` + `kaynak` ver.

### 2.4 Konu özeti (beklenen dokümanı için)
Her konu için 2–3 cümlelik `ozet`: "2021–2025'te N soru (yıl dağılımı); en çok … soruldu, … tekrarlandı. … , … ve … hiç sorulmadı." Hiç çıkmayan konularda: "2021–2025'te hiç soru gelmedi; kaynakta … düzenleniyor. Öne çıkan sorulmamış hükümler: …".

## 3. Güncellik
- Hedef 2027 sınavı; kaynak metinlerdeki **yürürlükteki** hüküm esastır. "Değişik", "Ek", "Mülga" dipnotlarını oku.
- KDV genel oranı %20. GK 241/1 için AYM 26.03.2026 iptal kararını dikkate al (iptal edilen ibareyi doğru hüküm olarak yazma).

## 4. Çıktı

Dosya: `$S/hap/sorulmayan/<KÜME>.json`. Python betiğiyle `json.dump(..., ensure_ascii=False, indent=1)` yaz; betikleri `$S/hap/work_sorulmayan_<KÜME>/` altında tut. Uzun iş: konu konu yaz ve her konudan sonra dosyayı güncelle (yarıda kesilirse emek kaybolmasın).

```json
{
 "kume": "K03",
 "konular": [
  {
   "konu": "TRANSIT",
   "kaynak_ozeti": "GK md. 84-92; GY md. 212-239; Seri No 4 Transit Tebliği md. 1-40",
   "ozet": "2021–2025'te 21 soru (…); … hiç sorulmadı.",
   "alt_konular": [
    {
     "ad": "Kapsamlı teminatta indirim ve teminattan vazgeçme",
     "dayanak": "Seri No 4 Transit Tebliği md. 11",
     "durum": "KISMEN",
     "cikmis": ["2022/66"],
     "sc": [
      {"s": "…?", "c": "… .", "dayanak": "Seri No 4 Tebliğ md. 11/2", "kanit": "en az on milyon Türk lirası tutarındaki kapsamlı teminat", "kaynak": "kaynak2/gm/23_23-SERİ_NO_4.md"}
     ]
    }
   ],
   "beklenen": [
    {"metin": "… **on milyon TL** …", "dayanak": "Seri No 4 Tebliğ 11/2", "degisiklik": "31.12.2023 (Seri No 15)", "kanit": "…", "kaynak": "kaynak2/gm/23_23-SERİ_NO_4.md"}
   ]
  }
 ]
}
```

- `durum` SORULDU olan alt konularda `sc: []`.
- `degisiklik` boş olabilir ("").
- `kanit` kaynak dosyada **aynen** geçmeli (büyük-küçük harf ve noktalama dahil; birden çok boşluk tek boşluk sayılır). Kaynak `.md` ise markdown işaretlerini (`**`) kesite alma.

## 5. Öz-denetim
1. `kanit` kesitlerini kendin doğrula: her biri için `grep -F` (ya da Python `in`) ile dosyada ara; bulunmayanı düzelt.
2. Soru–cevap ve beklenen haplarda çıkmış soruda ölçülmüş bilgi yok mu?
3. Hedef sayılar tuttu mu? Aynı hüküm iki kez yazıldı mı?
4. JSON geçerli mi?

## 6. Son rapor (en fazla 15 satır)
Konu başına alt konu sayısı (sorulan/kısmen/sorulmayan), soru–cevap ve beklenen hap sayısı; `degisiklik` taşıyan hap sayısı; kaynakta bulamadığın ya da okuyamadığın bölümler.
