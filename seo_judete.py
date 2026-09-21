# -*- coding: utf-8 -*-
"""
Dati per le 41 contee (județe) della Romania + București e testi delle pagine RO.

Ogni judet: code, name, jud ("județul X"), injud ("în județul X"), seat (capoluogo),
geo (coordinate del capoluogo), towns (altre città), sectors (settori industriali
rappresentativi, descritti in modo generico), nb (județe confinanti), region.
"""

J = {}
def add(code, name, seat, geo, towns, sectors, nb, region, slug=None, extra=None, **kw):
    J[code] = dict(code=code, name=name, seat=seat, geo=geo, towns=towns, sectors=sectors, nb=nb, region=region,
                   slug=slug or ('prelucrari-cnc-' + kw.pop('s')), jud='județul ' + name, injud='în județul ' + name,
                   extra=extra, **kw)

add('AB', 'Alba', 'Alba Iulia', (46.067, 23.570), 'Aiud, Sebeș, Blaj, Cugir și Ocna Mureș',
    'construcții de mașini și prelucrări mecanice, componente auto, industria lemnului și a materialelor de construcții',
    ['CJ', 'MS', 'SB', 'HD', 'AR', 'BH'], 'Centru', s='alba')
add('AR', 'Arad', 'Arad', (46.186, 21.312), 'Lipova, Ineu, Pecica, Curtici, Chișineu-Criș și Nădlac',
    'componente auto, construcția de vagoane, electronice și cablaje, parcuri industriale la granița cu Ungaria',
    ['BH', 'AB', 'HD', 'TM'], 'Vest', s='arad')
add('AG', 'Argeș', 'Pitești', (44.857, 24.869), 'Mioveni, Câmpulung, Curtea de Argeș, Costești și Topoloveni',
    'industria auto și rețeaua de furnizori din jurul platformei de la Mioveni, prelucrări metalice și petrochimie',
    ['BV', 'SB', 'VL', 'OT', 'TR', 'DB'], 'Sud-Muntenia', s='arges')
add('BC', 'Bacău', 'Bacău', (46.567, 26.914), 'Onești, Moinești, Comănești, Buhuși și Dărmănești',
    'industria aeronautică, chimie și petrochimie, prelucrări mecanice și industria lemnului',
    ['NT', 'VS', 'VN', 'CV', 'HR'], 'Nord-Est', s='bacau')
add('BH', 'Bihor', 'Oradea', (47.072, 21.921), 'Salonta, Marghita, Beiuș, Aleșd, Valea lui Mihai și Ștei',
    'componente auto și electrice în parcurile industriale din Oradea, mobilă, încălțăminte și prelucrări metalice',
    ['SM', 'SJ', 'CJ', 'AB', 'AR'], 'Nord-Vest', s='bihor')
add('BN', 'Bistrița-Năsăud', 'Bistrița', (47.133, 24.500), 'Beclean, Năsăud, Sângeorz-Băi și Prundu Bârgăului',
    'componente și cablaje auto, materiale de construcții și prelucrarea lemnului',
    ['MM', 'SV', 'MS', 'CJ'], 'Nord-Vest', s='bistrita-nasaud')
add('BT', 'Botoșani', 'Botoșani', (47.748, 26.666), 'Dorohoi, Darabani, Săveni, Flămânzi și Bucecea',
    'agricultură și mecanizare agricolă, industria ușoară și producție de componente',
    ['SV', 'IS'], 'Nord-Est', s='botosani')
add('BV', 'Brașov', 'Brașov', (45.658, 25.601), 'Făgăraș, Săcele, Codlea, Zărnești, Râșnov, Ghimbav și Cristian',
    'industria aeronautică, rulmenți și componente auto, construcții de mașini și prelucrări de precizie',
    ['CV', 'HR', 'MS', 'SB', 'AG', 'DB', 'PH', 'BZ'], 'Centru', s='brasov')
add('BR', 'Brăila', 'Brăila', (45.271, 27.957), 'Ianca, Însurăței și Făurei',
    'construcții navale și metalice, echipamente industriale și agricultură',
    ['GL', 'VN', 'BZ', 'IL', 'CT', 'TL'], 'Sud-Est', s='braila')
