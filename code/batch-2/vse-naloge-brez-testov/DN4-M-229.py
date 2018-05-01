# Tu pišite svoje funkcije:
import math

def koordinate(ime, kraji):
    for imena, x, y in kraji:
        if ime == imena:
            x0 = x
            y0 = y
            z = (x, y)
            return z
    else:
        return None
def razdalja_koordinat(x1,y1,x2,y2):
    d =math.sqrt(math.pow(x2 -x1, 2) + math.pow(y2 - y1, 2))
    return d


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    c = razdalja_koordinat(x1,y1,x2,y2)
    return c


def v_dometu(ime, domet, kraji):
    list = []
    for imena, x, y in kraji:
        k = razdalja(ime, imena, kraji)
        if k <= domet and ime != imena:
            list.append(imena)
    return list

def najbolj_oddaljeni(ime, imena, kraji):
    max_razdalja = 0
    max_ime = ""
    for i in imena:
        d = razdalja(ime, i, kraji)
        if d > max_razdalja:
            max_razdalja = d
            max_ime = i
    return max_ime


def zalijemo(ime, domet, kraji):
    x = v_dometu(ime, domet, kraji)
    c = najbolj_oddaljeni(ime, x, kraji)
    return c

def presek(s1, s2):
    s3 = []
    for n in s1:
        for n in s2:
            if s3.count(n) == 0 and s1.count(n) > 0 and s2.count(n) > 0:
                s3.append(n)
    return s3


def skupno_zalivanje(ime1, ime2, domet, kraji):
    range1 = v_dometu(ime1, domet, kraji)
    range2 = v_dometu(ime2, domet, kraji)
    moznosti = presek(range1, range2)
    return moznosti









