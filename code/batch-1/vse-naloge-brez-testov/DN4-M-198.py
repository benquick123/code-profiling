# Tu pišite svoje funkcije:

from math import sqrt

def koordinate(ime, kraji):
    for kraj_sez, x, y in kraji:
        if ime == kraj_sez:
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    tocke = (koordinate(ime1, kraji) + koordinate(ime2, kraji))
    x1, y1, x2, y2 = tocke
    return razdalja_koordinat(x1, y1, x2, y2)

"""---------------------------------------------------------------------------"""

def v_dometu(ime, domet, kraji):
    resitev = []
    x, y = koordinate(ime, kraji)
    for kraj_sez, x3, y3 in kraji:
        if razdalja_koordinat(x3, y3, x, y) <= domet and ime != kraj_sez:
            resitev.append(kraj_sez)
    return resitev

def najbolj_oddaljeni(ime, imena, kraji):
    x, y = koordinate(ime, kraji)
    naj_razdalja = 0
    naj_kraj = ""
    for mesto in imena:
        x1, y1 = koordinate(mesto, kraji)
        r = razdalja_koordinat(x1, y1, x, y)
        if r > naj_razdalja:
            naj_razdalja = r
            naj_kraj = mesto
    return naj_kraj


def zalijemo(ime, domet, kraji):
    vsi_v_dosegu = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, vsi_v_dosegu, kraji)

"""------------------------------------------------------------------"""

def presek(s1, s2):
    s_resitev =[]
    for vrednost1 in s1:
        if vrednost1 in s2:
            s_resitev.append(vrednost1)
    return s_resitev

def skupno_zalivanje(ime1, ime2, domet, kraji):
    domet_ime1 = v_dometu(ime1, domet, kraji)
    domet_ime2 = v_dometu(ime2, domet, kraji)
    return presek(domet_ime1, domet_ime2)


