# Tu pišem moje funkcije:

from math import *


def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y


def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


def razdalja(ime1, ime2, kraji):
    xy1 = koordinate(ime1, kraji)
    xy2 = koordinate(ime2, kraji)
    return razdalja_koordinat(xy1[0], xy1[1], xy2[0], xy2[1])


def v_dometu(ime1, domet, kraji):
    s = []
    for ime2, x2, y2 in kraji:
        if (razdalja(ime1, ime2, kraji) <= domet) and ime2 != ime1:
            s.append(ime2)
    return (s)


def najbolj_oddaljeni(ime1, imena, kraji):
    naj = ime1
    for ime in imena:
        for ime2, x2, y2 in kraji:
            if ime == ime2 and razdalja(ime1, ime2, kraji) > razdalja(ime1, naj, kraji):
                naj = ime2
    return(naj)


def zalijemo(ime1, domet, kraji):
    naj = ime1
    for ime2, x2, y2 in kraji:
        if razdalja(ime1, ime2, kraji) <= domet and razdalja(ime1, ime2, kraji) > razdalja(ime1, naj, kraji):
            naj = ime2
    return(naj)


def presek(s1, s2):
    s = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                s.append(e2)
    return(s)


def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return(presek(s1, s2))

#################

