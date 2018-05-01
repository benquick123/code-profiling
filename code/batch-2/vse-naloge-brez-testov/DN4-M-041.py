# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for ime1, x1, y1 in kraji:
        if ime1 == ime:
            return x1, y1
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    lst = []
    x1, y1 = koordinate(ime, kraji)
    for ime2, x2, y2 in kraji:
        if ime2 != ime:
            raz = razdalja_koordinat(x1, y1, x2, y2)
            if raz <= domet:
                lst.append(ime2)
    return lst

def najbolj_oddaljeni(ime, imena, kraji):
    max_razdalja = 0
    max_ime = ""
    for ime2 in imena:
        raz = razdalja(ime, ime2, kraji)
        if max_razdalja < raz:
            max_razdalja = raz
            max_ime = ime2
    return max_ime

def zalijemo(ime, domet, kraji):
    lst = v_dometu(ime, domet, kraji)
    max_razdalja = 0
    kraj = ""
    for e in lst:
        razdalja_vsak_kraj = razdalja(ime, e, kraji)
        if max_razdalja < razdalja_vsak_kraj:
            max_razdalja = razdalja_vsak_kraj
            kraj = e
    return kraj

def presek(s1, s2):
    skupni = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                skupni.append(e1)
    return skupni




