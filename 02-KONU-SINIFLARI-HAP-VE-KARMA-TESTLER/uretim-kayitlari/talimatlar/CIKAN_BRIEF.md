# ÇIKAN SORULARDAN HAP BİLGİ — ORTAK TALİMAT

Gümrük Müşavirliği (GM) sınavına hazırlanan adaylar için **"Çıkan Sorulardan Hap Bilgi"** dokümanı hazırlanıyor. 2021–2025 GM sınavlarının 500 sorusu konu konu sınıflandırıldı. Sen bir **konu kümesinden** sorumlusun: kümendeki her konunun bütün çıkmış sorularını oku ve her sorunun **ölçtüğü bilgiyi** tek satırlık, sınav öncesi okunacak bir **hap** cümlesine çevir.

Kısaltma: `S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`

## 1. Girdiler

- `$S/hap/girdi/<KÜME>.md`: kümendeki konular (kod, ad, sınıf, yıl dağılımı) ve kaynak dosyalar.
- `$S/konu/dosya/<KONU>.md`: her konunun çıkmış soruları. Her soru için kitapçık metni (doğru şık «…» içinde, resmî cevap anahtarı), analizdeki dayanak tahmini, çeldirici mantığı ve ölçülen bilgi notu var. Dayanaktaki "(?)" işaretleri tahmindir; maddeyi kaynaktan sen bul.
- Kaynak mevzuat: girdi dosyasındaki yollar (`$S/kaynak2/...`, `$S/kaynak/txt/...`). Büyük dosyayı baştan sona okuma; `grep -n` ile maddeyi bul, o bölümü oku. `SAİR MEVZUAT KİTABI.md` 366 sayfadır; başlıkla grep et.
- Soru metni bozuk ya da eksikse aynı soruyu `$S/analysis/<yıl>.md` dosyasındaki "1. Soru tablosu" satırından ve `$S/exams/<yıl>_red.txt` kitapçığından kontrol et.

## 2. Hap nasıl yazılır (örnek dokümandan birebir biçim)

Örnek (başka bir sınavın aynı dokümanından):

> ★ Alıcının **pazarlama dahil kendi hesabına** yaptığı faaliyetler, satıcı yararına ya da satıcıyla anlaşmaya dayansa bile satıcıya **dolaylı ödeme sayılmaz** ve fiyata **ilave edilmez**. (GK 24/3-b; GY 43/1-g · 2021/31, 2022/52, 2024/23) — Tuzak: 'Satıcıya dolaylı ödeme sayılır / kıymete dahil edilir' ifadesi yanlış (2021/31, 2022/52); pazarlama faaliyetleri 27/1-b'deki bedelsiz sağlanan unsurlar arasında da yoktur (2024/23).

> İndirgeme yönteminde aynı veya yakın tarihte satış yoksa, ithal tarihinden itibaren **doksan gün** içinde ithal edildiği hal ve durumda Türkiye'de yapılan **ilk satışın** birim fiyatı esas alınır. (GY 48/3 · 2021/39) — Tuzak: 20, 30, 60 veya 120 gün değil.

> Gümrük kıymeti, EXW 5.000 TL faturaya mesafe oranıyla ayrılan **Türkiye sınırına kadarki 500 TL navlun** ile **100 TL sigorta** eklenerek **5.600 TL** bulunur. (GK 27/1-e, 28/a; GY 51/6 · 2025/36) — Tuzak: Sınırdan sonraki 500 TL navlun eklenmez (6.050 / 6.100 yanlış).

> Akaryakıt Uygulama Yönetmeliğinde öngörülmeyen durumları sonuçlandırmaya 2021 sınavı tarihinde **Ticaret, İçişleri ve Hazine ve Maliye** Bakanlıkları yetkiliydi. (Akaryakıt Yön. 21/1 · 2021/95) — Tuzak: Adalet Bakanlığı yetkili değildir. — Not: 18.01.2024 değişikliğiyle güncel metinde yalnız Ticaret ve İçişleri Bakanlıkları yetkili.

Kurallar:

