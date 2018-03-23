# Tu pišite svoje funkcije:
import math

def koordinate(ime, kraji):
    tup = None
    for i, a, b in kraji:
        if i == ime:
            x = a
            y = b
            tup = (x, y)

    return tup


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja= razdalja_koordinat(x1, y1, x2, y2)

    return razdalja

def v_dometu(ime, domet, kraji):
    seznam_imen = []
    for i,x,y in kraji:
        razdalja2 = razdalja(ime, i, kraji)
        if razdalja2 <= domet and razdalja2 > 0:
            seznam_imen.append(i)
    return seznam_imen


def najbolj_oddaljeni(ime, imena, kraji):
    naj_kraj = ""
    naj_razdalja = 0
    for i in imena:
        razdalja1 = razdalja(ime, i, kraji)
        if razdalja1 > naj_razdalja:
            naj_razdalja = razdalja1
            naj_kraj = i
    return naj_kraj


def zalijemo(ime, domet, kraji):

    naj_razdalja = 0

    seznam = v_dometu(ime, domet, kraji)
    x1, y1 = koordinate(ime, kraji)

    for i in seznam:
        x2, y2= koordinate(i, kraji)
        razdalja = razdalja_koordinat(x1, y1, x2, y2)
        if razdalja > naj_razdalja:
            naj_razdalja = razdalja
            naj_kraj = i

    return naj_kraj


def presek(s1, s2):

    seznam=[]

    for i in s1:
        for j in s2:
            if i == j:
                seznam.append(i)
    return seznam


def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam1 = v_dometu(ime1, domet, kraji)
    seznam2 = v_dometu(ime2, domet, kraji)
    return presek(seznam2, seznam1)



