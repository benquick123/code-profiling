# Tu pišite svoje funkcije:
from math import *

def koordinate (ime , kraji):
    for mesto , x , y in kraji:
        if (ime == mesto):
            return x , y


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2 ))
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate (ime1 , kraji)
    x2, y2 = koordinate (ime2 , kraji)
    distance = razdalja_koordinat(x1, y1, x2, y2)
    return distance

def v_dometu(ime, domet, kraji):
    ime1 = ime
    krajivdometu=[]
    for mesto, x ,y in kraji:
        ime2 = mesto
        Vdometu = razdalja(ime1, ime2, kraji)
        if Vdometu <= domet and ime1 != ime2:
            krajivdometu.append(ime2)

    return krajivdometu

def najbolj_oddaljeni(ime, imena, kraji):
    najmesto=""
    najrazdalja=0
    for mesto, x , y in kraji:
        if ime== mesto:
            x1= x
            y1= y
    for mesta in imena:
        for mesto, x ,y in kraji:
            if mesta== mesto :
                razdalja = sqrt(pow((x1 - x), 2) + pow((y1 - y), 2))
                if razdalja > najrazdalja:
                    najmesto= mesto
                    najrazdalja= razdalja
    return najmesto

def zalijemo(ime, domet, kraji):
    najkraj= ""
    najrazdalja = 0
    for mesto, x, y in kraji:
        if ime == mesto:
            x1 = x
            y1 = y
    for mesto, x, y in kraji:
        razdalja = sqrt(pow((x1 - x), 2) + pow((y1 - y), 2))
        if razdalja <= domet and mesto != ime and najrazdalja < razdalja:
             najkraj= mesto
             najrazdalja= razdalja
    return najkraj

def presek(s1, s2):
    s3=[]
    for x in s1:
        for y in s2:
            if x == y:
                s3.append(y)
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    zalivanih= []
    for mesto, x , y in kraji:
        if ime1 == mesto:
            x1=x
            y1=y
        if ime2 == mesto:
            x2=x
            y2=y
    for mesto, x , y in kraji:
        razdalja1 = sqrt(pow((x1 - x), 2) + pow((y1 - y), 2))
        razdalja2 = sqrt(pow((x2 - x), 2) + pow((y2 - y), 2))
        if razdalja1 < domet and razdalja2 < domet:
            zalivanih.append(mesto)
    return zalivanih














