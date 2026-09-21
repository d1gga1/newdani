# -*- coding: utf-8 -*-
"""
Dati per paese delle landing page europee.

forms:  n   = nome usato a metà frase (con articolo se serve)
        nom = nome a inizio frase (default: n con maiuscola)
        N   = etichetta breve / endonimo (default: nom)
        in  = "in <paese>"      to = "verso <paese>"
city / city_geo = città di riferimento per la distanza dal laboratorio di Turț
city_log        = forma declinata della città dove la grammatica lo richiede
customs: eu | eea | fta | cu | saa | dcfta | mc
days:    sovrascrive il tempo di transito calcolato
extra:   paragrafo aggiuntivo (nella lingua della pagina) nella sezione logistica
"""

C = []
def add(**k):
    f = k['forms']
    f.setdefault('nom', f['n'][0].upper() + f['n'][1:])
    f.setdefault('N', f['nom'])
    C.append(k)

# ================================================================ UNIONE EUROPEA
add(iso='DE', en='Germany', lang='de', hreflang='de-DE', og='de_DE', slug='cnc-bearbeitung-deutschland', customs='eu',
    forms=dict(n='Deutschland', **{'in': 'in Deutschland', 'to': 'nach Deutschland'}),
    city='Berlin', city_geo=(52.52, 13.405),
    hubs='Bayern, Baden-Württemberg, Nordrhein-Westfalen, Niedersachsen und Sachsen',
    sectors='Automobil- und Zulieferindustrie, Maschinen- und Anlagenbau, Elektrotechnik und Landtechnik')

add(iso='AT', en='Austria', lang='de', hreflang='de-AT', og='de_AT', slug='cnc-bearbeitung-oesterreich', customs='eu',
    forms=dict(n='Österreich', **{'in': 'in Österreich', 'to': 'nach Österreich'}),
    city='Wien', city_geo=(48.208, 16.372),
    hubs='Oberösterreich, die Steiermark, Niederösterreich und Vorarlberg',
    sectors='Maschinen- und Anlagenbau, Fahrzeug- und Zulieferindustrie, Metallverarbeitung und Energietechnik')

add(iso='FR', en='France', lang='fr', hreflang='fr-FR', og='fr_FR', slug='usinage-cnc-france', customs='eu',
    forms=dict(n='la France', N='France', **{'in': 'en France', 'to': 'en France'}),
    city='Paris', city_geo=(48.857, 2.352),
    hubs='l’Auvergne-Rhône-Alpes, les Hauts-de-France, le Grand Est, l’Occitanie et les Pays de la Loire',
    sectors='l’aéronautique, l’automobile, la mécanique, le ferroviaire et l’énergie')

add(iso='BE', en='Belgium (French)', lang='fr', hreflang='fr-BE', og='fr_BE', slug='usinage-cnc-belgique', customs='eu',
    forms=dict(n='la Belgique', N='Belgique', **{'in': 'en Belgique', 'to': 'en Belgique'}),
    city='Bruxelles', city_geo=(50.85, 4.35),
    hubs='la Wallonie (Liège, Charleroi, Mons), la Flandre et la région bruxelloise',
    sectors='la chimie, la mécanique et la métallurgie, l’automobile, l’agroalimentaire et la logistique')

add(iso='BE', en='Belgium (Dutch)', lang='nl', hreflang='nl-BE', og='nl_BE', slug='cnc-verspaning-belgie', customs='eu',
    forms=dict(n='België', **{'in': 'in België', 'to': 'naar België'}),
    city='Brussel', city_geo=(50.85, 4.35),
    hubs='Antwerpen, Gent, Limburg en West-Vlaanderen',
    sectors='chemie, metaalverwerking en machinebouw, automotive, voeding en logistiek')

add(iso='NL', en='Netherlands', lang='nl', hreflang='nl-NL', og='nl_NL', slug='cnc-verspaning-nederland', customs='eu',
    forms=dict(n='Nederland', **{'in': 'in Nederland', 'to': 'naar Nederland'}),
    city='Amsterdam', city_geo=(52.37, 4.90),
    hubs='Noord-Brabant (regio Eindhoven), Zuid-Holland, Gelderland en Overijssel',
    sectors='hightech- en machinebouw, halfgeleiderapparatuur, voedingsmiddelenindustrie en de maritieme en offshoresector')

