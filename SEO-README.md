# SEO – pagine per paese e per județ

## Cosa è stato aggiunto

| Cosa | URL | Lingua |
|---|---|---|
| Hub Europa | `/europe/` | EN |
| 45 pagine paese | es. `/de/cnc-bearbeitung-deutschland/`, `/fr/usinage-cnc-france/` | lingua locale |
| Hub județe | `/ro/judete/` | RO |
| 42 pagine județ (41 + București) | es. `/ro/prelucrari-cnc-cluj/` | RO |
| Sezione "zone deservite" in home EN e RO | `/` e `/ro/` | EN / RO |
| `sitemap.xml` completa con hreflang | `/sitemap.xml` | — |

Ogni pagina ha: title e meta description mirati, canonical, hreflang (cluster di 45 lingue
+ `x-default`), Open Graph/Twitter, JSON-LD (`WebPage` + `Service` con `areaServed` +
`BreadcrumbList` + `FAQPage`), breadcrumb visibile, contenuti locali (distanza, tempi di
trasporto, dogana/IVA, settori industriali del paese/județ), FAQ, form di richiesta offerta
(Web3Forms, stessa chiave della home) e link interni verso hub e paesi/județe vicini.

## Come rigenerare

```bash
cd newdani
python3 build_ro.py     # solo se hai modificato index.html (rigenera /ro/)
python3 -B build_seo.py # rigenera tutte le landing page, la sitemap e le sezioni in home
```

**Ordine importante:** `build_ro.py` ricostruisce `ro/index.html` da `index.html`, quindi va
lanciato *prima* di `build_seo.py` (che inserisce la sezione "zone deservite" in entrambe le home
tra i marcatori `<!-- AREAS:START -->` / `<!-- AREAS:END -->` e aggiorna `areaServed` nel JSON-LD).

## Dove si modificano i contenuti

| File | Contenuto |
|---|---|
| `seo_countries.py` | dati per paese: nome, città di riferimento, regioni industriali, settori, dogana, tempi |
| `seo_judete.py` | dati dei 42 județe + tutti i testi in rumeno |
| `seo_l_west.py` / `seo_l_east.py` / `seo_l_north.py` | testi nelle 27 lingue europee |
| `build_seo.py` | template HTML/CSS, JSON-LD, sitemap, hub |

Aggiungere un paese = una voce `add(...)` in `seo_countries.py` (se la lingua esiste già);
aggiungere una lingua = un blocco `L['xx'] = dict(...)` con le stesse chiavi di `L['en']`.

## Da fare dopo la pubblicazione

1. Google Search Console: aggiungere la proprietà `dajboctechdon.com` e inviare `sitemap.xml`
   (fare lo stesso su Bing Webmaster Tools).
2. Creare/verificare il profilo Google Business per l'indirizzo di Turț (categoria: "atelier de
   prelucrări mecanice" / "machine shop"): è il fattore più forte per le ricerche locali in RO.
3. Aggiungere il sito su directory B2B di settore (es. Europages, Kompass, listini di
   subfurnitura CNC) con lo stesso NAP – nome, indirizzo, telefono – usato nel sito.
4. Foto reali dell'officina e dei pezzi lavorati: sostituire `images/engineer.webp` con foto
   proprie e aggiungere una galleria (le immagini originali aiutano molto).
5. Monitorare in Search Console quali paesi/județe ricevono impression e arricchire quelle pagine
   con casi concreti (materiali lavorati, tolleranze tipiche, dimensioni massime dei pezzi).
