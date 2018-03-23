# Tu pišite svoje funkcije:

import math
def koordinate(ime, kraji):
    a = (None)
    for x in kraji:
        if x[0] == ime:
            a = (x[1],x[2])
            break
    return a

def razdalja_koordinat(x1, y1, x2, y2):
    formula = (x2-x1) ** 2 + (y2 - y1) ** 2
    racun = math.sqrt(formula)
    return racun

def razdalja(ime1, ime2, kraji):
    prva = koordinate(ime1,kraji)
    druga = koordinate(ime2,kraji)
    razdalja = razdalja_koordinat(prva[1],prva[0],druga[1],druga[0])
    return razdalja
def v_dometu(ime, domet, kraji):
    sez = []
    koo1 = koordinate(ime,kraji)

    for x in kraji:
        koo2 = koordinate(x[0],kraji)
        razdalja = razdalja_koordinat(koo1[1],koo1[0],koo2[1],koo2[0])
        if razdalja <= domet and x[0] != ime:
            sez.append(x[0])
    return sez
def najbolj_oddaljeni(ime, imena, kraji):
    oddalj = 0
    ime1 = ""
    koo1 = koordinate(ime, kraji)
    for x in imena:
        for y in kraji:
            if x == y[0]:
                koo2 = (y[1],y[2])
        razdalja = razdalja_koordinat(koo1[1], koo1[0], koo2[1], koo2[0])
        if razdalja > oddalj:
            oddalj = razdalja
            ime1 = x
    return ime1
def zalijemo(ime, domet, kraji):
    oddalj = 0
    ime1 = ""
    koo1 = koordinate(ime, kraji)
    for x in kraji:
        koo2 = koordinate(x[0],kraji)
        razdalja = razdalja_koordinat(koo1[1], koo1[0], koo2[1], koo2[0])
        if razdalja < domet:
            if razdalja > oddalj:
                ime1 = x[0]
                oddalj = razdalja
    return ime1
def presek(s1, s2):
    sez = []
    for x in s1:
        for y in s2:
            if x == y:
                sez.append(x)
                break
    return sez
def skupno_zalivanje(ime1, ime2, domet, kraji):
    sez = []
    koo1 = koordinate(ime1, kraji)
    koo2 = koordinate(ime2, kraji)
    for x in kraji:
        koo3 = koordinate(x[0],kraji)
        razdalja = razdalja_koordinat(koo1[1], koo1[0], koo3[1], koo3[0])
        razdalja1 = razdalja_koordinat(koo2[1], koo2[0], koo3[1], koo3[0])
        if razdalja < domet and razdalja1 < domet:
            sez.append(x[0])
    return sez