add('BZ', 'Buzău', 'Buzău', (45.150, 26.823), 'Râmnicu Sărat, Nehoiu, Pogoanele și Pătârlagele',
    'industria metalurgică și a produselor din sârmă, echipamente și componente, agricultură',
    ['VN', 'BR', 'IL', 'PH', 'BV', 'CV'], 'Sud-Est', s='buzau')
add('CS', 'Caraș-Severin', 'Reșița', (45.300, 21.889), 'Caransebeș, Oțelu Roșu, Oravița, Bocșa, Moldova Nouă și Anina',
    'tradiție siderurgică și de construcții de mașini, hidroenergie și prelucrarea lemnului',
    ['TM', 'HD', 'GJ', 'MH'], 'Vest', s='caras-severin')
add('CL', 'Călărași', 'Călărași', (44.200, 27.333), 'Oltenița, Budești, Lehliu-Gară și Fundulea',
    'siderurgie, construcții navale pe Dunăre, agricultură și mecanizare agricolă',
    ['GR', 'IF', 'IL', 'CT'], 'Sud-Muntenia', s='calarasi')
add('CJ', 'Cluj', 'Cluj-Napoca', (46.770, 23.590), 'Turda, Dej, Câmpia Turzii, Gherla, Huedin și Florești',
    'echipamente industriale și electrice, componente auto, IT și inginerie, metalurgie',
    ['MM', 'BN', 'MS', 'AB', 'BH', 'SJ'], 'Nord-Vest', s='cluj')
add('CT', 'Constanța', 'Constanța', (44.176, 28.635), 'Mangalia, Medgidia, Năvodari, Cernavodă, Ovidiu și Hârșova',
    'activitatea portuară, construcții și reparații navale, energie și petrochimie',
    ['TL', 'BR', 'IL', 'CL'], 'Sud-Est', s='constanta')
add('CV', 'Covasna', 'Sfântu Gheorghe', (45.867, 25.787), 'Târgu Secuiesc, Covasna, Baraolt și Întorsura Buzăului',
    'industria lemnului, producție de componente, prelucrări mecanice și industria alimentară',
    ['HR', 'BC', 'VN', 'BZ', 'BV'], 'Centru', s='covasna')
add('DB', 'Dâmbovița', 'Târgoviște', (44.925, 25.457), 'Moreni, Pucioasa, Găești, Titu și Fieni',
    'siderurgie și prelucrări metalice, echipamente pentru industria petrolieră și materiale de construcții',
    ['PH', 'BV', 'AG', 'TR', 'GR', 'IF'], 'Sud-Muntenia', s='dambovita')
add('DJ', 'Dolj', 'Craiova', (44.319, 23.800), 'Băilești, Calafat, Filiași, Dăbuleni și Segarcea',
    'industria auto, construcția de material rulant, echipamente electrice și energie',
    ['MH', 'GJ', 'VL', 'OT'], 'Sud-Vest Oltenia', s='dolj')
add('GL', 'Galați', 'Galați', (45.435, 28.008), 'Tecuci, Târgu Bujor și Berești',
    'siderurgie, construcții navale, metalurgie și echipamente industriale',
    ['VS', 'VN', 'BR', 'TL'], 'Sud-Est', s='galati')
add('GR', 'Giurgiu', 'Giurgiu', (43.904, 25.969), 'Bolintin-Vale și Mihăilești',
    'activitate portuară pe Dunăre, logistică, agricultură și producție industrială ușoară',
    ['TR', 'DB', 'IF', 'CL'], 'Sud-Muntenia', s='giurgiu')
add('GJ', 'Gorj', 'Târgu Jiu', (45.035, 23.275), 'Motru, Rovinari, Bumbești-Jiu, Novaci și Târgu Cărbunești',
    'energie și minerit, echipamente, reparații și mentenanță industrială',
    ['HD', 'VL', 'DJ', 'MH', 'CS'], 'Sud-Vest Oltenia', s='gorj')
add('HR', 'Harghita', 'Miercurea Ciuc', (46.358, 25.804), 'Odorheiu Secuiesc, Gheorgheni, Toplița, Cristuru Secuiesc și Bălan',
    'industria lemnului, prelucrări metalice, componente și industria alimentară',
    ['MS', 'SV', 'NT', 'BC', 'CV', 'BV'], 'Centru', s='harghita')