add(iso='LU', en='Luxembourg', lang='fr', hreflang='fr-LU', og='fr_LU', slug='usinage-cnc-luxembourg', customs='eu',
    forms=dict(n='le Luxembourg', N='Luxembourg', **{'in': 'au Luxembourg', 'to': 'au Luxembourg'}),
    city='Luxembourg', city_geo=(49.61, 6.13),
    hubs='Esch-sur-Alzette, Luxembourg-Ville, Differdange et le nord du pays',
    sectors='la sidérurgie et la métallurgie, les composants automobiles, les matériaux et la logistique')

add(iso='IT', en='Italy', lang='it', hreflang='it-IT', og='it_IT', slug='lavorazioni-cnc-italia', customs='eu',
    forms=dict(n='l’Italia', nom='L’Italia', N='Italia', **{'in': 'in Italia', 'to': 'in Italia'}),
    city='Milano', city_geo=(45.464, 9.19),
    hubs='Lombardia, Veneto, Emilia-Romagna e Piemonte',
    sectors='meccanica strumentale e macchine utensili, automotive e componentistica, macchine agricole e oleodinamica')

add(iso='ES', en='Spain', lang='es', hreflang='es-ES', og='es_ES', slug='mecanizado-cnc-espana', customs='eu',
    forms=dict(n='España', **{'in': 'en España', 'to': 'a España'}),
    city='Madrid', city_geo=(40.417, -3.704),
    hubs='Cataluña, el País Vasco, Navarra, la Comunidad Valenciana, Aragón y Madrid',
    sectors='la automoción, la maquinaria y los bienes de equipo, la industria agroalimentaria y las energías renovables')

add(iso='PT', en='Portugal', lang='pt', hreflang='pt-PT', og='pt_PT', slug='maquinacao-cnc-portugal', customs='eu',
    forms=dict(n='Portugal', **{'in': 'em Portugal', 'to': 'para Portugal'}),
    city='Lisboa', city_geo=(38.722, -9.139),
    hubs='o Norte (Porto, Braga, Aveiro), a região de Leiria e a Grande Lisboa',
    sectors='componentes automóveis, moldes e metalomecânica, agroindústria e energias renováveis')

add(iso='IE', en='Ireland', lang='en', hreflang='en-IE', og='en_IE', slug='cnc-machining-ireland', customs='eu',
    forms=dict(n='Ireland', **{'in': 'in Ireland', 'to': 'to Ireland'}),
    city='Dublin', city_geo=(53.35, -6.26), days='4–6',
    hubs='Dublin, Cork, Galway, Limerick and the Midlands',
    sectors='medical devices, pharmaceuticals, food processing and precision engineering')

add(iso='MT', en='Malta', lang='en', hreflang='en-MT', og='en_MT', slug='cnc-machining-malta', customs='eu',
    forms=dict(n='Malta', **{'in': 'in Malta', 'to': 'to Malta'}),
    city='Valletta', city_geo=(35.899, 14.514), days='5–8',
    hubs='Hal Far, Bulebel, Marsa and the Grand Harbour area',
    sectors='electronics, pharmaceuticals, aircraft maintenance and marine engineering',
    extra='Shipments to Malta travel by road to an Italian port and then by ferry; small urgent parts can also be sent by air express.')

add(iso='PL', en='Poland', lang='pl', hreflang='pl-PL', og='pl_PL', slug='obrobka-cnc-polska', customs='eu',
    forms=dict(n='Polska', **{'in': 'w Polsce', 'to': 'do Polski'}),
    city='Warszawa', city_geo=(52.23, 21.01),
    hubs='Śląsk, Wielkopolska, Dolny Śląsk i Podkarpacie (Dolina Lotnicza)',
    sectors='motoryzacja, przemysł maszynowy, produkcja AGD i przemysł lotniczy')

add(iso='CZ', en='Czechia', lang='cs', hreflang='cs-CZ', og='cs_CZ', slug='cnc-obrabeni-cesko', customs='eu',
    forms=dict(n='Česko', **{'in': 'v Česku', 'to': 'do Česka'}),
    city='Praha', city_geo=(50.075, 14.437),
    hubs='Mladá Boleslav, Plzeň, Brno, Ostrava a Zlín',
    sectors='automobilový průmysl, strojírenství, elektrotechnika a hutnictví')

add(iso='SK', en='Slovakia', lang='sk', hreflang='sk-SK', og='sk_SK', slug='cnc-obrabanie-slovensko', customs='eu',
    forms=dict(n='Slovensko', **{'in': 'na Slovensku', 'to': 'na Slovensko'}),
    city='Bratislava', city_geo=(48.148, 17.107),
    hubs='Bratislava, Trnava, Žilina, Nitra a Košice',
    sectors='automobilový priemysel, strojárstvo, elektrotechnika a hutníctvo')

