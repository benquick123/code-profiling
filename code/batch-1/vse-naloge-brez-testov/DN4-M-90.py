from math import *

def koordinate(ime,kraji):
    for kraj,x,y in kraji:
        if kraj==ime:
            return (x,y)

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja=daljava=sqrt((x1-x2)**2+(y1-y2)**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    (x1,y1)=koordinate(ime1,kraji)
    (x2,y2)=koordinate(ime2,kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime,domet,kraji):
    seznam_krajev=[]
    (x1,y1)= koordinate(ime,kraji)
    for kraj,x2,y2 in kraji:
        if razdalja_koordinat(x1,y1,x2,y2)<= domet and razdalja_koordinat(x1,y1,x2,y2)>0:
            seznam_krajev.append(kraj)
    return seznam_krajev


def najbolj_oddaljeni(ime, imena, kraji):
    max_razdalja=0
    max_kraj=""
    (x1,y1)=koordinate(ime,kraji)
    for kraj in imena:
        (x2,y2)=koordinate(kraj,kraji)
        if razdalja_koordinat(x1,y1,x2,y2)>max_razdalja:
            max_razdalja=razdalja_koordinat(x1,y1,x2,y2)
            max_kraj=kraj
    return max_kraj

def zalijemo(ime,domet,kraji):
    max_razdalja=0
    max_kraj=""
    (x1,y1)=koordinate(ime,kraji)
    for kraj,x2,y2 in kraji:
        (x2,y2)=koordinate(kraj,kraji)
        if razdalja_koordinat(x1,y1,x2,y2)<=domet and razdalja_koordinat(x1,y1,x2,y2)>max_razdalja:
            max_razdalja=razdalja_koordinat(x1,y1,x2,y2)
            max_kraj=kraj
    return max_kraj

def presek(s1,s2):
    skupni_el=[]
    for e in s1:
        if e in s2:
            skupni_el.append(e)
    return skupni_el

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam1=v_dometu(ime1,domet,kraji)
    seznam2=v_dometu(ime2,domet,kraji)
    return presek(seznam1,seznam2)


