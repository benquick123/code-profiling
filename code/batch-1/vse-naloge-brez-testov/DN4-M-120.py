# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for kraj in kraji:
        if kraj[0] == ime:
            return (kraj[1], kraj[2])
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    koo1 = koordinate(ime1, kraji)
    koo2 = koordinate(ime2, kraji)
    return razdalja_koordinat(koo1[0], koo1[1], koo2[0], koo2[1])

def v_dometu(ime, domet, kraji):
    seznam = []
    koo1 = koordinate(ime, kraji)
    for kraj in kraji:
        d = razdalja_koordinat(koo1[0], koo1[1], kraj[1], kraj[2])
        if (d <= domet) & (d != 0.0):
            seznam.append(kraj[0])
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    seznam = []
    maximum = 0.0
    the_kraj = None
    koo1 = koordinate(ime, kraji)
    for i in imena:
        koo2 = koordinate(i, kraji)
        d = razdalja_koordinat(koo1[0], koo1[1], koo2[0], koo2[1])
        if d > maximum:
            maximum = d
            the_kraj = i
    return the_kraj

def zalijemo(ime, domet, kraji):
    naj_razdalja = 0
    for kraj in kraji:
        d = razdalja(ime, kraj[0], kraji)
        if (d > naj_razdalja) & (d < domet):
            naj_razdalja = d
            naj_kraj = kraj[0]
    return naj_kraj

def presek(s1, s2):
    seznam = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                seznam.append(e1)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    seznam = presek(s1, s2)
    return seznam

