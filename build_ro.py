#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_ro.py — genereaza / genera la versione rumena statica del sito.

index.html (EN) e' la sorgente. Questo script applica le traduzioni RO
contenute nell'oggetto T dentro index.html e scrive ro/index.html con
HTML gia' tradotto lato server (indicizzabile da Google), meta tag,
hreflang e JSON-LD in rumeno.

Uso:  python3 build_ro.py
Da rilanciare ogni volta che si modifica index.html.
"""
import io, os, re, json, subprocess, sys

SRC = 'index.html'
OUT_DIR = 'ro'
OUT = os.path.join(OUT_DIR, 'index.html')

# ---------------------------------------------------------------- traduzioni
def load_translations():
    """Estrae l'oggetto T da index.html usando node (parsing affidabile)."""
    js = r'''
const fs=require('fs');
const html=fs.readFileSync('index.html','utf8');
const i=html.indexOf('const T = {');
const j=html.indexOf('\nconst typeWords', i);
const src=html.slice(i,j).replace(/^const T = /,'').replace(/;\s*$/,'');
const T=eval('('+src+')');
process.stdout.write(JSON.stringify(T));
'''
    p = subprocess.run(['node','-e',js], capture_output=True, text=True)
    if p.returncode: sys.exit('node error: '+p.stderr)
    return json.loads(p.stdout)

# ------------------------------------------------- sostituzione [data-i18n]
TAG_RE = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*\bdata-i18n="([^"]+)"[^>]*>')

def find_close(html, start, tag):
    depth, i = 1, start
    o_re = re.compile(r'<%s\b' % tag, re.I)
    c_re = re.compile(r'</%s\s*>' % tag, re.I)
    while True:
        o, c = o_re.search(html, i), c_re.search(html, i)
        if not c: return None
        if o and o.start() < c.start():
            depth += 1; i = o.end()
        else:
            depth -= 1
            if depth == 0: return c.start()
            i = c.end()

def translate(html, T):
    out, pos, missing = [], 0, []
    for m in TAG_RE.finditer(html):
        if m.start() < pos: continue
        tag, key = m.group(1), m.group(2)
        close = find_close(html, m.end(), tag)
        if close is None: continue
        inner = html[m.end():close]
        val = T.get(key)
        if val is None:
            missing.append(key); continue
        if '<svg' in inner:                      # conserva l'icona SVG
            val = val + ' ' + inner[inner.index('<svg'):]
        out.append(html[pos:m.end()]); out.append(val)
        pos = close
    out.append(html[pos:])
    if missing: print('  ! chiavi mancanti:', sorted(set(missing)))
    return ''.join(out)

# ------------------------------------------------------------------ JSON-LD
ORG_ID = "https://dajboctechdon.com/#organization"
SITE_ID = "https://dajboctechdon.com/#website"
RO_URL = "https://dajboctechdon.com/ro/"

SERVICES_RO = [
 ("Colectarea informațiilor și a cerințelor","Stabilirea obiectivelor proiectului, colectarea, documentarea și confirmarea cerințelor clientului înainte de începerea proiectării."),
 ("Proiectare mecanică","Proiectare de produse și utilaje la comandă pentru industria auto, industrială, agricolă și energetică."),
 ("Simulare","Simulare și verificare a capacității, conformității și rezistenței fiecărui design înainte de producție."),
 ("Prelucrări CNC și fabricare","Strunjire, frezare și prelucrări mecanice CNC de precizie ale componentelor metalice, realizate integral intern."),
 ("Asamblare","Asamblarea pieselor prelucrate în produse finite complete și testate."),
 ("Control al producției","Gestionarea completă a procesului de producție, cu control al calității în fiecare etapă."),
 ("Testare","Testare riguroasă a componentelor și ansamblurilor conform standardelor de siguranță și performanță."),
 ("Livrare și logistică","Gestionarea completă a logisticii pentru livrarea produselor asamblate în siguranță și la timp."),
]