add('HD', 'Hunedoara', 'Deva', (45.883, 22.901), 'Hunedoara, Petroșani, Orăștie, Brad, Hațeg, Lupeni și Vulcan',
    'siderurgie și prelucrări metalice, minerit, componente auto și echipamente industriale',
    ['AR', 'AB', 'SB', 'VL', 'GJ', 'CS', 'TM'], 'Vest', s='hunedoara')
add('IL', 'Ialomița', 'Slobozia', (44.564, 27.366), 'Fetești, Urziceni, Țăndărei și Amara',
    'agricultură și mecanizare agricolă, industria alimentară și logistică',
    ['CL', 'IF', 'PH', 'BZ', 'BR', 'CT'], 'Sud-Muntenia', s='ialomita')
add('IS', 'Iași', 'Iași', (47.158, 27.601), 'Pașcani, Hârlău, Târgu Frumos și Podu Iloaiei',
    'industrie farmaceutică, componente auto și electronice, metalurgie, IT și inginerie',
    ['BT', 'SV', 'NT', 'VS'], 'Nord-Est', s='iasi')
add('IF', 'Ilfov', 'Buftea', (44.563, 25.948), 'Voluntari, Otopeni, Pantelimon, Popești-Leordeni, Chitila, Bragadiru și Măgurele',
    'logistică și parcuri industriale din jurul Bucureștiului, producție de echipamente și cercetare',
    ['B', 'DB', 'PH', 'IL', 'CL', 'GR'], 'București-Ilfov', s='ilfov')
add('MM', 'Maramureș', 'Baia Mare', (47.659, 23.581), 'Sighetu Marmației, Borșa, Vișeu de Sus, Târgu Lăpuș, Seini și Baia Sprie',
    'industria lemnului și a mobilei, prelucrări metalice, componente și echipamente industriale',
    ['SM', 'SJ', 'CJ', 'BN', 'SV'], 'Nord-Vest', s='maramures',
    extra='Maramureșul este județ vecin cu atelierul nostru, așa că piesele ajung foarte repede, iar ridicarea personală din Turț este la îndemână.')
add('MH', 'Mehedinți', 'Drobeta-Turnu Severin', (44.627, 22.656), 'Orșova, Strehaia, Vânju Mare și Baia de Aramă',
    'hidroenergie, construcții navale și de vagoane, agricultură',
    ['CS', 'GJ', 'DJ'], 'Sud-Vest Oltenia', s='mehedinti')
add('MS', 'Mureș', 'Târgu Mureș', (46.542, 24.558), 'Reghin, Sighișoara, Târnăveni, Luduș și Iernut',
    'industria chimică, energie, componente și prelucrări mecanice, industria lemnului',
    ['BN', 'SV', 'HR', 'BV', 'SB', 'AB', 'CJ'], 'Centru', s='mures')
add('NT', 'Neamț', 'Piatra Neamț', (46.927, 26.371), 'Roman, Târgu Neamț, Bicaz și Roznov',
    'siderurgie și producția de țevi, chimie, industria lemnului și prelucrări mecanice',
    ['SV', 'IS', 'VS', 'BC', 'HR'], 'Nord-Est', s='neamt')
add('OT', 'Olt', 'Slatina', (44.430, 24.371), 'Caracal, Balș, Corabia, Scornicești și Drăgănești-Olt',
    'industria aluminiului, componente auto și anvelope, prelucrări metalice și agricultură',
    ['DJ', 'VL', 'AG', 'TR'], 'Sud-Vest Oltenia', s='olt')
add('PH', 'Prahova', 'Ploiești', (44.946, 26.036), 'Câmpina, Sinaia, Băicoi, Mizil, Breaza, Vălenii de Munte și Bușteni',
    'rafinare și echipamente pentru industria petrolieră, rulmenți și componente, parcuri industriale',
    ['BV', 'BZ', 'IL', 'IF', 'DB'], 'Sud-Muntenia', s='prahova')
add('SM', 'Satu Mare', 'Satu Mare', (47.790, 22.885), 'Carei, Negrești-Oaș, Tășnad, Livada, Ardud, Halmeu și Turț',
    'componente auto și cablaje, prelucrări metalice, industria alimentară și agricultură',
    ['MM', 'SJ', 'BH'], 'Nord-Vest', s='satu-mare')
