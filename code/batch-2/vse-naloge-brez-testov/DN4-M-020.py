# Tu pišite svoje funkcije:

from math import *


def koordinate(ime, kraji):
    for ime_kraja, x, y in kraji:
        if ime == ime_kraja:
            return x, y


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return razdalja


def razdalja(ime1, ime2, kraji):
    k1 = koordinate(ime1, kraji)
    k2 = koordinate(ime2, kraji)
    x1, y1 = k1
    x2, y2 = k2
    razdalja = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja


def v_dometu(ime, domet, kraji):
    s = []
    for kraj, x, y in kraji:
        oddaljenost = razdalja(ime, kraj, kraji)
        if oddaljenost <= domet and kraj != ime:
            s.append(kraj)
    return s


def najbolj_oddaljeni(ime, imena, kraji):
    najbolj_oddaljen = 0
    for kraj in imena:
        oddaljenost = razdalja(ime, kraj, kraji)
        if oddaljenost > najbolj_oddaljen:
            najbolj_oddaljen = oddaljenost
            naj_ime = kraj
    return naj_ime


def zalijemo(ime, domet, kraji):
    zaliti = v_dometu(ime, domet, kraji)
    naj_zalit = najbolj_oddaljeni(ime, zaliti, kraji)
    return naj_zalit


def presek(s1, s2):
    p = []
    for element1 in s1:
        for element2 in s2:
            if element1 == element2:
                p.append(element1)
    return p


def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    s = presek(s1, s2)
    return s