add(iso='HU', en='Hungary', lang='hu', hreflang='hu-HU', og='hu_HU', slug='cnc-megmunkalas-magyarorszag', customs='eu',
    forms=dict(n='Magyarország', **{'in': 'Magyarországon', 'to': 'Magyarországra'}),
    city='Budapest', city_geo=(47.498, 19.04),
    hubs='Győr, Kecskemét, Debrecen, Nyíregyháza és Budapest térsége',
    sectors='az autóipar, a gépgyártás, az elektronika és a mezőgazdasági gépgyártás',
    extra='Műhelyünk mindössze néhány tíz kilométerre van a magyar határtól, így a kelet-magyarországi – például nyíregyházi, mátészalkai vagy debreceni – ügyfeleinkhez rövid idő alatt, akár egy napon belül is eljuthatnak az alkatrészek.')

add(iso='SI', en='Slovenia', lang='sl', hreflang='sl-SI', og='sl_SI', slug='cnc-obdelava-slovenija', customs='eu',
    forms=dict(n='Slovenija', **{'in': 'v Sloveniji', 'to': 'v Slovenijo'}),
    city='Ljubljana', city_geo=(46.056, 14.506),
    hubs='Ljubljana, Maribor, Celje, Novo mesto in Kranj',
    sectors='avtomobilska industrija, kovinskopredelovalna industrija, elektroindustrija in orodjarstvo')

add(iso='HR', en='Croatia', lang='hr', hreflang='hr-HR', og='hr_HR', slug='cnc-obrada-hrvatska', customs='eu',
    forms=dict(n='Hrvatska', **{'in': 'u Hrvatskoj', 'to': 'u Hrvatsku'}),
    city='Zagreb', city_geo=(45.815, 15.982),
    hubs='Zagreb, Varaždin, Rijeka, Osijek i Split',
    sectors='metaloprerađivačka industrija, brodogradnja, prehrambena industrija i energetika')

add(iso='BG', en='Bulgaria', lang='bg', hreflang='bg-BG', og='bg_BG', slug='cnc-obrabotka-bulgaria', customs='eu',
    forms=dict(n='България', **{'in': 'в България', 'to': 'до България'}),
    city='София', city_geo=(42.698, 23.322),
    hubs='София, Пловдив, Русе, Стара Загора и Варна',
    sectors='машиностроене, автомобилни компоненти, електротехника и енергетика')

add(iso='GR', en='Greece', lang='el', hreflang='el-GR', og='el_GR', slug='katergasies-cnc-ellada', customs='eu',
    forms=dict(n='Ελλάδα', nom='Η Ελλάδα', N='Ελλάδα', **{'in': 'στην Ελλάδα', 'to': 'στην Ελλάδα'}),
    city='Αθήνα', city_log='την Αθήνα', city_geo=(37.984, 23.728),
    hubs='η Αττική, η Θεσσαλονίκη, η Βοιωτία και η Θεσσαλία',
    sectors='μεταλλουργία και μεταλλικές κατασκευές, ναυπηγοεπισκευή, τρόφιμα και ενέργεια')

add(iso='CY', en='Cyprus', lang='el', hreflang='el-CY', og='el_CY', slug='katergasies-cnc-kypros', customs='eu',
    forms=dict(n='Κύπρος', nom='Η Κύπρος', N='Κύπρος', **{'in': 'στην Κύπρο', 'to': 'στην Κύπρο'}),
    city='Λευκωσία', city_log='τη Λευκωσία', city_geo=(35.185, 33.382), days='6–9',
    hubs='η Λευκωσία, η Λεμεσός, η Λάρνακα και η Πάφος',
    sectors='ναυτιλία, κατασκευές, ενέργεια και τρόφιμα',
    extra='Οι αποστολές προς την Κύπρο γίνονται οδικώς έως ελληνικό λιμάνι και στη συνέχεια με θαλάσσια μεταφορά· μικρά επείγοντα εξαρτήματα μπορούν να σταλούν και με αεροπορική ταχυμεταφορά.')

add(iso='SE', en='Sweden', lang='sv', hreflang='sv-SE', og='sv_SE', slug='cnc-bearbetning-sverige', customs='eu',
    forms=dict(n='Sverige', **{'in': 'i Sverige', 'to': 'till Sverige'}),
    city='Stockholm', city_geo=(59.329, 18.069),
    hubs='Västra Götaland, Stockholm–Mälardalen, Småland och Skåne',
    sectors='fordonsindustri, verkstadsindustri, gruv- och stålindustri samt energiteknik')

