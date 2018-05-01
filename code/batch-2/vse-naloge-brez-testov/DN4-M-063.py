# Tu pišite svoje funkcije:
from math import *

def v_dometu(ime, domet, kraji):
    seznam = []
    x1, y1 = koordinate(ime, kraji)
    for ime1, x2, y2 in kraji:
        if razdalja_koordinat(x1, y1, x2, y2) <= domet and ime1 != ime:
            seznam.append(ime1)
    return seznam

def koordinate(ime, kraji):
    for ime1, x, y in kraji:
        if ime1 == ime:
            return (x, y)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    if x1 != abs(x1) and x2 == abs(x2):
        razdx = x2 + abs(x1)
    if (x1 == abs(x1) and x2 == abs(x2)) or (x1 != abs(x1) and x2 != abs(x2)):
        razdx = abs(x2 - x1)
    if x1 == abs(x1) and x2 != abs(x2):
        razdx = x1 + abs(x2)

    if y1 != abs(y1) and y2 == abs(y2):
        razdy = y2 + abs(y1)
    if (y1 == abs(y1) and y2 == abs(y2)) or (y1 != abs(y1) and y2 != abs(y2)):
        razdy = abs(y2 - y1)
    if y1 == abs(y1) and y2 != abs(y2):
        razdy = y1 + abs(y2)
    return sqrt(razdx ** 2 + razdy ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def najbolj_oddaljeni(ime, imena, kraji):
    max_razdalja = 0
    for mesto in imena:
        if razdalja(ime, mesto, kraji) > max_razdalja:
            max_razdalja = razdalja(ime, mesto, kraji)
            a = mesto
    return a

def zalijemo(ime, domet, kraji):
    naj_raz = 0
    for mesto, _, __ in kraji:
        raz = razdalja(ime, mesto, kraji)
        if raz <= domet and raz > naj_raz:
            naj_raz = raz
            naj_kraj = mesto
    return naj_kraj

def presek(s1, s2):
    s = []
    for i1 in s1:
        for i2 in s2:
            if i1 == i2:
                s.append(i2)
    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))

