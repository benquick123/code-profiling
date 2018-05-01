from math import *

def koordinate(ime, kraji):
    for k in kraji:
        if (k[0] == ime):
            return (k[1], k[2])
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2-x1)**2 + (y2-y1)**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    k1 = koordinate(ime1, kraji)
    k2 = koordinate(ime2, kraji)
    razdalja = razdalja_koordinat(k1[0] ,k1[1] ,k2[0] ,k2[1])
    return razdalja

def v_dometu(ime, domet, kraji):
    k = koordinate(ime, kraji)
    li = []
    for kraj in kraji:
        razdalja = razdalja_koordinat(k[0], k[1], kraj[1], kraj[2])
        if (razdalja <= domet):
            if (kraj[0]!= ime):
                li.append(kraj[0])
    return li

def najbolj_oddaljeni(ime, imena, kraji):
    k = koordinate(ime, kraji)
    naj = 0.0
    x = "Napaka"
    for kraj in imena:
        k2 = koordinate(kraj, kraji)
        razd = razdalja_koordinat(k[0],k[1],k2[0],k2[1])
        if (razd >= naj):
            naj = razd
            x = kraj
    return x

def zalijemo(ime, domet, kraji):
    li = v_dometu(ime, domet, kraji)
    zal = najbolj_oddaljeni(ime, li, kraji)
    return zal


def presek(s1, s2):
    li = []
    for d1 in s1:
        for d2 in s2:
            if (d1 == d2):
                if (d1 not in li):
                    li.append(d1)
    return li

def skupno_zalivanje(ime1, ime2, domet, kraji):
    li1 = v_dometu(ime1, domet, kraji)
    li2 = v_dometu(ime2, domet, kraji)

    rez = presek(li1, li2)
    return rez




