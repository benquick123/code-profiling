#Ogrevalne
from math import *

def koordinate(ime, kraji):
    for im, x, y in kraji:
        if im == ime:
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

#Obvezne
def v_dometu(ime, domet, kraji):
    seznam = []
    x1, y1 = koordinate(ime, kraji)
    for im, x, y in kraji:
        razdalja = razdalja_koordinat(x1, y1, x, y)
        if razdalja <= domet and im != ime:
            seznam.append(im)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    x1, y1 = koordinate(ime, kraji)
    iskaniKraj = []
    najvecjaRazdalja = 0
    for im in imena:
        x,y = koordinate(im, kraji)
        razdalja = razdalja_koordinat(x1, y1, x, y)
        if razdalja > najvecjaRazdalja:
            najvecjaRazdalja = razdalja
            iskaniKraj = im
    return iskaniKraj

def zalijemo(ime, domet, kraji):
    najvecjaRazdalja = 0
    iskaniKraj = []
    x1, y1 = koordinate(ime, kraji)
    for im, x, y in kraji:
        razdalja = razdalja_koordinat(x1, y1, x, y)
        if razdalja > najvecjaRazdalja and razdalja <= domet:
            najvecjaRazdalja = razdalja
            iskaniKraj = im
    return iskaniKraj

#Dodatni
def presek(s1, s2):
    seznam = []
    for ime1 in s1:
        for ime2 in s2:
            if(ime1 == ime2):
                seznam.append(ime1)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam1 = v_dometu(ime1,domet,kraji)
    seznam2 = v_dometu(ime2, domet, kraji)
    return presek(seznam1,seznam2)



