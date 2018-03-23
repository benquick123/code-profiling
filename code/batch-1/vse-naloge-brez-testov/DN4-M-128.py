# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for ime_kraja, x, y in kraji:
        if ime_kraja == ime:
            return (x, y)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    raz = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return raz

def razdalja(ime1, ime2, kraji):
    xy1 = koordinate(ime1,kraji)
    xy2 = koordinate(ime2,kraji)
    return razdalja_koordinat(xy1[0], xy1[1], xy2[0], xy2[1])


def v_dometu(ime, domet, kraji):
    izpis = []
    for ime_kraja, x, y in kraji:
        if razdalja(ime,ime_kraja,kraji) <= domet and ime != ime_kraja:
            izpis.append(ime_kraja)
    return izpis

def najbolj_oddaljeni(ime, imena, kraji):
    max_oddaljenost = 0
    max_mesto = ""
    i = 0

    while i < len(imena):
        raz = razdalja(ime,imena[i],kraji)
        if raz > max_oddaljenost:
            max_oddaljenost = raz
            max_mesto = imena[i]
        i += 1
    return max_mesto

def zalijemo(ime, domet, kraji):
    max_oddaljenost = 0
    max_mesto = ""
    i = 0
    for ime_kraja, x, y in kraji:
        raz = razdalja(ime,kraji[i][0], kraji)
        if raz > max_oddaljenost and raz <= domet:
            max_oddaljenost = raz
            max_mesto = kraji[i][0]
        i += 1

    return max_mesto

