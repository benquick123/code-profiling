# Tu pišite svoje funkcije:

from math import *

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    z = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return z

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)

    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    s = []
    for kraj, x, y in kraji:
        if ime == kraj:
            x0, y0 = x, y
            break

    for kraj, x, y in kraji:
        r = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if r <= domet and kraj != ime:
            s.append(kraj)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    r = 0
    for kraj, x, y in kraji:
        if ime == kraj:
            x0, y0 = x, y
            break

    for kraj, x, y in kraji:
        if kraj in imena:
            z = sqrt((x - x0) ** 2 + (y - y0) ** 2)
            if z > r:
                r = z
                naj = kraj
    return naj

def zalijemo(ime, domet, kraji):
    r = 0
    for kraj, x, y in kraji:
        if ime == kraj:
            x0, y0 = x, y

    for kraj, x, y in kraji:
        z = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if r < z <= domet:
            r = z
            naj = kraj

    return naj

def presek(s1, s2):
    s3 = []
    for i in s1:
        if i in s2:
            s3.append(i)
    return(s3)

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return presek(s1, s2)

