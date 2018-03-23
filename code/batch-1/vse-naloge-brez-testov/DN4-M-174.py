# Tu pišite svoje funkcije:
from math import sqrt

def koordinate(ime, kraji):
    for name, x1, y1 in kraji:
        if name == ime:
            x = x1
            y = y1
            return ((x, y))
    else:
        return (None)

def razdalja_koordinat(x1, y1, x2, y2):
    return (sqrt((x1-x2)**2 + (y1-y2)**2))

def razdalja(ime1, ime2, kraji):
    x1, y1=koordinate(ime1, kraji)
    x2, y2=koordinate(ime2, kraji)
    return (razdalja_koordinat(x1, y1, x2, y2))


def v_dometu(ime, domet, kraji):
    f = []
    for name, x1, y1 in kraji:
        if razdalja(ime, name, kraji) <= domet and ime != name:
            f.append(name)
    return (f)

def najbolj_oddaljeni(ime, imena, kraji):
    maxd   = 0
    maxIme = ""
    for name in imena:
        if razdalja(ime, name, kraji) > maxd:
            maxd = razdalja(ime, name, kraji)
            maxIme = name
    return(maxIme)

def zalijemo(ime, domet, kraji):
    maxd   = 0
    maxIme = ""
    for name, x1, y1 in kraji:
        z = razdalja(ime, name, kraji)
        if z > maxd and z <= domet:
            maxd = z
            maxIme = name
    return(maxIme)

def presek(s1, s2):
    s3 = []
    for s_temp in s1:
        for s_temp2 in s2:
            if s_temp == s_temp2:
                s3.append(s_temp)
    return (s3)

def skupno_zalivanje(ime1, ime2, domet, kraji):
    d = []
    for ime_temp, x_temp, y_temp in kraji:
        if razdalja(ime1, ime_temp, kraji) <= domet and razdalja(ime2, ime_temp, kraji) <= domet:
            d.append(ime_temp)
    return (d)