add(iso='DK', en='Denmark', lang='da', hreflang='da-DK', og='da_DK', slug='cnc-bearbejdning-danmark', customs='eu',
    forms=dict(n='Danmark', **{'in': 'i Danmark', 'to': 'til Danmark'}),
    city='København', city_geo=(55.676, 12.568),
    hubs='Midtjylland, Syddanmark, Nordjylland og Hovedstadsområdet',
    sectors='vindenergi, fødevare- og procesindustri, maskinindustri og medicoteknik')

add(iso='FI', en='Finland', lang='fi', hreflang='fi-FI', og='fi_FI', slug='cnc-koneistus-suomi', customs='eu',
    forms=dict(n='Suomi', **{'in': 'Suomessa', 'to': 'Suomeen'}),
    city='Helsinki', city_log='Helsingistä', city_geo=(60.17, 24.94),
    hubs='Pirkanmaa, Pohjanmaa, Varsinais-Suomi ja pääkaupunkiseutu',
    sectors='kone- ja metalliteollisuus, metsäteollisuus, energia ja meriteollisuus')

add(iso='EE', en='Estonia', lang='et', hreflang='et-EE', og='et_EE', slug='cnc-tootlus-eesti', customs='eu',
    forms=dict(n='Eesti', **{'in': 'Eestis', 'to': 'Eestisse'}),
    city='Tallinn', city_log='Tallinnast', city_geo=(59.437, 24.754),
    hubs='Tallinn, Tartu, Pärnu ja Ida-Virumaa',
    sectors='metalli- ja masinatööstus, elektroonika, puidutööstus ja energeetika')

add(iso='LV', en='Latvia', lang='lv', hreflang='lv-LV', og='lv_LV', slug='cnc-apstrade-latvija', customs='eu',
    forms=dict(n='Latvija', **{'in': 'Latvijā', 'to': 'uz Latviju'}),
    city='Rīga', city_log='Rīgas', city_geo=(56.949, 24.106),
    hubs='Rīga, Liepāja, Ventspils, Daugavpils un Valmiera',
    sectors='metālapstrāde un mašīnbūve, kokapstrāde, pārtikas rūpniecība un loģistika')

add(iso='LT', en='Lithuania', lang='lt', hreflang='lt-LT', og='lt_LT', slug='cnc-apdirbimas-lietuva', customs='eu',
    forms=dict(n='Lietuva', **{'in': 'Lietuvoje', 'to': 'į Lietuvą'}),
    city='Vilnius', city_log='Vilniaus', city_geo=(54.687, 25.28),
    hubs='Vilnių, Kauną, Klaipėdą ir Šiaulius',
    sectors='metalo apdirbimas ir mašinų gamyba, lazerių technologijos, baldų ir maisto pramonė')

# ================================================================ EEA / CH / UK
add(iso='GB', en='United Kingdom', lang='en', hreflang='en-GB', og='en_GB', slug='cnc-machining-uk', customs='fta',
    forms=dict(n='the UK', nom='The UK', N='United Kingdom', **{'in': 'in the UK', 'to': 'to the UK'}),
    city='London', city_geo=(51.507, -0.128), days='4–6',
    hubs='the Midlands, the North West, Yorkshire, Wales and Scotland',
    sectors='aerospace, automotive, precision engineering and energy')

add(iso='CH', en='Switzerland (German)', lang='de', hreflang='de-CH', og='de_CH', slug='cnc-bearbeitung-schweiz', customs='fta',
    forms=dict(n='die Schweiz', nom='Die Schweiz', N='Schweiz', **{'in': 'in der Schweiz', 'to': 'in die Schweiz'}),
    city='Zürich', city_geo=(47.377, 8.54), days='3–5',
    hubs='Zürich, Aargau, St. Gallen, Basel und die Region Jura',
    sectors='Präzisionsmechanik, Maschinen-, Elektro- und Metallindustrie (MEM), Medizintechnik und Uhrenindustrie')

add(iso='CH', en='Switzerland (French)', lang='fr', hreflang='fr-CH', og='fr_CH', slug='usinage-cnc-suisse', customs='fta',
    forms=dict(n='la Suisse', N='Suisse', **{'in': 'en Suisse', 'to': 'en Suisse'}),
    city='Genève', city_geo=(46.204, 6.143), days='3–5',
    hubs='l’Arc jurassien, Genève, Vaud, Neuchâtel et le Valais',
    sectors='la microtechnique et l’horlogerie, les machines, les technologies médicales et la mécanique de précision')

