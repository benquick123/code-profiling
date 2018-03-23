from math import *

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y
        else:
            None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def razdalja(ime1, ime2, kraji):
    a, b = koordinate(ime1, kraji)
    c, d = koordinate(ime2, kraji)
    return razdalja_koordinat(a, b, c, d)

def v_dometu(ime, domet, kraji):
    imena = []
    for kraj, x, y in kraji:
        if ime == kraj:
            ime0 = ime
            x0 = x
            y0 = y
            for ime1, x, y in kraji:
                razdalja = sqrt(((x0 - x) ** 2) + ((y0 - y) ** 2))
                if ime0 != ime1:
                    if razdalja <= domet:
                        imena.append(ime1)
    return imena

def najbolj_oddaljeni(ime, imena, kraji):
    najvecja = 0
    for kraj in imena:
        a = razdalja(ime, kraj, kraji)
        if a > najvecja:
            najvecja = a
            pravi = kraj
    return pravi

def zalijemo(ime, domet, kraji):
    a = v_dometu(ime, domet, kraji)
    b = najbolj_oddaljeni(ime, a, kraji)
    return b

def presek(s1, s2):
    rez = []
    for v in s1:
        for e in s2:
            if v == e:
                rez.append(e)
    return rez

def skupno_zalivanje(ime1, ime2, domet, kraji):
    a = v_dometu(ime1, domet, kraji)
    b = v_dometu(ime2, domet, kraji)
    c = presek(a, b)
    return c



