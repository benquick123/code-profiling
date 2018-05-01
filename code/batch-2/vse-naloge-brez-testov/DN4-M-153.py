# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for ime_kraja, x, y in kraji:
        if (ime_kraja == ime):
            x1 = x
            y1 = y
            return x1, y1

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja_k = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja_k

def razdalja(ime1, ime2, kraji):
    kx1, ky1 = koordinate(ime1, kraji)
    kx2, ky2 = koordinate(ime2, kraji)
    razdalja = razdalja_koordinat(kx1, ky1, kx2, ky2)
    return razdalja

def v_dometu(ime, domet, kraji):
    for ime_k, x0, y0 in kraji:
        if ime_k == ime:
            break
    naj_kraj = []
    for ime, x, y in kraji:
        razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if razdalja <= domet:
            if ime == ime_k:
                continue
            naj_kraj.append(ime)
    return naj_kraj

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    k1 = koordinate(ime, kraji)
    x1 = k1[0]
    y1 = k1[1]
    for ime_k in imena:
        k2 = koordinate(ime_k, kraji)
        x2 = k2[0]
        y2 = k2[1]
        razdalja = razdalja_koordinat(x1, y1, x2, y2)
        if razdalja > naj_razdalja:
            naj_razdalja = razdalja
            naj_kraj = ime_k
    return naj_kraj

    for ime_k, x0, y0 in kraji:
        if ime_k == ime:
            break
    naj_razdalja = 0
    imena_k = []
    for ime in imena:
        imena_k.append(koordinate(ime, kraji))
    return imena_k

def zalijemo(ime, domet, kraji):
    for ime_k, x0, y0 in kraji:
        if ime_k == ime:
            break
    naj_razdalja = 0
    for ime, x, y in kraji:
        razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if naj_razdalja < razdalja <= domet:
            naj_razdalja = razdalja
            naj_kraj = ime
    return naj_kraj


