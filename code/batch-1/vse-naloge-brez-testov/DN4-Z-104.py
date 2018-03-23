# Tu pišite svoje funkcije:
from math import *


def koordinate(ime, kraji):
    koordinate = None
    for kraj, x, y in kraji:
        if ime == kraj:
            koordinate = (x, y)
    return koordinate


def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)


def v_dometu(ime, domet, kraji):
    seznam = []
    x1, y1 = koordinate(ime, kraji)
    for kraj, x2, y2 in kraji:
        if 0 < razdalja_koordinat(x1, y1, x2, y2) <= domet:
            seznam.append(kraj)
    return seznam


def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for kraj in imena:
        dolžina = razdalja(ime, kraj, kraji)
        if dolžina > naj_razdalja:
            naj_razdalja = dolžina
            naj_kraj = kraj
    return naj_kraj


def zalijemo(ime, domet, kraji):
    imena = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, imena, kraji)


def presek(s1, s2):
    return [e for e in s1 if e in s2]


def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    for ime, x, y in kraji:
        if razdalja(ime, ime1, kraji) < domet and razdalja(ime, ime2, kraji) < domet:
            seznam.append(ime)
    return seznam


