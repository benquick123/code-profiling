def koordinate(ime, mesta):
    for mesto in mesta:
        if mesto[0] == ime:
            return mesto[1], mesto[2]
    return None

from math import *

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2-x1)**2 + (y2-y1)**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    c1 = koordinate(ime1, kraji)
    c2 = koordinate(ime2, kraji)
    return razdalja_koordinat(c1[0], c1[1], c2[0], c2[1])

def v_dometu(ime, domet, kraji):
    seznam = []
    for mesto in kraji:
        if ime != mesto[0] and razdalja(ime, mesto[0], kraji) <= domet:
            seznam.append(mesto[0])
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    r = 0
    for mesto in imena:
        a = razdalja(ime, mesto, kraji)
        if a > r:
            r = a
            mmesto = mesto
    return mmesto

def zalijemo(ime, domet, kraji):
    relevantni = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, relevantni, kraji)