add('SJ', 'Sălaj', 'Zalău', (47.192, 23.057), 'Șimleu Silvaniei, Jibou, Cehu Silvaniei și Ileanda',
    'producția de anvelope și cabluri, componente industriale și prelucrări metalice',
    ['SM', 'MM', 'CJ', 'BH'], 'Nord-Vest', s='salaj',
    extra='Sălajul se învecinează cu județul Satu Mare, astfel că termenele de transport sunt foarte scurte.')
add('SB', 'Sibiu', 'Sibiu', (45.793, 24.152), 'Mediaș, Cisnădie, Avrig, Agnita, Copșa Mică și Dumbrăveni',
    'componente auto și industria prelucrătoare, construcții de mașini, gaze naturale și energie',
    ['AB', 'MS', 'BV', 'AG', 'VL', 'HD'], 'Centru', s='sibiu')
add('SV', 'Suceava', 'Suceava', (47.651, 26.255), 'Fălticeni, Rădăuți, Câmpulung Moldovenesc, Vatra Dornei, Gura Humorului și Siret',
    'industria lemnului și a mobilei, prelucrări metalice, echipamente și agricultură',
    ['MM', 'BN', 'MS', 'HR', 'NT', 'IS', 'BT'], 'Nord-Est', s='suceava')
add('TR', 'Teleorman', 'Alexandria', (43.969, 25.333), 'Roșiorii de Vede, Turnu Măgurele, Zimnicea și Videle',
    'agricultură și mecanizare agricolă, industria alimentară, rulmenți și componente',
    ['OT', 'AG', 'DB', 'GR'], 'Sud-Muntenia', s='teleorman')
add('TM', 'Timiș', 'Timișoara', (45.748, 21.208), 'Lugoj, Sânnicolau Mare, Jimbolia, Buziaș, Deta și Recaș',
    'componente auto și electronice, IT și inginerie, parcuri industriale și agricultură',
    ['AR', 'HD', 'CS'], 'Vest', s='timis')
add('TL', 'Tulcea', 'Tulcea', (45.179, 28.805), 'Babadag, Măcin, Isaccea și Sulina',
    'construcții navale, activitate portuară pe Dunăre, metalurgie și pescuit',
    ['CT', 'BR', 'GL'], 'Sud-Est', s='tulcea')
add('VS', 'Vaslui', 'Vaslui', (46.640, 27.729), 'Bârlad, Huși și Negrești',
    'rulmenți și prelucrări mecanice, industria ușoară și agricultură',
    ['IS', 'NT', 'BC', 'VN', 'GL'], 'Nord-Est', s='vaslui')
add('VL', 'Vâlcea', 'Râmnicu Vâlcea', (45.100, 24.369), 'Drăgășani, Băbeni, Horezu, Brezoi, Călimănești și Ocnele Mari',
    'industria chimică, hidroenergie, prelucrări mecanice și componente',
    ['SB', 'AG', 'OT', 'DJ', 'GJ', 'HD'], 'Sud-Vest Oltenia', s='valcea')
add('VN', 'Vrancea', 'Focșani', (45.697, 27.186), 'Adjud, Mărășești, Odobești și Panciu',
    'industria alimentară și viticultură, prelucrarea lemnului, componente și echipamente',
    ['BC', 'VS', 'GL', 'BR', 'BZ', 'CV'], 'Sud-Est', s='vrancea')
add('B', 'București', 'București', (44.426, 26.103), 'toate cele șase sectoare, Voluntari, Otopeni, Pantelimon, Popești-Leordeni și Chiajna',
    'inginerie și echipamente industriale, energie, cercetare, producție și mentenanță',
    ['IF'], 'București-Ilfov', slug='prelucrari-cnc-bucuresti')
# București non è un județ: forme dedicate
J['B'].update(jud='zona metropolitană', injud='în București', seatin='în București', tot='toată zona metropolitană')



