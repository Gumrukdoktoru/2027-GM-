# DENEME ÇAPRAZ KONTROLÜ (son okuma)

Sorular kümeler hâlinde üretildi ve küme küme doğrulandı. Şimdi bir denemenin **100 sorusu bir arada**, gerçek sınav sırasıyla okunacak. Sen bu denemeyi sınava girecek iyi hazırlanmış bir aday gibi baştan sona çözen, aynı zamanda Bakanlık adına son okumayı yapan uzmansın.

`S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad`

## Girdi

- Kitapçık: `$S/deneme/birlesik/DENEME-<n>_SORU-KITAPCIGI.md`
- Cevap anahtarı ve çözümler: `$S/deneme/birlesik/DENEME-<n>_CEVAP-ANAHTARI-VE-COZUMLER.md`
- Makine verisi (her sorunun `id`, `no`, `cevap` alanlarıyla): `$S/deneme/birlesik/deneme<n>.json`
- Kaynaklar ve yazım kuralları: `$S/deneme/BRIEF.md` (Bölüm 2 kaynak tablosu, Bölüm 4 kurallar).

## Ne arıyorsun

1. **Deneme içi sızıntı:** Bir sorunun kökü, öncülü ya da (olumsuz kökte doğru olan) bir şıkkı başka bir sorunun cevabını veriyor mu? Ör. bir O2 sorusunun doğru çeldiricisi, başka bir sorunun aradığı bilginin ta kendisi.
2. **Çelişki:** İki soru aynı hükmü farklı söylüyor mu (biri "30 gün", öbürü "60 gün" diyor ve ikisi de doğru sunuluyor)?
3. **Tekrar:** Aynı bilgi iki soruda ölçülüyor mu?
4. **Cevap anahtarı:** Her soruyu önce anahtara bakmadan çöz; anahtarla uyuşmayan her soruyu kaynaktan kesinleştir. Hesap sorularında aritmetiği yap.
5. **Biçim ve dil:** Kökte olumsuz yüklem vurgulu mu; şık harfiyle atıf ("A şıkkı", "ilk şık") açıklamada ya da tuzakta kalmış mı (şıklar karıştırıldı, bu tür atıflar artık yanlış); doğru şık uzunluğuyla ya da kökle kelime ortaklığıyla bariz ele veriyor mu; Bakanlık diline aykırı ifade, yazım hatası, bozuk karakter var mı; ortak veri setli sorularda başlık doğru numaraları gösteriyor mu.
6. **Deneme bütünlüğü:** Konu ve tip dağılımında göze batan yığılma (ör. aynı tebliğden art arda 5 soru) var mı.

## Çıktı

Hiçbir dosyayı **değiştirme**. Bulduğun her sorun için bir düzeltme önerisi yaz:

`$S/deneme/capraz/deneme<n>_yamalar.json` — JSON dizi:

```json
[
  {"id": "GM-B1-04", "no": 37, "sorun": "E şıkkı 41. sorunun cevabını veriyor", "alan": "siklar", "indeks": 4, "eski": "…", "yeni": "…"},
  {"id": "SR-A-13", "no": 8, "sorun": "tuzakta konum atfı", "alan": "tuzak", "eski": "… ilk şıkka kayar.", "yeni": "… 'X' ifadesine kayar."},
  {"id": "HS-A-03", "no": 18, "sorun": "anahtar yanlış", "alan": "dogru_icerik", "yeni": "<doğru şıkkın tam metni>"}
]
```

- `alan`: `kok`, `kok_on`, `onculler` (+`indeks`), `siklar` (+`indeks`), `aciklama`, `tuzak`, `dayanak`, `dogru_icerik` (doğru şıkkın metni; anahtar değişikliği için).
- `eski` alanına değiştirilecek metni birebir yaz (yamayı uygulayan betik metni arayıp değiştirecek); `kok`, `aciklama`, `tuzak` için yalnız değişen parçayı yazman yeterli.
- Bir şıkkı değiştiriyorsan yeni şık aynı kategoride, kesin yanlış (olumsuz kökte kesin doğru) ve kaynakla doğrulanmış olmalı.
- Gerekirse açıklamayı da yamala ki çözüm metni yeni şıkla uyumlu kalsın.
- Bir soru kurtarılamıyorsa `"alan": "yeniden_yaz"` ile tam yeni soru nesnesini (`BRIEF.md` şemasıyla, aynı `id`, `deneme`, `alan`, `konu`, `alt_tip`) `yeni` alanına koy.

Sonra kısa bir özet döndür (en fazla 15 satır): kaç sorun, kaçı anahtar düzeltmesi, kaçı sızıntı/çelişki, kaçı biçim; yeniden yazılması önerilen soru varsa id'si.
