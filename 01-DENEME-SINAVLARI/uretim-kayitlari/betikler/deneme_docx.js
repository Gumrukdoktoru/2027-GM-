// Deneme sınavı Word belgesi (örnek GMY Deneme düzeni)
// Kullanım: node deneme_docx.js <girdi.json> <cikti.docx> <tam|kitapcik>
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, BorderStyle, Header, Footer, PageNumber, HeadingLevel, LevelFormat,
} = require('docx');

const [, , IN, OUT, MODE] = process.argv;
const D = JSON.parse(fs.readFileSync(IN, 'utf8'));
const NAVY = '1B3A5C', GOLD = 'B8860B', CREAM = 'F4F1E8', GRAY = '555555';
const L = 'ABCDE';
const CONTENT_W = 11906 - 2 * 1134; // A4, 2 cm kenar boşluğu

// ---- yardımcılar -------------------------------------------------------
function runs(text, base = {}) {
  // **x**, <u>x</u> ve ikisinin birleşimini TextRun'lara çevirir
  const out = [];
  const re = /(\*\*<u>[\s\S]*?<\/u>\*\*|<u>\*\*[\s\S]*?\*\*<\/u>|\*\*[\s\S]*?\*\*|<u>[\s\S]*?<\/u>)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    const bold = t.includes('**'), und = t.includes('<u>');
    const inner = t.replace(/\*\*/g, '').replace(/<\/?u>/g, '');
    out.push(new TextRun({ text: inner, ...base, bold: bold || base.bold, underline: und ? {} : undefined }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}
const lines = (t) => (t || '').split('\n').map((s) => s.trim()).filter(Boolean);
const P = (children, opts = {}) => new Paragraph({ children, ...opts });
const sp = (before, after) => ({ spacing: { before, after } });
const ROMA = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'];

function heading1(text, pageBreak = false) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1, pageBreakBefore: pageBreak,
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 4 } },
    spacing: { before: 360, after: 180 },
    children: [new TextRun({ text })],
  });
}
function heading2(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 120 }, keepNext: true,
    border: { left: { style: BorderStyle.SINGLE, size: 36, color: GOLD, space: 8 } }, children: [new TextRun({ text })] });
}
const border = { style: BorderStyle.SINGLE, size: 4, color: '000000' };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(text, w, opts = {}) {
  return new TableCell({
    borders, width: { size: w, type: WidthType.DXA },
    shading: opts.fill ? { fill: opts.fill, type: ShadingType.CLEAR, color: 'auto' } : undefined,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [new Paragraph({
      alignment: opts.center ? AlignmentType.CENTER : AlignmentType.LEFT, spacing: { after: 40 },
      children: runs(String(text), { bold: !!opts.bold, color: opts.color, size: opts.size || 20 }),
    })],
  });
}
function kvTable(rows) {
  const w1 = Math.round(CONTENT_W * 0.3), w2 = CONTENT_W - w1;
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [w1, w2],
    rows: [
      new TableRow({ tableHeader: true, children: [cell('Alan', w1, { bold: true, fill: NAVY, color: 'FFFFFF' }), cell('Değer', w2, { bold: true, fill: NAVY, color: 'FFFFFF' })] }),
      ...rows.map(([a, b], i) => new TableRow({ children: [cell(a, w1, { fill: i % 2 ? CREAM : undefined }), cell(b, w2, { fill: i % 2 ? CREAM : undefined })] })),
    ],
  });
}
function gridTable(headers, values) {
  const n = headers.length, w = Math.floor(CONTENT_W / n), widths = Array(n).fill(w);
  widths[n - 1] = CONTENT_W - w * (n - 1);
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, children: headers.map((h, i) => cell(h, widths[i], { bold: true, fill: NAVY, color: 'FFFFFF' })) }),
      new TableRow({ children: values.map((v, i) => cell(v, widths[i])) }),
    ],
  });
}
function dataTable(rows) {
  // sütun genişliği içerik uzunluğuyla orantılı (en az 600 DXA)
  const n = rows[0].length;
  const wt = Array.from({ length: n }, (_, j) => Math.min(60, Math.max(4, ...rows.map((r) => String(r[j] || '').length))));
  const tot = wt.reduce((a, b) => a + b, 0);
  // en uzun kelime bölünmesin
  const minW = Array.from({ length: n }, (_, j) => Math.max(600, 260 + 120 * Math.max(...rows.map((r) => Math.max(...String(r[j] || '').split(/\s+/).map((x) => x.length))))));
  const widths = wt.map((w, j) => Math.max(minW[j], Math.floor((CONTENT_W * w) / tot)));
  const over = widths.reduce((a, b) => a + b, 0) - CONTENT_W;
  const big = widths.indexOf(Math.max(...widths));
  widths[big] -= over;
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({ children: r.map((c, j) => cell(c, widths[j], { bold: i === 0, fill: i === 0 ? CREAM : undefined })) })),
  });
}

