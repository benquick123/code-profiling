from math import *
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return (x,y)
            break

def razdalja_koordinat(x1, y1, x2, y2):

    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)


    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
     vdometu = []
     for kraj, x,y in kraji:
         a = razdalja(ime, kraj, kraji)
         if  a <= domet:
             if ime != kraj:
                 vdometu.append(kraj)

     return vdometu

def najbolj_oddaljeni(ime, imena, kraji):
    najoda = 0
    kraj3 = []
    for ime2 in imena:
        temp = razdalja(ime, ime2, kraji)
        if temp > najoda:
            najoda = temp
            kraj3 = ime2
    return  kraj3

def zalijemo(ime, domet, kraji):
    krajivdometu = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, krajivdometu, kraji)

def presek(s1, s2):
    pre=[]
    for a in s1:
        for b in s2:
            if a==b:
                pre.append(a)
    return pre

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return presek(s1,s2)
# Tu pišite svoje funkcije:




