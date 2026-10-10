#!/bin/bash
# Kullanım: teslim.sh <birlesik_dir> <hedef_dir>
set -e
S=/tmp/claude-0/-home-user/a109eae8-faba-5ba4-baac-1e5c0fbf53f4/scratchpad
B=$1; H=$2
mkdir -p "$H/veri"
for d in 1 2 3; do
  for f in DENEME-${d}_SORU-KITAPCIGI DENEME-${d}_CEVAP-ANAHTARI-VE-COZUMLER; do
    cp "$B/$f.md" "$H/$f.md"
    python3 $S/scripts/mdfix.py docx "$B/$f.md" "$S/tmpmd/$f.md"
    pandoc "$S/tmpmd/$f.md" -f markdown+pipe_tables+bracketed_spans -t docx --reference-doc=$S/ref_gm.docx -o "$H/$f.docx"
  done
  cp "$B/deneme$d.json" "$H/veri/deneme$d.json"
done
cd "$H" && timeout 600 soffice --headless --convert-to pdf --outdir "$H" DENEME-*.docx >/dev/null 2>&1
ls -la "$H"
