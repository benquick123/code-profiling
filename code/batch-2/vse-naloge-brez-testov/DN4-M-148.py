# Tu pišite svoje funkcije:
# Ogrevalne funkcije
from math import sqrt
def koordinate(ime, kraji):
    for ime_kraja, x, y in kraji:
        if ime == ime_kraja:
            return x, y


def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2,kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

# Obvezni del
def v_dometu(ime, domet, kraji):
    lahko_zadane = []
    for neko_ime, x, y in kraji:
        if neko_ime != ime:
            if razdalja (ime, neko_ime, kraji) <= domet:
                lahko_zadane.append(neko_ime)
    return (lahko_zadane)

def najbolj_oddaljeni(ime, imena, kraji):
    naj = 0
    for ime_kraja in imena:
        if razdalja (ime, ime_kraja, kraji) > naj:
                naj = razdalja (ime, ime_kraja, kraji)
                najdlje = ime_kraja
    return (najdlje)

def zalijemo(ime, domet, kraji):
    naj = 0
    for neko_ime, x, y in kraji:
        if neko_ime != ime:
            if naj < razdalja (ime, neko_ime, kraji) <= domet:
                naj = razdalja (ime, neko_ime, kraji)
                najdlje = neko_ime
    return (najdlje)
    
def presek(s1, s2):
    i = []
    for a in s1:
        if a in s1 and a in s2:
            i.append(a)
    return i

def skupno_zalivanje(ime1, ime2, domet, kraji):
    zaliti_kraji = []
    for ime, x, y in kraji: 
        if razdalja(ime, ime1, kraji) <= domet and razdalja(ime, ime2, kraji) <= domet:
            zaliti_kraji.append(ime)
    return zaliti_kraji
            

# Dodatni del 

