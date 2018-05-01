# Tu pišite svoje funkcije:

from math import *

def koordinate(ime, kraji):

    for i, x1, y1 in kraji:
        if i == ime:
            return x1,y1
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

def razdalja(ime1, ime2, kraji):
    x1,y1=koordinate(ime1,kraji)
    x2,y2=koordinate(ime2,kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):

    lista_imen=[]
    for i, x, y in kraji:
        if razdalja(ime,i,kraji) <= domet and i!=ime:
            lista_imen.append(i)

    return lista_imen

def najbolj_oddaljeni(ime, imena, kraji):

    razdalja2=0

    for i, x, y in kraji:
        if i in imena:
            if razdalja(ime,i,kraji) > razdalja2:
                name=i
                razdalja2 = razdalja(ime,i,kraji)

    return name

def zalijemo(ime, domet, kraji):

    imena=v_dometu(ime,domet,kraji)

    return najbolj_oddaljeni(ime,imena,kraji)

def presek(s1, s2):
    return list(set(s1)&set(s2))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1=v_dometu(ime1,domet,kraji)
    s2=v_dometu(ime2,domet,kraji)
    return presek(s1,s2)

