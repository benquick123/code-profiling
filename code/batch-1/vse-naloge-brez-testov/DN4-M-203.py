# Tu pišite svoje funkcije:
import math

def koordinate(ime, kraji):
    for (name, x1, y1) in kraji:
        if ime in name:
            return (x1, y1)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return a

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    x1, y1 = koordinate(ime, kraji)
    k = []
    for (ime2, x2, y2) in kraji:
        if domet >= razdalja_koordinat(x1, y1, x2, y2) and ime != ime2:
            k.append(ime2)
    return k

def najbolj_oddaljeni(ime, imena, kraji):
    x1, y1 = koordinate(ime, kraji)
    k = None
    p = 0
    for (ime2, x2, y2) in kraji:
        for ime1 in imena:
            if ime1 == ime2:
                a = razdalja_koordinat(x1, y1, x2, y2)
                if a >= p:
                    p = a
                    k = ime2
    return k


def zalijemo(ime, domet, kraji):
    x1, y1 = koordinate(ime, kraji)
    k = None
    p = 0
    for (ime2, x2, y2) in kraji:
        a = razdalja_koordinat(x1, y1, x2, y2)
        if domet >= a and a > p:
            p = a
            k = ime2
    return k


def presek(s1, s2):
    a = list(set(s1).intersection(s2))
    return a

def skupno_zalivanje(ime1, ime2, domet, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    k = []
    for (ime3, x3, y3) in kraji:
        a = razdalja_koordinat(x1, y1, x3, y3)
        b = razdalja_koordinat(x2, y2, x3, y3)
        if domet >= a and domet >= b:
            k.append(ime3)
    return k



