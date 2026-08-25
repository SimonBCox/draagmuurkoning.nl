# draagmuurkoning.nl

Site van De Draagmuurkoning: doorbraakservice van MAREE Aanneming en Cox
Constructieadvies. Statische HTML, gedeelde stijl in `css/style.css`
(geen inline kopieën, anders dan bij coxadvies.nl). Hosting straks via
GitHub Pages met eigen repo, zelfde beheer als coxadvies.nl.

## Status: lanceerklaar, wacht op sleutel en DNS

Regel blijft: er komt niets op de site dat niet uit een echt
projectdossier komt. De bedragen-belofte is tijdelijk uit de teksten
gehaald tot de dossiers compleet zijn.

Het ruwe beeldmateriaal staat in `beeldmateriaal/` en blijft via
`.gitignore` buiten de repo. Geen inloggegevens of wachtwoorden in deze
map bewaren; die horen in `administratie/bedrijf/`.

## Nog te doen voor livegang

**Blokkerend**
- [ ] GitHub-repo aanmaken (bijv. SimonBCox/draagmuurkoning.nl, publiek),
      remote koppelen, pushen, Pages aanzetten op de main-branch
- [ ] DNS bij de registrar: A-records op de apex naar 185.199.108.153,
      185.199.109.153, 185.199.110.153 en 185.199.111.153, plus CNAME
      `www` naar `simonbcox.github.io`; daarna in GitHub Pages het domein
      invullen en Enforce HTTPS aanvinken (CNAME-bestand staat klaar)
- [ ] Web3Forms-sleutel aanmaken op web3forms.com en invullen bij
      `access_key` in index.html; afleveradressen staan in hún dashboard,
      niet in het formulier (les van coxadvies.nl)

**Kan na livegang, wel snel oppakken**
- [ ] WhatsApp-nummer in de knop "App een foto van je muur" (nu: link naar contactblok)
- [ ] JSON-LD op de homepage activeren zodra telefoon en plaats vaststaan
- [ ] Projectcijfers uit de dossiers: plaats, overspanning, profiel,
      werkdagen, bedrag; dan meta-regel en price-badge terugzetten op de
      kaarten (aanwijzingen staan als comments in de HTML) en de
      bedragen-belofte terugbrengen in de teksten
- [ ] Detailpagina's per project via sjabloon-project.html + sitemap aanvullen
- [ ] Portretfoto's Jordy en Simon (home + /over-ons/)
- [ ] Verzekeringen (CAR MAREE, beroepsaansprakelijkheid Cox) bevestigen
      en toevoegen op /over-ons/
- [ ] Handelsnaam "De Draagmuurkoning" registreren onder MAREE Aanneming
      B.V.; nodig voor het Google-bedrijfsprofiel
- [ ] Hero-videoloop zodra er liggend 1080p-materiaal is (mp4 H.264,
      15 tot 20 s, max 8 MB, geluidloos, met posterframe)

**Na livegang**
- [ ] Google-bedrijfsprofiel aanmaken (kan pas na handelsnaamregistratie)
- [ ] Google Search Console én Bing Webmaster Tools aanmelden
- [ ] Links plaatsen vanaf aannemingmaree.nl, maree-betonboringen.nl en coxadvies.nl
- [ ] Recensieroutine: na elke oplevering een recensieverzoek
- [ ] Per nieuw project: sjabloon kopiëren, sitemap.xml aanvullen, kaart toevoegen

## Kaart van de site

    /                       homepage (hero, stappen, projecten, team, faq, contact)
    /draagmuur-doorbreken/  dienstpagina, SEO-hoofdpagina
    /projecten/             overzicht; per project een submap via sjabloon-project.html
    /over-ons/              team en bedrijfsgegevens
    /faq/                   vragen, met FAQPage-schema
    /privacy/ /bedankt/     formulier-randwerk (noindex)
    404.html, robots.txt, sitemap.xml, llms.txt, CNAME

Let op de GitHub Pages-cache: wijzigingen zijn tot tien minuten na een
push nog niet zichtbaar. Hard verversen voor je concludeert dat iets
stuk is.
