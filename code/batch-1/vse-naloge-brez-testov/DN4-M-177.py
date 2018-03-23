#Teste dodatnih nalog sem izbrisal
# Tu pišite svoje funkcije:

from math import *

#Ogrevalne funkcije

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return ( x, y)

def razdalja_koordinat (x, y , x1 , y1):
    razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x,y = koordinate (ime1, kraji)
    x1, y1 = koordinate (ime2, kraji)
    return razdalja_koordinat(x,y,x1,y1)

#Obvezni del

def v_dometu (ime, domet, kraji):
    seznam_krajev = []
    x1,y1 = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if razdalja <= domet and kraj != ime:
            seznam_krajev.append(kraj)
    return seznam_krajev


def najbolj_oddaljeni(ime, imena, kraji):
    x1 , y1 = koordinate(ime, kraji)
    najrazdalja = 0
    imekraja = ""
    for i in imena:
        for kraj, x, y in kraji:
            if i == kraj:
                razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                if razdalja > najrazdalja:
                    najrazdalja = razdalja
                    imekraja = kraj
    return imekraja

def zalijemo(ime, domet, kraji):
    x1, y1 = koordinate(ime, kraji)
    razdalj0 = 0
    imekraja = ""
    for ime, x, y in kraji:
        razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if (razdalja <= domet and razdalja > razdalj0):
            razdalj0 = razdalja
            imekraja = ime
    return imekraja


