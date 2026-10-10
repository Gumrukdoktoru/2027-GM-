# Üretim kayıtları

Denemelerin nasıl üretildiğinin kaydı. Dosyalardaki `/tmp/.../scratchpad` yolları üretim sırasında kullanılan çalışma klasörüdür; buraya kopyalanmadı.

| Dosya / klasör | İçerik |
|---|---|
| `plan_gm_sair.csv` | GM ve Sair sorularının deneme × konu × alt tip planı |
| `slotlar/` | 12 konu kümesinin slot listeleri (tarife ve hesap dahil) |
| `BRIEF.md` | Soru üreten ajanların ortak talimatı (kaynaklar, yazım kuralları, JSON şeması, öz-denetim) |
| `VERIFY.md` | Bağımsız doğrulama talimatı |
| `dogrulama/` | Küme küme doğrulama raporları (her soru için TAMAM / DÜZELT / YENİDEN YAZ ve gerekçesi) |
| `CAPRAZ.md`, `capraz/` | Deneme bazında çapraz kontrol talimatı ve uygulanan yamalar |
| `betikler/` | Plan (`blueprint.py`, `slots.py`), birleştirme (`birlestir.py`), yama (`yama_uygula.py`), denetim (`lint_deneme.py`) ve teslim (`teslim.sh`) betikleri |

Yeni deneme üretmek için aynı akış kullanılabilir: plan → küme üretimi (BRIEF) → doğrulama (VERIFY) → birleştirme → çapraz kontrol (CAPRAZ) → yama → teslim.
