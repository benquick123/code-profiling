# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for kraj,x,y in kraji:
        if kraj == ime:
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    OddaljenostKraja = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return OddaljenostKraja

def razdalja(ime1, ime2, kraji):
    k1 = koordinate(ime1,kraji)
    k2 = koordinate(ime2,kraji)
    return razdalja_koordinat(k1[0], k1[1], k2[0], k2[1])

def v_dometu(ime, domet, kraji):
    a = []
    for kraj in kraji:
            if razdalja(ime, kraj[0], kraji) <= domet and kraj[0] != ime:
                a.append(kraj[0])
    return a

def najbolj_oddaljeni(ime, imena, kraji):
    najkraj = "kraj"
    najraz = 0
    for kraj in imena:
        if razdalja(ime, kraj, kraji) > najraz:
            najkraj = kraj
            najraz = razdalja(ime, kraj, kraji)
    return najkraj

def zalijemo(ime, domet, kraji):
    najkraj = "kraj"
    krajivdometu = v_dometu(ime, domet, kraji)
    najkraj = najbolj_oddaljeni(ime, krajivdometu, kraji)
    return najkraj