def ro_jsonld(T):
    faq = []
    for i in range(1, 20):
        q, a = T.get('faq.q%d' % i), T.get('faq.a%d' % i)
        if not q: break
        faq.append({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}})
    org = {
      "@type":["Organization","LocalBusiness"],"@id":ORG_ID,
      "name":"DajbocTechDon","legalName":"DajbocTechDon S.R.L.","url":"https://dajboctechdon.com/",
      "logo":{"@type":"ImageObject","url":"https://dajboctechdon.com/images/logo-removebg-preview.png","width":675,"height":369},
      "image":"https://dajboctechdon.com/images/og-image.jpg",
      "description":"DajbocTechDon S.R.L. este o firmă românească de inginerie și producție din județul Satu Mare, specializată în prelucrări mecanice CNC de precizie, proiectarea și fabricarea de utilaje la comandă și producția internă de componente metalice pentru industria auto, industrială, agricolă și energetică.",
      "slogan":"Partenerul Tău de Încredere în Afaceri","foundingDate":"2023",
      "founder":{"@type":"Person","name":"Daniel Dan"},
      "address":{"@type":"PostalAddress","streetAddress":"Str. Valceleni Nr. 69","addressLocality":"Turt","addressRegion":"Satu Mare","postalCode":"447330","addressCountry":"RO"},
      "geo":{"@type":"GeoCoordinates","latitude":47.9333,"longitude":23.2000},
      "telephone":"+40744987550","email":"contact@dajboctechdon.com",
      "priceRange":"$$","currenciesAccepted":"RON, EUR",
      "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"09:00","closes":"18:00"}],
      "sameAs":["https://www.linkedin.com/company/dajboctechdon/"],
      "knowsLanguage":["ro","en"],
      "areaServed":[{"@type":"Country","name":"România"},{"@type":"Place","name":"Uniunea Europeană"}],
      "knowsAbout":["Prelucrări CNC","Strunjire CNC","Frezare CNC","Prelucrări prin așchiere","Piese metalice de precizie","Proiectare utilaje","Confecții metalice","Utilaje agricole","Prototipare","Inginerie mecanică"],
      "hasOfferCatalog":{"@type":"OfferCatalog","name":"Servicii de inginerie și fabricație",
        "itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":n,"description":d,"provider":{"@id":ORG_ID},"areaServed":"RO"}} for n,d in SERVICES_RO]}
    }
    site = {"@type":"WebSite","@id":SITE_ID,"url":"https://dajboctechdon.com/","name":"DajbocTechDon","inLanguage":"ro","publisher":{"@id":ORG_ID}}
    page = {"@type":"WebPage","@id":RO_URL+"#webpage","url":RO_URL,
            "name":"Prelucrări CNC Satu Mare | Fabricare Utilaje – DajbocTechDon",
            "isPartOf":{"@id":SITE_ID},"about":{"@id":ORG_ID},"inLanguage":"ro",
            "description":"Prelucrări mecanice CNC de precizie, proiectare și fabricare de utilaje la comandă în Satu Mare, România."}
    faqp = {"@type":"FAQPage","@id":RO_URL+"#faq","inLanguage":"ro","mainEntity":faq}
    graph = {"@context":"https://schema.org","@graph":[org,site,page,faqp]}
    return ('<!-- JSONLD:START -->\n<script type="application/ld+json">\n'
            + json.dumps(graph, ensure_ascii=False, indent=1) + '\n</script>\n<!-- JSONLD:END -->')

# ------------------------------------------------------------- head rumeno
RO_TITLE = "Prelucrări CNC Satu Mare | Fabricare Utilaje – DajbocTechDon"
RO_DESC  = ("DajbocTechDon S.R.L. — prelucrări mecanice CNC de precizie, strunjire și frezare, "
            "proiectare și fabricare de utilaje la comandă în Satu Mare, România.")

