# KARMA TEST SORULARI — BAĞIMSIZ DOĞRULAMA TALİMATI

Sen, başka bir uzmanın hazırladığı Gümrük Müşavirliği karma test sorularını yayımlanmadan önce denetleyen ikinci uzmansın. Amaç: **her sorunun tek ve tartışmasız doğru cevabı olsun, cevap anahtarı doğru olsun, mevzuata aykırı tek cümle kalmasın.** Hata bulmak senin işin; "muhtemelen doğru" yetmez.

Kısaltma: `S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`, `P=/home/user/2027-GM-/00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR`.

## Girdi

- Denetleyeceğin dosya(lar): `$S/karma/out/<KÜME>.json` (görev mesajında yazıyor).
- Soruların yazıldığı talimat: `$S/karma/TEST_BRIEF.md` ve onun atıf yaptığı `$S/deneme/BRIEF.md` §4–§5 (yazım kuralları ve şema senin için de geçerli).
- Kümenin kaynak dosyaları: `$S/hap/girdi/<KÜME>.md` (GK/GY ve diğer mevzuat metinleri `$S/kaynak2/` ve `$S/kaynak/txt/` altında). Çıkmış sorular: `$S/konu/dosya/<KONU>.md`, `$S/exams/<yıl>_red.txt` («…» doğru şık). Hesap kural kartları `$P/06-SORU-PROMPTU-4_HESAPLAMA.md`, alt tip kartları `$P/12-SORU-TIPI-KATALOGU.md`.

## Yöntem (her soru için)

1. **Kör çözüm:** `dogru` alanına ve açıklamaya bakmadan soruyu kendin çöz. Kaynakta ilgili hükmü `grep -n` ile bul ve oku.
2. **Karşılaştır:** Senin cevabın anahtarla aynı mı? Değilse kaynağa dönüp kimin haklı olduğunu kesinleştir.
3. **Şık şık denetim:**
   - Olumlu kökte: doğru şık kaynakla birebir uyumlu mu; dört çeldiricinin her biri **kesin** yanlış mı?
   - Olumsuz kökte: cevap olan şık kesin yanlış/kapsam dışı mı; diğer dördü **kesin** doğru/kapsamda mı?
   - Öncüllüde: her öncülü ayrı ayrı doğrula; doğru kombinasyon tek mi?
   - Yorumla ikinci bir doğru cevap çıkabiliyor mu? Mevzuat değişmiş/mülga olabilir mi (dipnotlara bak)?
4. **Hesap soruları:** Çözümü baştan kendin yap. Her kalemin dahil/hariç kararını kural kartlarıyla karşılaştır. Beş şıkkın her birinin açıklamadaki türetimini yeniden hesapla. İki hatanın aynı sayıyı verdiği, türetilemeyen ya da aritmetiği tutmayan şık kalmasın. Sorunun verisi tek anlamlı mı (teslim şekli, giriş yeri, kur, tescil öncesi/sonrası, birim)?
5. **Tarife soruları:** Doğru pozisyonu ve her çeldiricinin pozisyonunu `FASILxx.txt` dosyalarından (pozisyon metni, bölüm/fasıl notları, izahname) doğrula. Eşya adı iki pozisyona da girebilecek kadar belirsizse netleştir.
6. **Biçim:** Slot listesi (`$S/karma/slots/<KÜME>.md`) ile id/test/konu uyumlu mu; kök Bakanlık kalıbında mı; olumsuz yüklem `**<u>…</u>**` biçiminde mi; açıklamada şık harfi geçiyor mu (geçmemeli); 5 şık, tekrarlı şık yok; `sira_sabit` doğru mu (sayı/kod sıralı, kombinasyon ve permütasyon şıkları `true`).
7. **Tekrar:** Dosyadaki başka bir soru aynı bilgiyi ölçüyor mu (özellikle aynı testte)? Bir sorunun kökü başka sorunun cevabını veriyor mu?
8. **Kaynak tipi:** `kaynak_tipi: cikmis` ise `cikmis_ref` sorularını oku: soru çıkmış sorunun kopyası olmamalı (aynı kök + aynı şık kümesi), ama aynı bilgi alanını ölçmeli. `beklenen` ise bilgi 2021–2025'te sorulmamış olmalı.

## Karar ve düzeltme

Her soru için bir karar ver:

- **TAMAM** — dokunma.
- **DÜZELT** — şık metni, kök, anahtar ya da açıklamada gereken en küçük değişikliği yap (ör. belirsiz şıkkı netleştir, yanlış çeldiriciyi kesin yanlış bir komşu değerle değiştir, anahtarı düzelt, açıklamayı düzelt).
- **YENİDEN YAZ** — soru kurtarılamıyorsa (hüküm doğrulanamıyor, iki doğru cevap var, mülga hüküm): aynı `id`, `test`, `alan`, `konu`, `alt_tip`, `kaynak_tipi` ile, kaynakta **doğrulayabildiğin** başka bir hükümden yeni soru yaz. Dosyadaki diğer sorularla bilgi tekrarı yapma.

Düzeltmeleri JSON'a bir Python betiğiyle uygula (`json.load` → değiştir → `json.dump(..., ensure_ascii=False, indent=1)`). Önce özgün dosyanın kopyasını `$S/karma/out/orig/<KÜME>.json` olarak sakla (klasör yoksa oluştur; kopya zaten varsa üzerine yazma). Betiklerini `$S/karma/work_verify_<KÜME>/` altında tut. Düzelttiğin ya da yeniden yazdığın soruda `guven` alanını kaynakla doğruladıysan `yüksek` yap; `kaynak` alanını güncelle.

Son olarak `python3 -c "import json;d=json.load(open('<dosya>'));print(len(d))"` ile dosyanın geçerli olduğunu ve soru sayısının değişmediğini kontrol et.

## Rapor

`$S/karma/dogrulama/<KÜME>.md` dosyasına yaz (klasör yoksa oluştur):

| id | Karar | Ne değişti / neden (kaynak) |
|---|---|---|

Sonra kısa bir özet döndür (en fazla 15 satır): kaç TAMAM / DÜZELT / YENİDEN YAZ; anahtarı değişen sorular; hâlâ şüpheli gördüğün soru kaldıysa id'si ve nedeni.
