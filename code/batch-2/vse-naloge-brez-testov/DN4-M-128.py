# Tu pišite svoje funkcije:
from math import*

def koordinate(ime, kraji):
    s = ()
    for i, x, y in kraji:
        if ime == i:
            s = s + (x,y)
            return(s)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    xprva, yprva = koordinate(ime1, kraji)
    xdruga, ydruga = koordinate(ime2, kraji)
    return razdalja_koordinat(xprva, yprva, xdruga, ydruga)

def v_dometu(ime, domet, kraji):
    z = []
    for imeTest, xTest, yTest in kraji:
        if(ime != imeTest):
            if razdalja(ime, imeTest, kraji) <= domet:
                z.append(imeTest)
    return z

def najbolj_oddaljeni(ime, imena, kraji):
    najvecjaTest = 0
    for ime1 in imena:
        razTest = razdalja(ime, ime1, kraji)
        if(razTest > najvecjaTest):
            najvecjaTest = razTest
            izpis = ime1
    return izpis

def zalijemo(ime, domet, kraji):
    imena = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, imena, kraji)

def presek(s1, s2):
    u = []
    for a in s1:
        for b in s2:
            if a == b:
                u.append(a)
    return u

def skupno_zalivanje(ime1, ime2, domet, kraji):
    c = v_dometu(ime1, domet, kraji)
    d = v_dometu(ime2, domet, kraji)
    e = presek(c, d)
    return e

