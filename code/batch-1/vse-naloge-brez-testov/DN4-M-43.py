# Tu pišite svoje funkcije:

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y

from math import*

def razdalja_koordinat(x1, y1, x2, y2):
    x = sqrt((x1-x2)**2+(y1-y2)**2)
    return x

def razdalja(ime1, ime2, kraji):
    x3, y3 = koordinate(ime1, kraji)
    x4, y4 = koordinate(ime2, kraji)
    r = razdalja_koordinat(x3, y3, x4, y4)
    return r

def  v_dometu(ime, domet, kraji):
    s = []
    for ime3, x5, y5 in kraji:
        r1 = razdalja(ime, ime3, kraji)
        if ime3 != ime:
            if domet >= r1:
                s.append(ime3)
    return s





