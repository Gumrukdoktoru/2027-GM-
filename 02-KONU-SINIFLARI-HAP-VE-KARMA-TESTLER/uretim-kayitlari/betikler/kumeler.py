import json, sys, os, collections
S = sys.argv[1]
K2 = f'{S}/kaynak2'
rows = {r['id']: r for r in json.load(open(f'{S}/konu/siniflar.json', encoding='utf-8'))}
G, GE, D, T = 'kaynak2/gm/', 'kaynak2/genelge/', 'kaynak2/diger/', 'kaynak/txt/'
SAIR = D + 'SAİR MEVZUAT KİTABI.md'
KUME = {
 'K01': (['KIYMET', 'MENSE', 'BTB', 'DTO'], [G+'12_12-KIYMET_VE_KAPLAR.md', G+'10_10-MENŞEİ.md', G+'06_6-KARAR.md', G+'07_7-BİLGİ.md', D+'VERGI_HESAPLAMA_DERLEMESI.md', D+'Hesaplamaçıkmış.md']),
 'K02': (['TANIM', 'GENEL', 'OZET', 'GDY', 'BEYAN', 'MUAYENE', 'SDG', 'SONRADAN', 'TASIT', 'KABOTAJ', 'ESIS'],
         [G+'01_1-TANIMLAR.md', G+'05_5-SONRADAN_KONTROL.md', G+'06_6-KARAR.md', G+'07_7-BİLGİ.md', G+'08_8-SÜRELER_VE_DİĞER_HÜKÜMLER.md', G+'09_9-TAR.POZ.AYIRMA.md',
          G+'13_13-TAŞITLAR.md', G+'14_14-KABOTAJ.md', G+'15_15-ÖZET_BEYAN.md', G+'16_16-GOBİK_VE_SAHTE_EŞYA.md', G+'17_17-BEYAN.md', G+'18_18-Ser.Dol.Giriş_Rejimi.md',
          GE+'gumruk_genel_tebligi_x1varis_oncesi_gumruk_islemlerix2_seri_no_1.md', GE+'gumruk_genel_tebligi_x1yukumlu_kayit_ve_takip_sistemix2_seri_no_1.md',
          GE+'elektronik_tebligat_sistemi_genel_tebligi_x1sira_no_1x2.md', GE+'g_g_tebligi_x1gumruk_islerix2_seri_no_16_gumruk_gozetiminde_sahibine_veya_eksik_beyanla_es.md', GE+'sayac_islemleri_tebligi_x1seri_no_1x2.md']),
 'K03': (['TRANSIT', 'TIR', 'AKTRANSIT', 'TRBASIT', 'ANTREPO'],
         [G+'20_20-TRANSİT_REJİMİ.md', G+'21_21-TIR_SÖZLEŞMESİ.md', G+'22_22-SERİ_NO_3.md', G+'23_23-SERİ_NO_4.md', G+'24_24-SERİ_NO_5.md', G+'25_25-SERİ_NO_6.md',
          G+'26_26-seri_no_8.md', G+'27_27-seri_no_14.md', G+'28_28-antrepo_rejimi.md', G+'29_29-iŞLETİCİLER.md']),
 'K04': (['DIR', 'HIR', 'GI', 'SARTLI', 'IHRG', 'GERIGELEN'],
         [G+'19_19-ŞARTLI_M_VE_E.E.G.R.md', G+'32_32-DAHİLDE_İŞLEME.md', G+'33_33-GKAİR.md', G+'34_34-GEÇİCİ_İTHALAT.md', G+'35_35-_hir.md', G+'36_36-ihracat.md', G+'37_37-geri_gelen_eşya.md',
          GE+'dahilde_isleme_rejimi_karari_sayisi_2005-8391.md', GE+'dahilde_isleme_rejimi_tebligi_ihracat_2006_12.md', GE+'dtm_2008-02_dahilde_isleme_rejimi_kapsaminda_telafi_edici_vergi_x1tevx2_uygulamalari.md']),
 'K05': (['MUAF', 'POSTA', 'KUMANYA', 'GSM', 'SINIR', 'SB', 'FSMH', 'TASFIYE'],
         [G+'16_16-GOBİK_VE_SAHTE_EŞYA.md', G+'30_30-Güm.Sat.Mağazaları.md', G+'38_38-serbest_bölge.md', G+'39_39-muafiyetler.md', G+'40_40-posta_ve_hızlı_kargo.md',
          G+'41_41-sınır_ticareti.md', G+'42_42-kumanya.md', G+'43_43-tasfiye.md', GE+'posta_ve_hizli_kargo_yoluyla_tasinan_esyanin_gumruk_islemlerine_iliskin_teblig_seri_no_1.md',
          GE+'tasfiye_genel_tebligi_x1elektronik_ihalex2_seri_no_1.md', SAIR + ' (Serbest Bölgeler Uygulama Yönetmeliği bölümü)']),
 'K06': (['YUKUM', 'TAHAKKUK', 'TEMINAT', 'GERIVERME', 'CEZA', 'ITIRAZ', 'UZLASMA'],
         [G+'44_44-yükümlülük.md', G+'45_45-tebliğ.md', G+'46_46-teminat_ve_faiz.md', G+'47_47-geri_verme_kaldırma.md', G+'48_48-cezalar.md', G+'49_49-itirazlar.md', G+'50_50-uzlaşma.md']),
 'K07': (['YYS', 'OKS', 'MUSAVIR', 'YGM'],
         [G+'02_2-TEMSİL.md', G+'03_3-YYS.md', G+'04_4-OKSB.md', G+'31_31-YGM.md', G+'51_51-disiplin_cezaları.md', SAIR + ' (Onaylanmış Kişi Statüsü GGT ve G.G.T. Seri No 71 bölümleri)']),
 'K08': (['KACAK', 'KAMBIYO', 'KKDF', 'DAMGA'],
         [D+'kaçakçılık.md', GE+'tasfiye_genel_tebligi_x1kacak_esya_ve_kacak_esya_naklinde_kullanilan_tasitlara_iliskin_isl.md',
          SAIR + ' (1567 sayılı Kanun, 32 sayılı Karar, 2018-32/48 ve 2008-32/34 Tebliğleri, Nakit Kontrolleri Genelgesi 2024/1, KKDF Kararı bölümleri)']),
 'K09': (['KDV', 'OTV', 'TESVIK'],
         [SAIR + ' (KDV Kanunu, 2007/13033 KDV oranları Kararı, ÖTV Kanunu, DYY Kanunu 4875, 2025/9903 Kararı, GGT Yatırım Teşvik Seri No 9, 2025-1 Tebliğ bölümleri)',
          GE+'ozel_tuketim_vergisi_x1ix2_sayili_liste_uygulama_genel_tebligi.md', GE+'ozel_tuketim_vergisi_ii_sayili_liste_uygulama_genel_tebligi.md',
          GE+'ozel_tuketim_vergisi_x1iiix2_sayili_liste_uygulama_genel_tebligi.md', GE+'ozel_tuketim_vergisi_x1ivx2_sayili_liste_uygulama_genel_tebligi.md',
          GE+'YATIRIMLARDA_DEVLET_YARDIMLARI_HAKKINDA_KARAR_9903_PDF_97_slayt_.md', D+'VERGI_HESAPLAMA_DERLEMESI.md']),
 'K10': (['ITHR', 'URUN', 'TPS', 'KOTA', 'TICHAK'],
         [D+'ck_2020-03350_ithalat_rejimi_karari.md', D+'ck_2025-10790_ithalat_rejimi_kararinda_degisiklik_yapilmasina_iliskin_karar.md', GE+'ithalatta_ilave_gumruk_vergisi_uygulanmasina_iliskin_karar.md',
          T+'4 - TEKNİK DÜZENLEMELER.txt', GE+'2026-01_yurt_icinde_duzenlenen_uluslararasi_fuarlara_iliskin_ithalat_tebligi.md',
          SAIR + ' (3577 Kanunu, 99/13482 Kararı ve Yönetmeliği, Korunma Önlemleri Kararı ve Yönetmeliği, Kota ve Tarife Kontenjanı Kararları, Gözetim Kararı ve Yönetmeliği, Ticari Hakların Korunması Kararı, İthalat Genelgesi 2020/1, Teknik Düzenlemeler Rejimi Kararı, Ürün Güvenliği ve Denetimi Tebliğleri, İthalat Tebliğleri bölümleri)']),
 'K11': (['MENSEBELGE', 'STA', 'GB'],
         [D+'STA ve KÜMÜLASYONLAR.md', GE+'gumruk_genel_tebligi_x1genellestirilmis_tercihler_sistemix2_seri_no_5.md', GE+'gumruk_genel_tebligi_x1uluslararasi_anlasmalarx2_seri_no_7.md',
          GE+'27.03.2026_120421282_revize_pem_mense_kurallari_kapsaminda_ulkeler_ve_esya_bazinda_telafi_.md',
          SAIR + ' (1/95 OKK, 2006/10895 Gümrük Birliği Kararı, GTS menşe kararları, STA/kümülasyon özet tablosu bölümleri)']),
 'K12': (['INCO', 'ODEME', 'IHRR', 'IHRSAY', 'EIHR', 'ELMAS'],
         [D+'Diş Ticarette Teslim Şekilleri.md', GE+'ihracat_rejim_karari_22.12.1995_95-7623.md', GE+'ihracat_yonetmeligi_2006.md', GE+'ihraci_yasak_ve_on_izne_bagli_mallara_iliskin_teblig_96-31.md',
          GE+'ihraci_kayda_bagli_mallara_iliskin_teblig_ihracat_2006-7.md', GE+'bedelsiz_ihracata_iliskin_teblig_no_ihracat_2008_12.md', GE+'ihracat_sayilan_satis_ve_teslimler_hakkinda_teblig_2005-02.md',
          GE+'ihracat_sayilan_satis_ve_teslimlerde_vergi_harc_istisnasi_hakkinda_99-13812_sayili_karar.md', GE+'ck_2022-05986_e-ihracat_destekleri_hakkinda_karar.md',
          GE+'dis_ticaret_sermaye_sirketi_statusune_iliskin_teblig_ihracat_2025-07.md', GE+'ham_elmas_dis_ticaretinin_duzenlenmesine_ve_denetlenmesine_dair_karara_iliskin_teblig_2006.md',
          GE+'nesli_tehlike_altinda_olan_yabani_hayvan_ve_bitki_turlerinin_dis_ticaretine_iliskin_teblig.md', GE+'ihracata_yonelik_devlet_yardimlari_karari_94-6401.md',
          GE+'yurt_disinda_fuar_duzenlenmesine_ve_degerlendirilmesine_iliskin_teblig_2010-5.md', SAIR + ' (Teslim Şekilleri ve Ödeme Şekilleri bölümleri)']),
 'K13': (['T_GYKK', 'T_HS22', 'T_YAPI', 'T_GIDA', 'T_KIMYA'],
         [T+'TARİFENİNYORUMU İLE İLGİLİ GENEL KURALLAR 2017.txt', T+'FASIL01.txt … FASIL40.txt', T+'İÇİNDEKİLER, KISALTMALAR VE SEMBOLLER.txt', D+'TARIFE_ANA_DERLEME.md (Tarife ders notu ve Tarife Kitabı bölümleri)',
          GE+'gumruk_genel_tebligi_x1gumruk_tarife_cetveli_izahnamesix2_seri_no_4.md', GE+'genelge_2016-06_esyanin_set_olarak_siniflandirilmasina_iliskin_rehber_x1set_esyanin_tarife.md', GE+'genelge_*.md (sınıflandırma genelgeleri)',
          G+'09_9-TAR.POZ.AYIRMA.md', G+'12_12-KIYMET_VE_KAPLAR.md (GK 15-16 tarife ve kaplar)']),
 'K14': (['T_TEKSTIL', 'T_METAL', 'T_MAKINE', 'T_TASIT', 'T_CESITLI'],
         [T+'FASIL41.txt … FASIL97.txt', T+'TARİFENİNYORUMU İLE İLGİLİ GENEL KURALLAR 2017.txt', D+'TARIFE_ANA_DERLEME.md (Tarife ders notu ve Tarife Kitabı bölümleri)',
          GE+'gumruk_genel_tebligi_x1gumruk_tarife_cetveli_izahnamesix2_seri_no_4.md', GE+'genelge_*.md (sınıflandırma genelgeleri)', GE+'gumruk_genel_tebligi_x1tarife*siniflandirma_kararlari*.md']),
}
HEDEF_SC = {'ÇOK': (40, 70), 'ORTA': (25, 40), 'AZ': (15, 25), 'HİÇ': (15, 30)}
HEDEF_HAP = {'ÇOK': 16, 'ORTA': 10, 'AZ': 6, 'HİÇ': 6}
seen = collections.Counter()
for kid, (konular, kay) in KUME.items():
    for k in konular: seen[k] += 1
    L = [f'# Küme {kid}\n', '## Konular\n', '| Konu kodu | Konu | Ders | Sınıf | 5 yılda | 21–25 | Eğilim | Çıkmış soru dosyası | Beklenen hap hedefi | Soru–cevap hedefi |', '|---|---|---|---|---|---|---|---|---|---|']
    for k in konular:
        r = rows[k]
        L.append(f"| {k} | {r['ad']} | {r['ders']} | {r['sinif']} | {r['toplam']} | {'-'.join(map(str, r['yillar']))} | {r['egilim']} | `$S/konu/dosya/{k}.md` | {HEDEF_HAP[r['sinif']]} | {HEDEF_SC[r['sinif']][0]}–{HEDEF_SC[r['sinif']][1]} |")
    L += ['', '## Kaynak dosyalar (`$S/` altında)', ''] + [f'- `{x}`' for x in kay] + ['']
    open(f'{S}/hap/girdi/{kid}.md', 'w', encoding='utf-8').write('\n'.join(L))
    for x in kay:
        p = x.split(' (')[0].split(' …')[0]
        if '*' in p or '…' in x: continue
        if not os.path.exists(f'{S}/{p}'): print('YOK', kid, p)
allk = set(rows)
print('eksik konu', allk - set(seen), 'çift', [k for k, v in seen.items() if v > 1])
json.dump({k: v[0] for k, v in KUME.items()}, open(f'{S}/hap/kumeler.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for kid, (konular, _) in KUME.items():
    print(kid, sum(rows[k]['toplam'] for k in konular), 'soru', len(konular), 'konu')
