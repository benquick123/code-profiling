# Tu pišite svoje funkcije:

from math import *


def koordinate(ime, kraji):
    for kraj, x,y in kraji:
        if kraj==ime:
            return (x,y)


def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def razdalja(ime1, ime2, kraji):
    k1 = koordinate(ime1,kraji)
    k2 = koordinate(ime2,kraji)
    return razdalja_koordinat(k1[0],k1[1],k2[0],k2[1])

def v_dometu(ime, domet, kraji):
    for kraj, x0, y0 in kraji:
        if kraj == ime:
            break
    kraji1 = []
    for ime, x, y in kraji:
        razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if razdalja<=domet and ime != kraj:
            kraji1.append(ime)

    return kraji1


def najbolj_oddaljeni(ime, imena, kraji):
    for kraj,x0,y0 in kraji:
        if kraj==ime:
            break

    najdlje_kraj = ("kraj",0)
    for kraj1,x1,y1 in kraji:
        if kraj1 in imena and kraji[0]!=ime:
            razdalja = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
            if razdalja > najdlje_kraj[1]:
                najdlje_kraj=(kraj1,razdalja)


    return (najdlje_kraj[0])


def zalijemo(ime, domet, kraji):
    for kraj,x0,y0 in kraji:
        if kraj==ime:
            break

    najdlje_kraj = ("kraj",0)
    for kraj1, x1,y1 in kraji:
        if kraj1!=ime:
            razdalja = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
            if razdalja>najdlje_kraj[1] and razdalja<domet:
                najdlje_kraj=(kraj1,razdalja)

    return najdlje_kraj[0]


def presek(s1, s2):
    temp = []
    for a in s1:
        if a in s2:
            temp.append(a)
    return temp


def skupno_zalivanje(ime1, ime2, domet, kraji):
    for kraj1, x1, y1 in kraji:
        if kraj1 == ime1:
            break
    for kraj2, x2, y2 in kraji:
        if kraj2 == ime2:
            break

    dosegljivi_kraji = []
    for trenuten_kraj, x, y in kraji:
        razdalja1 = sqrt((x - x1) ** 2 + (y - y1) ** 2)
        razdalja2 = sqrt((x - x2) ** 2 + (y - y2) ** 2)
        if razdalja1 < domet and razdalja2 < domet:
            dosegljivi_kraji.append(trenuten_kraj)

    return dosegljivi_kraji


