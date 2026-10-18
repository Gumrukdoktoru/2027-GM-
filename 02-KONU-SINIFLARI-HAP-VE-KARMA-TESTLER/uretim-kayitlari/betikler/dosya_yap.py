import json, re, sys, os
S = sys.argv[1]
rows = json.load(open(f'{S}/konu/siniflar.json', encoding='utf-8'))
Q = {q['id']: q for q in json.load(open(f'{S}/konu/eslesme.json', encoding='utf-8'))['sorular']}
TAL = re.compile(r'Salon Ba|Salon Kod|salon ad|Kimlik No|Optik|cevap kâğıd|Cevap form|Sınav süresi|sınav Ticaret Bakanlığı|Bu kitapçıkta 100|kurşun kalem|arka kapa|müsvedde|özel durumunuz|doğru cevabı vardır|Yanlış cevaplarınız|silme işlemi|kuralları önceden|SINAV BAŞLAMIŞTIR|Cevaplamaya istediğiniz|Cevaplamaya geçmeden|her hakkı saklı|Soru kitapçığınızın|Kitapçığınızın|kitapçığında her sorunun|değerlendirmesi sadece doğru|gereksiz hiçbir|algılamayacaktır', re.I)
def bol(y):
    t = open(f'{S}/exams/{y}_red.txt', encoding='utf-8').read()
    def cands(n):
        return [m for m in re.finditer(r'(?m)^\s*' + str(n) + r'\s*[\.\-](?!\d)\s*', t) if not TAL.search(t[m.start():m.start() + 160])]
    out = {}
    for n in range(1, 101):
        c = cands(n)
        if not c: continue
        st = c[0].start()
        nx = [m.start() for m in cands(n + 1) if m.start() > st]
        end = nx[0] if nx else st + 2500
        s = t[st:end]
        s = re.sub(r'--- sayfa \d+ ---[^\n]*\n', '', s)
        s = re.sub(r'(?m)^(Diğer Sayfaya Geçiniz|\) - - - - -|\d{1,2}|ı-oe.*|BOYU YAŞAM|OGRENME MERKEZi|.*Öğrenme Merkezi.*|.*GÜMRÜK\s*)\s*$\n?', '', s)
        out[n] = s.strip()[:4000]
    return out
TX = {y: bol(y) for y in range(2021, 2026)}
eksik = [(y, n) for y in TX for n in range(1, 101) if n not in TX[y]]
print('eksik', eksik)
json.dump({str(y): {str(n): v for n, v in d.items()} for y, d in TX.items()}, open(f'{S}/konu/soru_metinleri.json', 'w', encoding='utf-8'), ensure_ascii=False)
for r in rows:
    out = [f"# {r['ad']} ({r['id']}) — {r['toplam']} soru, sınıf {r['sinif']}, eğilim {r['egilim']}, yıllar 21-25: {r['yillar']}\n"]
    for qid in r['sorular']:
        y, n = map(int, qid.split('/')); q = Q[qid]; tx = TX[y].get(n, 'METİN BULUNAMADI')
        out.append(f"## {qid}  [{q['alan']}]  {q['alt']}\n- Dayanak (analiz): {q['dayanak']}\n- Kök tipi: {q['kok']}\n- Doğru cevap (resmî anahtar): {q['dogru']}\n- Çeldirici mantığı: {q['celdirici']}\n- Ölçülen: {q['hedef']}\n\n```\n{tx}\n```\n")
    tmp = f"{S}/konu/dosya/{r['id']}.md.tmp"
    open(tmp, 'w', encoding='utf-8').write('\n'.join(out)); os.replace(tmp, f"{S}/konu/dosya/{r['id']}.md")
