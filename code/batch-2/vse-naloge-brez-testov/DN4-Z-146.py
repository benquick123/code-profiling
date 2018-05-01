# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for kraj, x0, y0 in kraji:
        if kraj == ime:
            return x0, y0
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return razdalja

def razdalja(ime1, ime2, kraji):
    (x1, y1) = koordinate(ime1, kraji)
    (x2, y2) = koordinate(ime2, kraji)
    raz = razdalja_koordinat(x1, y1, x2, y2)
    return raz

def v_dometu(ime, domet, kraji):
    k = []
    for kraj, x, y in kraji:
        if razdalja(ime, kraj, kraji) <= domet and not kraj == ime:
            k.append(kraj)
    return k

def najbolj_oddaljeni(ime, imena, kraji):
    n = ""
    naj = 0
    for kraj in imena:
        if razdalja(ime, kraj, kraji) > naj:
            n = kraj
            naj = razdalja(ime, kraj, kraji)
    return n

def zalijemo(ime, domet, kraji):
    n = ""
    naj = 0
    for kraj, x, y in kraji:
        if razdalja(ime, kraj, kraji) > naj and razdalja(ime, kraj, kraji) <= domet:
            n = kraj
            naj = razdalja(ime, kraj, kraji)
    return n

def zalijemo_seznam(ime,domet,kraji):
    n = []
    for kraj, x, y in kraji:
        if razdalja(ime, kraj, kraji) <= domet:
            n.append(kraj)
    return n

def presek(s1,s2):
    p = []
    for x in s1:
        for y in s2:
            if y == x:
                p.append(y)
    return p

def skupno_zalivanje(ime1, ime2, domet, kraji):
    X = zalijemo_seznam(ime1, domet, kraji)
    Y = zalijemo_seznam(ime2, domet, kraji)
    z = presek(X, Y)
    return z

