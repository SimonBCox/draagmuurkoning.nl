# -*- coding: utf-8 -*-
"""Vervolg 2: de FAQ-teksten en de omzetting naar /en/."""
import re
from pathlib import Path

import maak_engels as m1
import maak_engels_deel2 as m2

SITE = m1.SITE

FAQ = [
    ("Veelgestelde vragen over draagmuur doorbreken | De Draagmuurkoning",
     "Questions about removing a load-bearing wall | De Draagmuurkoning"),
    ("Mag je zomaar een draagmuur doorbreken? Wat kost het, hoe lang duurt het en moet je uit huis? De antwoorden, zonder omwegen.",
     "Can you just remove a load-bearing wall? What does it cost, how long does it take and do you have to move out? Straight answers."),
    ("Vergunning, kosten, doorlooptijd, stof en staal: de antwoorden zonder omwegen.",
     "Permit, cost, timing, dust and steel: straight answers."),
    ("Antwoorden zonder omwegen", "Straight answers"),
    ("De vragen die we het vaakst krijgen, met het antwoord meteen vooraan. Staat jouw vraag er niet bij? Stel hem via het <a href=\"../#contact\" style=\"color:var(--gold)\">contactformulier</a>, dan hoor je het binnen één werkdag.",
     "The questions we get most often, with the answer up front. Not there? Ask us through the <a href=\"/en/#contact\" style=\"color:var(--gold)\">contact form</a> and you will hear back within one working day."),
    ("Hoe weet ik of een muur dragend is?", "How do I know if a wall is load-bearing?"),
    ("Steenachtige muren van 100 mm en dikker zijn vaak dragend, en de richting van de vloerbalken erboven verklapt veel: liggen die haaks op de muur, dan rusten ze er waarschijnlijk op. Zekerheid geeft alleen de bouwtekening of een blik van een constructeur. Stuur ons een paar foto's; dat is meestal genoeg voor een eerste oordeel en kost je niets.",
     "Masonry walls of 100 mm and thicker often carry load, and the direction of the joists above tells you a lot: if they run at right angles to the wall, they probably rest on it. Only the building drawings or an engineer can give certainty. Send us a few photos; that is usually enough for a first opinion and costs you nothing."),
    ("Steenachtige muren van 100 mm en dikker zijn vaak dragend, en de richting van de vloerbalken erboven verklapt veel. Zekerheid geeft alleen de bouwtekening of een beoordeling door een constructeur. Een paar foto's zijn meestal genoeg voor een eerste oordeel.",
     "Masonry walls of 100 mm and thicker often carry load, and the direction of the joists above tells you a lot. Only the building drawings or an assessment by a structural engineer gives certainty. A few photos are usually enough for a first opinion."),
    ("Reken op enkele duizenden euro's voor het complete traject. De prijs hangt af van de overspanning, van wat er op de muur draagt en van de afwerking die je wilt. Het gaat in twee stappen: na je foto's krijg je een richtprijs voor het geheel en een vaste prijs voor tekening en berekening. Zodra de berekening klaar is, weten we welk profiel en welke opleggingen nodig zijn, en dan staat de prijs voor de uitvoering vast. Bij <a href=\"../projecten/\">onze projecten</a> zie je hoe zulke doorbraken er in de praktijk uitzien.",
     "Expect a few thousand euros for the complete job. The price depends on the span, on what the wall carries and on the finishing you want. It works in two steps: after your photos you get an indicative price for the whole job plus a fixed price for the drawing and the calculation. Once the calculation is done we know which section and which bearings are needed, and the price for the work is fixed. Our <a href=\"/en/projects/\">projects</a> show what jobs like this look like in practice."),
    ("Enkele duizenden euro's voor het complete traject, afhankelijk van de overspanning en van wat er op de muur draagt. De prijs komt in twee stappen tot stand: na de eerste foto's volgt een richtprijs voor het geheel plus een vaste prijs voor tekening en berekening. Zodra de constructieberekening klaar is, is bekend welk profiel en welke opleggingen nodig zijn en staat de prijs voor de uitvoering vast.",
     "A few thousand euros for the complete job, depending on the span and on what the wall carries. The price comes in two steps: after the first photos there is an indicative price for the whole job plus a fixed price for the drawing and the calculation. Once the structural calculation is done, the section and the bearings are known and the price for the work is fixed."),
    ("Hoe lang duurt een doorbraak?", "How long does the job take?"),
    ("De uitvoering duurt meestal twee tot vijf werkdagen, inclusief herstelwerk. Daarvoor zit het papierwerk: tekening, berekening en de vergunningsprocedure van de gemeente, die wettelijk acht weken beslistermijn heeft. Je krijgt van ons vooraf één planning voor het geheel.",
     "The work usually takes two to five working days, including making good. Before that comes the paperwork: drawing, calculation and the municipal permit procedure, for which the municipality has eight weeks by law. You get one schedule for the whole thing up front."),
    ("De uitvoering duurt meestal twee tot vijf werkdagen, inclusief herstelwerk. Daarvoor zit het papierwerk: tekening, berekening en de vergunningsprocedure, waarvoor de gemeente wettelijk acht weken beslistermijn heeft.",
     "The work usually takes two to five working days, including making good. Before that comes the paperwork: drawing, calculation and the permit procedure, for which the municipality has eight weeks by law."),
    ("Moet ik uit huis tijdens de uitvoering?", "Do I have to move out while you work?"),
    ("Meestal niet. We schermen het werkgebied af en zagen met stofafzuiging. Het blijft sloopwerk, dus een paar dagen stof en lawaai horen erbij, maar in de rest van het huis kun je gewoon blijven wonen.",
     "Usually not. We screen off the work area and saw with dust extraction. It stays demolition work, so a few days of dust and noise come with it, but you can carry on living in the rest of the house."),
    ("Meestal niet. Het werkgebied wordt afgeschermd en beton wordt gezaagd met stofafzuiging. Het blijft sloopwerk, dus een paar dagen stof en lawaai horen erbij, maar wonen in de rest van het huis kan gewoon doorgaan.",
     "Usually not. The work area is screened off and concrete is sawn with dust extraction. It stays demolition work, so a few days of dust and noise come with it, but living in the rest of the house can carry on."),
    ("Wat komt er voor de muur in de plaats?", "What replaces the wall?"),
    ("Een stalen ligger die het gewicht van de verdiepingen overneemt, opgelegd op het muurwerk dat blijft staan. Bij brede openingen of weinig overblijvend muurwerk komen er stalen kolommen onder: een portaal. Welk profiel er nodig is, volgt uit de berekening. Meer daarover lees je bij <a href=\"../draagmuur-doorbreken/\">draagmuur doorbreken</a>.",
     "A steel beam that takes over the load from the floors above, bearing on the masonry that stays. For wide openings, or where little masonry is left, steel columns go underneath: a portal frame. Which section is needed follows from the calculation. There is more about that under <a href=\"/en/load-bearing-wall-removal/\">removing a load-bearing wall</a>."),
    ("Mijn muur is al doorgebroken en de gemeente vraagt om papieren. Kan dat nog?",
     "My wall is already open and the municipality is asking for paperwork. Can that still be fixed?"),
    ("Ja, dat heet legalisatie. We beoordelen wat er geplaatst is, rekenen de bestaande situatie door en leveren de berekening en tekening die de gemeente vraagt. Is er constructief iets niet in orde, dan hoor je dat eerlijk, met een voorstel om het op te lossen.",
     "Yes, that is called legalisation. We assess what has been installed, calculate the existing situation and deliver the drawing and calculation the municipality asks for. If something is not structurally sound, you will hear that honestly, with a proposal to put it right."),
    ("Nee. Voor het doorbreken van een dragende muur is vrijwel altijd een omgevingsvergunning nodig, met een constructieberekening die aantoont dat je huis veilig blijft. Wij verzorgen de tekening, de berekening en de aanvraag, dus je hoeft zelf niets met de gemeente te regelen.",
     "No. Removing a load-bearing wall almost always needs an environmental permit, with a structural calculation showing your home stays safe. We take care of the drawing, the calculation and the application, so you never have to deal with the municipality yourself."),
    ("Antwoord niet gevonden?", "Question not answered?"),
    ("Stel je vraag of stuur een paar foto's. Je hoort binnen één werkdag van ons.",
     "Ask your question or send a few photos. You will hear from us within one working day."),
    ("Nee. Voor het doorbreken van een dragende muur is vrijwel altijd een omgevingsvergunning nodig, met een constructieberekening die aantoont dat de woning veilig blijft. De Draagmuurkoning verzorgt de tekening, de berekening en de aanvraag.",
     "No. Removing a load-bearing wall almost always needs an environmental permit, with a structural calculation showing the home stays safe. De Draagmuurkoning takes care of the drawing, the calculation and the application."),
    ("Ja. Wie al een aannemer heeft, kan alleen tekening en berekening afnemen. Wie al een goedgekeurde berekening heeft, kan alleen de uitvoering afnemen. Het totaalpakket is er voor wie er geen omkijken naar wil hebben.",
     "Yes. If you already have a builder, you can order just the drawing and the calculation. If you already have an approved calculation, you can order just the work. The complete package is for people who would rather not think about it."),
]

