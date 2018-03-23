from math import *


def koordinate(ime, kraji):
    for ime_kraja, x1, y1 in kraji:
        if ime_kraja == ime:
            return x1, y1
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja = razdalja_koordinat(x1,y1,x2,y2)
    return razdalja

def v_dometu(ime, domet, kraji):
    seznam=[]
    x1, y1 = koordinate(ime, kraji)
    for ime_kraja, x2, y2 in kraji:
        razdalja = razdalja_koordinat(x1,y1,x2,y2)
        if razdalja<=domet and ime!=ime_kraja:
            seznam.append(ime_kraja)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    najdaljsa_razdalja=0
    x1, y1 = koordinate(ime, kraji)

    for ime_kraja in imena:
        for ime_kraja2, x2, y2 in kraji:
            if ime_kraja == ime_kraja2:
                razdalja=razdalja_koordinat(x1,y1,x2,y2)
                if razdalja > najdaljsa_razdalja:
                    najdaljsa_razdalja = razdalja
                    najbolj_oddaljeno_mesto = ime_kraja2
    return najbolj_oddaljeno_mesto

def zalijemo(ime, domet, kraji):
    x1, y1 = koordinate(ime, kraji)
    najdaljsa_razdalja = 0

    for ime_kraja, x2, y2 in kraji:
        razdalja = razdalja_koordinat(x1, y1, x2, y2)
        if razdalja < domet and razdalja > najdaljsa_razdalja:
            najdaljsa_razdalja = razdalja
            ime_kraja2 = ime_kraja
    return ime_kraja2

def presek(s1, s2):
    seznam=[]
    for ime1 in s1:
        for ime2 in s2:
            if ime1==ime2:
                seznam.append(ime2)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):

    seznam=[]

    for ime_1,x1,y1 in kraji:
        if ime_1==ime1:
            break

    for ime_2,x2,y2 in kraji:
        if ime_2==ime2:
            break

    for ime_3,x3,y3 in kraji:
        razdalja1=razdalja_koordinat(x1,y1,x3,y3)
        razdalja2=razdalja_koordinat(x2,y2,x3,y3)
        if razdalja1 < domet and razdalja2 < domet:
            seznam.append(ime_3)
    return seznam