1. **Hap = doğru bilgi.** Sorunun doğru cevabından ve kökünden doğru kuralı çıkar, olumlu bir cümleyle yaz. Olumsuz kökte ("hangisi yanlıştır / değildir"), doğru cevap olan şık **yanlış** bilgidir: hapta onun doğrusunu yaz, yanlış ifadeyi "Tuzak" kısmına koy. Liste sorularında listeyi ve listeye girmeyen öğeyi birlikte ver ("… sayılır; … sayılmaz").
2. **Tek cümle, en fazla ~45 kelime.** Konuyu bilmeyen biri okuyunca kuralı öğrenebilmeli. Sayı, süre, oran, makam, belge adı, şart gibi **sınavda sorulan unsur** `**kalın**` yazılır (cümle başına 2–4 kalın öbek).
3. **Dayanak + soru kimliği:** `dayanak` alanına madde ("GK 24/3-b; GY 43/1-g", "5607 md. 3/10", "Seri No 4 Transit Tebliği 11/2", "TGTC 85.39; Fasıl 85 Not 12"), `sorular` alanına "yıl/no" listesi. Maddeyi kaynak dosyada **gör**; göremediysen analizdeki tahmini aynen kullanma, en emin olduğun yazımı ver ve `kaynak_disi: true` yap.
4. **Tuzak:** Çeldiricilerin en öğreticisini kısa yaz: "X değil", "'…' ifadesi yanlıştı", "… ile karıştırılmamalı". Şık harfi kullanma.
5. **Birleştirme (★):** Aynı bilgi birden çok soruda ölçüldüyse (aynı kural, aynı liste, aynı süre) **tek hapta birleştir**, `sorular` alanına hepsini yaz. Tuzakta hangi yılda hangi yanlış ifadenin kullanıldığını yıl yıl belirt. ★ işaretini sen yazma; birleştirme betiği, farklı yıllardan soru içeren hapları ★ ile işaretleyecek.
6. **Bir soru → bir hap.** Kümendeki **her çıkmış soru en az bir hapta** geçmeli. Bir soru iki ayrı kural ölçüyorsa (ör. hem süre hem makam) iki hap yazabilirsin; aynı soru kimliği iki hapta geçebilir.
7. **Hesap soruları:** Hapta hesabın **kuralını ve sonucunu** ver: hangi kalem dahil, hangisi hariç, hangi sırayla, sonuç kaç. ("… ilave edilir, … düşülür; CIF 50.000 + … = **55.000 TL**"). Tuzakta en sık çeldiricinin hangi hatadan çıktığını yaz.
8. **Tarife soruları:** Eşya → pozisyon eşleşmesini ve dayanak notu/GYKK'yı ver ("**Ahtapot** canlı/taze/dondurulmuş hâlde **03.07**'de yumuşakçalarla sınıflandırılır. (TGTC 03.07 · 2025/54) — Tuzak: 03.06 kabuklu hayvanlar, 16.05 hazırlanmış yumuşakçalar değil."). "Hangi pozisyonlar aynı fasılda" türü sorularda pozisyonları sırala.
9. **Güncellik (`not` alanı):** Sınav tarihinden sonra hüküm değiştiyse (kaynakta "değişik", "mülga", yeni tarihli fıkra görürsen) hap **sınav tarihindeki resmî cevaba** göre yazılır ve `not` alanına güncel hüküm ve değişiklik tarihi yazılır. Önemli bilinen değişiklikler: GK 241/1'de AYM 26.03.2026 kararıyla "ikincil düzenlemelere aykırılık" ibaresi iptal edildi; KDV Kanunu md. 21'e 24.07.2025'te (I) sayılı listede teminata bağlanan ÖTV'nin matraha girmesi eklendi; antrepo yatırım izni asgari faaliyet süresi 22.08.2025'te üç yıl oldu; konsinye ihracatta kesin satış bildirimi 06.05.2025'te 120 gün oldu. Yıllık değişen tutarlar (usulsüzlük cezası, asgari ücret tarifesi, teminat tutarları) için hapta sınavdaki tutarı yıl belirterek ver ("2024 sınavında 828 TL").
10. **Kaynak dışı (◇):** Bilgiyi kaynak metinde birebir doğrulayamadıysan (ör. Incoterms ayrıntısı, CISG, DTÖ Anlaşması, TCMB genelgesi, bir STA'nın taraf ülke listesi) hapı yalnız soru ve resmî cevaptan kur ve `kaynak_disi: true` yap. Bilgiyi uydurma; resmî cevabın söylediğinden fazlasını iddia etme.
11. **Resmî cevap tartışmalıysa** (kaynak metin resmî cevabı desteklemiyorsa) hapı resmî cevaba göre yaz, `not` alanında kaynağın ne dediğini belirt ("Not: Kaynak metne göre …; resmî anahtar … kabul etti."). Anahtarı tartışmalı bilinen sorular: 2021/89-90, 2022/94, 2023/72-73, 2024/46, 2025/12, 2025/16.
12. **Sıra:** Bir konunun hapları önce birleşik (çok yıllı) olanlar, sonra kronolojik. Sırayı sen ver (`sira` alanı yok; dizideki sıra esas).
13. Dil: sade Türkçe, Bakanlık terimleri (beyan sahibi, yükümlü, gümrük idaresi, gümrüklenmiş değer…). "Aday", "biz", "unutma" gibi hitaplar yok.

## 3. Konu özeti

Her konu için 1–2 cümlelik `ozet` yaz: konu 5 yılda kaç kez, hangi alt başlıklardan soruldu; en çok tekrarlanan bilgi ne; eğilim (son iki yıl) ne söylüyor. Örnek: "2021–2025'te 21 soru; NCTS tanımları, kapsamlı teminat ve kefil hükümleri her yıl geldi, 2023'ten itibaren basitleştirmeler (Seri No 5, 6) ve boru hattı da soruldu."

Hiç sorusu olmayan konular (HİÇ sınıfı) için hap yazma; `haplar: []` ve `ozet: ""` bırak.

## 4. Çıktı

Dosya: `$S/hap/cikan/<KÜME>.json`. JSON'u bir Python betiğiyle `json.dump(..., ensure_ascii=False, indent=1)` kullanarak yaz; betiği `$S/hap/work_cikan_<KÜME>/` altında tut.

```json
{
 "kume": "K03",
 "konular": [
  {
   "konu": "TRANSIT",
   "ozet": "…",
   "haplar": [
    {
     "metin": "Kapsamlı teminatta teminattan vazgeçme izni için … **on milyon TL** …",
     "dayanak": "Seri No 4 Transit Tebliği 11/2",
     "sorular": ["2022/66", "2025/65"],
     "tuzak": "…",
     "not": "",
     "kaynak_disi": false,
     "kaynak": "kaynak2/gm/23_23-SERİ_NO_4.md MADDE 11"
    }
   ]
  }
 ]
}
```

- `metin`: nokta ile biten tek cümle; dayanak ve soru kimliği **metne yazılmaz** (birleştirmede eklenir).
- `tuzak`, `not`: boş olabilir (""). "Tuzak:" ve "Not:" sözcüklerini alana yazma.
- `kaynak`: doğrulamada baktığın dosya ve madde; kaynak dışıysa "soru ve resmî cevap".

## 5. Öz-denetim

1. Her konunun her çıkmış soru kimliği en az bir hapta mı? `python3` ile say: dosyadaki kimlikler ∪ hap.sorular.
2. Olumsuz köklü sorularda hap doğru bilgiyi mi söylüyor (yanlış şıkkı hap yapmadın mı)?
3. Sayılar, süreler, makamlar kaynakla birebir mi?
4. Birleştirdiğin haplar gerçekten aynı bilgi mi (yakın ama farklı iki kural tek hapta karışmasın)?

## 6. Son rapor (en fazla 15 satır)

Konu başına hap sayısı ve soru kapsaması, `kaynak_disi` hap sayısı, `not` yazılan haplar (kısa), resmî cevabı kaynakla çelişen sorular.
