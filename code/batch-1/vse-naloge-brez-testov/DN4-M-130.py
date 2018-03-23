# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for kraj,x,y in kraji:
        if ime==kraj:
            return x,y

def razdalja_koordinat(x1, y1, x2, y2):
    return  sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2,kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    s = []
    for kraj,x,y in kraji:
        if razdalja(ime, kraj, kraji) <= domet and kraj != ime:
            s.append(kraj)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for kraj in imena:
        if razdalja(ime, kraj, kraji) > naj_razdalja:
            naj_razdalja = razdalja(ime, kraj, kraji)
            naj_kraj = kraj

    return naj_kraj

def zalijemo(ime, domet, kraji):
    naj_razdalja = 0
    for kraj,x,y in kraji:
        if razdalja(ime, kraj, kraji) <= domet and razdalja(ime, kraj, kraji) > naj_razdalja:
            naj_razdalja = razdalja(ime, kraj, kraji)
            naj_kraj = kraj

    return naj_kraj

def presek(s1, s2):
    s = []
    for element1 in s1:
        for element2 in s2:
            if element1==element2:
                s.append(element2)
    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s = []
    for kraj,x,y in kraji:
        if razdalja(ime1,kraj,kraji) <= domet and razdalja(ime2,kraj,kraji) <= domet:
            s.append(kraj)

    return s