HEAD_SUBS = [
 (re.compile(r'<title>.*?</title>', re.S), '<title>%s</title>' % RO_TITLE),
 (re.compile(r'<meta name="description" content="[^"]*">'), '<meta name="description" content="%s">' % RO_DESC),
 (re.compile(r'<link rel="canonical" href="[^"]*">'), '<link rel="canonical" href="%s">' % RO_URL),
 (re.compile(r'<meta property="og:locale" content="[^"]*">'), '<meta property="og:locale" content="ro_RO">'),
 (re.compile(r'<meta property="og:locale:alternate" content="[^"]*">'), '<meta property="og:locale:alternate" content="en_US">'),
 (re.compile(r'<meta property="og:title" content="[^"]*">'), '<meta property="og:title" content="Prelucrări CNC și fabricare utilaje | DajbocTechDon Satu Mare">'),
 (re.compile(r'<meta property="og:description" content="[^"]*">'), '<meta property="og:description" content="Prelucrări mecanice CNC de precizie, proiectare de utilaje la comandă și producție internă în Satu Mare, România.">'),
 (re.compile(r'<meta property="og:url" content="[^"]*">'), '<meta property="og:url" content="%s">' % RO_URL),
 (re.compile(r'<meta name="twitter:title" content="[^"]*">'), '<meta name="twitter:title" content="Prelucrări CNC și fabricare utilaje | DajbocTechDon">'),
 (re.compile(r'<meta name="twitter:description" content="[^"]*">'), '<meta name="twitter:description" content="Prelucrări mecanice CNC de precizie și fabricare de utilaje la comandă în Satu Mare, România.">'),
]

ALT_RO = {
 'DajbocTechDon — CNC machining and engineering, Satu Mare, Romania':'DajbocTechDon — prelucrări CNC și inginerie mecanică, Satu Mare, România',
 'Gathering technical requirements for a CNC manufacturing project':'Colectarea cerințelor tehnice pentru un proiect de fabricație CNC',
 'Mechanical design of custom industrial machinery':'Proiectarea mecanică a utilajelor industriale la comandă',
 'Simulation and verification of a mechanical design before production':'Simularea și verificarea unui proiect mecanic înainte de producție',
 'Precision CNC machining of metal components in-house':'Prelucrări CNC de precizie ale componentelor metalice, realizate intern',
 'Assembly of machined parts into a finished product':'Asamblarea pieselor prelucrate într-un produs finit',
 'Quality control during the production process':'Controlul calității în timpul procesului de producție',
 'Testing machined components for safety and performance':'Testarea componentelor prelucrate pentru siguranță și performanță',
 'Logistics and delivery of finished assembled goods':'Logistica și livrarea produselor finite asamblate',
 'DajbocTechDon engineer working on precision CNC manufacturing in Satu Mare, Romania':'Inginer DajbocTechDon la o prelucrare CNC de precizie în Satu Mare, România',
 'DajbocTechDon S.R.L. logo':'Logo DajbocTechDon S.R.L.',
 'DajbocTechDon — precision CNC machining and engineering, Satu Mare, Romania':'DajbocTechDon — prelucrări CNC de precizie și inginerie, Satu Mare, România',
}

def main():
    T = load_translations()
    ro = T['ro']
    html = io.open(SRC, encoding='utf-8').read()

    html = translate(html, ro)
    html = html.replace('<html lang="en">', '<html lang="ro">', 1)

    for rx, new in HEAD_SUBS:
        html = rx.sub(lambda m, n=new: n, html, count=1)

    # JSON-LD rumeno
    html = re.sub(r'<!-- JSONLD:START -->.*?<!-- JSONLD:END -->', lambda m: ro_jsonld(ro), html, flags=re.S)

    # alt text tradotti
    for en, rot in ALT_RO.items():
        html = html.replace('alt="%s"' % en, 'alt="%s"' % rot)

    # switcher: RO attiva
    html = html.replace('<a class="lang-btn active" href="/" id="btn-en" hreflang="en" lang="en" aria-label="English version" aria-current="true">',
                        '<a class="lang-btn" href="/" id="btn-en" hreflang="en" lang="en" aria-label="English version">')
    html = html.replace('<a class="lang-btn" href="/ro/" id="btn-ro" hreflang="ro" lang="ro" aria-label="Versiunea în limba română">',
                        '<a class="lang-btn active" href="/ro/" id="btn-ro" hreflang="ro" lang="ro" aria-label="Versiunea în limba română" aria-current="true">')

    # percorsi relativi -> risalgono di una cartella
    html = re.sub(r'(src|href)="images/', lambda m: '%s="../images/' % m.group(1), html)

    os.makedirs(OUT_DIR, exist_ok=True)
    io.open(OUT, 'w', encoding='utf-8').write(html)
    print('OK  ->', OUT, len(html), 'byte')

if __name__ == '__main__':
    main()
