# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return(x, y)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    s = []
    for mesto, x, y in kraji:
        if mesto != ime:
            if razdalja(ime, mesto, kraji) <= domet:
                s.append(mesto)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    s = []
    naj_r = 0
    naj_k = ''
    for kraj, x, y in kraji:
        if kraj in imena:
            r = razdalja(ime, kraj, kraji)
            s.append((kraj, r))
            for kraj, r in s:
                if r > naj_r:
                    naj_r = r
                    naj_k = kraj
    return naj_k

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime,domet,kraji), kraji)

def presek(s1, s2):
    return list(set(s1).intersection(s2))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    mes1 = []
    mes2 = []
    for mesto, x, y in kraji:
        if mesto == ime1:
            for mesto, x, y in kraji:
                if razdalja(mesto,ime1,kraji) <= domet:
                    mes1.append(mesto)
        if mesto == ime2:
            for mesto, x, y in kraji:
                if razdalja(mesto,ime2,kraji) <= domet:
                    mes2.append(mesto)
    return presek(mes1, mes2)


