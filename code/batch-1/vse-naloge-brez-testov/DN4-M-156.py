from math import *
def koordinate(ime, kraji):
    for i, x, y in kraji:
        if i == ime:
            return ( x, y)

def razdalja_koordinat (x1: object, y1: object, x2: object, y2: object) -> object:
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate (ime1, kraji)
    x2, y2 = koordinate (ime2, kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu (ime, domet, kraji):
    seznam_krajev = []
    x1,y1 = koordinate(ime, kraji)
    for i, x, y in kraji:
        razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if razdalja <= domet and i != ime:
            seznam_krajev.append(i)
    return seznam_krajev


def najbolj_oddaljeni(ime, imena, kraji):
    x1 , y1 = koordinate(ime, kraji)
    najrazdalja = 0
    imek = ""
    for i in imena:
        for im, x, y in kraji:
            if i == im:
                razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                if razdalja > najrazdalja:
                    najrazdalja = razdalja
                    imek = im
    return imek

def zalijemo(ime, domet, kraji):
    x1, y1 = koordinate(ime, kraji)
    koncrazdalj = 0
    imek = ""
    for ime, x, y in kraji:
        razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if (razdalja <= domet and razdalja > koncrazdalj):
            koncrazdalj = razdalja
            imek = ime
    return imek

def presek(s1,s2):
    seznam = []
    for i in s1:
        for j in s2:
            if i == j:
                seznam.append(i)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    x1,y1 = koordinate(ime1, kraji)
    x2,y2 = koordinate(ime2,kraji)
    for ime, x, y in kraji:
        if sqrt((x - x1) ** 2 + (y - y1) ** 2) < domet and sqrt((x - x2) ** 2 + (y - y2) ** 2) < domet:
            seznam.append(ime)
    return seznam


