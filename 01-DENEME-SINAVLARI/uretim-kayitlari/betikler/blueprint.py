import random, collections, csv, sys
random.seed(2027)
CAT={'V1':'V','V2':'V','V3':'V','B1':'B','B2':'B','E1':'E','E2':'E','O3':'X','D2':'X','G3':'X'}
GM_TARGET={'O2':11,'O1':6,'Ö3':4,'G1':4,'Ö1':3,'D1':2,'Ö2':2,'D3':2,'D6':1,'K1':1,'V':2,'B':2,'E':1,'X':1}
GM_TOP=[('GM07',4,'Transit rejimi','O2 Ö3 Ö1 Ö2 K1 G1 O1 B2 E2 V2 D6 D1'),
('GM08',4,'Antrepo rejimi ve geçici depolama yeri/antrepo işleticileri','O2 O1 B2 G1 Ö3 Ö1 E2 D1 V2 D6'),
('GM14',3,'Muafiyetler (GK 167-168, 2009/15481 Karar)','O1 D3 O2 Ö3 G1 B2 V2'),
('GM02',3,'Gümrük kıymeti (sözel)','O3 O2 G1 O1 Ö3 D6 Ö1 V3'),
('GM20',3,'YYS, onaylanmış kişi, izinli alıcı/gönderici, yerinde gümrükleme','O1 Ö3 O2 G1 D3 K1'),
('GM11',2,'Geçici ithalat / geçici ihracat','V1 O2 G1 D1 O1 Ö3 D3'),
('GM05',2,'Gümrük beyanı, basitleştirilmiş usuller, muayene, eşyanın teslimi','D1 Ö2 O2 G1 K1 O1 Ö1'),
('GM17',2,'Gümrük yükümlülüğü, tahakkuk, tebliğ, ödeme, zamanaşımı, teminat, tecil, faiz','G1 O2 D6 D1 Ö2 O1 B1'),
('GM04',2,'Özet beyan, gümrüğe sunma, geçici depolama, çıkış bildirimi','O2 D1 G1 O1 Ö1 D6'),
('GM13',2,'Geri gelen eşya','Ö3 O1 D3 O2 V2 G1'),
('GM21',2,'Gümrük müşavirliği, temsil, YGM, disiplin','O2 D6 D1 O1 E1 K1 D2'),
('GM19',2,'Cezalar (GK 234-241), uzlaşma, itiraz (sözel)','Ö1 B1 O2 D1 G1 D6 Ö2'),
('GM15',1,'Posta ve hızlı kargo','D3 O2 B2 D1 O1 G1'),
('GM03',1,'Menşe (tercihsiz), BTB/BMB','Ö1 O3 O2 G1 D6 Ö3 K1'),
('GM23',1,'Fikri ve sınai haklar','Ö2 Ö3 O2 D1 G1 O1'),
('GM09',1,'Dahilde işleme rejimi (gümrük yönü)','Ö3 O2 G3 K1 G1 Ö2'),
('GM18',1,'Geri verme – kaldırma','G1 O1 O2 D6 D1'),
('GM16',1,'Gemiler/uçaklar: akaryakıt, kumanya, dış sefer','V2 O2 D6 G1'),
('GM12',1,'İhracat rejimi (gümrük yönü)','O1 O2 D6 V1 G1'),
('GM22',1,'Gümrüksüz satış mağazaları, sınır ticareti, serbest bölgeler','O2 V2 G1 D3 O1'),
('GM06',1,'Serbest dolaşıma giriş, nihai kullanım','O1 O2 D6 G1'),
('GM10',1,'Hariçte işleme, gümrük kontrolü altında işleme','E1 D6 K1 O2 G1 V3'),
('ROT',1,'D1: Genel hükümler/tanımlar/kararlar · D2: Tasfiye · D3: Genel hükümler (gümrük idareleri, gizlilik, kararların iptali/geri alınması)','O2 Ö3 O1 D2 G3')]
SR_TARGET={'O1':7,'D3':3,'D2':2,'O2':2,'Ö1':2,'Ö3':2,'K1':2,'E1':2,'B1':1,'D6':1,'G1':1,'Ö2':1,'Ö4':1,'D4':1,'X':2}
CAT_SR={'G2':'X','E3':'X','D5':'X','O3':'X','Ö5':'X'}
SR_TOP=[('SR10',5,'Tercihli ticaret ve menşe ispat belgeleri (STA/TTA, A.TR, EUR.1, GTS, kümülasyon, taraf ülkeler)','E1 D4 O1 D2 D3 Ö3 K1 G1 B1 E3'),
('SR01',3,'5607 Kaçakçılıkla Mücadele Kanunu ve yönetmelikleri','O1 Ö4 D3 O2 D6 Ö1 Ö2 D4 K1'),
('SR02',3,'Kambiyo (32 sayılı Karar, tebliğler, TCMB İhracat Genelgesi, kıymetli maden, nakit)','O1 B1 K1 D3 O2 Ö1 D6 D2'),
('SR15',2,'Dış ticaret işlemleri (Incoterms 2020, ödeme şekilleri, taşıma belgeleri)','K1 O1 D2 D4 E1 G1'),
('SR06',3,'İhracat rejimi (Ticaret yönü: İhracat Rejimi Kararı, İhracat Yönetmeliği, yasak/ön izin/kayda bağlı, bedelsiz)','O1 D3 B1 Ö3 O2 D6 Ö1'),
('SR04',2,'ÖTV (listeler, istisnalar, ithalatta uygulama)','O1 D3 O3 D6 E1 Ö3 D5'),
('SR05',2,'Damga vergisi, KKDF, fonlar','D3 O1 D6 Ö3 O2'),
('SR14',2,'DTÖ/GATT VII Kıymet Anlaşması, TFA, DGÖ, transfer fiyatlandırması, uluslararası kuruluşlar','G2 O1 D2 K1 O2 G1'),
('SR08',2,'Ürün güvenliği, teknik düzenlemeler, TAREKS, ithalat denetim tebliğleri','E1 Ö3 O1 D2 D3 O2'),
('SR07',1,'İthalat rejimi, ilave gümrük vergisi','O2 O1 Ö1 D6 D3'),
('SR16',2,'TIR, ATA karneleri, İstanbul Sözleşmesi','O1 D2 D6 O2 Ö2 K1 G1'),
('SR03',1,'KDV (sözel)','D3 O1 G1 D6 O2'),
('SR12',1,'DİR Kararı ve Tebliği (Ticaret yönü)','Ö1 O2 D6 B1 O1'),
('ROT',1,'D1: Yatırımlarda devlet yardımları (2025/9903) · D2: Ticaret politikası savunma araçları (damping, korunma, gözetim) · D3: 1/95 OKK ve Gümrük Birliği esasları','O1 G2 O2 K1 E3 D2 Ö5')]
def cat(t,catmap): return catmap.get(t,t)
def solve(top,target,catmap,used):
    best=None
    for it in range(20000):
        rem=dict(target); assign=[]; ok=True
        order=list(range(len(top))); random.shuffle(order)
        res={}
        for i in sorted(order,key=lambda i: len(top[i][3].split())):
            code,n,name,allowed=top[i]; al=allowed.split(); picks=[]
            for k in range(n):
                cands=[a for a in al if rem.get(cat(a,catmap),0)>0 and a not in picks]
                if not cands: ok=False;break
                # prefer unused in other denemeler
                w=[ (1 if (code,a) in used else 6) for a in cands]
                a=random.choices(cands,weights=w)[0]; picks.append(a); rem[cat(a,catmap)]-=1
            if not ok: break
            res[code]=picks
        if ok and all(v==0 for v in rem.values()):
            score=sum(1 for c,p in res.items() for a in p if (c,a) in used)
            if best is None or score<best[0]: best=(score,res)
            if score==0: break
    return best[1]
out=[]
for alan,top,target,catmap in [('GM',GM_TOP,GM_TARGET,CAT),('SAİR',SR_TOP,SR_TARGET,CAT_SR)]:
    used=set()
    for d in (1,2,3):
        res=solve(top,target,catmap,used)
        for code,n,name,allowed in top:
            for a in res[code]:
                used.add((code,a)); out.append((d,alan,code,name,a))
w=csv.writer(open(sys.argv[1],'w',encoding='utf-8',newline=''))
w.writerow(['deneme','alan','konu','konu_adi','alt_tip'])
for r in out: w.writerow(r)
c=collections.Counter((r[0],r[1],r[4]) for r in out)
for d in (1,2,3):
    print(d,'GM',sorted((k[2],v) for k,v in c.items() if k[0]==d and k[1]=='GM'))
    print(d,'SR',sorted((k[2],v) for k,v in c.items() if k[0]==d and k[1]=='SAİR'))
