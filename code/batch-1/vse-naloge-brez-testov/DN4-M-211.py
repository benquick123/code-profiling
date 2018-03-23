from math import *

def koordinate(ime, kraji):
    for mesto, x0, y0 in kraji:
        if ime == mesto:
         return (x0, y0)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja_kraji = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja_kraji

def v_dometu(ime, domet, kraji):
    seznam_mest=[]
    ime1 = ime
    for ime2, x2, y2 in kraji:
        if ime2 != ime:
            if razdalja(ime1, ime2, kraji) <= domet:
                seznam_mest.append(ime2)
    return seznam_mest

def najbolj_oddaljeni(ime, imena, kraji):
    ime1 = ime
    naj_razdalja = 0
    naj_mesto = 0
    for ime2 in imena:
        if razdalja(ime1, ime2, kraji) > naj_razdalja:
            naj_mesto = ime2
            naj_razdalja = razdalja(ime1, ime2, kraji)
    return naj_mesto

def zalijemo(ime, domet, kraji):
    imena=v_dometu(ime, domet, kraji)
    x=najbolj_oddaljeni(ime, imena, kraji)
    return x

def presek(s1, s2):
    seznam_elementov=[]
    for x in s1:
        for y in s2:
            if y == x:
                seznam_elementov.append(y)
    return (seznam_elementov)

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1=v_dometu(ime1, domet, kraji)
    s2=v_dometu(ime2, domet, kraji)
    return presek(s1, s2)
