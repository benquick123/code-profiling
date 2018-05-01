# Tu pišite svoje funkcije:

from math import *

def koordinate(ime, kraji):
    for kraj in kraji:
        if(kraj[0] == ime):
            return (kraj[1], kraj[2])
    return None


def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def razdalja(ime1, ime2, kraji):
    koordinate1 = koordinate(ime1, kraji)
    koordinate2 = koordinate(ime2, kraji)
    return razdalja_koordinat(koordinate1[0], koordinate1[1], koordinate2[0], koordinate2[1])


def v_dometu(ime, domet, kraji):
    seznamKrajev = []
    for kraj in kraji:
        if(kraj[0] != ime and razdalja(ime, kraj[0], kraji) <= domet):
            seznamKrajev.append(kraj[0])
    return seznamKrajev


def najbolj_oddaljeni(ime, imena, kraji):
    maxLen = -1
    returnIme = None
    for imeL in imena:
        if(razdalja(ime, imeL, kraji) > maxLen):
            maxLen = razdalja(ime, imeL, kraji)
            returnIme = imeL
    return returnIme


def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)


def presek(s1, s2):
    presekKraji = []
    for kraj1 in s1:
        for kraj2 in s2:
            if(kraj1 == kraj2):
                presekKraji.append(kraj1)
    return presekKraji

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznamKrajev = []
    for kraj in kraji:
        if razdalja(ime1, kraj[0], kraji) < domet and razdalja(ime2, kraj[0], kraji) < domet:
            seznamKrajev.append(kraj[0])
    return seznamKrajev

