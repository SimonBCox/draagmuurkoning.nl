# draagmuurkoning.nl

Site van De Draagmuurkoning: doorbraakservice van MAREE Aanneming en Cox
Constructieadvies. Statische HTML, gedeelde stijl in `css/style.css`
(geen inline kopieën, anders dan bij coxadvies.nl). Hosting straks via
GitHub Pages met eigen repo, zelfde beheer als coxadvies.nl.

## Status: prototype

Alles tussen `[haken]` is bewust een invulveld. Er komt niets live dat
niet uit een echt projectdossier komt.

## Checklist voor livegang

**Besluiten (Simon + Jordy)**
- [ ] Handelsnaam "De Draagmuurkoning" registreren bij KvK onder MAREE Aanneming B.V.
- [ ] Contractpartij en verzekeringen bepalen; invullen op /over-ons/ en /privacy/
- [ ] Echte projectbedragen op de site: akkoord Jordy
- [ ] Aanspreekvorm definitief (site staat nu op "je")
- [ ] Werkgebied definitief (nu: Betuwe, Nijmegen, Arnhem als anker)
- [ ] Hoofdnummer en mailadres (info@draagmuurkoning.nl waarheen?)

**Inhoud**
- [ ] Drie projecten invullen: foto's Jordy + bedragen + constructiegegevens
      (kaarten op / en /projecten/, detailpagina's via sjabloon-project.html)
- [ ] Portretfoto's Jordy en Simon (home + /over-ons/)
- [ ] Videoloop hero (mp4 H.264, 15 tot 20 s, max 8 MB) + posterframe;
      tot die tijd: foto-hero
- [ ] Favicon en og:image maken
- [ ] JSON-LD op de homepage activeren (staat in comment) met echte NAP-gegevens

**Techniek**
- [ ] Nieuwe GitHub-repo aanmaken, deze map erin, Pages aanzetten
- [ ] DNS: A-records apex naar GitHub Pages, CNAME www; HTTPS aanvinken
      (CNAME-bestand staat al klaar met www.draagmuurkoning.nl)
- [ ] Web3Forms: nieuwe sleutel aanmaken, afleveradressen in het dashboard
      instellen (les coxadvies: afleveradres staat in hun dashboard, niet in
      het formulier), action + redirect naar /bedankt/ invullen
- [ ] WhatsApp-links invullen in de knoppen op de homepage

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
