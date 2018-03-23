from math import *

def koordinate(ime, kraji):
    for e, k1, k2 in kraji:
        if e == ime:
            return k1, k2

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja

def v_dometu(ime, domet, kraji):
    s = []
    x1, y1 = koordinate(ime, kraji)
    for ime2, x2, y2 in kraji:
        razdalja1 = razdalja_koordinat(x1, y1, x2 ,y2)
        if razdalja1 <= domet and ime != ime2:
            s.append(ime2)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razd = 0
    naj_ime = ''
    for im, x1, y1 in kraji:
        if ime == im:
            break
    for ime in imena:
        for ime1, k_1, k_2 in kraji:
            if ime == ime1:
                razdalja = sqrt(((k_1 - x1) ** 2) + ((k_2 - y1) ** 2))
        if razdalja > naj_razd:
            naj_razd = razdalja
            naj_ime = ime
    return naj_ime

def zalijemo(ime, domet, kraji):
    naj_ime = ''
    najrazd = 0
    x1, y1 = koordinate(ime, kraji)
    for ime2, x2, y2 in kraji:
        razdalja2 = razdalja_koordinat(x1, y1, x2, y2)
        if razdalja2 <= domet and najrazd < razdalja2:
            najrazd = razdalja2
            naj_ime = ime2
    return naj_ime
def presek(s1, s2):
    s = []
    for e in s1:
        for f in s2:
            if e == f:
                s.append(f)
    return s
def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    s = presek(s1, s2)
    return s


# Tu pišite svoje funkcije:




