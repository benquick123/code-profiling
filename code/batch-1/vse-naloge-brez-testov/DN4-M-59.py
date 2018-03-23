# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for kraj in kraji:
        if ime == kraj[0]:
            return kraj[1], kraj[2]


def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def razdalja(ime1, ime2, kraji):
    k1x, k1y = koordinate(ime1, kraji)
    k2x, k2y = koordinate(ime2, kraji)
    return razdalja_koordinat(k1x, k1y, k2x, k2y)

def v_dometu(ime, domet, kraji):
    s = []
    for kraj in kraji:
        if kraj[0] != ime:
            raz = razdalja(ime, kraj[0], kraji)
            if raz <= domet:
                s.append(kraj[0])
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    naj = "", 0
    for kraj in imena:
        raz = razdalja(ime, kraj, kraji)
        if raz > naj[1]:
            naj = kraj, raz
    return naj[0]

def zalijemo(ime, domet, kraji):
    naj = "", 0
    for kraj in kraji:
        raz = razdalja(ime, kraj[0], kraji)
        if naj[1] < raz <= domet:
            naj = kraj[0], raz
    return naj[0]

def presek(s1, s2):
    k=[]
    for s1k in s1:
        for s2k in s2:
            if s1k == s2k:
                k.append(s1k)
    return k

def skupno_zalivanje(ime1, ime2, domet, kraji):
    kraji1 = v_dometu(ime1, domet, kraji)
    kraji2 = v_dometu(ime2, domet, kraji)
    k = presek(kraji1, kraji2)
    return k