// ---- soru --------------------------------------------------------------
function question(q, withAnswer) {
  const out = [];
  let numbered = false;
  const numRun = () => { numbered = true; return new TextRun({ text: `${q.no}- `, bold: true }); };
  if (q._ortak_baslik) {
    out.push(P([new TextRun({ text: q._ortak_baslik, bold: true })], { keepNext: true, ...sp(200, 80) }));
    for (const l of lines(q.ortak_veri)) out.push(P(runs(l), { keepNext: true, ...sp(0, 40) }));
  }
  const kokOn = lines(q.kok_on);
  kokOn.forEach((l, i) => out.push(P([...(numbered ? [] : [numRun()]), ...runs(l)], { keepNext: true, ...sp(i === 0 && !q._ortak_baslik ? 200 : 40, 60) })));
  const hasOnc = (q.onculler || []).length > 0;
  (q.onculler || []).forEach((o, i) => {
    const first = !numbered;
    out.push(P([...(first ? [numRun()] : []), new TextRun({ text: `${ROMA[i]}. ` }), ...runs(o)],
      { keepNext: true, indent: first ? { left: 360, hanging: 360 } : { left: 360 }, ...sp(first ? 200 : 0, 40) }));
  });
  if (q.tablo && q.tablo.length) {
    if (!numbered) out.push(P([numRun()], { keepNext: true, ...sp(200, 60) }));
    out.push(dataTable(q.tablo));
  }
  const kok = lines(q.kok);
  kok.forEach((l, i) => {
    const first = !numbered;
    out.push(P([...(first ? [numRun()] : []), ...runs(l)],
      first ? { keepNext: true, ...sp(200, 80) } : hasOnc ? { keepNext: true, indent: { left: 360 }, ...sp(0, 40) } : { keepNext: true, ...sp(60, 80) }));
  });
  q.siklar.forEach((s, i) => out.push(P([new TextRun({ text: `${L[i]}) ` }), ...runs(s)],
    { keepNext: withAnswer || i < 4, indent: { left: 360, hanging: 360 }, ...sp(0, 40) })));
  if (withAnswer) {
    const c = L[q.dogru];
    out.push(P([new TextRun({ text: 'Doğru Cevap: ', bold: true }), new TextRun({ text: c, bold: true, color: NAVY })], { keepNext: true, ...sp(80, 40) }));
    // örnekteki gibi tek paragraf: açıklama + tuzak + kapanış cümlesi + (MD dayanak)
    const ger = lines(q.aciklama).map((g) => (/[.!?:;)]$/.test(g) ? g : g + '.')).join(' ');
    const tuzak = (q.tuzak || '').trim();
    const kapanis = `${tuzak ? ' ' + tuzak : ''} Bu nedenle doğru cevap ${c} seçeneğidir.${q.dayanak ? ' (MD ' + q.dayanak.trim().replace(/\.$/, '') + ')' : ''}`;
    out.push(P([new TextRun({ text: 'Gerekçe: ', bold: true }), ...runs(ger + kapanis)], sp(0, 120)));
  }
  return out;
}

// ---- belge -------------------------------------------------------------
const M = D.meta;
const body = [];
// Kapak
body.push(P([], sp(2400, 0)));
body.push(P([new TextRun({ text: M.ust_baslik, bold: true, color: GOLD, size: 28 })], { alignment: AlignmentType.CENTER }));
body.push(P([], sp(400, 0)));
body.push(P([new TextRun({ text: M.baslik, bold: true, color: NAVY, size: 56 })], { alignment: AlignmentType.CENTER }));
body.push(P([new TextRun({ text: M.alt_baslik, color: NAVY, size: 26 })], { alignment: AlignmentType.CENTER, ...sp(200, 0),
  border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GOLD, space: 8 } } }));
