import csv,sys,os,collections
D=sys.argv[1]
rows=list(csv.DictReader(open(f'{D}/plan_gm_sair.csv',encoding='utf-8')))
AG={'GM-A1':('GM',['GM07','GM08']),
    'GM-A2':('GM',['GM11','GM09','GM10','GM06','GM12','GM13','GM16','GM22']),
    'GM-B1':('GM',['GM14','GM02','GM03','GM18']),
    'GM-B2':('GM',['GM04','GM05','GM17']),
    'GM-C':('GM',['GM20','GM21','GM15','GM23','GM19','ROT']),
    'SR-A':('SAİR',['SR01','SR02','SR04','SR05','SR03']),
    'SR-B':('SAİR',['SR10','SR15','SR14','SR16']),
    'SR-C':('SAİR',['SR06','SR08','SR07','SR12','ROT'])}
TR=[(1,'TR01','Fasıl/bölüm/pozisyon kapsamı','O4 O4 O4 D5 D5 D4 D4'),(1,'TR02','Bölüm/fasıl notları, izahname','O4 O4 D5'),
(1,'TR05','GTİP yapısı, HS 2022/HS 2027 değişiklikleri, 474 sayılı Kanun, Fasıl 99','O4 D5 G2'),(1,'TR04','Tanımı verilen eşyanın pozisyonu','V4 V4'),(1,'TR03','GYKK uygulaması','G4 O4'),
(2,'TR01','Fasıl/bölüm/pozisyon kapsamı','O4 O4 O4 D5 D5 D4 D4'),(2,'TR02','Bölüm/fasıl notları, izahname','O4 O4 D5'),
(2,'TR05','GTİP yapısı, HS 2022/HS 2027 değişiklikleri, 474 sayılı Kanun, Fasıl 99','O4 D5 B2'),(2,'TR04','Tanımı verilen eşyanın pozisyonu','V4 V4'),(2,'TR03','GYKK uygulaması','E1 O4'),
(3,'TR01','Fasıl/bölüm/pozisyon kapsamı','O4 O4 O4 D5 D5 D4 S2'),(3,'TR02','Bölüm/fasıl notları, izahname','O4 O4 D5'),
(3,'TR05','GTİP yapısı, HS 2022/HS 2027 değişiklikleri, 474 sayılı Kanun, Fasıl 99','O4 D5 D4'),(3,'TR04','Tanımı verilen eşyanın pozisyonu','V4 V4'),(3,'TR03','GYKK uygulaması','G4 O4')]
TRAG={'TR-A':['TR01','TR02'],'TR-B':['TR03','TR04','TR05']}
HS={'HS-A':[
(1,'H1+H2 seti',"Ortak veri setli iki soru: önce gümrük kıymeti (H1, 7–9 kalem), sonra KDV matrahı (H2)"),
(1,'H1',"Tek başına kalem listeli kıymet (farklı teslim şekli: EXW/FOB/CFR; assist, komisyon, ambalaj, demuraj)"),
(1,'H6',"Royalti/lisans listesi (satış koşulu olan/olmayan, çoğaltma hakkı, stopajlı brüt)"),
(1,'H6',"Serbest bölgeden ithalatta kıymet ya da kendi kendini taşıyan eşya"),
(1,'H6',"Dolaylı ödeme / temettü ayıklama ya da yeniden satış hasılası payı"),
(2,'H1+H2 seti',"Ortak veri setli iki soru: gümrük kıymeti (H1) + KDV matrahı (H2); kur ve tescil öncesi/sonrası giderler"),
(2,'H1',"Tek başına kalem listeli kıymet (Deneme 1’dekinden farklı kalem karması)"),
(2,'H6',"Gözetim değeri ya da taşıyıcı ortamdaki yazılım"),
(2,'H6',"Satış komisyonu–alım komisyonu ayrımı ya da royalti ağırlıklı az kalemli özel durum"),
(2,'H5',"Kıymet yöntemi: aynı/benzer eşya + miktar/ticari düzey düzeltmesi ya da hesaplanmış kıymet"),
(3,'H1+H2 seti',"Ortak veri setli iki soru: gümrük kıymeti (H1) + KDV matrahı (H2)"),
(3,'H1',"Tek başına kalem listeli kıymet (avans/peşin ödeme kuru tuzağı, CFR’de sigorta)"),
(3,'H6',"Yeniden satış hasılası ya da dolaylı ödeme (Deneme 1’de kullanılmayanı)"),
(3,'H6',"Kendi kendini taşıyan eşya ya da serbest bölge (Deneme 1’de kullanılmayanı)"),
(3,'H6',"Royalti listesi (farklı kurgu) ya da kullanılmış taşıt (yalnız kaynakta kesin kural bulunursa)")],
'HS-B':[
(1,'H3',"GV–İGV–ÖTV–KDV zinciri (ÖTV matraha katılıyor)"),(1,'H3',"MIN/MAX’lı gümrük vergisi (kalem bazında karşılaştırma)"),(1,'H3',"(I) sayılı liste / litre başı ÖTV tuzağı ya da KKDF’nin matrahlara etkisi"),
(1,'H4',"Noksan kıymet: GV+EMY+KDV farkının 3 katı (GK 234/1) ya da kendiliğinden bildirim"),(1,'H8',"İhracat bedelinin yurda getirilme süresi (vade + ek süre)"),
(2,'H3',"Nispi ÖTV ile asgari maktu vergi karşılaştırması"),(2,'H3',"Tescil kuru, mal mukabili/peşin ödeme ayrımında KKDF ve KDV matrahı"),(2,'H3',"ÖTV’nin doğmadığı ithalat (motorlu araç ticareti) ya da listeye özgü farklı kural"),
(2,'H4',"Uzlaşma / peşin ödeme indirimi / ceza matrahı"),(2,'H8',"Antrepo götürü teminatı (alan/hacim kademesi; tuzak veri)"),
(3,'H3',"Vergi zinciri (GV–İGV–ÖTV–KDV), kıymete eklemeler sonrası"),(3,"H3","ÖTV (III) ya da (IV) sayılı listede nispi oranlı eşya + KDV zinciri; ya da İGV dahil zincir (Deneme 1–2’den farklı kurgu)"),
(3,'H7',"Hesapsız hesap (uzlaşılan tutara ayrıca indirim yok vb.)"),(3,'H4',"Ek tahakkuk + ceza (2 no.lu beyanla ödenen KDV’nin durumu vb.)"),(3,'H8',"Kısmi muafiyetli geçici ithalatta aylık %3 üzerinden alınacak vergi (toplam vergiyi aşamaz kuralı) ya da tecil faizi hesabı")]}
def w(name,lines):
    open(f'{D}/slots/{name}.md','w',encoding='utf-8').write('\n'.join(lines)+'\n')