add(iso='LI', en='Liechtenstein', lang='de', hreflang='de-LI', og='de_LI', slug='cnc-bearbeitung-liechtenstein', customs='eea',
    forms=dict(n='Liechtenstein', **{'in': 'in Liechtenstein', 'to': 'nach Liechtenstein'}),
    city='Vaduz', city_geo=(47.141, 9.521), days='3–5',
    hubs='Schaan, Vaduz, Balzers und Eschen',
    sectors='Präzisionstechnik, Maschinenbau, Fahrzeugzulieferung und Bautechnik',
    extra='Liechtenstein bildet mit der Schweiz ein gemeinsames Zollgebiet; die Verzollung erfolgt daher nach Schweizer Verfahren, meist über den Grenzübergang Schaanwald oder Buchs.')

add(iso='NO', en='Norway', lang='nb', hreflang='nb-NO', og='nb_NO', slug='cnc-maskinering-norge', customs='eea',
    forms=dict(n='Norge', **{'in': 'i Norge', 'to': 'til Norge'}),
    city='Oslo', city_geo=(59.914, 10.752), days='4–6',
    hubs='Vestlandet, Oslo-regionen, Trøndelag og Sør-Norge',
    sectors='olje og gass, maritim industri, havbruk, aluminium og fornybar energi')

add(iso='IS', en='Iceland', lang='en', hreflang='en-IS', og='en_IS', slug='cnc-machining-iceland', customs='eea',
    forms=dict(n='Iceland', **{'in': 'in Iceland', 'to': 'to Iceland'}),
    city='Reykjavík', city_geo=(64.147, -21.942), days='7–14',
    hubs='the Reykjavík capital region, Akureyri and the East Fjords',
    sectors='fishing and fish processing, aluminium smelting, geothermal energy and marine technology',
    extra='Shipments to Iceland travel by road to a continental port and then by sea freight; small urgent parts can be sent by air express in a few days.')

# ================================================================ MICROSTATI
add(iso='MC', en='Monaco', lang='fr', hreflang='fr-MC', og='fr_MC', slug='usinage-cnc-monaco', customs='mc',
    forms=dict(n='Monaco', **{'in': 'à Monaco', 'to': 'à Monaco'}),
    city='Monaco', city_geo=(43.738, 7.424),
    hubs='Fontvieille et l’ensemble de la Principauté, ainsi que la Côte d’Azur voisine',
    sectors='les industries légères de Fontvieille, le yachting, le bâtiment et les services techniques')

add(iso='SM', en='San Marino', lang='it', hreflang='it-SM', og='it_SM', slug='lavorazioni-cnc-san-marino', customs='cu',
    forms=dict(n='San Marino', **{'in': 'a San Marino', 'to': 'a San Marino'}),
    city='San Marino', city_geo=(43.936, 12.447),
    hubs='Serravalle, Borgo Maggiore, Dogana e le aree produttive della Repubblica',
    sectors='meccanica, lavorazione dei metalli e manifattura')

add(iso='AD', en='Andorra', lang='ca', hreflang='ca-AD', og='ca_AD', slug='mecanitzat-cnc-andorra', customs='cu',
    forms=dict(n='Andorra', **{'in': 'a Andorra', 'to': 'a Andorra'}),
    city='Andorra la Vella', city_geo=(42.507, 1.521),
    hubs='Andorra la Vella, Escaldes-Engordany i la resta de parròquies',
    sectors='la construcció, les instal·lacions de muntanya, l’energia i el manteniment tècnic')

# ================================================================ BALCANI OCC., MD, UA, TR
add(iso='RS', en='Serbia', lang='sr', hreflang='sr-RS', og='sr_RS', slug='cnc-obrada-srbija', customs='saa',
    forms=dict(n='Srbija', **{'in': 'u Srbiji', 'to': 'u Srbiju'}),
    city='Beograd', city_geo=(44.787, 20.457), days='2–4',
    hubs='Beograd, Novi Sad, Kragujevac, Niš i Subotica',
    sectors='automobilska industrija i komponente, metaloprerađivačka industrija, poljoprivreda i energetika')

