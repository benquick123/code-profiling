# Tu pišite svoje funkcije:
from math import *
def koordinate(ime,kraji):
    for ime1,koordinata1,koordinata2 in kraji:
        if ime == ime1:
            return(koordinata1,koordinata2)
    return None
def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
def razdalja(ime1, ime2, kraji):
    koordinate1 = koordinate(ime1,kraji)
    koordinate2 = koordinate(ime2,kraji)
    return razdalja_koordinat(koordinate1[0],koordinate1[1],koordinate2[0],koordinate2[1])
def v_dometu(ime, domet, kraji):
    kraji_v_dometu = []
    for i in range(len(kraji)):
        if razdalja(ime,kraji[i][0],kraji) <= domet and ime != kraji[i][0]:
            kraji_v_dometu.append(kraji[i][0])
    return kraji_v_dometu
def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for i in range(len(imena)):
        if razdalja(ime,imena[i],kraji) > naj_razdalja:
            naj_razdalja = razdalja(ime,imena[i],kraji)
            naj_ime = imena[i]
    return naj_ime
def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime,v_dometu(ime,domet,kraji),kraji)
def presek(s1, s2):
    presek1 = []
    for i in range(len(s1)):
        for ii in range(len(s2)):
            if s1[i] == s2[ii]:
                presek1.append(s1[i])
    return presek1
def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1,domet,kraji),v_dometu(ime2,domet,kraji))


