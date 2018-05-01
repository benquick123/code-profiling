# Tu pišite svoje funkcije:

from math import *

def koordinate(ime, kraji):
    for ime0, x0, y0 in kraji:
        if ime == ime0:
            return (x0, y0)

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    c = razdalja_koordinat(x1, y1, x2, y2)
    return c

def v_dometu(ime, domet, kraji):
    s=[]
    x1, y1 = koordinate(ime, kraji)
    for ime2, x2, y2 in kraji:
        if razdalja(ime, ime2, kraji) <= domet and ime != ime2:
             s.append(ime2)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    s = 0
    for ime2 in imena:
        if razdalja(ime, ime2, kraji) > s:    
            s = razdalja(ime, ime2, kraji)
            ime3 = ime2
    return ime3

def zalijemo(ime, domet, kraji):
    s = 0
    for ime2, x, y in kraji:
        razdalja_kraja = razdalja(ime, ime2, kraji)
        if razdalja_kraja > s and razdalja_kraja < domet:
            s = razdalja_kraja
            ime_final = ime2
    return ime_final


def presek(s1, s2):
    s = []
    for i in s1:
        if i in s2 and i not in s:
            s.append(i)
    return s



