// Kullanım: node cikti_gm.js S → GK_GM_Deneme{S}_100soru.docx (öğrenci sürümü; PDF'e çevrilir)
const fs = require('fs');
const { d, p, h1, h2, table, pb, doc, coverPage, runs } = require('./gk.js');
const { Paragraph, TextRun } = d;
const S = process.argv[2]; const Q = JSON.parse(fs.readFileSync('set' + S + '.json')); const L = 'ABCDE';
const B = []; const add = (...x) => x.flat().forEach(e => B.push(e));
const soru = (q) => {
  add(new Paragraph({ keepNext: true, keepLines: true, spacing: { before: 200, after: 80 }, children: [new TextRun({ text: q.no + '- ', bold: true }), ...runs(q.kok[0])] }));
  q.kok.slice(1).forEach(l => add(new Paragraph({ keepNext: true, keepLines: true, indent: { left: 360 }, spacing: { after: 40 }, children: runs(l) })));
  q.opts.forEach((o, j) => add(new Paragraph({ keepNext: j < 4, keepLines: true, indent: { left: 360, hanging: 360 }, spacing: { after: 40 }, children: [new TextRun(L[j] + ') '), ...runs(o)] })));
};
add(h1('Sınav Bilgileri'), table(['Alan', 'Değer'], [
  ['Sınav', 'Gümrük Müşavirliği Deneme Sınavı ' + S],
  ['Soru sayısı', '100'],
  ['Model', '2024 ve 2025 GM sınavlarında ölçülen bilgi alanları esas alınmıştır; 2021–2023 sınavlarında sık sorulan konular da kapsamdadır.'],
], [3, 7]));
add(p(''), p('Her sorunun yalnız bir doğru cevabı vardır. Sorular çıkmış soruların kopyası değildir; kurumun soru dili ve ölçtüğü bilgi alanları esas alınarak özgün olarak hazırlanmıştır.'));
add(pb(), h1('BÖLÜM A — SORU KİTAPÇIĞI'));
for (const q of Q) soru(q);
add(pb(), h1('Cevap Anahtarı'));
for (let s = 0; s < 100; s += 10) { const part = Q.slice(s, s + 10); add(table(part.map(q => String(q.no)), [part.map(q => q.harf)], part.map(() => 1)), p('')); }
add(pb(), h1('BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR'));
for (const q of Q) {
  add(new Paragraph({ keepNext: true, spacing: { before: 280, after: 40 }, children: [new TextRun({ text: q.madde, italics: true, color: 'B8860B', size: 20 })] }));
  soru(q);
  add(new Paragraph({ keepNext: true, spacing: { before: 80, after: 40 }, children: [new TextRun({ text: 'Doğru Cevap: ', bold: true }), new TextRun({ text: q.harf, bold: true, color: '1B3A5C' })] }));
  add(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: 'Gerekçe: ', bold: true }), ...runs(q.g)] }));
}
const kon = {}; Q.forEach(q => { kon[q.konu] = (kon[q.konu] || 0) + 1; });
add(pb(), h1('Konu Dağılımı'), table(['Konu', 'Soru'], Object.entries(kon).sort((a, b) => b[1] - a[1]).map(([k, v]) => [k, String(v)]), [8, 2]));
const out = doc({ header: 'Gümrük Koçu - Ufuk Çetintaş', footer: 'Gümrük Koçu - Ufuk Çetintaş',
  cover: coverPage('GM DENEME SINAVI ' + S, '100 Soru · 2024–2025 Sınavları Esas', 'Gümrük Müşavirliği Sınavına Hazırlık'), body: B });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync('GK_GM_Deneme' + S + '_100soru.docx', b); console.log('docx ok', S); });
