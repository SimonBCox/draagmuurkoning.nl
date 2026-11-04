"""Bouwt het vierkante logo voor het Google-bedrijfsprofiel.

Google toont het logo klein, als vierkant of als rondje naast de naam. Het
woordmerk is daarvoor te breed, dus hier staan "Draagmuur" en "koning" onder
elkaar, met de kroon op de g zoals in het woordmerk. De letteromtrekken komen
uit logo_wordmerk_licht.svg (gemaakt door bouw_logo.py), zodat het vierkant
altijd met het woordmerk overeenkomt. Alles blijft binnen de ingeschreven
cirkel, want Google snijdt het logo op sommige plekken rond af.
"""

import re
from pathlib import Path

import fitz  # PyMuPDF, rendert de SVG naar PNG

HIER = Path(__file__).parent
BRON = HIER / "logo_wordmerk_licht.svg"

ZIJDE = 720.0          # pixels; Google vraagt minimaal 250, 720 is het advies
ACHTERGROND = "#121417"  # --coal van de site, ook de favicon
BLOKBREEDTE = 560.0    # breedte van "Draagmuur" in het vierkant
REGELAFSTAND = 170.0   # basislijn tot basislijn, in eenheden van het woordmerk

CAP = 100.0            # kapitaalhoogte in het woordmerk (bouw_logo.CAP)


def lees_woordmerk():
    tekst = BRON.read_text(encoding="utf-8")
    groepen = re.findall(r'(<g fill="[^"]+") transform="translate\(([\d.]+),([\d.]+)\) (scale\([^)]+\))">(.*?)</g>', tekst, re.S)
    kroon = re.search(r'<path fill="([^"]+)" d="(M [^"]+)"/>\s*</svg>', tekst)
    hoogte = float(re.search(r'viewBox="0 0 [\d.]+ ([\d.]+)"', tekst).group(1))
    if len(groepen) != 2 or not kroon:
        raise SystemExit(f"{BRON.name} heeft niet de verwachte opbouw (twee woorden en een kroon)")
    return groepen, kroon, hoogte


def bouw():
    (donker, goud), kroon, hoogte = lees_woordmerk()
    x_donker, basis = float(donker[1]), float(donker[2])
    x_goud = float(goud[1])
    marge = x_donker
    onderkant = hoogte - marge - basis      # staartlengte onder de basislijn

    kroon_x = [float(x) for x in re.findall(r"([\d.]+),[\d.]+", kroon.group(2))]
    breedte_1 = x_goud - x_donker
    breedte_2 = max(kroon_x) - x_goud

    k = BLOKBREEDTE / breedte_1
    # Kapitaal van regel 1 tot staart van regel 2 staat midden in het vierkant.
    b1 = (ZIJDE - (REGELAFSTAND + onderkant - CAP) * k) / 2
    b2 = b1 + REGELAFSTAND * k

    def plaats(x0, x, y, inhoud):
        return f'<g transform="translate({x:.2f},{y:.2f}) scale({k:.5f}) translate({-x0:.2f},{-basis:.2f})">{inhoud}</g>'

    regel_1 = f'{donker[0]} transform="translate({x_donker:.2f},{basis:.2f}) {donker[3]}">{donker[4]}</g>'
    regel_2 = (f'{goud[0]} transform="translate({x_goud:.2f},{basis:.2f}) {goud[3]}">{goud[4]}</g>'
               f'<path fill="{kroon.group(1)}" d="{kroon.group(2)}"/>')

    svg = "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ZIJDE:.0f} {ZIJDE:.0f}" width="{ZIJDE:.0f}" height="{ZIJDE:.0f}" role="img" aria-label="De Draagmuurkoning">',
        "<title>De Draagmuurkoning</title>",
        f'<rect width="{ZIJDE:.0f}" height="{ZIJDE:.0f}" fill="{ACHTERGROND}"/>',
        plaats(x_donker, (ZIJDE - breedte_1 * k) / 2, b1, regel_1),
        plaats(x_goud, (ZIJDE - breedte_2 * k) / 2, b2, regel_2),
        "</svg>",
    ])
    doel = HIER / "logo_vierkant.svg"
    doel.write_text(svg, encoding="utf-8")

    pagina = fitz.open(doel)[0]
    pagina.get_pixmap(alpha=False).save(HIER / "logo_vierkant.png")
    print(f"logo_vierkant  {ZIJDE:.0f} x {ZIJDE:.0f}   schaal {k:.3f}, kapitaalhoogte {CAP * k:.0f} px")


bouw()
