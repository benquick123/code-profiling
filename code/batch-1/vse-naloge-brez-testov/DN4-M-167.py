# Tu pišite svoje funkcije:
from math import *


def koordinate(ime, kraji):
    for iskano_ime, x, y in kraji:
        if ime == iskano_ime:
            terka = (x, y)
            return terka


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja


def razdalja(ime1, ime2, kraji):
    ime = ime1
    x1, y1 = koordinate(ime, kraji)
    ime = ime2
    x2, y2 = koordinate(ime, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)


def v_dometu(ime, domet, kraji):
    s = []
    for kraj, x0, y0 in kraji:
        if ime == kraj:
            break
    for kraj, x, y in kraji:
        razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if razdalja <= domet and kraj != ime:
            s.append(kraj)
    return s


def najbolj_oddaljeni(ime, imena, kraji):
    for kraj, x0, y0 in kraji:
        if ime == kraj:
            break

    naj_razdalja = 0
    for iskano in imena:
        ime = iskano
        x, y = koordinate(ime, kraji)

        razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if naj_razdalja < razdalja:
                naj_razdalja = razdalja
                naj_kraj = ime
    return naj_kraj


def zalijemo(ime, domet, kraji):
    for kraj, x0, y0 in kraji:
        if ime == kraj:
            break
    naj_razdalja = 0

    for kraj, x, y in kraji:
        razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if razdalja <= domet and naj_razdalja < razdalja:
            naj_razdalja = razdalja
            naj_kraj = kraj
    return naj_kraj


def presek(s1, s2):
    s_presek = []
    for x in s1:
        for y in s2:
            if y == x:
                s_presek.append(y)
    return s_presek


def skupno_zalivanje(ime1, ime2, domet, kraji):
    ime = ime1
    s1 = v_dometu(ime, domet, kraji)

    ime = ime2
    s2 = v_dometu(ime, domet, kraji)

    return presek(s1, s2)




