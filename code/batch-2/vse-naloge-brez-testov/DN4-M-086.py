# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for ime_kraja, x, y in kraji:
        if ime_kraja == ime:
            x_os = x
            y_os = y
            return(x_os, y_os)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    kraj1 = koordinate(ime1, kraji)
    x1, y1 = kraj1
    kraj2 = koordinate(ime2, kraji)
    x2, y2 = kraj2
    razdalja = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja

def v_dometu(ime, domet, kraji):
    s = []
    for ime1, x, y in kraji:
        if ime1 == ime:
            x1 = x
            y1 = y
            a = ime1

    for ime2, x2, y2 in kraji:
        if ime2 == a:
            continue
        razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if razdalja <= domet:
            s.append(ime2)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    razdalja_max = 0
    for ime1, x, y in kraji:
        if ime1 == ime:
            x1 = x
            y1 = y
            break

    for kraj in imena:
        for ime2, x2, y2 in kraji:
            if kraj == ime2:
                razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if razdalja > razdalja_max:
                    razdalja_max = razdalja
                    kraj_max = ime2
    return kraj_max

def zalijemo(ime, domet, kraji):
    razdalja_max = 0
    for ime1, x, y in kraji:
        if ime1 == ime:
            x1 = x
            y1 = y
    kraj_max = ime1

    for ime2, x2, y2 in kraji:
        razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if razdalja_max < razdalja < domet:
             razdalja_max = razdalja
             kraj_max = ime2
    return kraj_max

def presek(s1, s2):
    s = []
    for i in s1:
        for j in s2:
            if i == j:
                s.append(i)
    return s


def skupno_zalivanje(ime1, ime2, domet, kraji):
    s = []
    for ime, x, y in kraji:
        if ime == ime1:
            x1 = x
            y1 = y
            kraj1 = ime
    for ime, x, y in kraji:
        if ime == ime2:
            x2 = x
            y2 = y
            kraj2 = ime
    for ime, x, y in kraji:
        razdalja1 = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        razdalja2 = sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
        if razdalja1 <= domet and razdalja2 <= domet:
            s.append(ime)
    return s


    return 0


