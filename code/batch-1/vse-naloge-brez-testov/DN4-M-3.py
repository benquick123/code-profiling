# Tu pišite svoje funkcije:

from math import *
def koordinate(ime, kraji):
    j = 0
    for i in kraji:
        if i[0] == ime:
            j = 1
            break
    if j:
        return (i[1], i[2])
    else:
        return (None)

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(((x1-x2)** 2)+((y1-y2)**2))

def razdalja(ime1, ime2, kraji):
    ko1 = koordinate(ime1,kraji)
    ko2 = koordinate(ime2, kraji)
    return razdalja_koordinat(ko1[0],ko1[1],ko2[0],ko2[1])

def v_dometu(ime, domet, kraji):
    mesta = []
    for i in kraji:
        if razdalja(ime, i[0], kraji) <= domet and ime != i[0]:
            mesta.append(i[0])
    return mesta

def najbolj_oddaljeni(ime, imena, kraji):
    naj = imena[0]
    for i in imena:
        if razdalja(ime,i,kraji) > razdalja(ime,naj,kraji):
            naj = i
    return naj

def zalijemo(ime, domet, kraji):
    for i in kraji:
        if razdalja(ime,i[0],kraji)<domet:
            naj= i[0]
            break
    for i in kraji:
        if razdalja(ime,naj,kraji)<razdalja(ime,i[0],kraji)<domet:
            naj=i[0]
    return naj

def presek(s1, s2):
    s3 = []
    for i in s1:
        for j  in s2:
            if(i == j):
                s3.append(i)
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    skup = []
    for i in kraji:
        raz1=razdalja(ime1,i[0],kraji)
        raz2=razdalja(ime2,i[0],kraji)
        if (raz1 < domet > raz2):
            skup.append(i[0])
    return skup

