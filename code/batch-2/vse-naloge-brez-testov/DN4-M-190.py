# Tu pišite svoje funkcije:

from math import sqrt

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

def razdalja(ime1, ime2, kraji):
    kraj1 = koordinate(ime1, kraji)
    kraj2 = koordinate(ime2, kraji)
    return razdalja_koordinat(kraj1[0], kraj1[1], kraj2[0], kraj2[1])

def v_dometu(ime, domet, kraji):
    t = []
    kraj = koordinate(ime, kraji)
    for name, x, y in kraji:
        razdalja = razdalja_koordinat(kraj[0], kraj[1], x, y)
        if 0 < razdalja <= domet:
            t.append(name)
    return t

def najbolj_oddaljeni(ime, imena, kraji):
    max = 0
    kraj = koordinate(ime, kraji)
    for e in imena:
        kraj2 = koordinate(e, kraji)
        razdalja = razdalja_koordinat(kraj[0], kraj[1], kraj2[0], kraj2[1])
        if razdalja > max:
            max = razdalja
            naj_kraj = e
    return naj_kraj

def zalijemo(ime, domet, kraji):
    max = 0
    kraj1 = koordinate(ime, kraji)
    for name, x, y in kraji:
        razdalja = razdalja_koordinat(kraj1[0], kraj1[1], x, y)
        if max <= razdalja <= domet:
            max = razdalja
            naj_kraj = name
    return naj_kraj

def presek(s1, s2):
    t = []
    for ime in s1:
        for name in s2:
            if ime == name:
                t.append(name)
    return t

def skupno_zalivanje(ime1, ime2, domet, kraji):
    kraji1 = v_dometu(ime1, domet, kraji)
    kraji2 = v_dometu(ime2, domet, kraji)
    return presek(kraji1, kraji2)