add(iso='ME', en='Montenegro', lang='sr', hreflang='sr-ME', og='sr_ME', slug='cnc-obrada-crna-gora', customs='saa',
    forms=dict(n='Crna Gora', **{'in': 'u Crnoj Gori', 'to': 'u Crnu Goru'}),
    city='Podgorica', city_geo=(42.441, 19.263), days='3–5',
    hubs='Podgorica, Nikšić, Bar i Pljevlja',
    sectors='energetika, metalurgija, brodogradnja i građevinarstvo')

add(iso='BA', en='Bosnia and Herzegovina', lang='bs', hreflang='bs-BA', og='bs_BA', slug='cnc-obrada-bosna-i-hercegovina', customs='saa',
    forms=dict(n='Bosna i Hercegovina', **{'in': 'u Bosni i Hercegovini', 'to': 'u Bosnu i Hercegovinu'}),
    city='Sarajevo', city_geo=(43.856, 18.413), days='3–5',
    hubs='Sarajevo, Zenica, Tuzla, Banja Luka i Mostar',
    sectors='metaloprerađivačka i automobilska industrija, drvna industrija i energetika')

add(iso='MK', en='North Macedonia', lang='mk', hreflang='mk-MK', og='mk_MK', slug='cnc-obrabotka-severna-makedonija', customs='saa',
    forms=dict(n='Северна Македонија', **{'in': 'во Северна Македонија', 'to': 'во Северна Македонија'}),
    city='Скопје', city_geo=(41.998, 21.425), days='3–5',
    hubs='Скопје, Битола, Штип, Тетово и технолошко-индустриските развојни зони',
    sectors='автомобилски компоненти, металопреработувачка индустрија, земјоделство и енергетика')

add(iso='AL', en='Albania', lang='sq', hreflang='sq-AL', og='sq_AL', slug='perpunim-cnc-shqiperi', customs='saa',
    forms=dict(n='Shqipëria', **{'in': 'në Shqipëri', 'to': 'në Shqipëri'}),
    city='Tirana', city_geo=(41.328, 19.819), days='3–5',
    hubs='Tirana, Durrësi, Elbasani, Fieri dhe Shkodra',
    sectors='energjia, industria nxjerrëse dhe përpunuese, ndërtimi dhe bujqësia')

add(iso='XK', en='Kosovo', lang='sq', hreflang='sq', og='sq_XK', slug='perpunim-cnc-kosove', customs='saa',
    forms=dict(n='Kosova', **{'in': 'në Kosovë', 'to': 'në Kosovë'}),
    city='Prishtina', city_geo=(42.663, 21.166), days='3–5',
    hubs='Prishtina, Prizreni, Ferizaj, Peja dhe Mitrovica',
    sectors='përpunimi i metaleve, ndërtimi, energjia dhe bujqësia')

add(iso='MD', en='Moldova', lang='ro', hreflang='ro-MD', og='ro_MD', slug='prelucrari-cnc-moldova', customs='dcfta',
    forms=dict(n='Republica Moldova', **{'in': 'în Republica Moldova', 'to': 'în Republica Moldova'}),
    city='Chișinău', city_geo=(47.011, 28.863), days='2–3',
    hubs='Chișinău, Bălți, Ungheni, Cahul și zonele economice libere',
    sectors='industria alimentară și vinicolă, componente auto și cablaje, agricultură și construcții')

add(iso='UA', en='Ukraine', lang='uk', hreflang='uk-UA', og='uk_UA', slug='cnc-obrobka-ukraina', customs='dcfta',
    forms=dict(n='Україна', **{'in': 'в Україні', 'to': 'в Україну'}),
    city='Київ', city_geo=(50.45, 30.523), days='3–7',
    hubs='Закарпаття, Львів, Київ і Дніпро',
    sectors='машинобудування, металургія, аграрний сектор та енергетика',
    extra='Наш цех розташований неподалік від румунсько-українського кордону (пункт пропуску Халмеу – Дякове), тож Закарпаття та захід України знаходяться від нас на невеликій відстані.')

add(iso='TR', en='Türkiye', lang='tr', hreflang='tr-TR', og='tr_TR', slug='cnc-isleme-turkiye', customs='cu',
    forms=dict(n='Türkiye', **{'in': "Türkiye'de", 'to': "Türkiye'ye"}),
    city='İstanbul', city_geo=(41.008, 28.978), days='3–5',
    hubs='İstanbul, Kocaeli, Bursa, İzmir ve Ankara',
    sectors='otomotiv ve yan sanayi, makine imalatı, beyaz eşya ve savunma sanayii')

COUNTRIES = C
