# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for ime2, x0, y0 in kraji:
        if ime2 == ime:
            return(x0, y0)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1-x2)**2+(y1-y2)**2)
    return (razdalja)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):
    seznam = []
    for kraj, x0, y0 in kraji:
        if kraj == ime:
            for kraj2, x1, y1 in kraji:
                razdalja = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
                if razdalja <= domet:
                    naj_razdalja=razdalja
                    if naj_razdalja > 0:
                        city = kraj2
                        seznam.append(city)
            return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    city = imena[0]
    for kraj in imena:
        if razdalja(ime, kraj, kraji) > razdalja(ime, city, kraji):
            city = kraj
    return city

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)

def presek(s1, s2):
    seznam = []
    for element1 in s1:
        for element2 in s2:
            if element1==element2:
                seznam.append(element1)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    kraj1 = v_dometu(ime1, domet, kraji)
    kraj2 = v_dometu(ime2, domet, kraji)
    return presek(kraj1, kraj2)





