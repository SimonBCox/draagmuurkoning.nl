"""Bouwt het logo van De Draagmuurkoning op als echte vector.

De letters komen als omtrekken uit Poppins, niet uit een afbeelding: exacte
curven, scherp op elk formaat. De maatvoering volgt de lettermaten
(kapitaalhoogte, x-hoogte, staartlengte), zodat de onderregel nooit tegen de
staart van de g aan loopt.
"""

import re
from pathlib import Path

import cv2
import numpy as np
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

HIER = Path(__file__).parent
FONTS = HIER / "fonts"
BRON = Path(r"C:\Users\simon\OneDrive\Cox Constructieadvies\website\draagmuurkoning.nl\images\logo\logo_draagmuurkoning_officieel.jpg")
DOEL = BRON.parent

WEGING = "SemiBold"
WOORD_DONKER = "Draagmuur"
WOORD_GOUD = "koning"
ONDERREGEL = "SPECIALIST IN CONSTRUCTIE DOORBRAKEN"

CAP = 100.0          # kapitaalhoogte in SVG-eenheden; alles schaalt hierop mee
MARGE = 14.0
REGEL_BREEDTE = 0.60  # onderregel t.o.v. de breedte van het woordmerk
REGEL_SPATIE = 0.24   # letterspatiëring onderregel, in em


def merkkleuren():
    """Haalt de twee kleuren uit het aangeleverde logo."""
    afb = cv2.imread(str(BRON))[415:665, 115:1375]
    blauw, groen, rood = (afb[:, :, i].astype(int) for i in range(3))
    lum = 0.299 * rood + 0.587 * groen + 0.114 * blauw
    goud = (rood - blauw) > 60
    donker = ((rood - blauw) <= 60) & (lum < 90)
    naar_hex = lambda m: "#%02X%02X%02X" % tuple(int(np.median(k[m])) for k in (rood, groen, blauw))
    return naar_hex(donker), naar_hex(goud)


class Zetter:
    def __init__(self, bestand):
        self.font = TTFont(bestand)
        self.glyfs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.upem = self.font["head"].unitsPerEm
        self.hmtx = self.font["hmtx"]
        os2 = self.font["OS/2"]
        self.cap = getattr(os2, "sCapHeight", 700) or 700
        self.xh = getattr(os2, "sxHeight", 520) or 520
        self.desc = abs(self.font["hhea"].descent)

    def zet(self, tekst, spatie_em=0.0):
        paden, x = [], 0.0
        for teken in tekst:
            naam = self.cmap.get(ord(teken))
            if naam is None:
                x += self.upem * 0.28
                continue
            pen = SVGPathPen(self.glyfs)
            self.glyfs[naam].draw(pen)
            d = pen.getCommands()
            if d:
                paden.append(f'<path transform="translate({x:.1f},0)" d="{d}"/>')
            x += self.hmtx[naam][0] + spatie_em * self.upem
        if spatie_em:
            x -= spatie_em * self.upem
        return "".join(paden), x


def kroonpad(x, y, b, h):
    """Drie punten met een gesloten voet, in de stijl van het origineel."""
    p = [(0, 1), (0.10, 0.16), (0.32, 0.60), (0.50, 0.0), (0.68, 0.60), (0.90, 0.16), (1, 1)]
    punten = " ".join(f"{x + px * b:.2f},{y + py * h:.2f}" for px, py in p)
    return "M " + punten.replace(" ", " L ", 0).replace(",", ",", 1) and "M " + " L ".join(
        f"{x + px * b:.2f},{y + py * h:.2f}" for px, py in p) + " Z"


def bouw(met_onderregel=True):
    kleur_donker, kleur_goud = merkkleuren()
    woord = Zetter(FONTS / f"Poppins-{WEGING}.ttf")
    regel = Zetter(FONTS / "Poppins-Medium.ttf")

    S = CAP / woord.cap
    pad_donker, br_donker = woord.zet(WOORD_DONKER)
    pad_goud, br_goud = woord.zet(WOORD_GOUD)
    breedte_woord = (br_donker + br_goud) * S
    staart = woord.desc * S
    xhoogte = woord.xh * S

    pad_regel, br_regel_font = regel.zet(ONDERREGEL, REGEL_SPATIE)
    S_regel = (REGEL_BREEDTE * breedte_woord) / br_regel_font
    breedte_regel = br_regel_font * S_regel
    cap_regel = regel.cap * S_regel

    basislijn = MARGE + CAP
    onder_woord = basislijn + staart

    if met_onderregel:
        regel_basislijn = onder_woord + CAP * 0.30 + cap_regel
        hoogte = regel_basislijn + MARGE
    else:
        regel_basislijn = None
        hoogte = onder_woord + MARGE

    breedte = breedte_woord + 2 * MARGE
    x_woord = MARGE

    # Kroontje boven de laatste letter.
    k_b = CAP * 0.42
    k_h = CAP * 0.30
    k_x = x_woord + breedte_woord - k_b - CAP * 0.02
    k_y = basislijn - xhoogte - k_h + CAP * 0.03
    kroon = kroonpad(k_x, k_y, k_b, k_h)

    for naam_kleur, (tekst_kleur, goud_kleur) in {
        "donker": (kleur_donker, kleur_goud),
        "licht": ("#EFECE5", "#E2A43C"),
    }.items():
        delen = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {breedte:.1f} {hoogte:.1f}" width="{breedte:.0f}" height="{hoogte:.0f}" role="img" aria-label="De Draagmuurkoning">',
            "<title>De Draagmuurkoning</title>",
            f'<g fill="{tekst_kleur}" transform="translate({x_woord:.2f},{basislijn:.2f}) scale({S:.5f},-{S:.5f})">{pad_donker}</g>',
            f'<g fill="{goud_kleur}" transform="translate({x_woord + br_donker * S:.2f},{basislijn:.2f}) scale({S:.5f},-{S:.5f})">{pad_goud}</g>',
            f'<path fill="{goud_kleur}" d="{kroon}"/>',
        ]
        if met_onderregel:
            x_regel = (breedte - breedte_regel) / 2
            y_lijn = regel_basislijn - cap_regel / 2
            gat = CAP * 0.16
            blok = 0.80 * breedte_woord              # lijnen lopen niet tot de rand door
            lijn_lengte = max((blok - breedte_regel) / 2 - gat, 6)
            x_lijn_links = (breedte - blok) / 2
            delen += [
                f'<g fill="{tekst_kleur}" transform="translate({x_regel:.2f},{regel_basislijn:.2f}) scale({S_regel:.5f},-{S_regel:.5f})">{pad_regel}</g>',
                f'<rect fill="{goud_kleur}" x="{x_lijn_links:.2f}" y="{y_lijn:.2f}" width="{lijn_lengte:.2f}" height="{CAP*0.022:.2f}"/>',
                f'<rect fill="{goud_kleur}" x="{breedte - x_lijn_links - lijn_lengte:.2f}" y="{y_lijn:.2f}" width="{lijn_lengte:.2f}" height="{CAP*0.022:.2f}"/>',
            ]
        delen.append("</svg>")
        stam = "logo" if met_onderregel else "logo_wordmerk"
        (DOEL / f"{stam}_{naam_kleur}.svg").write_text("\n".join(delen), encoding="utf-8")

    soort = "met onderregel" if met_onderregel else "woordmerk"
    print(f"{soort:16} {breedte:6.0f} x {hoogte:5.0f}   kleuren {kleur_donker} / {kleur_goud}")


bouw(True)
bouw(False)
