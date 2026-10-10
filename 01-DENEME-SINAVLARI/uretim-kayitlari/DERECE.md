# Zorluk, ölçülen bilgi ve çıkmış soru karşılığı etiketleme

`S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`

Girdi: `$S/deneme/birlesik/deneme<n>.json` (100 soru; alanlar: id, no, alan, konu, alt_tip, kok_on, onculler, tablo, kok, siklar, dogru, cevap, aciklama, dayanak, kaynak).
Çıkmış sorular: `$S/exams/<yıl>_red.txt` (doğru şık «…»), konu dizini `$S/analysis/konu_eslesme.csv` (yil,no,alan,kod,…,kisa_konu).

Her soru için şu alanları üret:

- `zorluk`: ÇK (çok kolay) · K (kolay) · O (orta) · Z (zor) · ÇZ (çok zor). Denemenin 100 sorusunu iyi hazırlanmış bir adayın gözüyle kolaydan zora sırala ve **tam olarak 10 ÇK, 20 K, 40 O, 20 Z, 10 ÇZ** dağıt (göreli zorluk). Ölçüt: bilginin ne kadar sık sorulduğu ve bilindiği, çeldiricilerin yakınlığı, işlem adımı sayısı, olumsuz/öncüllü kurgunun okuma yükü.
- `ozet`: Sorunun ölçtüğü bilginin tek cümlelik özeti (en fazla 200 karakter), doğru bilgiyi kural olarak yazar. Örnek: "Kısmi muafiyetli geçici ithalatta süre teslim tarihinden başlar; YYS sahibine dokuz ay uzatma verilir (GY 379/3, 380/5)."
- `kalip`: Şu listeden biri: HESAP, OLAY, KAPSAM_DIŞI, YANLIŞ, ÖNERMELİ, EŞLEŞTİRME, DOĞRU, SÜRE, BOŞLUK, KAVRAM, KAPSAM, BELGE, ZORUNLULUK, YETKİ, ORAN-TUTAR, MUAFİYET, TANIM, SONUÇ, SIRALAMA. Yol gösterici eşleme: H* → HESAP; V* → OLAY; O1/O3/O4 → KAPSAM_DIŞI; O2 → YANLIŞ; Ö* → ÖNERMELİ; E* → EŞLEŞTİRME; G* → DOĞRU; B* → BOŞLUK; K1 → KAVRAM; S* → SIRALAMA; D1 → SÜRE ya da ORAN-TUTAR; D2 → BELGE, YETKİ ya da TANIM; D3/D4/D5 → KAPSAM ya da MUAFİYET; D6 → SONUÇ ya da ZORUNLULUK. Sorunun asıl ölçtüğü şeye göre karar ver.
- `ders`: GM → "Gümrük Mevzuatı", SAİR → "Sair Mevzuat", TARİFE → "Tarife", HESAP → "Hesaplama".
- `konu`: Kısa konu adı (ör. "Transit", "Gümrük Kıymeti", "Menşe", "Kambiyo", "Kaçakçılık", "ÖTV", "Tarife – 84. Fasıl", "Geçici İthalat").
- `cikmis`: Bu sorunun ölçtüğü **bilgi alanı** 2021–2025 sınavlarında soruldu mu? Sorulduysa en yakın çıkmış soruyu "yıl/no" biçiminde yaz (ör. "2024/61"); birden fazlaysa en fazla iki tanesini virgülle yaz. Aynı konu değil, aynı hüküm/bilgi alanı ölçüsü kullan. Sorulmadıysa "" bırak. `kaynak` alanında çıkmış soru atfı varsa ondan başla; yoksa konu dizininden o konunun sorularını kitapçıkta okuyarak karar ver.

Çıktı: `$S/deneme/derece/deneme<n>.json` — `[{"id": "...", "no": 1, "zorluk": "O", "ozet": "...", "kalip": "YANLIŞ", "ders": "...", "konu": "...", "cikmis": "2023/86"}, ...]` (100 nesne, `no` sırasıyla). Betikle yaz (`json.dump(..., ensure_ascii=False, indent=1)`), sonunda dağılımı (10/20/40/20/10) ve 100 nesneyi kontrol et.

Kısa rapor döndür: zorluk dağılımı, `cikmis` dolu soru sayısı, kalıp dağılımı.
