# Domača naloga 4
# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for ime1, x, y in kraji:
        if ime1 == ime:
            return x, y
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1, kraji)
    x2,y2 = koordinate(ime2, kraji)
    razdalja1 = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja1

def v_dometu(ime, domet, kraji):
    izpis = []
    for ime1, x, y in kraji:
        if ime1 == ime:
            x2=x
            y2=y
        if ime1 != ime:
            razdalja2 = razdalja(ime, ime1, kraji)
            if razdalja2 <= domet:
                izpis.append(ime1)
    return izpis

def najbolj_oddaljeni(ime, imena, kraji):
    najbolj_kraj = ""
    najbolj_razd = 0
    for ime1, x, y in kraji:
        if ime1 == ime:
            x2 = x
            y2 = y
    for ime2 in imena:
        for ime3, x1, y1 in kraji:
            if ime2 == ime3:
                x3=x1
                y3=y1
        razdalja2 = razdalja_koordinat(x2, y2, x3, y3)
        if razdalja2 > najbolj_razd:
            najbolj_razd = razdalja2
            najbolj_kraj = ime2
    return najbolj_kraj

def zalijemo(ime, domet, kraji):
    najbolj_kraj = ""
    najbolj_razd = 0
    for ime1, x, y in kraji:
        if ime1 == ime:
            x2 = x
            y2 = y
    for ime2, x, y in kraji:
        razdalja = razdalja_koordinat(x, y, x2, y2)
        if razdalja >najbolj_razd and razdalja <= domet:
            najbolj_razd = razdalja
            najbolj_kraj = ime2
    return najbolj_kraj

def presek(s1, s2):
    izpis = []
    for st1 in s1:
        for st2 in s2:
            if st1 == st2:
                izpis.append(st2)
    return izpis

def skupno_zalivanje(ime1, ime2, domet, kraji):
    izpis = []
    x1,y1 = koordinate(ime1, kraji)
    x2,y2 = koordinate(ime2, kraji)
    for ime, x, y in kraji:
        if ime != ime1 and ime != ime2:
            razdalja1 = razdalja_koordinat(x, y, x1, y1)
            if razdalja1 <= domet:
                razdalja2 = razdalja_koordinat(x, y, x2, y2)
                if razdalja2 <= domet:
                    izpis.append(ime)
    return izpis