body.push(P([], sp(300, 0)));
body.push(P([new TextRun({ text: M.hazirlik, bold: true, size: 26 })], { alignment: AlignmentType.CENTER }));
body.push(P([], sp(3600, 0)));
body.push(P([new TextRun({ text: MODE === 'kitapcik' ? 'SORU KİTAPÇIĞI' : 'SORU KİTAPÇIĞI · CEVAP ANAHTARI · GEREKÇELİ ÇÖZÜMLER', bold: true, color: NAVY, size: 24 })], { alignment: AlignmentType.CENTER }));
// Sınav bilgileri
body.push(heading1('Sınav Bilgileri', true));
body.push(kvTable(M.bilgiler));
for (const n of M.notlar) body.push(P(runs(n), sp(160, 0)));
// Bölüm A
body.push(heading1('BÖLÜM A — SORU KİTAPÇIĞI', true));
let blok = null;
for (const q of D.sorular) {
  if (q._blok !== blok) { blok = q._blok; body.push(heading2(blok)); }
  body.push(...question(q, false));
}
if (MODE === 'tam') {
  // Cevap anahtarı
  body.push(heading1('Cevap Anahtarı', true));
  for (let k = 0; k < 5; k++) {
    const sl = D.sorular.slice(k * 20, k * 20 + 20);
    body.push(gridTable(sl.map((q) => String(q.no)), sl.map((q) => L[q.dogru])));
    body.push(P([], sp(0, 160)));
  }
  // Bölüm B
  body.push(heading1('BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR', true));
  for (const q of D.sorular) {
    body.push(P([new TextRun({ text: q._etiket, italics: true, color: GOLD, size: 20 })], { keepNext: true, ...sp(280, 40) }));
    body.push(...question(q, true));
  }
  // Dağılım
  body.push(heading1('Dağılım', true));
  for (const [ad, hdr, val] of D.dagilim) {
    body.push(heading2(ad));
    // çok sütunlu kalıp tablosu parçalara bölünür (sütun sayısı en uzun başlığa göre)
    const per = Math.max(1, Math.min(10, Math.floor(CONTENT_W / (300 + 130 * Math.max(...hdr.map((h) => h.length))))));
    for (let k = 0; k < hdr.length; k += per) {
      if (k) body.push(P([], sp(0, 120)));
      body.push(gridTable(hdr.slice(k, k + per), val.slice(k, k + per)));
    }
  }
  if (D.konu_tablo) {
    body.push(heading2('Konu'));
    const w1 = Math.floor(CONTENT_W * 0.5), w2 = CONTENT_W - w1;
    body.push(new Table({
      width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [w1, w2],
      rows: [new TableRow({ tableHeader: true, children: [cell('Konu', w1, { bold: true, fill: NAVY, color: 'FFFFFF' }), cell('Soru', w2, { bold: true, fill: NAVY, color: 'FFFFFF' })] }),
        ...D.konu_tablo.map(([a, b], i) => new TableRow({ children: [cell(a, w1, { fill: i % 2 ? CREAM : undefined }), cell(b, w2, { fill: i % 2 ? CREAM : undefined })] }))],
    }));
  }
  // Üretim notu
  body.push(heading1('Üretim Notu', true));
  for (const n of D.uretim_notu) body.push(new Paragraph({ numbering: { reference: 'mad', level: 0 }, ...sp(0, 60), children: runs(n) }));
  // Hafıza
  if (D.hafiza && D.hafiza.length) {
    body.push(heading1('HAFIZA GÜNCELLEMESİ', true));
    for (const h of D.hafiza) body.push(P([new TextRun({ text: h, font: 'Courier New', size: 14 })], sp(0, 10)));
    body.push(P([new TextRun({ text: `Toplam: ${D.hafiza.length} satır`, font: 'Courier New', size: 14, bold: true })], sp(80, 0)));
  }
}

const doc = new Document({
  creator: 'GM Deneme', title: M.baslik,
  styles: {
    default: { document: { run: { font: 'Arial', size: 22 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 32, bold: true, color: NAVY, font: 'Arial' }, paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 26, bold: true, color: NAVY, font: 'Arial' }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [{ reference: 'mad', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, right: 1134, bottom: 1134, left: 1134 } }, titlePage: true },
    headers: {
      default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GOLD, space: 2 } },
        children: [new TextRun({ text: M.ust_bilgi, bold: true, color: NAVY, size: 18 })] })] }),
      first: new Header({ children: [new Paragraph({ children: [] })] }),
    },
    footers: {
      default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
        new TextRun({ text: `${M.alt_bilgi} | Sayfa `, color: GRAY, size: 16 }), new TextRun({ children: [PageNumber.CURRENT], color: GRAY, size: 16 }),
        new TextRun({ text: ' / ', color: GRAY, size: 16 }), new TextRun({ children: [PageNumber.TOTAL_PAGES], color: GRAY, size: 16 })] })] }),
      first: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
        new TextRun({ text: `${M.alt_bilgi} | Sayfa `, color: GRAY, size: 16 }), new TextRun({ children: [PageNumber.CURRENT], color: GRAY, size: 16 }),
        new TextRun({ text: ' / ', color: GRAY, size: 16 }), new TextRun({ children: [PageNumber.TOTAL_PAGES], color: GRAY, size: 16 })] })] }),
    },
    children: body,
  }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync(OUT, b); console.log('yazıldı', OUT); });
