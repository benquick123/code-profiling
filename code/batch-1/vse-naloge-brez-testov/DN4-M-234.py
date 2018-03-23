# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for i, x, y in kraji:
        if ime == i:
            return x,y

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1,kraji)
    x2,y2 = koordinate(ime2,kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):
    seznam=[]
    x,y=koordinate(ime, kraji)
    for i, x2, y2 in kraji:
        if x!=x2 and y!=y2:
            if razdalja_koordinat(x,y,x2,y2)<=domet:
                seznam.append(i)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    maks=imena[0]
    for i in imena:
        if razdalja(ime,i,kraji)>razdalja(ime,maks,kraji):
            maks=i
    return maks

def zalijemo(ime, domet, kraji):
    a=v_dometu(ime,domet,kraji)
    return najbolj_oddaljeni(ime,a,kraji)

def presek(s1, s2):
    s3=[]
    for a in s1:
        for b in s2:
            if a==b:
                s3.append(a)
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1=v_dometu(ime1,domet,kraji)
    s2=v_dometu(ime2,domet,kraji)
    return presek(s1,s2)

