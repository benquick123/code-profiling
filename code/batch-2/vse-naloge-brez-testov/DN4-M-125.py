# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for i, x, y in kraji:
        if i == ime:
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja

def v_dometu(ime, domet, kraji):
    skrajev = []
    for ime0, x0, y0 in kraji:
        if ime0 == ime:
            xk = x0
            yk = y0

    for i, x, y in kraji:
        razdalja = sqrt((xk - x) ** 2 + (yk - y) ** 2)
        if razdalja <= domet and i != ime:
            skrajev.append(i)
    return skrajev

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for ime0, x0, y0 in kraji:
        if ime0 == ime:
            xk = x0
            yk = y0

    for ime in imena:
        for i, x, y in kraji:
            if i == ime:
                xk1 = x
                yk1 = y
        razdalja = sqrt((xk - xk1) ** 2 + (yk - yk1) ** 2)
        if razdalja > naj_razdalja:
            naj_razdalja = razdalja
            najoddaljen = ime

    return najoddaljen

def zalijemo(ime, domet, kraji):
    naj_razdalja = 0
    for ime1, x1, y1 in kraji:
        if ime1 == ime:
            xk = x1
            yk = y1

    for ime, x, y in kraji:
        razdalja = sqrt((xk - x) ** 2 + (yk - y) ** 2)
        if razdalja <= domet and razdalja > naj_razdalja:
            naj_razdalja = razdalja
            naj_kraj = ime
    return naj_kraj

def presek(s1, s2):
    s = []
    for i in s1:
        for j in s2:
            if i == j:
                s.append(i)
    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s = []
    for ime, x1, y1 in kraji:
        if ime == ime1:
            break

    for ime, x2, y2 in kraji:
        if ime == ime2:
            break

    for ime, x, y in kraji:
        if sqrt((x - x1) ** 2 + (y - y1) ** 2) < domet and sqrt((x - x2) ** 2 + (y - y2) ** 2) < domet:
            s.append(ime)
    return s



