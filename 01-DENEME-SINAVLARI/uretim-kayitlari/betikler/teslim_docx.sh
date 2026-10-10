#!/bin/bash
# Örnek düzeninde tam deneme + soru kitapçığı üretir ve PDF'e çevirir.
# Kullanım: bash teslim_docx.sh <scratchpad> <hedef_klasör>
set -e
S="$1"; R="$2"
python3 "$S/scripts/deneme_hazirla.py" "$S/deneme/birlesik" "$S/deneme/derece" "$S/deneme/docx"
for d in 1 2 3; do
  node "$S/scripts/deneme_docx.js" "$S/deneme/docx/deneme${d}_docx.json" "$R/DENEME-${d}.docx" tam
  node "$S/scripts/deneme_docx.js" "$S/deneme/docx/deneme${d}_docx.json" "$R/DENEME-${d}_SORU-KITAPCIGI.docx" kitapcik
done
cd "$R" && soffice --headless --convert-to pdf DENEME-?.docx DENEME-?_SORU-KITAPCIGI.docx >/dev/null 2>&1
for f in DENEME-?.pdf DENEME-?_SORU-KITAPCIGI.pdf; do echo "$f $(pdfinfo "$f" | awk '/Pages/{print $2}') sayfa"; done