for ag,(alan,codes) in AG.items():
    L=[f'# Slot listesi — {ag} ({alan})','','| # | Deneme | Konu kodu | Konu | Alt tip |','|---|---|---|---|---|']; n=0
    for d in '123':
        for code in codes:
            for r in rows:
                if r['deneme']==d and r['alan']==alan and r['konu']==code:
                    n+=1; L.append(f"| {n} | {d} | {code} | {r['konu_adi']} | {r['alt_tip']} |")
    L.append(''); L.append(f'Toplam: {n} soru'); w(ag,L); print(ag,n)
for ag,codes in TRAG.items():
    L=[f'# Slot listesi — {ag} (TARİFE)','','| # | Deneme | Konu kodu | Konu | Alt tip |','|---|---|---|---|---|']; n=0
    for d,code,name,ats in TR:
        if code in codes:
            for a in ats.split(): n+=1; L.append(f'| {n} | {d} | {code} | {name} | {a} |')
    L.append(''); L.append(f'Toplam: {n} soru'); w(ag,L); print(ag,n)
for ag,sl in HS.items():
    L=[f'# Slot listesi — {ag} (HESAP)','','| # | Deneme | Alt tip | Kurgu hedefi |','|---|---|---|---|']; n=0
    for d,at,desc in sl:
        k=2 if at=='H1+H2 seti' else 1
        n+=k; L.append(f'| {n-k+1}{"–"+str(n) if k==2 else ""} | {d} | {at} | {desc} |')
    L.append(''); L.append(f'Toplam: {n} soru'); w(ag,L); print(ag,n)
