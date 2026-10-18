# Üretim kayıtları

Konu sınıfları, hap dokümanları ve karma testlerin nasıl üretildiğinin kaydı. Betiklerdeki `$S` yolları üretim sırasında kullanılan çalışma klasörünü gösterir.

| Dosya / klasör | İçerik |
|---|---|
| `betikler/taksonomi.py`, `siniflar.py`, `dosya_yap.py` | 500 sorunun 76 konuya eşlenmesi, sınıf ve eğilim hesabı, konu dosyalarının (soru metni + resmî anahtar + mevzuat) hazırlanması |
| `kumeler.json`, `betikler/kumeler.py` | 76 konunun 14 çalışma kümesine (K01–K14) dağılımı ve konu başına hap/soru–cevap hedefleri |
| `talimatlar/CIKAN_BRIEF.md` | Çıkan sorulardan hap yazım talimatı (hap satırı biçimi, ★ ve ◇ kuralları) |
| `talimatlar/SORULMAYAN_BRIEF.md` | Alt konu işaretleme (SORULDU/KISMEN/SORULMADI), soru–cevap ve beklenen hap talimatı; her kayıt kaynak metinden birebir kanıt kesitiyle |
| `betikler/hap_kontrol.py` | Çıkan haplarda her sorunun geçtiğini, soru–cevap ve beklenen kanıtlarının kaynakta birebir bulunduğunu denetler |
| `cikar.json` | Güncelliğini yitirdiği için elle çıkarılan kayıtlar |
| `betikler/hap_belgeler.py`, `hap_docx.js`, `md2blok.py` | Doküman bloklarının kurulması ve Word çıktısı |
| `talimatlar/TEST_BRIEF.md`, `slotlar/` | Karma test yazım talimatı ve 150 sorunun konu × sınıf × test slotları |
| `talimatlar/KARMA_VERIFY.md`, `dogrulama/` | Küme bazında bağımsız doğrulama talimatı ve 14 rapor (her soru için TAMAM / DÜZELT / YENİDEN YAZ) |
| `talimatlar/KARMA_CAPRAZ.md`, `capraz/` | Test bazında son okuma talimatı ve uygulanan yamalar |
| `betikler/karma_birlestir.py`, `karma_hazirla.py`, `karma_md.py`, `yama_uygula.py`, `deneme_docx.js` | Testlerin birleştirilmesi (blok sırası, harf dengesi), yamaların uygulanması ve Word çıktısı |
| `betikler/sayi_ek_kontrol.py` | Sayılara gelen eklerin (18'i, 16'sı, 30'da…) ses uyumu denetimi |
