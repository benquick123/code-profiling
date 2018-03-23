# Tu pišite svoje funkcije:
from math import *


def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y
    return None


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)


def v_dometu(ime, domet, kraji):
    tarce=[]
    for kraj, x, y in kraji:
        dolzina = razdalja(ime, kraj, kraji)
        if domet >= dolzina and ime != kraj:
            tarce.append(kraj)
    return tarce


def najbolj_oddaljeni(ime, imena, kraji):
    max_dolzina = 0
    for kraj in imena:
        dolzina = razdalja(ime, kraj, kraji)
        if dolzina > max_dolzina:
            max_dolzina = dolzina
            max_kraj = kraj
    return max_kraj


def zalijemo(ime, domet, kraji):
    max_dolzina = 0
    for kraj, x, y in kraji:
        dolzina = razdalja(ime, kraj, kraji)
        if domet > dolzina > max_dolzina and ime != kraj:
            max_dolzina = dolzina
            max_kraj = kraj
    return max_kraj


def presek(s1, s2):
    return list(set(s1).intersection(set(s2)))


def skupno_zalivanje(ime1, ime2, domet, kraji):
    tarce1 = v_dometu(ime1, domet, kraji)
    tarce2 = v_dometu(ime2, domet, kraji)
    return presek(tarce1, tarce2)


