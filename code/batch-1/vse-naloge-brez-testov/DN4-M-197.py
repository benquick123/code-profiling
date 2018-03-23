# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for mesto, cordx, cordy in kraji:
        if mesto == ime:
            x1 = cordx
            y1 = cordy
            return x1, y1

def razdalja_koordinat(x1,y1,x2,y2):
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja

def razdalja(ime1,ime2,kraji):
    x1,y1 = koordinate(ime1,kraji)
    x2,y2 = koordinate(ime2,kraji)
    razdalja = razdalja_koordinat(x1,y1,x2,y2)
    return razdalja

def v_dometu(ime, domet, kraji):
    krajiL = []
    x1,y1 = koordinate(ime,kraji)
    for mesto, x2, y2 in kraji:
        razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if (razdalja <= domet and not mesto == ime):
            krajiL.append(mesto)
    return krajiL

def najbolj_oddaljeni(ime,imena,kraji):
    razdalja2 = 0
    for mesto in imena:
        razdalja1 = razdalja(ime, mesto, kraji)
        if razdalja1 > razdalja2:
            razdalja2 = razdalja1
            kraj = mesto
    return kraj

def zalijemo(ime, domet, kraji):
    mesta=v_dometu(ime, domet,kraji)
    kraj=najbolj_oddaljeni(ime,mesta,kraji)
    return kraj

def presek(s1, s2):
    s3=list(set(s1).intersection(s2))
    return s3

def skupno_zalivanje(ime1,ime2,domet,kraji):
    kraji1=v_dometu(ime1,domet, kraji)
    kraji2=v_dometu(ime2,domet, kraji)
    kraji=presek(kraji1,kraji2)
    return kraji