PAGINAS = {
    "index.html": ("en/index.html", m1.HOME, "/", "/en/"),
    "draagmuur-doorbreken/index.html": ("en/load-bearing-wall-removal/index.html", m2.DIENST, "/draagmuur-doorbreken/", "/en/load-bearing-wall-removal/"),
    "projecten/index.html": ("en/projects/index.html", m2.PROJECTEN + m1.CARROUSEL, "/projecten/", "/en/projects/"),
    "over-ons/index.html": ("en/about/index.html", m2.OVER, "/over-ons/", "/en/about/"),
    "faq/index.html": ("en/faq/index.html", FAQ + m1.HOME, "/faq/", "/en/faq/"),
    "privacy/index.html": ("en/privacy/index.html", m2.PRIVACY, "/privacy/", "/en/privacy/"),
    "bedankt/index.html": ("en/thank-you/index.html", m2.BEDANKT, "/bedankt/", "/en/thank-you/"),
}

LINKS = [
    (r'href="(\.\./)*draagmuur-doorbreken/"', 'href="/en/load-bearing-wall-removal/"'),
    (r'href="(\.\./)*projecten/"', 'href="/en/projects/"'),
    (r'href="(\.\./)*over-ons/"', 'href="/en/about/"'),
    (r'href="(\.\./)*faq/"', 'href="/en/faq/"'),
    (r'href="(\.\./)*privacy/"', 'href="/en/privacy/"'),
    (r'href="(\.\./)*bedankt/"', 'href="/en/thank-you/"'),
    (r'href="\.\./#contact"', 'href="/en/#contact"'),
    (r'href="\.\./\.\./#contact"', 'href="/en/#contact"'),
    (r'href="\./"', 'href="/en/"'),
    (r'href="\.\./"', 'href="/en/"'),
]

