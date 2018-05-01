# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return x, y

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    seznam = []
    for kraj, x, y in kraji:
        if kraj != ime and razdalja(ime, kraj, kraji) <= domet:
            seznam.append(kraj)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    maxDist = 0
    maxKraj = ''
    for kraj in imena:
        tmpDist = razdalja(ime, kraj, kraji)
        if tmpDist > maxDist:
            maxDist = tmpDist
            maxKraj = kraj
    return maxKraj

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)

def presek(s1, s2):
    seznam = []
    for prvi in s1:
        for drugi in s2:
            if prvi == drugi:
                seznam.append(prvi)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam1 = v_dometu(ime1, domet, kraji)
    seznam2 = v_dometu(ime2, domet, kraji)
    return presek(seznam1, seznam2)

