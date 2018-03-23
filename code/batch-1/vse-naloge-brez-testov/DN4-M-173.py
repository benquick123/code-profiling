from math import *

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj==ime:
            koordinate=(x, y)
            return koordinate

def razdalja_koordinat(x1, y1, x2, y2):
    dolzina = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return dolzina

def razdalja(ime1, ime2, kraji):
    x, y = koordinate(ime1, kraji)
    x1, y1 = koordinate(ime2, kraji)
    return razdalja_koordinat(x, y, x1, y1)

def v_dometu(ime, domet, kraji):
    kraji_domet = []
    for kraj1, x, y in kraji:
        if razdalja(ime, kraj1, kraji) <= domet and kraj1 != ime:
            kraji_domet.append(kraj1)
    return kraji_domet

def najbolj_oddaljeni(ime, imena, kraji):
    naj_oddaljen = ime
    razdal = 0
    razdal1= 0
    for ime2 in imena:
        razdal1 = razdalja(ime, ime2, kraji)
        if razdal1 > razdal:
           razdal=razdal1
           naj_oddaljen=ime2
    return naj_oddaljen

def zalijemo(ime, domet, kraji):
    kraji_domet = []
    raz = 0
    for kraj1, x, y in kraji:
        if raz < razdalja(ime, kraj1, kraji) <= domet and kraj1 != ime:
            raz=razdalja(ime, kraj1, kraji)
            zalit=kraj1
    return zalit


