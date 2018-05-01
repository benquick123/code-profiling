# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return x, y

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    seznam_krajev = []
    for kraj, x, y in kraji:
        if ime != kraj:
            if razdalja(ime, kraj, kraji) <= domet:
                seznam_krajev.append(kraj)
    return seznam_krajev

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for kraj in imena:
        nova_razdalja = razdalja(kraj, ime, kraji)
        if nova_razdalja > naj_razdalja:
            naj_razdalja = nova_razdalja
            naj_kraj = kraj
    return naj_kraj

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)

def presek(s1, s2):
    seznam_presek = []
    for element1 in s1:
        for element2 in s2:
            if element1 == element2:
                seznam_presek.append(element1)
                break
    return seznam_presek

def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))


