from math import *

def koordinate(ime,kraji):
    for kraj,x,y in kraji:
        if kraj==ime:
            return x,y
    return None

def razdalja_koordinat(x1,y1,x2,y2):
    razdalja=sqrt((x2-x1)**2+(y2-y1)**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1,y1=koordinate(ime1,kraji)
    x2,y2=koordinate(ime2,kraji)
    razdaljaMedKraji=razdalja_koordinat(x1,y1,x2,y2)
    return razdaljaMedKraji

def v_dometu(ime,domet,kraji):
    Vdometu=[]
    for kraj,x,y in kraji:
        if kraj!=ime:
            domet2=razdalja(ime,kraj,kraji)
            if domet2<=domet:
                Vdometu.append(kraj)
    return Vdometu

def najbolj_oddaljeni(ime,imena,kraji):
    najdlje=ime
    for kraj in imena:
        if razdalja(ime,kraj,kraji)>razdalja(ime,najdlje,kraji):
            najdlje=kraj
    return najdlje

def zalijemo(ime,domet,kraji):
    imena=v_dometu(ime,domet,kraji)
    najDomet=najbolj_oddaljeni(ime,imena,kraji)
    return najDomet

def presek(s1,s2):
    skupne=[]

