from math import *

# Tu pišite svoje funkcije:

#OGREVALNE NALOGE
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return (x, y)
        else:
            None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return razdalja


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja

#OBVEZNI DEL

def v_dometu(ime, domet, kraji):
    xs = []
    x1, y1 = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        razdalja = razdalja_koordinat(x1, y1, x, y)
        if kraj != ime:
            if domet >= razdalja:
                xs.append(kraj)
    return xs

def najbolj_oddaljeni(ime, imena, kraji):
    naj_odd = 0
    k = 0
    a, b = koordinate(ime, kraji)
    for ime1 in imena:
        c, d = koordinate(ime1, kraji)
        r = razdalja_koordinat(a, b, c, d)
        if naj_odd < r:
            naj_odd = r
            k = str(ime1)
    return k

def zalijemo(ime, domet, kraji):
    naj_odd = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, naj_odd, kraji)

def presek(s1, s2):
    skupni = []
    for i in s1:
        for e in s2:
            if i == e:
                skupni.append(e)
    return skupni

def skupno_zalivanje(kraj1, kraj2, domet, kraji):
    return presek(v_dometu(kraj1, domet, kraji), v_dometu(kraj2, domet, kraji))