# ======================================================================== TESTI RO
RO = dict(
 title='Prelucrări CNC {seat} ({name}) | Strunjire și frezare – DajbocTechDon',
 title_same='Prelucrări CNC {seat} | Strunjire și frezare CNC – DajbocTechDon',
 title_b='Prelucrări CNC București | Strunjire, Frezare, Utilaje – DajbocTechDon',
 title_home='Prelucrări CNC Satu Mare | Strunjire și Frezare CNC – DajbocTechDon',
 desc='Strunjire și frezare CNC, piese metalice și utilaje la comandă pentru firme din {seat} și {jud}. Livrare în {days}. Cereți ofertă.',
 svc_name='Prelucrări CNC și utilaje la comandă – {name}',
 h1='Prelucrări CNC și piese metalice la comandă <span class="gt">pentru {seat} și {jud}</span>',
 badge='Atelier în Satu Mare · livrare {injud}',
 lead='DajbocTechDon S.R.L. execută strunjire și frezare CNC, piese metalice de precizie, prototipuri, piese de schimb și utilaje la comandă în atelierul propriu din Turț, județul Satu Mare. Lucrăm pentru firme din {seat} și din {tot} – inclusiv {towns}.',
 lead_home='DajbocTechDon S.R.L. are atelierul de prelucrări mecanice CNC în Turț, chiar în județul Satu Mare. Executăm strunjire și frezare CNC, piese metalice de precizie, prototipuri, piese de schimb și utilaje la comandă pentru firme din municipiul Satu Mare, Carei, Negrești-Oaș, Tășnad și din tot județul – cu posibilitate de ridicare personală din atelier.',
 cta_quote='Cereți o ofertă', cta_services='Serviciile noastre',
 f_dist='Turț – {seat}', f_dist_v='≈ {km} km în linie dreaptă',
 f_transit='Termen de livrare', f_transit_v='{days}',
 f_pay='Facturare', f_pay_v='RON sau EUR · firmă românească',
 f_series='Cantități', f_series_v='de la 1 bucată la serii medii',
 svc_tag='Ce facem', svc_title='Servicii de prelucrări CNC {injud}',
 svc_intro='Un singur partener pentru tot lanțul – de la cerințe și proiectare până la piesa finită, testată și livrată {seatin}.',
 svc=[('Colectarea cerințelor', 'Stabilim împreună obiectivele, toleranțele, materialele și cantitățile înainte de proiectare.'),
      ('Proiectare mecanică', 'Proiectăm piese, dispozitive și utilaje la comandă pentru industria auto, industrială, agricolă și energetică.'),
      ('Simulare', 'Verificăm capacitatea, conformitatea și rezistența proiectului înainte de producție.'),
      ('Strunjire și frezare CNC', 'Prelucrări mecanice CNC de precizie ale pieselor metalice, integral în atelierul propriu.'),
      ('Asamblare', 'Asamblăm piesele prelucrate și componentele achiziționate în subansambluri și produse finite.'),
      ('Controlul producției', 'Gestionăm întregul proces, cu control al calității la fiecare etapă.'),
      ('Testare', 'Control dimensional și funcțional, astfel încât fiecare piesă să respecte cerințele de siguranță și performanță.'),
      ('Livrare', 'Ambalare, documente și transport până la sediul sau fabrica dumneavoastră.')],
 ind_tag='Industrii', ind_title='Pentru industria din {jud}',
 ind_intro='Printre domeniile industriale reprezentative pentru {jud} se numără {sectors}. Pentru firmele din aceste sectoare executăm componente, piese de schimb și utilaje:',
 ind=[('Industria auto', 'Piese strunjite și frezate de precizie, dispozitive și subansambluri pentru producători și furnizori.'),
      ('Industrie și mentenanță', 'Utilaje la comandă, dispozitive de prindere, calibre și piese de schimb pentru linii de producție.'),
      ('Agricultură', 'Componente și piese de schimb pentru utilaje agricole, construite pentru condiții grele.'),
      ('Energie', 'Piese și subansambluri pentru producția de energie și infrastructura energetică.')],
 why_tag='De ce DajbocTechDon', why_title='De ce să lucrați cu noi',
 why=['Totul într-un singur atelier: proiectare, simulare, prelucrare CNC, asamblare și testare.',
      'Prototipuri, piese unicat, piese de schimb, serii mici și medii – fără cantități minime mari.',
      'Comunicare directă, în limba română, cu inginerii care vă execută piesele.',
      'Firmă românească: facturare în RON sau EUR, documente conforme și termene clare.',
      'Livrare rapidă {injud} prin curier sau transport dedicat.'],
 img_alt='Prelucrări CNC în atelierul DajbocTechDon din Turț, Satu Mare – piese pentru {seat}',
 how_tag='Cum lucrăm', how_title='De la desen la piesă în patru pași',
 how=[('Trimiteți cererea', 'Desen sau model 3D (PDF, STEP, IGES, DXF), material, cantitate și termenul dorit.'),
      ('Primiți oferta', 'Analizăm fezabilitatea și vă comunicăm prețul și termenul de execuție.'),
      ('Execuție', 'Prelucrare CNC, asamblare și testare în atelierul nostru, cu control al calității la fiecare pas.'),
      ('Livrare', 'Piesele ambalate și documentate ajung la adresa dumneavoastră.')],
 log_tag='Livrare', log_title='Livrare în {seat} și {jud}',
 log_ps=['Atelierul nostru se află în Turț, județul Satu Mare, la aproximativ {km} km în linie dreaptă de {seat}. Piesele mici și urgente pleacă prin curier rapid, iar subansamblurile și utilajele prin transport dedicat; termenul uzual de livrare {injud} este de {days} de la finalizarea comenzii.',
         'Livrăm în {tot}, inclusiv în {towns}. Condițiile de livrare (ridicare din atelier, livrare la sediu sau la punct de lucru) se stabilesc în ofertă. Piesele sunt curățate, protejate anticoroziv la nevoie și ambalate pentru transport, însoțite de documentele de livrare și, la cerere, de rapoarte de control.'],
 faq_title='Întrebări frecvente – {name}',
 faq=[('Livrați piese prelucrate CNC {seatin}?', 'Da. Livrăm piese strunjite și frezate, subansambluri și utilaje {seatin} și în {tot} ({towns}). Termenul uzual de transport este de {days} de la finalizarea comenzii.'),
      ('Ce informații vă trebuie pentru o ofertă de preț?', 'Un desen tehnic sau un model 3D (PDF, STEP, IGES sau DXF), materialul, cantitatea și termenul dorit. Dacă aveți doar o piesă uzată sau o idee, pornim de la cerințe, facem releveul și proiectăm piesa pentru dumneavoastră.'),
      ('Executați piese unicat și piese de schimb?', 'Da. Executăm prototipuri, piese unicat, piese de schimb pentru utilaje și serii mici și medii. Fiecare piesă este prelucrată și verificată în atelierul propriu.'),
      ('Puteți proiecta și construi un utilaj la comandă?', 'Da. Gestionăm tot ciclul: cerințe, proiectare, simulare, prelucrare CNC, asamblare, testare și livrare – potrivit pentru firme din industria auto, industrială, agricolă și energetică din {jud}.'),
      ('Cum pot cere o ofertă?', 'Completați formularul de pe această pagină, scrieți la contact@dajboctechdon.com sau sunați la +40 744 987 550. Revenim cu prețul și termenul de execuție.')],
 faq_home=[('Unde se află atelierul de prelucrări CNC?', 'Atelierul DajbocTechDon se află pe Str. Valceleni nr. 69, Turț, județul Satu Mare (cod poștal 447330). Program: luni–sâmbătă, 09:00–18:00.'),
      ('Livrați în municipiul Satu Mare, Carei și Negrești-Oaș?', 'Da. Livrăm în tot județul Satu Mare – municipiul Satu Mare, Carei, Negrești-Oaș, Tășnad, Livada, Ardud, Halmeu și comunele din jur –, de regulă {days}. Piesele pot fi ridicate și personal din atelier.'),
      ('Ce informații vă trebuie pentru o ofertă de preț?', 'Un desen tehnic sau un model 3D (PDF, STEP, IGES sau DXF), materialul, cantitatea și termenul dorit. Dacă aveți doar o piesă uzată sau o idee, pornim de la cerințe, facem releveul și proiectăm piesa.'),
      ('Executați piese unicat și piese de schimb?', 'Da. Executăm prototipuri, piese unicat, piese de schimb pentru utilaje agricole și industriale și serii mici și medii, toate prelucrate și verificate în atelierul propriu.'),
      ('Puteți proiecta și construi un utilaj la comandă?', 'Da. Gestionăm tot ciclul: cerințe, proiectare, simulare, prelucrare CNC, asamblare, testare și livrare.')],
 con_tag='Contact', con_title='Cereți o ofertă de preț',
 con_p='Trimiteți-ne desenul și cerințele – revenim cu prețul și termenul de execuție și livrare {seatin}.',
 more_title='Livrăm și în județele vecine',
 bc_page='{name}',
)

JUDETE = J
