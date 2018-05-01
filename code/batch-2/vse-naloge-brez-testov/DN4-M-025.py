# Tu pišite svoje funkcije: #bucha = nespremenljivka
from math import *

def koordinate(ime, kraji):
    x = 0
    y = 0
    for e in kraji:
        ime_kraja, x_koordinata, y_koordinata = e
        if ime == ime_kraja:
            x = x_koordinata
            y = y_koordinata
            return x, y
        elif ime == None:
            return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    x_ime, y_ime = koordinate(ime, kraji)
    zalij_kraje = []
    for a in kraji:
        kraj, x2, y2 = a
        razdalja = razdalja_koordinat(x_ime, y_ime, x2, y2)
        if domet >= razdalja and kraj != ime:
            zalij_kraje.append(kraj)
    return zalij_kraje

def najbolj_oddaljeni(ime, imena, kraji):
    oddaljeni = []
    x1, y1 = koordinate(ime, kraji)
    razdalja = 0
    for e in kraji:
        ime_kraja, x_koordinata, y_koordinata = e
        if ime == ime_kraja:
            x = x_koordinata
            y = y_koordinata
    kilometrina = 0
    for e in imena:
        for a in kraji:
            kraj1 = e
            ime_kraja, x, y = a
            if ime_kraja == kraj1:
                x_ime = x
                y_ime = y
                razdalja = sqrt(pow(x_ime - x1, 2) + pow(y_ime - y1, 2))
                oddaljeni.append([(razdalja), (kraj1)])
    vrni = 0
    for c in oddaljeni:
        razdalja, kraj1 = c
        if razdalja > kilometrina:
            kilometrina = razdalja
            vrni = kraj1
    return vrni

def zalijemo(ime, domet, kraji):
    razdalja = 0
    najdaljsa_razdalja = 0
    zalit_kraj = ""
    x_ime, y_ime = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        razdalja = razdalja_koordinat(x_ime, y_ime, x, y)
        if domet > razdalja > najdaljsa_razdalja:
            najdaljsa_razdalja = razdalja
            zalit_kraj = kraj
    return zalit_kraj


