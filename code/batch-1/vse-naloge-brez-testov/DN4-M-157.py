# Tu pišite svoje funkcije:
from math import *


def koordinate(ime, kraji):

    for kraj in kraji:
        if kraj[0] == ime :
            return (kraj[1] , kraj[2])

    return None


def razdalja_koordinat(x1, y1, x2, y2):

    raz = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return raz



def razdalja(ime1, ime2, kraji):

    ko1 = koordinate(ime1,kraji)
    ko2 = koordinate(ime2,kraji)
    raz = razdalja_koordinat(ko1[0],ko1[1],ko2[0],ko2[1])
    return raz



def v_dometu(ime, domet, kraji):

    kraji_v_dometu = []
    for kraj in kraji:
        if razdalja(ime, kraj[0], kraji) <= domet and kraj[0] != ime:
            kraji_v_dometu.append(kraj[0])
    return kraji_v_dometu


def najbolj_oddaljeni(ime, imena, kraji):

    najRaz = -9999
    najIme = None
    for kraj in imena:
        if razdalja(ime, kraj, kraji) > najRaz:
            najRaz = razdalja(ime, kraj, kraji)
            najIme = kraj
    return najIme


def zalijemo(ime, domet, kraji):

    najIme = najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)
    return najIme

def presek(s1, s2):

    presekSez = []
    for el1 in s1:
        for el2 in s2:
            if el1 == el2:
                presekSez.append(el1)
    return presekSez


def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    skupKraji = presek(s1,s2)
    return skupKraji



