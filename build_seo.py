#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_seo.py — genera le landing page SEO locali di dajboctechdon.com

  * una pagina per ogni stato europeo, nella lingua di quello stato
    (dati: seo_countries.py, testi: seo_langs.py)
  * una pagina per ogni judet della Romania + Bucuresti (seo_judete.py)
  * hub: /europe/ (EN) e /ro/judete/ (RO)
  * sitemap.xml completa con hreflang

Uso:   python3 build_seo.py
Da rilanciare dopo ogni modifica ai file seo_*.py (o dopo build_ro.py).
Le pagine generate sono HTML statico: nessun build server necessario
(GitHub Pages le serve cosi' come sono).
"""
import html, io, json, math, os, re, shutil, datetime

from seo_langs import LANGS
from seo_countries import COUNTRIES
from seo_judete import JUDETE, RO

BASE = 'https://dajboctechdon.com'
ORG_ID = BASE + '/#organization'
SITE_ID = BASE + '/#website'
TURT = (47.9333, 23.2000)          # atelier: Str. Valceleni 69, Turt, Satu Mare
TODAY = datetime.date.today().isoformat()
WEB3FORMS_KEY = '1b7d2f36-8581-4b54-a020-27ccb4ff4e80'
EUROPE_HUB = '/europe/'
JUDETE_HUB = '/ro/judete/'

esc = lambda s: html.escape(s, quote=True)


def km(a, b):
    R = 6371.0
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))


def round_km(d):
    return int(round(d / 10.0) * 10) if d >= 100 else int(round(d / 5.0) * 5)


def transit_days(d):
    """Tempo indicativo di trasporto su strada (groupage/LTL), in giorni lavorativi."""
    if d < 450:  return '1–2'
    if d < 900:  return '2–3'
    if d < 1400: return '3–4'
    if d < 2000: return '4–5'
    return '5–7'


def fmt_num(n, lang):
    s = f'{n:,}'
    if lang in ('en', 'ro-en'):
        return s
    if lang in ('de', 'it', 'es', 'pt', 'nl', 'da', 'sl', 'hr', 'sr', 'bs', 'tr', 'el', 'id', 'ro', 'ca'):
        return s.replace(',', '.')
    return s.replace(',', ' ')   # fr, pl, cs, sk, hu, sv, fi, nb, et, lv, lt, bg, mk, uk, sq


def fit_title(t, limit=65):
    """Accorcia il title se supera ~65 caratteri (limite visibile nei risultati Google)."""
    if len(t) <= limit:
        return t
    head = t.split(' | ')[0]
    for cand in (head + ' | DajbocTechDon', head):
        if len(cand) <= limit:
            return cand
    return head


def fill(s, ctx):
    """Sostituisce {chiave} con ctx[chiave]; lascia intatte le parentesi non note."""
    return re.sub(r'\{(\w+)\}', lambda m: str(ctx.get(m.group(1), m.group(0))), s)


# ============================================================ CSS condiviso
CSS = r"""
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#050508;--bg2:#0d0d14;--bg3:#111119;--accent:#00c8ff;--blue:#0070ff;--purple:#a855f7;--text:#e8e8f0;--muted:#8a8aa8;--border:rgba(255,255,255,.08)}
html{scroll-behavior:smooth}
body{font-family:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden}
a{color:var(--accent)}
img{max-width:100%;height:auto}
.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;z-index:2000;background:#000;padding:.5rem 1rem}
.topnav{position:sticky;top:0;z-index:1000;padding:.8rem 5%;display:flex;align-items:center;justify-content:space-between;background:rgba(5,5,8,.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--border)}
.nav-logo img{height:46px;width:auto;display:block}
.nav-links{display:flex;gap:1.6rem;list-style:none;align-items:center}
.nav-links a{text-decoration:none;color:var(--muted);font-size:.84rem;font-weight:500;letter-spacing:.05em;text-transform:uppercase;transition:color .3s}
.nav-links a:hover{color:var(--accent)}
.nav-cta{background:linear-gradient(135deg,var(--blue),var(--accent));color:#fff!important;padding:.45rem 1.15rem;border-radius:50px;font-weight:600!important}
.lang-pill{font-size:.75rem;font-weight:700;letter-spacing:.06em;border:1px solid var(--border);border-radius:50px;padding:.3rem .7rem;color:var(--muted);text-decoration:none}
.lang-pill:hover{color:var(--accent);border-color:var(--accent)}
.hero{position:relative;padding:4.5rem 5% 4rem;overflow:hidden;background-image:linear-gradient(rgba(0,200,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(0,200,255,.035) 1px,transparent 1px);background-size:55px 55px}
.hero::after{content:'';position:absolute;width:520px;height:520px;right:-120px;top:-160px;border-radius:50%;background:radial-gradient(circle,rgba(0,200,255,.13),transparent 65%);pointer-events:none}
.wrap{max-width:1150px;margin:0 auto;position:relative;z-index:1}
.bc{font-size:.8rem;color:var(--muted);margin-bottom:1.6rem}
.bc ol{list-style:none;display:flex;flex-wrap:wrap;gap:.4rem}
.bc li+li::before{content:'›';margin-right:.4rem;color:var(--accent)}
.bc a{color:var(--muted);text-decoration:none}.bc a:hover{color:var(--accent)}
.badge{display:inline-flex;align-items:center;gap:.5rem;background:rgba(0,200,255,.08);border:1px solid rgba(0,200,255,.22);border-radius:50px;padding:.4rem 1rem;font-size:.74rem;font-weight:700;color:var(--accent);letter-spacing:.1em;text-transform:uppercase;margin-bottom:1.4rem}
.badge i{width:8px;height:8px;background:var(--accent);border-radius:50%;display:inline-block}
h1{font-family:'Space Grotesk',sans-serif;font-size:clamp(2.1rem,5.2vw,3.9rem);font-weight:700;line-height:1.1;margin-bottom:1.3rem;max-width:950px}
.gt{background:linear-gradient(135deg,#00c8ff,#0070ff,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.lead{font-size:clamp(1rem,1.9vw,1.18rem);color:#b4b4c8;max-width:820px;margin-bottom:2rem}
.btns{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.8rem}
.btn-p,.btn-s{display:inline-flex;align-items:center;padding:.9rem 1.9rem;border-radius:50px;font-weight:600;font-size:.95rem;text-decoration:none;transition:transform .25s,box-shadow .25s}
.btn-p{background:linear-gradient(135deg,var(--blue),var(--accent));color:#fff;box-shadow:0 0 28px rgba(0,200,255,.25)}
.btn-s{border:1px solid var(--border);color:var(--text)}
.btn-p:hover,.btn-s:hover{transform:translateY(-3px)}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}
.fact{background:rgba(13,13,20,.85);border:1px solid var(--border);border-radius:16px;padding:1.1rem 1.2rem}
.fact dt{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:.35rem}
.fact dd{font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:1.08rem;color:var(--text)}
section{padding:4.8rem 5%}
section:nth-of-type(even){background:var(--bg2)}
.sh{margin-bottom:2.4rem;max-width:820px}
.stag{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:.7rem}
h2{font-family:'Space Grotesk',sans-serif;font-size:clamp(1.6rem,3.3vw,2.4rem);line-height:1.2;margin-bottom:.8rem}
.sdesc,.prose p{color:#a9a9c0;font-size:1rem}
.prose p+p{margin-top:1rem}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:1.1rem}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:1.1rem}
.card{background:var(--bg3);border:1px solid var(--border);border-radius:18px;padding:1.4rem;transition:border-color .3s,transform .3s}
.card:hover{border-color:rgba(0,200,255,.3);transform:translateY(-4px)}
.card .n{font-family:'Space Grotesk',sans-serif;color:var(--accent);font-weight:700;font-size:.85rem;margin-bottom:.5rem;display:block}
h3{font-size:1.02rem;font-weight:700;margin-bottom:.4rem}
.card p{font-size:.88rem;color:var(--muted)}
.split{display:grid;grid-template-columns:1.1fr .9fr;gap:3rem;align-items:center}
.split img{border-radius:22px;display:block;width:100%;object-fit:cover;aspect-ratio:653/382}
.checks{list-style:none;display:flex;flex-direction:column;gap:.85rem}
.checks li{padding-left:1.8rem;position:relative;color:#c4c4d6}
.checks li::before{content:'✓';position:absolute;left:0;top:0;color:var(--accent);font-weight:800}
.steps{counter-reset:s;display:grid;grid-template-columns:repeat(4,1fr);gap:1.1rem;list-style:none}
.steps li{counter-increment:s;background:var(--bg3);border:1px solid var(--border);border-radius:18px;padding:1.4rem}
.steps li::before{content:'0' counter(s);display:block;font-family:'Space Grotesk',sans-serif;font-size:1.6rem;font-weight:800;color:var(--accent);margin-bottom:.4rem}
.steps p{font-size:.88rem;color:var(--muted)}
.faq{max-width:900px;display:flex;flex-direction:column;gap:.9rem}
.faq details{background:var(--bg3);border:1px solid var(--border);border-radius:14px;padding:1.1rem 1.4rem}
.faq details[open]{border-color:rgba(0,200,255,.3)}
.faq summary{cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:1rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:'+';color:var(--accent);font-size:1.4rem;line-height:1}
.faq details[open] summary::after{content:'−'}
.faq details p{margin-top:.8rem;color:var(--muted);font-size:.95rem}
.cgrid{display:grid;grid-template-columns:1fr 1.3fr;gap:3rem}
.citems{list-style:none;display:flex;flex-direction:column;gap:.8rem;margin-top:1.4rem}
.citems li{background:var(--bg3);border:1px solid var(--border);border-radius:12px;padding:.9rem 1.1rem;font-size:.92rem}
.citems strong{display:block;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.citems a{color:var(--text);text-decoration:none}.citems a:hover{color:var(--accent)}
form.cf{background:var(--bg);border:1px solid var(--border);border-radius:22px;padding:2rem;display:flex;flex-direction:column;gap:.9rem}
.cf label{font-size:.8rem;color:var(--muted);display:block;margin-bottom:.3rem}
.cf input,.cf textarea{width:100%;background:rgba(255,255,255,.03);border:1px solid var(--border);border-radius:11px;padding:.85rem 1rem;color:var(--text);font:inherit;font-size:.95rem}
.cf input:focus,.cf textarea:focus{outline:none;border-color:var(--accent)}
.cf textarea{min-height:130px;resize:vertical}
.cf .row{display:grid;grid-template-columns:1fr 1fr;gap:.9rem}
.cf button{background:linear-gradient(135deg,var(--blue),var(--accent));color:#fff;border:0;border-radius:11px;padding:1rem;font:inherit;font-weight:600;cursor:pointer}
.cf .hp{display:none}
.chips{display:flex;flex-wrap:wrap;gap:.55rem}
.chips a{display:inline-flex;align-items:center;gap:.45rem;border:1px solid var(--border);border-radius:50px;padding:.42rem .9rem;font-size:.86rem;color:#c4c4d6;text-decoration:none;background:var(--bg3);transition:all .25s}
.chips a:hover,.chips a[aria-current]{border-color:var(--accent);color:var(--accent)}
.chips b{font-size:.68rem;color:var(--muted);font-weight:700;letter-spacing:.05em}
.more{margin-top:1.4rem;display:inline-block;font-weight:600}
.cols{columns:3 240px;column-gap:2rem}
.cols a{display:block;padding:.35rem 0;color:#c4c4d6;text-decoration:none;break-inside:avoid}
.cols a:hover{color:var(--accent)}
.cols small{color:var(--muted)}
footer{padding:2.6rem 5%;border-top:1px solid var(--border);font-size:.86rem;color:var(--muted)}
footer .wrap{display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:space-between;align-items:center}
footer a{color:var(--muted);text-decoration:none}footer a:hover{color:var(--accent)}
.flinks{display:flex;flex-wrap:wrap;gap:1.2rem}
@media(max-width:960px){.facts,.grid4,.steps{grid-template-columns:repeat(2,1fr)}.split,.cgrid{grid-template-columns:1fr}.nav-links li:not(.keep){display:none}}
@media(max-width:560px){.facts,.grid4,.steps,.grid2,.cf .row{grid-template-columns:1fr}section{padding:3.6rem 5%}.hero{padding:3rem 5%}.nav-links{gap:.8rem}}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">')

JS = r"""
<script>
(function(){
  var f=document.getElementById('qf'); if(!f) return;
  f.addEventListener('submit', async function(e){
    e.preventDefault();
    var b=f.querySelector('button'), m=f.dataset;
    var d=Object.fromEntries(new FormData(f).entries());
    if(!d.name||!d.email||!d.message){alert(m.missing);return;}
    var orig=b.textContent; b.textContent=m.sending; b.disabled=true;
    try{
      var r=await fetch('https://api.web3forms.com/submit',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify(d)});
      var j=await r.json(); if(!j.success) throw 0;
      b.textContent=m.sent; f.reset();
    }catch(err){ b.textContent=m.error; }
    setTimeout(function(){b.textContent=orig;b.disabled=false;},5000);
  });
})();
</script>"""


# ============================================================ blocchi HTML
def jsonld(graph):
    return ('<script type="application/ld+json">\n' +
            json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1) +
            '\n</script>')


def head(P):
    alts = ''.join('<link rel="alternate" hreflang="%s" href="%s">\n' % (h, BASE + u) for h, u in P.get('alternates', []))
    return f"""<!DOCTYPE html>
<html lang="{P['hl']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(P['title'])}</title>
<meta name="description" content="{esc(P['desc'])}">
<link rel="canonical" href="{BASE}{P['url']}">
{alts}<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="author" content="DajbocTechDon S.R.L.">
<link rel="icon" type="image/png" href="/images/logo-removebg-preview.png">
<link rel="apple-touch-icon" href="/images/logo-removebg-preview.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="DajbocTechDon S.R.L.">
<meta property="og:locale" content="{P['og_locale']}">
<meta property="og:title" content="{esc(P['title'])}">
<meta property="og:description" content="{esc(P['desc'])}">
<meta property="og:url" content="{BASE}{P['url']}">
<meta property="og:image" content="{BASE}/images/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(P['title'])}">
<meta name="twitter:description" content="{esc(P['desc'])}">
<meta name="twitter:image" content="{BASE}/images/og-image.jpg">
<meta name="theme-color" content="#050508">
{FONTS}
<style>{CSS}</style>
{jsonld(P['graph'])}
</head>
<body>
<a class="skip" href="#main">{esc(P['skip'])}</a>
<nav class="topnav">
  <a href="{P['home']}" class="nav-logo"><img src="/images/logo-white.webp" width="600" height="314" alt="DajbocTechDon S.R.L." fetchpriority="high"></a>
  <ul class="nav-links">
    <li><a href="{P['home']}">{esc(P['nav_home'])}</a></li>
    <li><a href="#services">{esc(P['nav_services'])}</a></li>
    <li><a href="#faq">{esc(P['nav_faq'])}</a></li>
    <li class="keep"><a class="lang-pill" href="{P['pill_href']}" title="{esc(P['pill_title'])}">{esc(P['pill'])}</a></li>
    <li class="keep"><a href="#contact" class="nav-cta">{esc(P['nav_contact'])}</a></li>
  </ul>
</nav>
"""


def breadcrumb_html(items):
    lis = []
    for i, (name, url) in enumerate(items):
        if i < len(items) - 1:
            lis.append(f'<li><a href="{url}">{esc(name)}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{esc(name)}</li>')
    return '<div class="bc" aria-label="breadcrumb"><ol>' + ''.join(lis) + '</ol></div>'


def breadcrumb_ld(items, url):
    return {"@type": "BreadcrumbList", "@id": BASE + url + "#breadcrumb",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u}
                                for i, (n, u) in enumerate(items)]}


def body(P):
    facts = ''.join(f'<div class="fact"><dt>{esc(k)}</dt><dd>{v}</dd></div>' for k, v in P['facts'])
    svcs = ''.join(f'<article class="card"><span class="n">{i+1:02d}</span><h3>{esc(t)}</h3><p>{d}</p></article>'
                   for i, (t, d) in enumerate(P['services']))
    inds = ''.join(f'<article class="card"><h3>{esc(t)}</h3><p>{d}</p></article>' for t, d in P['industries'])
    why = ''.join(f'<li>{w}</li>' for w in P['why'])
    steps = ''.join(f'<li><h3>{esc(t)}</h3><p>{d}</p></li>' for t, d in P['how'])
    log = ''.join(f'<p>{p}</p>' for p in P['log_ps'])
    faq = ''.join(f'<details{" open" if i == 0 else ""}><summary>{esc(q)}</summary><p>{a}</p></details>'
                  for i, (q, a) in enumerate(P['faq']))
    cur = ' aria-current="page"'
    chips = ''.join(
        '<a href="%s"%s hreflang="%s" lang="%s"><b>%s</b>%s</a>' % (u, cur if u == P['url'] else '', hl, hl, c, esc(n))
        for c, n, u, hl in P['chips'])
    return f"""<main id="main">
<header class="hero">
 <div class="wrap">
  {breadcrumb_html(P['bc'])}
  <div class="badge"><i></i>{esc(P['badge'])}</div>
  <h1>{P['h1']}</h1>
  <p class="lead">{P['lead']}</p>
  <div class="btns"><a class="btn-p" href="#contact">{esc(P['cta_quote'])}</a><a class="btn-s" href="#services">{esc(P['cta_services'])}</a></div>
  <dl class="facts">{facts}</dl>
 </div>
</header>

<section id="services"><div class="wrap">
 <div class="sh"><span class="stag">{esc(P['svc_tag'])}</span><h2>{esc(P['svc_title'])}</h2><p class="sdesc">{P['svc_intro']}</p></div>
 <div class="grid4">{svcs}</div>
</div></section>

<section id="industries"><div class="wrap">
 <div class="sh"><span class="stag">{esc(P['ind_tag'])}</span><h2>{esc(P['ind_title'])}</h2><p class="sdesc">{P['ind_intro']}</p></div>
 <div class="grid4">{inds}</div>
</div></section>

<section id="why"><div class="wrap split">
 <div><span class="stag">{esc(P['why_tag'])}</span><h2>{esc(P['why_title'])}</h2><ul class="checks">{why}</ul></div>
 <img src="/images/engineer.webp" width="653" height="382" loading="lazy" decoding="async" alt="{esc(P['img_alt'])}">
</div></section>

<section id="process"><div class="wrap">
 <div class="sh"><span class="stag">{esc(P['how_tag'])}</span><h2>{esc(P['how_title'])}</h2></div>
 <ol class="steps">{steps}</ol>
</div></section>

<section id="logistics"><div class="wrap">
 <div class="sh"><span class="stag">{esc(P['log_tag'])}</span><h2>{esc(P['log_title'])}</h2></div>
 <div class="prose">{log}</div>
</div></section>

<section id="faq"><div class="wrap">
 <div class="sh"><span class="stag">FAQ</span><h2>{esc(P['faq_title'])}</h2></div>
 <div class="faq">{faq}</div>
</div></section>

<section id="contact"><div class="wrap cgrid">
 <div>
  <span class="stag">{esc(P['con_tag'])}</span><h2>{esc(P['con_title'])}</h2>
  <p class="sdesc">{P['con_p']}</p>
  <ul class="citems">
   <li><strong>{esc(P['l_phone'])}</strong><a href="tel:+40744987550">+40 744 987 550</a></li>
   <li><strong>Email</strong><a href="mailto:contact@dajboctechdon.com">contact@dajboctechdon.com</a></li>
   <li><strong>{esc(P['l_addr'])}</strong>Str. Valceleni Nr. 69, 447330 Turț, Satu Mare, {esc(P['romania'])}</li>
   <li><strong>LinkedIn</strong><a href="https://www.linkedin.com/company/dajboctechdon/" rel="noopener" target="_blank">linkedin.com/company/dajboctechdon</a></li>
  </ul>
 </div>
 <form class="cf" id="qf" data-missing="{esc(P['f_missing'])}" data-sending="{esc(P['f_sending'])}" data-sent="{esc(P['f_sent'])}" data-error="{esc(P['f_error'])}">
  <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
  <input type="hidden" name="subject" value="{esc(P['mail_subject'])}">
  <input type="hidden" name="from_page" value="{BASE}{P['url']}">
  <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
  <div class="row">
   <div><label for="f-name">{esc(P['f_name'])}</label><input id="f-name" name="name" autocomplete="name" required></div>
   <div><label for="f-email">{esc(P['f_email'])}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
  </div>
  <div><label for="f-company">{esc(P['f_company'])}</label><input id="f-company" name="company" autocomplete="organization"></div>
  <div><label for="f-msg">{esc(P['f_msg'])}</label><textarea id="f-msg" name="message" required></textarea></div>
  <button type="submit">{esc(P['f_send'])}</button>
 </form>
</div></section>

<section id="areas"><div class="wrap">
 <div class="sh"><span class="stag">{esc(P['more_tag'])}</span><h2>{esc(P['more_title'])}</h2></div>
 <div class="chips">{chips}</div>
 <a class="more" href="{P['more_href']}">{esc(P['more_all'])} →</a>
</div></section>
</main>
"""


def footer(P):
    links = ''.join(f'<a href="{u}">{esc(n)}</a>' for n, u in P['foot_links'])
    return f"""<footer><div class="wrap">
 <p>© {datetime.date.today().year} DajbocTechDon S.R.L. · {esc(P['foot'])}</p>
 <div class="flinks">{links}</div>
</div></footer>
{JS}
</body>
</html>
"""


def write(url, content):
    path = url.strip('/') + '/index.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, 'w', encoding='utf-8').write(content)
    return path


# ============================================================ pagine paese
def country_url(c):
    return f"/{c['lang']}/{c['slug']}/"


def country_ctx(c, L):
    d = km(TURT, c['city_geo'])
    ctx = dict(c['forms'])
    ctx.update(city=c['city'], city_log=c.get('city_log', c['city']), km=fmt_num(round_km(d), L['code']),
               days=c.get('days') or transit_days(d),
               hubs=c['hubs'], sectors=c['sectors'])
    return ctx, d


def service_ld(name, desc, url, area, lang):
    return {"@type": "Service", "@id": BASE + url + "#service", "name": name, "description": desc,
            "serviceType": "CNC machining", "provider": {"@id": ORG_ID}, "areaServed": area,
            "availableLanguage": ["en", "ro"], "inLanguage": lang, "url": BASE + url,
            "hasOfferCatalog": {"@type": "OfferCatalog", "name": name}}


def build_country(c, all_chips, cluster):
    L = LANGS[c['lang']]
    ctx, d = country_ctx(c, L)
    F = lambda s: fill(s, ctx)
    url = country_url(c)
    ctype = c['customs']
    customs_long = F(L['customs_long'][ctype])
    faq = [(F(q), F(a)) for q, a in L['faq']] + [(F(L['faq_customs_q']), customs_long)]
    if c.get('extra_faq'):
        faq.insert(1, c['extra_faq'])
    log_ps = [F(L['log_p1'])]
    if c.get('extra'):
        log_ps.append(c['extra'])
    log_ps.append(customs_long)
    log_ps.append(F(L['log_p3']))
    bc = [(L['bc_home'], '/'), (L['bc_eu'], EUROPE_HUB), (F(L['bc_page']), url)]
    title, desc = fit_title(F(L['title'])), F(L['desc'])
    P = dict(
        hl=c['hreflang'] if len(c['hreflang']) > 2 else L['code'], url=url, title=title, desc=desc,
        og_locale=c['og'], alternates=cluster, home='/', skip=L['skip'],
        nav_home=L['nav_home'], nav_services=L['nav_services'], nav_faq='FAQ', nav_contact=L['nav_contact'],
        pill='EU', pill_href=EUROPE_HUB, pill_title=L['bc_eu'],
        bc=bc, badge=F(L['badge']), h1=F(L['h1']), lead=F(L['lead']),
        cta_quote=L['cta_quote'], cta_services=L['cta_services'],
        facts=[(F(L['f_dist']), F(L['f_dist_v'])), (L['f_transit'], F(L['f_transit_v'])),
               (L['f_customs'], F(L['customs_short'][ctype])), (L['f_quote'], L['f_quote_v'])],
        svc_tag=L['svc_tag'], svc_title=F(L['svc_title']), svc_intro=F(L['svc_intro']), services=L['svc'],
        ind_tag=L['ind_tag'], ind_title=F(L['ind_title']), ind_intro=F(L['ind_intro']), industries=L['ind'],
        why_tag=L['why_tag'], why_title=F(L['why_title']), why=[F(w) for w in L['why']],
        img_alt=L['img_alt'], how_tag=L['how_tag'], how_title=L['how_title'], how=L['how'],
        log_tag=L['log_tag'], log_title=F(L['log_title']), log_ps=log_ps,
        faq_title=F(L['faq_title']), faq=faq,
        con_tag=L['con_tag'], con_title=F(L['con_title']), con_p=F(L['con_p']),
        l_phone=L['l_phone'], l_addr=L['l_addr'], romania=L['romania'],
        f_name=L['f_name'], f_email=L['f_email'], f_company=L['f_company'], f_msg=L['f_msg'],
        f_send=L['f_send'], f_sending=L['f_sending'], f_sent=L['f_sent'], f_error=L['f_error'], f_missing=L['f_missing'],
        mail_subject=f"Website inquiry – {c['en']} ({c['lang']}) – dajboctechdon.com",
        more_tag=L['more_tag'], more_title=L['more_title'], more_all=L['more_all'], more_href=EUROPE_HUB,
        chips=all_chips, foot=L['foot'],
        foot_links=[(L['bc_home'], '/'), ('Europe', EUROPE_HUB), ('România', '/ro/'), ('Județe', JUDETE_HUB)],
    )
    area = {"@type": "Country", "name": c['en']}
    if c['iso'] != 'XK':
        area["identifier"] = c['iso']
    P['graph'] = [
        {"@type": "WebPage", "@id": BASE + url + "#webpage", "url": BASE + url, "name": title, "description": desc,
         "inLanguage": P['hl'], "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID},
         "breadcrumb": {"@id": BASE + url + "#breadcrumb"}, "mainEntity": {"@id": BASE + url + "#service"},
         "primaryImageOfPage": BASE + "/images/og-image.jpg", "dateModified": TODAY},
        service_ld(F(L['svc_name']), desc, url, area, P['hl']),
        breadcrumb_ld(bc, url),
        {"@type": "FAQPage", "@id": BASE + url + "#faq", "inLanguage": P['hl'],
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in faq]},
    ]
    return write(url, head(P) + body(P) + footer(P))


# ============================================================ pagine judet
def judet_url(j):
    return f"/ro/{j['slug']}/"


def build_judet(j, chips):
    d = km(TURT, j['geo'])
    ctx = dict(name=j['name'], seat=j['seat'], tot=j.get('tot', 'tot ' + j['jud']), towns=j['towns'], sectors=j['sectors'],
               km=fmt_num(round_km(d), 'ro'), jud=j['jud'], injud=j['injud'], seatin=j.get('seatin', 'în ' + j['seat']),
               days=j.get('days') or ('24 h' if d < 180 else ('24–48 h' if d < 450 else '48–72 h')),
               neighbors=', '.join(JUDETE[n]['name'] for n in j['nb']))
    F = lambda s: fill(s, ctx)
    url = judet_url(j)
    tkey = 'title_home' if j['code'] == 'SM' else ('title_b' if j['code'] == 'B' else ('title_same' if j['seat'] == j['name'] else 'title'))
    title = fit_title(F(RO[tkey]))
    desc = F(RO['desc'])
    faq = [(F(q), F(a)) for q, a in (RO['faq_home'] if j['code'] == 'SM' else RO['faq'])]
    bc = [('Acasă', '/ro/'), ('Județe', JUDETE_HUB), (F(RO['bc_page']), url)]
    nb_chips = [(JUDETE[n]['code'], 'Prelucrări CNC ' + JUDETE[n]['name'], judet_url(JUDETE[n]), 'ro') for n in j['nb']]
    lead = F(RO['lead_home'] if j['code'] == 'SM' else RO['lead'])
    if j.get('extra'):
        lead += ' ' + j['extra']
    P = dict(
        hl='ro', url=url, title=title, desc=desc, og_locale='ro_RO', alternates=[], home='/ro/', skip='Sari la conținut',
        nav_home='Acasă', nav_services='Servicii', nav_faq='FAQ', nav_contact='Contact',
        pill='RO', pill_href=JUDETE_HUB, pill_title='Toate județele',
        bc=bc, badge=F(RO['badge']), h1=F(RO['h1']), lead=lead,
        cta_quote=RO['cta_quote'], cta_services=RO['cta_services'],
        facts=[(F(RO['f_dist']), F(RO['f_dist_v'])), (RO['f_transit'], F(RO['f_transit_v'])),
               (RO['f_pay'], RO['f_pay_v']), (RO['f_series'], RO['f_series_v'])],
        svc_tag=RO['svc_tag'], svc_title=F(RO['svc_title']), svc_intro=F(RO['svc_intro']), services=RO['svc'],
        ind_tag=RO['ind_tag'], ind_title=F(RO['ind_title']), ind_intro=F(RO['ind_intro']), industries=RO['ind'],
        why_tag=RO['why_tag'], why_title=F(RO['why_title']), why=[F(w) for w in RO['why']],
        img_alt=F(RO['img_alt']), how_tag=RO['how_tag'], how_title=RO['how_title'], how=RO['how'],
        log_tag=RO['log_tag'], log_title=F(RO['log_title']), log_ps=[F(p) for p in RO['log_ps']],
        faq_title=F(RO['faq_title']), faq=faq,
        con_tag=RO['con_tag'], con_title=F(RO['con_title']), con_p=F(RO['con_p']),
        l_phone='Telefon', l_addr='Adresă', romania='România',
        f_name='Nume', f_email='Email', f_company='Firmă (opțional)', f_msg='Mesaj – descrieți piesa sau proiectul',
        f_send='Trimite cererea de ofertă', f_sending='Se trimite…', f_sent='✓ Trimis! Vă contactăm în curând.',
        f_error='✗ Eroare – încercați din nou', f_missing='Completați numele, emailul și mesajul.',
        mail_subject=f"Cerere ofertă – {j['name']} – dajboctechdon.com",
        more_tag='Zone deservite', more_title=F(RO['more_title']), more_all='Toate cele 41 de județe și București', more_href=JUDETE_HUB,
        chips=nb_chips, foot='Prelucrări CNC și fabricare utilaje, Satu Mare, România',
        foot_links=[('Acasă', '/ro/'), ('Județe', JUDETE_HUB), ('Europa', EUROPE_HUB), ('English', '/')],
    )
    area = ({"@type": "City", "name": "București"} if j['code'] == 'B' else
            {"@type": "AdministrativeArea", "name": "Județul " + j['name'], "containedInPlace": {"@type": "Country", "name": "România", "identifier": "RO"}})
    P['graph'] = [
        {"@type": "WebPage", "@id": BASE + url + "#webpage", "url": BASE + url, "name": title, "description": desc,
         "inLanguage": "ro", "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID},
         "breadcrumb": {"@id": BASE + url + "#breadcrumb"}, "mainEntity": {"@id": BASE + url + "#service"},
         "primaryImageOfPage": BASE + "/images/og-image.jpg", "dateModified": TODAY},
        service_ld(F(RO['svc_name']), desc, url, area, 'ro'),
        breadcrumb_ld(bc, url),
        {"@type": "FAQPage", "@id": BASE + url + "#faq", "inLanguage": "ro",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in faq]},
    ]
    return write(url, head(P) + body(P) + footer(P))


# ============================================================ hub
def hub_page(P, inner):
    return head(P) + f"""<main id="main">
<header class="hero"><div class="wrap">
 {breadcrumb_html(P['bc'])}
 <div class="badge"><i></i>{esc(P['badge'])}</div>
 <h1>{P['h1']}</h1>
 <p class="lead">{P['lead']}</p>
 <div class="btns"><a class="btn-p" href="{P['cta_href']}">{esc(P['cta_quote'])}</a><a class="btn-s" href="{P['home']}">{esc(P['cta_services'])}</a></div>
</div></header>
{inner}
</main>
""" + footer(dict(P, foot_links=P['foot_links'])).replace(JS, '')


def build_europe_hub(groups):
    url = EUROPE_HUB
    title = 'CNC Machining Supplier in Europe | DajbocTechDon, Romania'
    desc = ('Precision CNC machining, custom machine building and metal parts from Romania, delivered to customers in '
            'every European country. EU supplier: no customs within the EU single market.')
    bc = [('Home', '/'), ('Europe', url)]
    secs = []
    items = []
    for gname, gl in groups:
        links = ''.join(f'<a href="{country_url(c)}" hreflang="{c["hreflang"]}"><b>{c["iso"]}</b> {esc(c["forms"]["N"])} <small>· {esc(c["en"])} · {esc(LANGS[c["lang"]]["kw"])}</small></a>'
                        for c in gl)
        secs.append(f'<h2 style="margin:2.2rem 0 1rem;font-size:1.3rem">{esc(gname)}</h2><div class="cols">{links}</div>')
        items += gl
    secs.append('<h2 style="margin:2.2rem 0 1rem;font-size:1.3rem">Romania</h2><div class="cols">'
                '<a href="/ro/">RO România <small>· Romania · Prelucrări CNC</small></a>'
                f'<a href="{JUDETE_HUB}">RO Toate județele <small>· all 41 counties + Bucharest</small></a></div>')
    inner = f"""<section id="countries"><div class="wrap">
 <div class="sh"><span class="stag">Where we deliver</span><h2>CNC machining for every European country</h2>
 <p class="sdesc">Each page below is written in the local language and explains delivery times, customs and VAT rules for shipments from our workshop in Satu Mare, Romania.</p></div>
 {''.join(secs)}
</div></section>
<section id="why"><div class="wrap split">
 <div><span class="stag">Why Romania</span><h2>A near-shore CNC partner inside the EU</h2><ul class="checks">
 <li>EU member state: goods move freely within the single market – no customs, no duties, intra-community B2B supply with VAT reverse charge.</li>
 <li>Everything in-house in one workshop: requirements, design, simulation, CNC turning and milling, assembly, testing and delivery.</li>
 <li>Prototypes, one-off parts, spare parts and small to medium series for the automotive, industrial, agricultural and energy sectors.</li>
 <li>Quotes in EUR; we work in English and Romanian.</li>
 <li>Road freight to most of Central and Western Europe in a few working days.</li>
 </ul></div>
 <img src="/images/engineer.webp" width="653" height="382" loading="lazy" decoding="async" alt="DajbocTechDon engineer at a CNC machine in Satu Mare, Romania">
</div></section>
<section id="contact"><div class="wrap"><div class="sh"><span class="stag">Request a quote</span><h2>Send us your drawing</h2>
<p class="sdesc">Email your drawing (PDF, STEP, DXF…) to <a href="mailto:contact@dajboctechdon.com">contact@dajboctechdon.com</a> or call <a href="tel:+40744987550">+40 744 987 550</a>. You can also use the form on the page for your country.</p></div></div></section>"""
    alts = [(c['hreflang'], country_url(c)) for c in items]
    P = dict(hl='en', url=url, title=title, desc=desc, og_locale='en_GB',
             alternates=alts + [('x-default', url)], home='/', skip='Skip to content',
             nav_home='Home', nav_services='Services', nav_faq='FAQ', nav_contact='Contact',
             pill='RO', pill_href=JUDETE_HUB, pill_title='Romania – all counties',
             bc=bc, badge='Satu Mare, Romania → all of Europe',
             h1='CNC machining &amp; custom machine building <span class="gt">for all of Europe</span>',
             lead=('DajbocTechDon S.R.L. is a Romanian engineering and CNC manufacturing company. We machine precision metal '
                   'components and design and build custom machines in-house, and we deliver them to customers across the '
                   'European Union and the rest of Europe. Choose your country for local information.'),
             cta_quote='Request a quote', cta_href='#contact', cta_services='Company homepage',
             foot='CNC machining and custom machine building, Satu Mare, Romania',
             foot_links=[('Home', '/'), ('România', '/ro/'), ('Județe', JUDETE_HUB)])
    P['graph'] = [
        {"@type": "CollectionPage", "@id": BASE + url + "#webpage", "url": BASE + url, "name": title, "description": desc,
         "inLanguage": "en", "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID}, "breadcrumb": {"@id": BASE + url + "#breadcrumb"}},
        breadcrumb_ld(bc, url),
        {"@type": "ItemList", "name": "CNC machining by country", "numberOfItems": len(items),
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c['en'], "url": BASE + country_url(c)} for i, c in enumerate(items)]},
    ]
    return write(url, hub_page(P, inner))


def build_judete_hub():
    url = JUDETE_HUB
    title = 'Prelucrări CNC în toată România – toate județele | DajbocTechDon'
    desc = ('Prelucrări mecanice CNC, strunjire, frezare și utilaje la comandă din Satu Mare, cu livrare în toate cele 41 de '
            'județe și în București. Alegeți județul pentru termene și detalii.')
    bc = [('Acasă', '/ro/'), ('Județe', url)]
    regions = {}
    for j in JUDETE.values():
        regions.setdefault(j['region'], []).append(j)
    secs = []
    for r in ['Nord-Vest', 'Centru', 'Nord-Est', 'Sud-Est', 'Sud-Muntenia', 'București-Ilfov', 'Sud-Vest Oltenia', 'Vest']:
        links = ''.join(f'<a href="{judet_url(j)}"><b style="color:var(--accent);font-size:.75rem">{j["code"]}</b> Prelucrări CNC {esc(j["name"])} <small>· {esc(j["seat"])}</small></a>'
                        for j in sorted(regions[r], key=lambda x: x['name']))
        secs.append(f'<h2 style="margin:2.2rem 0 1rem;font-size:1.3rem">Regiunea {esc(r)}</h2><div class="cols">{links}</div>')
    inner = f"""<section id="judete"><div class="wrap">
 <div class="sh"><span class="stag">Zone deservite</span><h2>Livrăm piese CNC în toate județele</h2>
 <p class="sdesc">Atelierul nostru din Turț (județul Satu Mare) execută piese metalice prin strunjire și frezare CNC, prototipuri, serii mici și medii și utilaje la comandă. Pentru fiecare județ găsiți distanța, termenele de livrare și întrebările frecvente.</p></div>
 {''.join(secs)}
</div></section>
<section id="contact"><div class="wrap"><div class="sh"><span class="stag">Cerere de ofertă</span><h2>Trimiteți-ne desenul tehnic</h2>
<p class="sdesc">Trimiteți desenul (PDF, STEP, DXF…) la <a href="mailto:contact@dajboctechdon.com">contact@dajboctechdon.com</a> sau sunați la <a href="tel:+40744987550">+40 744 987 550</a>. Revenim cu ofertă de preț și termen de execuție.</p></div></div></section>"""
    P = dict(hl='ro', url=url, title=title, desc=desc, og_locale='ro_RO', alternates=[], home='/ro/', skip='Sari la conținut',
             nav_home='Acasă', nav_services='Servicii', nav_faq='FAQ', nav_contact='Contact',
             pill='EU', pill_href=EUROPE_HUB, pill_title='Europa',
             bc=bc, badge='Satu Mare → toată România',
             h1='Prelucrări CNC și utilaje la comandă <span class="gt">în toată România</span>',
             lead=('DajbocTechDon S.R.L. din Turț, județul Satu Mare, realizează strunjire și frezare CNC, piese metalice de precizie, '
                   'prototipuri și utilaje la comandă pentru clienți din toate cele 41 de județe și din București.'),
             cta_quote='Cere o ofertă', cta_href='#contact', cta_services='Pagina principală',
             foot='Prelucrări CNC și fabricare utilaje, Satu Mare, România',
             foot_links=[('Acasă', '/ro/'), ('Europa', EUROPE_HUB), ('English', '/')])
    P['graph'] = [
        {"@type": "CollectionPage", "@id": BASE + url + "#webpage", "url": BASE + url, "name": title, "description": desc,
         "inLanguage": "ro", "isPartOf": {"@id": SITE_ID}, "about": {"@id": ORG_ID}, "breadcrumb": {"@id": BASE + url + "#breadcrumb"}},
        breadcrumb_ld(bc, url),
        {"@type": "ItemList", "name": "Prelucrări CNC pe județe", "numberOfItems": len(JUDETE),
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": j['name'], "url": BASE + judet_url(j)}
                             for i, j in enumerate(sorted(JUDETE.values(), key=lambda x: x['name']))]},
    ]
    return write(url, hub_page(P, inner))


# ============================================================ sitemap
def sitemap(cluster):
    def u(loc, prio, alts=None, freq='monthly'):
        x = f'  <url>\n    <loc>{BASE}{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n'
        for h, a in (alts or []):
            x += f'    <xhtml:link rel="alternate" hreflang="{h}" href="{BASE}{a}"/>\n'
        return x + '  </url>\n'
    home_alts = [('en', '/'), ('ro', '/ro/'), ('x-default', '/')]
    out = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n']
    out.append(u('/', '1.0', home_alts))
    out.append(u('/ro/', '1.0', home_alts))
    out.append(u(EUROPE_HUB, '0.9', cluster))
    out.append(u(JUDETE_HUB, '0.9'))
    for c in COUNTRIES:
        out.append(u(country_url(c), '0.8', cluster))
    for j in sorted(JUDETE.values(), key=lambda x: (x['code'] != 'SM', x['name'])):
        out.append(u(judet_url(j), '0.9' if j['code'] == 'SM' else '0.7'))
    out.append('</urlset>\n')
    io.open('sitemap.xml', 'w', encoding='utf-8').write(''.join(out))


# ============================================================ homepage EN / RO
AREAS_CSS = ('<style>#areas{background:var(--bg2)}#areas .area-chips{display:flex;flex-wrap:wrap;gap:.55rem;justify-content:center;max-width:1100px;margin:0 auto}'
             '#areas .area-chips a{display:inline-flex;gap:.45rem;align-items:center;border:1px solid var(--border);border-radius:50px;padding:.42rem .9rem;'
             'font-size:.85rem;color:var(--muted);text-decoration:none;background:var(--bg3);transition:all .25s}'
             '#areas .area-chips a:hover{border-color:var(--accent);color:var(--accent)}#areas .area-chips b{font-size:.66rem;color:var(--accent);letter-spacing:.05em}'
             '#areas .area-more{text-align:center;margin-top:1.8rem;font-size:.95rem}#areas .area-more a{color:var(--accent);font-weight:600;text-decoration:none;margin:0 .6rem}</style>')


def areas_block(lang):
    if lang == 'en':
        chips = ''.join(f'<a href="{country_url(c)}" hreflang="{c["hreflang"]}" lang="{LANGS[c["lang"]]["code"]}"><b>{c["iso"]}</b>{esc(c["forms"]["N"])}</a>' for c in COUNTRIES)
        head_ = ('<div class="stag">Where We Deliver</div><h2 class="stit">CNC Machining Across Europe</h2>'
                 '<p class="sdesc">From our workshop in Satu Mare we deliver CNC machined parts and custom machines to every Romanian county '
                 'and to customers all over Europe. Choose your country for delivery times, customs and VAT information in your language:</p>')
        more = f'<a href="{EUROPE_HUB}">All European countries →</a><a href="{JUDETE_HUB}">Romania: all 41 counties + Bucharest →</a>'
    else:
        chips = ''.join(f'<a href="{judet_url(j)}"><b>{j["code"]}</b>{esc(j["name"])}</a>'
                        for j in sorted(JUDETE.values(), key=lambda x: x['name']))
        head_ = ('<div class="stag">Zone deservite</div><h2 class="stit">Prelucrări CNC în toată România</h2>'
                 '<p class="sdesc">Din atelierul nostru din Turț, județul Satu Mare, livrăm piese prelucrate CNC și utilaje la comandă '
                 'în toate cele 41 de județe și în București, precum și în toată Europa. Alegeți județul:</p>')
        more = f'<a href="{JUDETE_HUB}">Toate județele →</a><a href="{EUROPE_HUB}">Livrări în Europa →</a><a href="/ro/prelucrari-cnc-moldova/">Republica Moldova →</a>'
    return (f'<!-- AREAS:START -->\n{AREAS_CSS}\n<section id="areas">\n  <div class="sh">{head_}</div>\n'
            f'  <div class="area-chips">{chips}</div>\n  <p class="area-more">{more}</p>\n</section>\n<!-- AREAS:END -->')


def patch_home(path, lang):
    """Inserisce la sezione 'zone servite' e aggiorna areaServed nel JSON-LD della homepage."""
    if not os.path.exists(path):
        return
    s = io.open(path, encoding='utf-8').read()
    if '<!-- AREAS:START -->' not in s:
        s = s.replace('<!-- FAQ -->', '<!-- AREAS:START -->\n<!-- AREAS:END -->\n<!-- FAQ -->', 1)
    s = re.sub(r'<!-- AREAS:START -->.*?<!-- AREAS:END -->', lambda m: areas_block(lang), s, flags=re.S)
    m = re.search(r'(<!-- JSONLD:START -->\s*<script type="application/ld\+json">)(.*?)(</script>)', s, re.S)
    if m:
        data = json.loads(m.group(2))
        seen, area = set(), [{"@type": "Country", "name": "Romania" if lang == 'en' else 'România', "identifier": "RO"}]
        for c in COUNTRIES:
            if c['iso'] in seen:
                continue
            seen.add(c['iso'])
            x = {"@type": "Country", "name": c['en'].split(' (')[0]}
            if c['iso'] != 'XK':
                x["identifier"] = c['iso']
            area.append(x)
        for node in data.get('@graph', []):
            if node.get('@id') == ORG_ID:
                node['areaServed'] = area
        s = s[:m.start(2)] + '\n' + json.dumps(data, ensure_ascii=False, indent=1) + '\n' + s[m.end(2):]
    io.open(path, 'w', encoding='utf-8').write(s)


# ============================================================ main
GROUP_ORDER = [
    ('European Union', lambda c: c['customs'] == 'eu'),
    ('EEA, Switzerland & United Kingdom', lambda c: c['customs'] in ('eea', 'fta')),
    ('Microstates', lambda c: c['iso'] in ('AD', 'MC', 'SM')),
    ('Western Balkans, Moldova, Ukraine & Türkiye', lambda c: c['customs'] in ('saa', 'dcfta') or c['iso'] == 'TR'),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    # pulizia delle pagine generate in precedenza (solo le cartelle gestite da questo script)
    def clean(p):
        # in alcune cartelle (es. cartelle condivise con Claude) la cancellazione non e' permessa:
        # le pagine vengono comunque riscritte, quindi l'errore si puo' ignorare.
        if os.path.isdir(p):
            shutil.rmtree(p, ignore_errors=True)
    for c in COUNTRIES:
        clean(country_url(c).strip('/'))
    for j in JUDETE.values():
        clean(judet_url(j).strip('/'))

    cluster = [(c['hreflang'], country_url(c)) for c in COUNTRIES] + [('x-default', EUROPE_HUB)]
    chips = [(c['iso'], c['forms']['N'], country_url(c), c['hreflang']) for c in COUNTRIES]
    n = 0
    for c in COUNTRIES:
        build_country(c, chips, cluster); n += 1
    for j in JUDETE.values():
        build_judet(j, None); n += 1
    groups = []
    used = set()
    for g, f in GROUP_ORDER:
        gl = [c for c in COUNTRIES if f(c) and country_url(c) not in used]
        used.update(country_url(c) for c in gl)
        groups.append((g, gl))
    build_europe_hub(groups)
    build_judete_hub()
    sitemap(cluster)
    patch_home('index.html', 'en')
    patch_home(os.path.join('ro', 'index.html'), 'ro')
    print(f'OK: {n} landing page + 2 hub + sitemap.xml ({len(COUNTRIES)} paesi, {len(JUDETE)} judete)')


if __name__ == '__main__':
    main()
