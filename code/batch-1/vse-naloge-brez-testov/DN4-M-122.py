# Tu pišite svoje funkcije:
from math import *


def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime==kraj:
            break
    else:
        return None
    return x, y


def razdalja_koordinat(x1, y1, x2, y2):
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


def razdalja(ime1, ime2, kraji):
    x1, y1=koordinate(ime1, kraji)
    x2, y2=koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)


def v_dometu(ime, domet, kraji):
    t=[]
    x1, y1 = koordinate(ime, kraji)
    for kraj_1, x2, y2 in kraji:
        d1=razdalja_koordinat(x1, y1, x2, y2)
        if domet >= d1 and kraj_1 != ime:
            t.append(kraj_1)
    return t

def najbolj_oddaljeni(ime, imena, kraji):
    d=0
    x1, y1 = koordinate(ime, kraji)
    for kraj_1 in imena:
        x2, y2 = koordinate(kraj_1, kraji)
        d1 = razdalja_koordinat(x1, y1, x2, y2)
        if d1>d:
            d=d1
            najkraj=kraj_1
    return najkraj

def zalijemo(ime, domet, kraji):
    t = v_dometu(ime, domet, kraji)
    f = najbolj_oddaljeni(ime, t, kraji)
    return f

def presek(s1, s2):
    t=[]
    for e in s1:
        for r in s2:
            if r==e:
                t.append(r)
    return t

def skupno_zalivanje(ime1, ime2, domet, kraji):
    a = v_dometu(ime1, domet, kraji)
    b = v_dometu(ime2, domet, kraji)
    t = presek(a,b)
    return t


