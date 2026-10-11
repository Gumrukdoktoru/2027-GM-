"""Kullanım: python3 cikti_gm.py S  → GK_GM_Deneme{S}_100soru.md (kayıt: soru kitapçığı, cevap anahtarı, gerekçeler, dağılım, hafıza satırları)"""
import json, collections, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
S = int(sys.argv[1]); Q = json.load(open(f'set{S}.json')); L = 'ABCDE'; C = collections.Counter
md = ["# Gümrük Koçu - Ufuk Çetintaş", "", f"## GM Deneme Sınavı {S}", "",
      "| Alan | Değer |", "|---|---|", f"| Set | Gümrük Müşavirliği Deneme {S} |",
      "| Model | 2024 ve 2025 GM sınavları esas (resmî cevap anahtarlarıyla) + 2021–2023 sık sorulanlar |",
      "| Soru sayısı | 100 |", "",
      "# BÖLÜM A — SORU KİTAPÇIĞI", ""]
for q in Q:
    md += [f"**{q['no']}-** " + q['kok'][0], ""]
    md += [l + "  " for l in q['kok'][1:]] + ([""] if len(q['kok']) > 1 else [])
    md += [f"{L[j]}) {o}  " for j, o in enumerate(q['opts'])] + [""]
md += ["## Cevap Anahtarı", ""]
for s0 in range(0, 100, 20):
    part = Q[s0:s0+20]
    md += ["| " + " | ".join(str(q['no']) for q in part) + " |", "|" + "---|" * 20, "| " + " | ".join(q['harf'] for q in part) + " |", ""]
md += ["# BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR", ""]
for q in Q:
    md += [f"*{q['madde']}*", "", f"**{q['no']}-** " + q['kok'][0], ""]
    md += [l + "  " for l in q['kok'][1:]] + ([""] if len(q['kok']) > 1 else [])
    md += [f"{L[j]}) {o}  " for j, o in enumerate(q['opts'])]
    md += ["", f"**Doğru Cevap:** {q['harf']}  ", f"**Gerekçe:** {q['g']}", ""]
md += ["## Dağılım", ""]
def tab(t, cnt, order): return [f"**{t}**", "", "| " + " | ".join(order) + " |", "|" + "---|" * len(order), "| " + " | ".join(str(cnt.get(o, 0)) for o in order) + " |", ""]
md += tab("Doğru cevap harfi", C(q['harf'] for q in Q), list(L))
md += tab("Zorluk", C(q['z'] for q in Q), ["ÇK", "K", "O", "Z", "ÇZ"])
kal = C(q['kalip'] for q in Q); md += tab("Soru kalıbı", kal, [k for k, _ in kal.most_common()])
kon = C(q['konu'] for q in Q); md += ["**Konu**", "", "| Konu | Soru |", "|---|---|"] + [f"| {k} | {v} |" for k, v in kon.most_common()] + [""]
md += ["## HAFIZA GÜNCELLEMESİ", "", "```"]
md += [f"{q['id']} | {q['konu']} | {q['madde']} | {q['cek']} | {q['kalip']} | {q['z']} | {q['harf']} | GM-S{S}" for q in Q]
md += ["```", "", "---", "**Gümrük Koçu - Ufuk Çetintaş**"]
open(f'GK_GM_Deneme{S}_100soru.md', 'w').write("\n".join(md) + "\n"); print('md ok', S)
