# Tu pišite svoje funkcije:

import math;

def koordinate(ime, kraji):
    for i, x, y in kraji:
        if ime == i:
            return (x, y)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    for i, x, y in kraji:
        if ime == i:
            break
    kraji_v_dometu = []
    for ime, x1, y1 in kraji:
        razdalja = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        if razdalja <= domet and i != ime:
            kraji_v_dometu.append(ime)
    return kraji_v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    for ime_kraja, x, y in kraji:
        if ime == ime_kraja:
            break
    naj_kraj = ""
    naj_razdalja = -1
    for ime in imena:
        for i, x1, y1 in kraji:
            if i == ime:
                break
        razdalja = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        if razdalja > naj_razdalja:
            naj_razdalja = razdalja
            naj_kraj = ime
    return naj_kraj

def zalijemo(ime, domet, kraji):
    for i, x,  y in kraji:
        if i == ime:
            break
    naj_kraj = ""
    naj_razdalja = -1
    for ime, x1, y1 in kraji:
        razdalja = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        if razdalja > naj_razdalja and razdalja  <= domet:
            naj_razdalja = razdalja
            naj_kraj = ime
    return naj_kraj

def presek(s1, s2):
    s3 = []
    for s_1 in s1:
        for s_2 in s2:
            if s_1 == s_2:
                s3.append(s_1)
    return s3


def skupno_zalivanje(ime1, ime2, domet, kraji):
    for kraj, x, y in kraji:
        if kraj == ime1:
            x1, y1 = x, y
        if kraj == ime2:
            x2, y2 = x, y
    skupni_kraji = []
    for ime, x, y in kraji:
        prva_razdalja = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        druga_razdalja = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
        if prva_razdalja <= domet and druga_razdalja <= domet and ime != ime1 and ime !=ime2:
            skupni_kraji.append(ime)
    return skupni_kraji