MIDDELEN = [
    (r'(\.\./)*css/style\.css', '/css/style.css'),
    (r'(\.\./)*js/consent\.js', '/js/consent.js'),
    (r'(\.\./)*js/carrousel\.js', '/js/carrousel.js'),
    (r'(src|href)="(\.\./)*images/', r'\1="/images/'),
    (r'href="(\.\./)*favicon\.svg"', 'href="/favicon.svg"'),
]

TAALKNOP_EN = '<a class="lang" href="{nl}" hreflang="nl" lang="nl" title="Nederlandse versie">NL</a>\n    '
TAALKNOP_NL = '<a class="lang" href="{en}" hreflang="en" lang="en" title="English version">EN</a>\n    '


def hreflang(nl_pad, en_pad):
    b = "https://www.draagmuurkoning.nl"
    return (f'<link rel="alternate" hreflang="nl" href="{b}{nl_pad}">\n'
            f'<link rel="alternate" hreflang="en" href="{b}{en_pad}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{b}{nl_pad}">\n')


def zet_om(bron, doel, woordenlijst, nl_pad, en_pad):
    t = (SITE / bron).read_text(encoding="utf-8")

    # De Nederlandse bron heeft inmiddels zelf een taalknop en hreflang-regels;
    # die halen we eruit zodat opnieuw draaien niets verdubbelt.
    t = re.sub(r'\s*<a class="lang"[^>]*>[A-Z]{2}</a>', '', t)
    t = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', '', t)

    for nl, en in sorted(woordenlijst, key=lambda p: -len(p[0])):
        t = t.replace(nl, en)
    for nl, en in sorted(m1.GEDEELD, key=lambda p: -len(p[0])):
        t = t.replace(nl, en)

    for patroon, vervang in MIDDELEN:
        t = re.sub(patroon, vervang, t)
    for patroon, vervang in LINKS:
        t = re.sub(patroon, vervang, t)

    t = t.replace('<html lang="nl">', '<html lang="en">')
    t = t.replace('content="nl_NL"', 'content="en_GB"')
    t = t.replace(f'<link rel="canonical" href="https://www.draagmuurkoning.nl{nl_pad}">',
                  f'<link rel="canonical" href="https://www.draagmuurkoning.nl{en_pad}">')
    t = t.replace(f'<meta property="og:url" content="https://www.draagmuurkoning.nl{nl_pad}">',
                  f'<meta property="og:url" content="https://www.draagmuurkoning.nl{en_pad}">')
    t = t.replace('<link rel="stylesheet" href="/css/style.css">',
                  hreflang(nl_pad, en_pad) + '<link rel="stylesheet" href="/css/style.css">')
    t = t.replace('<a class="btn nav-cta"', TAALKNOP_EN.format(nl=nl_pad) + '<a class="btn nav-cta"')
    if 'class="lang"' not in t:  # bedanktpagina heeft geen cta-knop in de balk
        t = t.replace('</div>\n  </div>\n</nav>', '</div>\n    ' + TAALKNOP_EN.format(nl=nl_pad).rstrip() + '\n  </div>\n</nav>')

    uit = SITE / doel
    uit.parent.mkdir(parents=True, exist_ok=True)
    uit.write_text(t, encoding="utf-8")
    return doel


