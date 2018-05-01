# Tu pišite svoje funkcije:
def koordinate(ime, kraji):
    for kraj, x1, y1 in kraji:
        if ime == kraj:
            return ((x1, y1))

from math import *
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja

def v_dometu(ime, domet, kraji):
    s = []
    for kraj, x, y in kraji:
        raz = razdalja(kraj, ime, kraji)
        if  raz <= domet and kraj != ime:
            s.append(kraj)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
     najbolj_oddaljen = ""
     naj = 0
     for kraj, x, y in kraji:
         if kraj in imena:
             r = razdalja(kraj, ime, kraji)
             if r > naj:
                 naj = r
                 najbolj_oddaljen = kraj
     return (najbolj_oddaljen)

def zalijemo(ime, domet, kraji):
    naj_r = 0
    naj_k = 0
    for kraj, x, y in kraji:
        r = razdalja(kraj, ime, kraji)
        if r <= domet and r > naj_r:
            naj_r = r
            naj_k = kraj
    return naj_k

def presek(s1, s2):
    s = []
    for e in s1:
        for m in s2:
            if e == m:
                s.append(e)
    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):
        i = v_dometu(ime1, domet, kraji)
        k = v_dometu(ime2, domet, kraji)
        return (presek(i, k))


