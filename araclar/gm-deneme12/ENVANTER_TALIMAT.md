# GM Çıkmış Soru Envanteri — Analist Talimatı

Klasör: /home/claude/2027-gm-/araclar/gm-deneme12
Sana verilen YIL için Gümrük Müşavirliği (GM) sınavının 100 sorusunu tek tek analiz et ve `envanter/<YIL>.tsv` dosyasını yaz. Başka hiçbir dosyaya dokunma, git işlemi yapma.

## Girdiler
- `sinav/<YIL>.txt` (düz metin) ve `sinav/<YIL>_layout.txt` (iki sütunlu sayfa düzeni; soruları buradan sütun sütun okumak daha güvenli).
- `anahtarlar/<YIL>_anahtar.json` — kırmızı işaretten çıkarılmış resmî cevaplar ({"1":"C",...}; eksik numara olabilir → RESMI_CEVAP boş bırak, "?" yaz).
- `metin/` — sınav hazırlığında kullanılacak TÜM kaynak metinler (gümrük mevzuatı 1–51 numaralı dosyalar, tarife fasılları FASIL01–97, genelgeler, tebliğler, ÖTV/ÖİV tebliğleri, ihracat/dış ticaret mevzuatı, SAİR MEVZUAT KİTABI.txt, Tarife_Kitabi.txt, kaçakçılık.txt, hesaplama dosyaları, STA ve KÜMÜLASYONLAR.txt, 4 - TEKNİK DÜZENLEMELER.txt, vb.). Grep ile ara.

## Çıktı: envanter/<YIL>.tsv (UTF-8, sekme ayraçlı, başlık satırı dahil 101 satır)
Sütunlar:
`YIL	SORU_NO	KONU	ÖLÇÜLEN_BİLGİ	KALIP	KAYNAK_DOSYA	RESMI_CEVAP	DOGRU_SIK_METNI`

- KONU: aşağıdaki listeden TAM OLARAK birini yaz (gerekirse en yakınını seç):
  GK-Genel (tanımlar, temsil, karar, bilgi hakkı, süreler, YYS, OKSB, sonradan kontrol, tarife pozisyonu ayırma) |
  Tarife-Sınıflandırma (GTC yorum kuralları, bölüm/fasıl notları, pozisyon tespiti, izahname, sınıflandırma kararları, genelgeler, BTB) |
  Menşe-STA (tercihli/tercihsiz menşe, STA, PEM, kümülasyon, menşe ispat belgeleri, GTS) |
  Kıymet (GATT VII Anlaşması, gümrük kıymeti, transfer fiyatlandırması dahil) |
  Vergi-Hesaplama (gümrük vergileri hesaplama, KDV/ÖTV hesap, tarım payı, DFİF, kur, sayısal hesap) |
  Beyan-Serbest Dolaşım (özet beyan, eşyanın sunulması, geçici depolama, beyan, muayene, serbest dolaşıma giriş) |
  Transit-TIR-ATA |
  Antrepo-İşleticiler |
  DİR (dahilde işleme rejimi: GK, GY, DİR Kararı, DİR Tebliği, telafi edici vergi) |
  HİR-GKAİR |
  Geçici İthalat |
  İhracat-Geri Gelen (GK ihracat, geri gelen eşya) |
  Serbest Bölge-GSM-YGM |
  Muafiyetler |
  Posta-Kargo-Sınır Ticareti-Kumanya |
  Tasfiye |
  Yükümlülük-Teminat-Faiz-Geri Verme |
  Cezalar-İtiraz-Uzlaşma |
  Gümrük Müşavirliği-Disiplin |
  Kaçakçılık (5607 ve yönetmelikleri) |
  İthalat Rejimi-Ticaret Politikası (İthalat Rejimi Kararı, ilave gümrük vergisi, korunma, damping, gözetim) |
  İhracat-Dış Ticaret Mevzuatı (İhracat Rejim Kararı, İhracat Yönetmeliği, bedelsiz ihracat, ihracı yasak/kayda bağlı mallar, DTSŞ, e-ihracat, fuar tebliğleri, ihracat sayılan satış ve teslimler, devlet yardımları, ham elmas, CITES) |
  Kambiyo |
  Teknik Düzenlemeler-Ürün Güvenliği |
  İç Vergiler (KDV, ÖTV, ÖİV, damga vergisi, BSMV vb.) |
  Uluslararası Anlaşmalar-Kuruluşlar (DTÖ/GATT, TFA, 1/95 OKK, Gümrük Birliği, DGÖ, sözleşmeler) |
  Diğer
- ÖLÇÜLEN_BİLGİ: sorunun ölçtüğü hüküm, ≤25 kelime, kendi cümlenle (soru metnini kopyalama). Örn: "Konşimento damga vergisine tabi; elçilik/kurye mektubu, TIR ve ATA karnesi değil."
- KALIP: şu listeden biri: TANIM KAVRAM KAPSAM KAPSAM_DIŞI DOĞRU YANLIŞ ÖNERMELİ SÜRE ORAN-TUTAR YETKİ BELGE ŞART HESAP BOŞLUK EŞLEŞTİRME MÜEYYİDE OLAY TABİ ZORUNLULUK MATRAH DAYANAK SONUÇ MUAFİYET KISA_AD SINIFLANDIRMA
- KAYNAK_DOSYA: bilginin `metin/` içinde bulunduğu dosya adı (uzantısız; birden çoksa en asli olanı, en çok 2 dosya ";" ile). Grep ile gerçekten DOĞRU CEVABIN dayandığı hükmü bulduğundan emin ol. Bulamazsan `YOK` yaz (bu önemli: kaynakta olmayan alanlardan soru üretilmeyecek).
- RESMI_CEVAP: anahtardaki harf.
- DOGRU_SIK_METNI: resmî cevaba karşılık gelen şıkkın metni (kısaltabilirsin, ≤15 kelime).

## Ek
Dosyanın sonuna değil, ayrı bir `envanter/<YIL>_not.md` dosyasına ≤15 satır yaz: o yılın konu dağılımı (KONU→adet), kalıp dağılımı, KAYNAK_DOSYA=YOK olanların listesi, resmî cevabın kaynakla çeliştiğini düşündüğün sorular (kanıtla).

Bitince yalnız kısa bir rapor ver (konu dağılımı + YOK sayısı). Uzun açıklama yazma.
