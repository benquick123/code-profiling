# Tu pišite svoje funkcije:
from math import *

#ogrevalne funkcije
def koordinate(ime,kraji):
    for i in kraji:
        s = []
        if i[0] == ime:
            s.append((i[1]))
            s.append((i[2]))
            s = tuple(s)
            return s

def razdalja_koordinat(x1,y1,x2,y2):
    razdalja = sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return razdalja

def razdalja(ime1, ime2, kraji):
    k1 = koordinate(ime1,kraji)
    k2 = koordinate(ime2,kraji)
    razdalja = razdalja_koordinat(k1[0],k1[1],k2[0],k2[1])
    return razdalja
#---------------------------------------------------------------------------------
#obvezni del
def v_dometu(ime,domet,kraji):
    seznam = []
    k = koordinate(ime,kraji)
    for i in kraji:
        razdalja = sqrt(((i[1]-k[0])**2) + ((i[2]-k[1])**2))
        if i[0] != ime and razdalja <= domet:
            seznam.append(i[0])
    return seznam

def najbolj_oddaljeni(ime,imena,kraji):
    najdlje = 0
    najbolj_oddaljen = 0
    x1 = 0
    y1 = 0
    for i in kraji:
        if i[0] == ime:
            x1 = i[1]
            y1 = i[2]
        for j in imena:
            if j == i[0]:
                x2 = i[1]
                y2 = i[2]
                razdalja = sqrt(((x2-x1)**2) + ((y2-y1)**2))
                if razdalja > najdlje:
                    najbolj_oddaljen = i[0]
                    najdlje = razdalja
    return najbolj_oddaljen

def zalijemo(ime, domet, kraji):
    x1 = 0
    y1 = 0
    naj_razdalja = 0
    naj = 0
    for i in kraji:
        if i[0] == ime:
            x1 = i[1]
            y1 = i[2]
    for j in kraji:
        if j != ime:
            x2 = j[1]
            y2 = j[2]
            razdalja = sqrt(((x2-x1)**2) + ((y2-y1)**2))
            if razdalja <= domet and razdalja > naj_razdalja:
                naj_razdalja = razdalja
                naj = j[0]
    return naj
#---------------------------------------------------------------------------------
#dodatni del

def presek(s1, s2):
    o = []
    for i in s1:
        for j in s2:
            if i == j:
                o.append(i)
    return o

def skupno_zalivanje(ime1,ime2,domet,kraji):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    k = []
    for i in kraji:
        if i[0] == ime1:
            x1 = i[1]
            y1 = i[2]
        elif i[0] == ime2:
            x2 = i[1]
            y2 = i[2]
    for o in kraji:
        razdalja1 = sqrt(((o[1]-x1)**2) + ((o[2]-y1)**2))
        razdalja2 = sqrt(((o[1]-x2)**2) + ((o[2]-y2)**2))
        if razdalja1 <= domet and razdalja2 <= domet:
            k.append(o[0])
    return k

#---------------------------------------------------------------------------------
