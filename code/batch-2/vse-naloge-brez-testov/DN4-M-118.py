# Tu pišite svoje funkcije:
from math import sqrt

# Ogrevalne vaje
def koordinate(ime, kraj):
    terka = ()
    for imeKraja, dolzina, sirina in kraj:
        if ime == imeKraja:
            terka += dolzina, sirina
            return terka
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdaljaMedKrajema = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdaljaMedKrajema

def razdalja(ime1, ime2, kraji):
    kraj1 = koordinate(ime1, kraji)
    kraj2 = koordinate(ime2, kraji)
    return razdalja_koordinat(kraj1[0], kraj1[1], kraj2[0], kraj2[1])

# Obvezni del
def v_dometu(ime, domet, kraji):
    seznamKrajev = []
    for imeKraja, dolzina, sirina in kraji:
        if ime != imeKraja:
            razdaljaMedKrajema = razdalja(ime, imeKraja, kraji)
            if razdaljaMedKrajema <= domet:
                seznamKrajev.append(imeKraja)
    return seznamKrajev

def najbolj_oddaljeni(ime, imena, kraji):
    maximum = 0
    najKraj = ''
    for _ in imena:
        razdaljaMedKrajema = razdalja(ime, _, kraji)
        if razdaljaMedKrajema > maximum:
            maximum = razdaljaMedKrajema
            najKraj = _
    return najKraj

def zalijemo(ime, domet, kraji):
    seznamKrajev = v_dometu(ime, domet, kraji)
    najKraj = najbolj_oddaljeni(ime, seznamKrajev, kraji)
    return najKraj

# Dodatni del
def presek(s1, s2):
    seznam = []
    for i in s1:
        temp = i
        for j in s2:
            if temp == j:
                seznam.append(temp)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam1 = v_dometu(ime1, domet, kraji)
    seznam2 = v_dometu(ime2, domet, kraji)
    skupni = presek(seznam1, seznam2)
    return skupni

