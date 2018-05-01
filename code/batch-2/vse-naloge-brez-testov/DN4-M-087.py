# coding=utf-8
from math import *
# Tu pišite svoje funkcije:

def koordinate(ime,kraji):
    for ime1,x,y in kraji:
        if ime1 == ime:
            return x,y

def razdalja_koordinat(x1,y1,x2,y2):
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja

def razdalja(ime1,ime2,kraji):
    x1,y1=koordinate(ime1,kraji)
    x2,y2=koordinate(ime2,kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime,domet,kraji):
    x1,y1=koordinate(ime,kraji)
    s=[]
    for ime1,x,y in kraji:
        if razdalja_koordinat(x1,y1,x,y)<=domet and razdalja_koordinat(x1,y1,x,y)>0:
             s.append(ime1)
    return s

def najbolj_oddaljeni(ime,imena,kraji):
    max=0
    x1,y1=koordinate(ime,kraji)
    for ime1,x,y in kraji:
        if ime1 in imena:
            if razdalja(ime,ime1,kraji)>max:
                max=razdalja(ime,ime1,kraji)
                ime2=ime1
    return ime2

def zalijemo(ime,domet,kraji):
    max=0
    x1,y1=koordinate(ime,kraji)
    for ime1,x,y in kraji:
        if razdalja(ime,ime1,kraji)>max and razdalja(ime,ime1,kraji)<=domet:
            max=razdalja(ime,ime1,kraji)
            ime2=ime1
    return ime2

def presek(s1,s2):
    s=[]
    for a in s1:
        for b in s2:
            if a==b:
                s.append(b)
    return s

def skupno_zalivanje(ime1,ime2,domet,kraji):
    s=[]
    x1,y1=koordinate(ime1,kraji)
    x2,y2=koordinate(ime2,kraji)
    for ime3,x,y in kraji:
        if razdalja(ime1,ime3,kraji)<=domet and razdalja(ime2,ime3,kraji)<=domet:
            s.append(ime3)
    return s
