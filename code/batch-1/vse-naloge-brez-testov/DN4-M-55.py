# Tu pišite svoje funkcije:

from math import *


def koordinate(ime, kraji):
    for kr,x,y in kraji:
        if ime == kr:
            return zip(x,y)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1,kraji)
    x2,y2 = koordinate(ime2,kraji)

    return razdalja_koordinat(x1,y1,x2,y2)


def v_dometu(ime, domet, kraji):
    x1,y1 = koordinate(ime,kraji)
    kraj = []
    for kr,x,y in kraji:
        s1 = sqrt((x1 - x)**2 + (y1 - y)**2)
        if domet > s1:
            kraj.append(kr)
    return kraj

def najbolj_oddaljeni(ime, imena, kraji)
    x,y = koordinate(ime, karji)
    razdalja = 0
    krajNaj = ''
    for imen in imena:
        x1,y1 = koordinate(imen,kraji)
        if razdalja < razdalja_koordinat(x,y,x1,y1):
            krajNaj = imen
    return krajNaj

def zalijemo(ime, domet, kraji):
    x,y = koordinate(ime,kraji)
    NajRazdalja = 0
    NajKraj = ''
    for kr,x1,y1 in kraji:
        s = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if domet > s1 > NajRazdalja:
            NajRazdalja = s
            NajKraj = kr
    return NajKraj

