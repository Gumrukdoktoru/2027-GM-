# KARMA TEST ÇAPRAZ KONTROLÜ (son okuma)

Sorular 16 küme hâlinde yazıldı ve küme küme doğrulandı. Şimdi bir karma testin **50 sorusu bir arada**, testteki sırasıyla okunacak. Sen bu testi sınava girecek iyi hazırlanmış bir aday gibi baştan sona çözen, aynı zamanda Bakanlık adına son okumayı yapan uzmansın.

`S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`

## Girdi

- Okunur metin (her sorunun numarası, id'si, konusu, sınıfı, şıkları, cevabı, açıklaması): `$S/karma2/birlesik/KARMA-TEST-<n>.md`
- Makine verisi: `$S/karma2/birlesik/test<n>.json` (birleştirmede şıklar karıştırıldı; kaynak dosyalar `$S/karma2/out/B*.json`).
- Yazım kuralları: `$S/karma/TEST_BRIEF.md` ve `$S/deneme/BRIEF.md` §4. Hesap kural kartları: `/home/user/2027-GM-/00-SORU-YAZARI-ANALIZI-VE-PROMPTLAR/06-SORU-PROMPTU-4_HESAPLAMA.md`.
- Mevzuat metinleri: `$S/kaynak2/` (gm, genelge, diger) ve `$S/kaynak/txt/` (FASIL01–97 vb.).

## Ne arıyorsun

1. **Test içi sızıntı:** Bir sorunun kökü, öncülü ya da (olumsuz kökte doğru olan) bir şıkkı başka bir sorunun cevabını veriyor mu?
2. **Çelişki:** İki soru aynı hükmü farklı söylüyor mu?
3. **Tekrar:** Aynı bilgi iki soruda ölçülüyor mu (farklı kümelerden gelen sorular aynı hükme dokunmuş olabilir)?
4. **Cevap anahtarı:** Her soruyu önce anahtara bakmadan çöz; anahtarla uyuşmayan her soruyu kaynaktan kesinleştir. Hesap sorularında aritmetiği yap.
5. **Biçim ve dil:** Kökte olumsuz yüklem vurgulu mu (`**<u>…</u>**`); açıklamada ya da tuzakta şık harfiyle/konumla atıf ("A şıkkı", "ilk şık") kalmış mı (şıklar karıştırıldı, bu tür atıflar artık yanlış); doğru şık uzunluğuyla ya da kökle kelime ortaklığıyla bariz ele veriyor mu; Bakanlık diline aykırı ifade, yazım hatası, bozuk karakter var mı.
6. **Güncellik:** Şu değişikliklere aykırı bir doğru cevap ya da açıklama var mı: AYM 26.03.2026 (GK 241/1'de yalnız "ikincil düzenlemelere aykırılık" ibaresi iptal), Danıştay 12.08.2026 (GY 94 ve 130/1 iptal), KDVK 21/1-ç (24.07.2025), 2009/15481 sayılı Karar md. 62/1 (07.01.2026 CK, yürürlük 06.02.2026), TIR Tebliği 04.07.2026 değişikliği, 2025/9903 sayılı Kararın 2012/3305'in yerini alması.

## Çıktı

Hiçbir soru dosyasını **değiştirme**. Bulduğun her sorun için bir düzeltme önerisi yaz:

`$S/karma2/capraz/test<n>_yamalar.json` — JSON dizi (sorun yoksa `[]`):

```json
[
  {"id": "K03-07", "no": 12, "sorun": "E şıkkı 31. sorunun cevabını veriyor", "alan": "siklar", "eski": "<değişecek şıkkın tam metni>", "yeni": "…"},
  {"id": "K08-02", "no": 27, "sorun": "tuzakta konum atfı", "alan": "tuzak", "eski": "… ilk şıkka kayar.", "yeni": "… 'X' ifadesine kayar."},
  {"id": "K01-05", "no": 46, "sorun": "anahtar yanlış", "alan": "dogru_icerik", "yeni": "<doğru şıkkın tam metni>"}
]
```

- `alan`: `kok`, `kok_on`, `onculler`, `siklar`, `aciklama`, `tuzak`, `dayanak`, `ortak_veri`, `dogru_icerik` (doğru şıkkın metni; anahtar değişikliği için). Şık ve öncülleri **indeksle değil metinle** belirt: `eski` alanına değiştirilecek öğenin metnini birebir yaz (yamayı uygulayan betik metni arayıp değiştirir).
- `kok`, `aciklama`, `tuzak` için `eski`'ye yalnız değişen parçayı yazman yeterli; parça o alanda birebir geçmeli.
- Bir şıkkı değiştiriyorsan yeni şık aynı kategoride, kesin yanlış (olumsuz kökte kesin doğru) ve kaynakla doğrulanmış olmalı. Gerekirse açıklamayı da yamala ki çözüm metni yeni şıkla uyumlu kalsın.
- Bir soru kurtarılamıyorsa `"alan": "yeniden_yaz"` ile tam yeni soru nesnesini (aynı şema, aynı `id`, `test`, `alan`, `konu`, `alt_tip`, `kaynak_tipi`) `yeni` alanına koy.
- Yalnız gerçek sorunları yaz; üslup tercihi için yama önerme.

Sonra kısa bir özet döndür (en fazla 15 satır): kaç sorun, kaçı anahtar düzeltmesi, kaçı sızıntı/çelişki/tekrar, kaçı biçim; yeniden yazılması önerilen soru varsa id'si.


## İkinci set (Test 4–6) için ek

- n = 4, 5 ya da 6. Testin sorularını ilk setin 150 sorusuyla (`$S/karma/birlesik/KARMA-TEST-{1,2,3}.md`) ve 3 denemeyle de karşılaştır: aynı hükmü aynı kurguyla ölçen soru varsa yama öner (gerekirse `yeniden_yaz`).
