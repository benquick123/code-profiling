from math import *

def koordinate(ime,kraji):
    s = ()
    for kraj,x1,y1 in kraji:
        if ime == kraj:
            s += x1,y1
    if s == ():
        s = None
    return(s)

def razdalja_koordinat(x1, y1, x2, y2):
    return(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

def razdalja(ime1, ime2, kraji):
    s1 = koordinate(ime1,kraji)
    s2 = koordinate(ime2,kraji)
    r = razdalja_koordinat(s1[0],s1[1],s2[0],s2[1])
    return(r)

def v_dometu(ime, domet, kraji):

    s = []
    for kraj in kraji:
        r = razdalja(ime, kraj[0], kraji)
        if  r > 0.0:
            if r <= domet:
                s.append(kraj[0])
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    naj_kraj = None
    for ime2 in imena:
        if razdalja(ime,ime2,kraji) >= naj_razdalja:
            naj_razdalja = razdalja(ime,ime2,kraji)
            naj_kraj = ime2
    return naj_kraj

def zalijemo(ime, domet, kraji):
    return(najbolj_oddaljeni(ime,v_dometu(ime,domet,kraji),kraji))