def vul_nederlands_aan():
    """Zet de EN-knop en de hreflang-verwijzingen in de Nederlandse pagina's."""
    for bron, (_, _, nl_pad, en_pad) in PAGINAS.items():
        p = SITE / bron
        t = p.read_text(encoding="utf-8")
        if 'class="lang"' in t:
            continue
        diepte = bron.count("/")
        wortel = "" if diepte == 0 else "../" * diepte
        t = t.replace(f'<link rel="stylesheet" href="{wortel}css/style.css">',
                      hreflang(nl_pad, en_pad) + f'<link rel="stylesheet" href="{wortel}css/style.css">')
        if '<a class="btn nav-cta"' in t:
            t = t.replace('<a class="btn nav-cta"', TAALKNOP_NL.format(en=en_pad) + '<a class="btn nav-cta"')
        else:
            t = t.replace('</div>\n  </div>\n</nav>', '</div>\n    ' + TAALKNOP_NL.format(en=en_pad).rstrip() + '\n  </div>\n</nav>')
        p.write_text(t, encoding="utf-8")
        print("NL bijgewerkt:", bron)


if __name__ == "__main__":
    for bron, (doel, lijst, nl_pad, en_pad) in PAGINAS.items():
        print("EN gemaakt:", zet_om(bron, doel, lijst, nl_pad, en_pad))
    vul_nederlands_aan()
