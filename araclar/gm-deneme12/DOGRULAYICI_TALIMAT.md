# Çekişmeli Doğrulama Talimatı (GM Deneme 1–2)

Klasör: /home/claude/2027-gm-/araclar/gm-deneme12
HİÇBİR DOSYAYI DEĞİŞTİRME; yalnızca rapor yaz. Git işlemi yapma.

- `set1.json`, `set2.json`: 100'er soru. Alanlar: no, kok (liste), opts (A–E), harf (doğru), d (doğru şık metni), c (çeldiriciler), g (gerekçe; sonu "Bu nedenle doğru cevap X seçeneğidir. (MD …)"), madde, cek, kanit ("dosya | alıntı"), cikmis, konu, batch, bidx (sorunun `batch_<batch>.py` içindeki sırası).
- Kaynak: `metin/` (tek bilgi kaynağı; grep ile ara). Çıkmış GM sınavları: `sinav/<YIL>_layout.txt`. Resmî cevaplar ve bilgi alanları: `cikmis_envanter.tsv`; resmî cevabın güncel kaynakla çeliştiği sorular `envanter/<YIL>_not.md`.
- Kurallar: `/home/claude/2027-ye-haz-rl-k/promptlar/prompt-3-nihai-soru-hazirlama-kurallari.md` ve `/home/claude/2027-ye-haz-rl-k/CLAUDE.md` (Karar dayanaklı kök kuralı).

Sana verilen aralıktaki HER soru için:
1. İşaretli doğru şık kaynağa göre KESİN doğru mu? Hükmü kaynakta bul, çevresini oku (istisnalar, dipnotlu değişiklikler, "mülga" ibareleri, sonradan gelen değişik metinler). Hesap ve tarih sorularını Python ile yeniden yap.
2. Başka bir şık da savunulabilir mi (ÇİFT DOĞRU)? Olumsuz kökte (değildir/yanlıştır/yer almaz) yalnız bir şık mı uyuyor? Önermelide her öncülü ayrı ayrı değerlendir.
3. Gerekçe ve içindeki harf doğru şıkla uyumlu mu? Gerekçede kaynakta olmayan bilgi var mı?
4. Kaynakta olmayan rakam/süre/makam/bilgi (doğru şıkta, çeldiricinin yanlışlığında, kökteki olay verisinde, gerekçede) var mı? Eski-yeni kurum adı rakip şık olmuş mu?
5. Kök kuralları: madde/fıkra/bent numarası kökte ve şıkta yok; Karar dayanaklı kök "4458 sayılı …" ile başlamıyor; kök mevzuat adı + hükmün konusu içeriyor; yapay niteleme yok; marka dışı kurum adı (ör. başka eğitim kurumu) yok.
6. `cikmis` alanındaki çıkmış soruyu `sinav/<YIL>_layout.txt` içinde bul: metin/şık/kurgu KOPYASI var mı (aynı bilgi alanı serbest)?
7. Tarife sorularında: doğru pozisyonun dayanağı (bölüm/fasıl notu, pozisyon metni, izahname, genelge, sınıflandırma kararı) kaynakta açık mı; çeldirici pozisyonların yanlışlığı kesin mi?
8. Özel riskler (aralığında varsa kontrol et):
   - GK 241/1 usulsüzlük cezası yanında AYM 26.03.2026 kararına atıf var; 241/1'in ikincil düzenleme kapsamına veya TL tutarına dayanan soru olmamalı.
   - Posta/hızlı kargo: 2009/15481 Kararının 2026 değişikliği; soru güncel metne göre mi?
   - KDV matrahı: KDVK 21/ç (teminata bağlanan ÖTV (I)) güncel hükmü; resmî 2025/15 cevabı eski hükme göre.
   - Ders notu niteliğindeki kaynaklara (Hesaplama*, HESAPLAMA FORMÜLLERİ, Tarife ve Hesaplama 202601, SAİR MEVZUAT KİTABI, STA ve KÜMÜLASYONLAR) dayanan sorularda bilgi gerçekten kaynakta var mı, birincil mevzuatla (metin/ içinde varsa) çelişiyor mu?
   - Her yıl yeniden değerlenen TL tutarına dayanan soru var mı (tutar kökte verilmemişse sorun)?
9. Aynı sette iki sorunun aynı hükmü/çekirdeği ölçüp ölçmediğine bak (kendi aralığın içinde; aralık dışı şüpheyi de not et).

Çıktı: kısa rapor. Yalnız SORUNLU sorular: `set/no [batch_X.py #bidx]`, tür (YANLIŞ CEVAP / ÇİFT DOĞRU / KAYNAK DIŞI / GÜNCEL DEĞİL / KOPYA / GEREKÇE UYUMSUZ / KÖK KURALI / BELİRSİZ / TEKRAR), kanıt (dosya + birebir alıntı), SOMUT düzeltme (hangi şık/öncül/kök/gerekçe metni nasıl olmalı; doğru cevap değişiyorsa yeni doğru şık metni). Sorunsuzları aralıkla say. Şüpheleri "ŞÜPHE" diye ayrı ver. Gereksiz uzun yazma.
