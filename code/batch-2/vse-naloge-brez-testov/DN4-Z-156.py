# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    s = []
    x0, y0 = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        if kraj != ime and razdalja_koordinat(x0, y0, x, y) <= domet:
            s.append(kraj)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    trenutna_razdalja = 0
    x0, y0 = koordinate(ime, kraji)
    for i in imena:
        x1, y1 = koordinate(i, kraji)
        if razdalja_koordinat(x0, y0, x1, y1) > trenutna_razdalja:
            trenutna_razdalja = razdalja_koordinat(x0, y0, x1, y1)
            ime_naj_oddaljenega = i
    return ime_naj_oddaljenega

def zalijemo(ime, domet, kraji):
    s = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, s, kraji)


def presek(s1, s2):
    s = []
    for e in s1:
        for e2 in s2:
            if e == e2:
                s.append(e)
    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return presek(s1, s2)

