from math import *

# Tu pišite svoje funkcije:

# Obvezni del:

def koordinate(ime, kraji):
    for mesto, x, y in kraji:
        if ime == mesto:
            return x,y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    prazen_seznam = []
    x1,y1 = koordinate(ime, kraji)
    for mesto, x, y in kraji:
        if razdalja_koordinat(x1,y1,x,y) <= domet and mesto != ime:
            prazen_seznam.append(mesto)
    return prazen_seznam

def najbolj_oddaljeni(ime, imena, kraji):
    x1,y1 = koordinate(ime, kraji)

    najvecja_razdalja = 0
    naj_mesto = ""

    for imena1 in imena:
        for kraji1, x, y in kraji:
            if razdalja_koordinat(x1,y1,x,y) > najvecja_razdalja and kraji1 == imena1:
                najvecja_razdalja = razdalja_koordinat(x1,y1,x,y)
                naj_mesto = imena1
    return naj_mesto

def zalijemo(ime, domet, kraji):
    x1,y1 = koordinate(ime, kraji)

    najvecja_razdalja = 0
    razdalja = 0
    naj_mesto = ""

    for imena, x, y in kraji:
        razdalja = razdalja_koordinat(x1, y1, x, y)
        if razdalja < domet and najvecja_razdalja < razdalja:
            najvecja_razdalja = razdalja
            naj_mesto = imena
    return naj_mesto

# Dodatni del:

def presek(s1, s2):
    prazen_seznam = []

    for i in s1:
        for j in s2:
            if i == j:
                prazen_seznam.append(i)
    return prazen_seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    x1,y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)

    kraj1 = 0
    kraj2 = 0

    prazen_seznam = []

    for imena, x, y in kraji:
        razdalja_med_krajoma1 = razdalja_koordinat(x1,y1,x,y)
        razdalja_med_krajoma2 = razdalja_koordinat(x2,y2,x,y)

        if razdalja_med_krajoma1 <= domet and razdalja_med_krajoma2 <= domet:
            if imena != ime1 and imena != ime2:
                prazen_seznam.append(imena)
    return prazen_seznam


