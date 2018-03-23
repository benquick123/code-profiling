from math import *

# Tu pišite svoje funkcije:
# Ogrevalne funkcije
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y

def razdalja_koordinat(x1, y1, x2, y2):
    return  sqrt((x2 - x1)**2 + (y2 - y1)**2)


def razdalja(ime1, ime2, kraji):
    xy1 = koordinate(ime1, kraji)
    xy2 = koordinate(ime2, kraji)
    return razdalja_koordinat(xy1[0], xy1[1], xy2[0], xy2[1])

# Obvezni del

def v_dometu(ime, domet, kraji):
    naj_razdalja = 0
    sez = []
    kord = koordinate(ime, kraji)
    for nom1, x, y in kraji:
        razd = razdalja_koordinat(x, y, kord[0], kord[1])
        if naj_razdalja < razd <= domet:
            naj_razdalja = razd
        if naj_razdalja != 0 and razd != 0.0 and razd <= domet:
            sez.append(nom1)
    return sez

def najbolj_oddaljeni(ime, imena, kraji):
    najrazd = 0
    najkraj = ""
    for ime2 in imena:
        razd = razdalja(ime, ime2, kraji)
        if razd > najrazd:
            najrazd = razd
            najkraj = ime2
    return najkraj


def zalijemo(ime, domet, kraji):
    razd = 0
    krajdom = ""
    kord = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        razd1 = razdalja_koordinat(x, y, kord[0], kord[1])
        if razd1 > razd and razd1 <= domet:
            razd = razd1
            krajdom = kraj
    return krajdom

