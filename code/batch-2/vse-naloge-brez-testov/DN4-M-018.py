# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for kraj in kraji:
        kraj_ime, kraj_x, kraj_y = kraj
        if ime == kraj_ime:
            return (kraj_x, kraj_y)

    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return  sqrt((x2 - x1)**2 + (y2 - y1)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    kraji_novi = []
    kraj_x, kraj_y = koordinate(ime, kraji)
    for k in kraji:
        k_ime, k_x, k_y = k
        if ime != k_ime:
            if domet >= razdalja(ime, k_ime, kraji):
                kraji_novi.append(k_ime)

    return kraji_novi

def najbolj_oddaljeni(ime, imena, kraji):
    najIme = None
    najR = 0
    for i in imena:
        for k in kraji:
            k_ime, k_x, k_y = k
            if k_ime == i:
                r = razdalja(i, ime, kraji)
                if r > najR:
                    najR = r
                    najIme = i

    return najIme

def presek(s1, s2):
    s3 = []
    for i1 in s1:
        for i2 in s2:
            if i1 == i2:
                s3.append(i1)

    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    kraji1 = v_dometu(ime1, domet, kraji)
    kraji2 = v_dometu(ime2, domet, kraji)
    return presek(kraji1, kraji2)

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)

