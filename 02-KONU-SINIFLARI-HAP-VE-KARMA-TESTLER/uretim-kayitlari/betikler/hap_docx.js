// Hap / soru-cevap / katalog dokümanları için genel Word üreticisi (deneme dokümanlarıyla aynı görünüm)
// Kullanım: node hap_docx.js <girdi.json> <cikti.docx>
// Girdi: { meta: {...}, bloklar: [ {t: 'kapak'|'h1'|'h2'|'h3'|'p'|'kutu'|'madde'|'tablo'|'etiket'|'sc'|'sayfa'|'mono'|'ornek', ...} ] }
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, BorderStyle, Header, Footer, PageNumber, HeadingLevel, LevelFormat, PageBreak,
} = require('docx');

const [, , IN, OUT] = process.argv;
const D = JSON.parse(fs.readFileSync(IN, 'utf8'));
const M = D.meta;
const NAVY = '1B3A5C', GOLD = 'B8860B', CREAM = 'F4F1E8', GRAY = '555555', BOX = 'FFF8E7';
const CONTENT_W = 11906 - 2 * 1134;

// **kalın**, *italik*, <u>altı çizili</u>
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*<u>[\s\S]*?<\/u>\*\*|\*\*[\s\S]*?\*\*|<u>[\s\S]*?<\/u>|(?<![\w*])\*(?!\s)[^*\n]+?\*(?![\w*]))/g;
  let last = 0, m;
  text = String(text);
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ text: t.replace(/\*\*/g, '').replace(/<\/?u>/g, ''), ...base, bold: true, underline: t.includes('<u>') ? {} : undefined }));
    else if (t.startsWith('<u>')) out.push(new TextRun({ text: t.replace(/<\/?u>/g, ''), ...base, underline: {} }));
    else out.push(new TextRun({ text: t.slice(1, -1), ...base, italics: true }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}
const P = (children, opts = {}) => new Paragraph({ children, ...opts });
const border = { style: BorderStyle.SINGLE, size: 4, color: '000000' };
const borders = { top: border, bottom: border, left: border, right: border };
function cell(text, w, o = {}) {
  return new TableCell({
    borders: o.borders || borders, width: { size: w, type: WidthType.DXA },
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: 'auto' } : undefined,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: (Array.isArray(text) ? text : [text]).map((tx) => new Paragraph({ spacing: { after: 40 }, children: runs(tx, { bold: o.bold, color: o.color, size: o.size || 20 }) })),
  });
}
function widthsFrom(spec, n) {
  if (!spec) { const w = Math.floor(CONTENT_W / n); const a = Array(n).fill(w); a[n - 1] = CONTENT_W - w * (n - 1); return a; }
  const tot = spec.reduce((a, b) => a + b, 0); const a = spec.map((x) => Math.floor((CONTENT_W * x) / tot));
  a[a.length - 1] += CONTENT_W - a.reduce((x, y) => x + y, 0); return a;
}
function tablo(b) {
  const n = b.basliklar.length, w = widthsFrom(b.genislik, n);
  const rows = [new TableRow({ tableHeader: true, children: b.basliklar.map((h, i) => cell(h, w[i], { bold: true, fill: NAVY, color: 'FFFFFF' })) })];
  b.satirlar.forEach((r, j) => rows.push(new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, w[i], { fill: b.serit !== false && j % 2 ? CREAM : undefined, bold: b.kalin_ilk && i === 0 })) })));
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: w, rows });
}
function kutu(paras) {
  const gb = { style: BorderStyle.SINGLE, size: 12, color: GOLD };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({ children: [new TableCell({
      borders: { top: gb, bottom: gb, left: gb, right: gb }, width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { fill: BOX, type: ShadingType.CLEAR, color: 'auto' }, margins: { top: 80, bottom: 80, left: 120, right: 120 },
      children: paras.map((p) => new Paragraph({ spacing: { after: 60 }, children: runs(p, { size: 21 }) })),
    })] })],
  });
}
function ornek(lines) { // gerçek sınav örneği: gri zeminli, sol çizgili kutu
  const lb = { style: BorderStyle.SINGLE, size: 18, color: NAVY }, nb = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
    rows: [new TableRow({ children: [new TableCell({
      borders: { top: nb, bottom: nb, right: nb, left: lb }, width: { size: CONTENT_W, type: WidthType.DXA },
      shading: { fill: 'F2F4F7', type: ShadingType.CLEAR, color: 'auto' }, margins: { top: 60, bottom: 60, left: 160, right: 120 },
      children: lines.map((p) => new Paragraph({ spacing: { after: 30 }, children: runs(p, { size: 19 }) })),
    })] })],
  });
}
const body = [];
for (const b of D.bloklar) {
  switch (b.t) {
    case 'kapak':
      body.push(P([], { spacing: { before: 2400 } }));
      body.push(P([new TextRun({ text: b.ust, bold: true, color: GOLD, size: 28 })], { alignment: AlignmentType.CENTER }));
      body.push(P([], { spacing: { before: 400 } }));
      body.push(P([new TextRun({ text: b.baslik, bold: true, color: NAVY, size: b.boyut || 56 })], { alignment: AlignmentType.CENTER }));
      body.push(P([new TextRun({ text: b.alt, color: NAVY, size: 26 })], { alignment: AlignmentType.CENTER, spacing: { before: 200 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: GOLD, space: 8 } } }));
      body.push(P([], { spacing: { before: 300 } }));
      body.push(P([new TextRun({ text: b.hazirlik, bold: true, size: 26 })], { alignment: AlignmentType.CENTER }));
      if (b.not) { body.push(P([], { spacing: { before: 3600 } })); body.push(P([new TextRun({ text: b.not, bold: true, color: NAVY, size: 24 })], { alignment: AlignmentType.CENTER })); }
      break;
    case 'sayfa': body.push(P([new PageBreak()])); break;
    case 'h1': body.push(new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: !!b.yeni_sayfa, keepNext: true,
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: GOLD, space: 4 } }, spacing: { before: 360, after: 180 }, children: [new TextRun({ text: b.metin })] })); break;
    case 'h2': body.push(new Paragraph({ heading: HeadingLevel.HEADING_2, keepNext: true,
      border: { left: { style: BorderStyle.SINGLE, size: 36, color: GOLD, space: 8 } }, spacing: { before: 240, after: 120 }, children: [new TextRun({ text: b.metin })] })); break;
    case 'h3': body.push(new Paragraph({ heading: HeadingLevel.HEADING_3, keepNext: true, spacing: { before: 200, after: 80 }, children: [new TextRun({ text: b.metin })] })); break;
    case 'p': body.push(P(runs(b.metin), { spacing: { after: 120, line: 276 }, keepNext: !!b.keepNext })); break;
    case 'etiket': body.push(P([new TextRun({ text: b.metin, italics: true, color: GOLD, size: 19 })], { spacing: { after: 160 }, keepNext: true })); break;
    case 'kutu': body.push(kutu(b.paragraflar)); body.push(P([], { spacing: { after: 100 } })); break;
    case 'ornek': body.push(ornek(b.satirlar)); body.push(P([], { spacing: { after: 80 } })); break;
    case 'madde': for (const m of b.maddeler) body.push(new Paragraph({ numbering: { reference: 'mad', level: 0 }, spacing: { after: 60 }, children: runs(m) })); break;
    case 'tablo': body.push(tablo(b)); body.push(P([], { spacing: { after: 120, line: 276 } })); break;
    case 'dipnot': body.push(P(runs(b.metin, { italics: true, size: 18, color: GRAY }), { spacing: { after: 120 } })); break;
    case 'sc':
      body.push(P([new TextRun({ text: `S${b.no}. `, bold: true, color: NAVY }), ...runs(b.s)], { keepNext: true, spacing: { before: 140, after: 40 } }));
      body.push(P([new TextRun({ text: 'Cevap: ', bold: true }), ...runs(b.c + ' '), ...(b.dayanak ? [new TextRun({ text: `(${b.dayanak})`, italics: true, color: GRAY })] : [])],
        { indent: { left: 360 }, spacing: { after: 100 } }));
      break;
    case 'mono': for (const l of b.satirlar) body.push(P([new TextRun({ text: l, font: 'Courier New', size: 14 })], { spacing: { after: 10 } })); break;
    default: throw new Error('bilinmeyen blok ' + b.t);
  }
}
const footerP = () => new Paragraph({ alignment: AlignmentType.CENTER, children: [
  new TextRun({ text: `${M.alt_bilgi} | Sayfa `, color: GRAY, size: 16 }), new TextRun({ children: [PageNumber.CURRENT], color: GRAY, size: 16 }),
  new TextRun({ text: ' / ', color: GRAY, size: 16 }), new TextRun({ children: [PageNumber.TOTAL_PAGES], color: GRAY, size: 16 })] });
const doc = new Document({
  creator: 'GM Hazırlık', title: M.baslik,
  styles: {
    default: { document: { run: { font: 'Arial', size: 22 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 32, bold: true, color: NAVY, font: 'Arial' }, paragraph: { spacing: { before: 360, after: 180 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 26, bold: true, color: NAVY, font: 'Arial' }, paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { size: 23, bold: true, color: NAVY, font: 'Arial' }, paragraph: { spacing: { before: 200, after: 80 }, outlineLevel: 2 } },
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
    footers: { default: new Footer({ children: [footerP()] }), first: new Footer({ children: [footerP()] }) },
    children: body,
  }],
});
Packer.toBuffer(doc).then((b) => { fs.writeFileSync(OUT, b); console.log('yazıldı', OUT); });
