# Tu pišite svoje funkcije:

from math import *


def koordinate(ime, kraji):
    for kr in kraji:
        kraj, x, y = kr
        if ime == kraj:
            return x, y
    else:
        return None


def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)


def v_dometu(ime, domet, kraji):
    seznam = []
    x0, y0 = koordinate(ime, kraji)
    for kr in kraji:
        kraj, x1, y1 = kr
        if kraj != ime and razdalja_koordinat(x0, y0, x1, y1) <= domet:
            seznam += [kraj]
    return seznam


def najbolj_oddaljeni(ime, imena, kraji):
    najvecja_razdalja = 0
    naj_kraj = ""
    x0, y0 = koordinate (ime, kraji)
    for kr in imena:
        x, y = koordinate(kr, kraji)
        razd = razdalja_koordinat(x0, y0, x, y)
        if razd > najvecja_razdalja:
            najvecja_razdalja = razd
            naj_kraj = kr
    return naj_kraj


def zalijemo(ime, domet, kraji):
    x0, y0 = koordinate(ime, kraji)
    naj_razd = 0
    naj_kraj = ""
    for kr, x, y in kraji:
        razd = razdalja_koordinat(x0, y0, x, y)
        if razd > naj_razd and razd <= domet:
            naj_razd = razd
            naj_kraj = kr
    return naj_kraj


def vsebuje(el, seznam):
    for x in seznam:
        if el == x:
            return True
    return False


def presek(s1, s2):
    nov_seznam = []
    for x in s1:
        if vsebuje(x, s2):
            nov_seznam += [x]
    return nov_seznam


def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    for kr, x, y in kraji:
        if kr == ime1:
            x1 = x
            y1 = y
        elif kr == ime2:
            x2 = x
            y2 = y

    for kr, x, y in kraji:
        razd1 = sqrt(pow(abs(x1 - x), 2) + pow(abs(y1 - y), 2))
        razd2 = sqrt(pow(abs(x2 - x), 2) + pow(abs(y2 - y), 2))
        if razd1 <= domet and razd2 <= domet:
            seznam += [kr]
    return seznam


