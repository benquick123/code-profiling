# Tu pišite svoje funkcije:

import math

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):

    x, y = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)

    return razdalja_koordinat(x, y, x2, y2)

def v_dometu(ime, domet, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            break

    mesta_v_dometu = []

    for kraj2, x2, y2 in kraji:
        razdalja = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
        if 0 < razdalja <= domet:
            mesta_v_dometu.append(kraj2)

    return mesta_v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            break

    najvecja_razdalja = 0
    najbolj_oddaljen_kraj = ""

    for kraj_imena in imena:
        for kraj2, x2, y2 in kraji:
            if kraj_imena == kraj2:
                razdalja = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
                if razdalja >= najvecja_razdalja:
                    najvecja_razdalja = razdalja
                    najbolj_oddaljen_kraj = kraj2

    return najbolj_oddaljen_kraj

def zalijemo(ime, domet, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            break

    najvecja_razdalja = 0
    najbolj_oddaljen_kraj = ""

    for kraj2, x2, y2 in kraji:
        razdalja = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
        if razdalja >= najvecja_razdalja and razdalja <= domet:
            najvecja_razdalja = razdalja
            najbolj_oddaljen_kraj = kraj2
                        
    return najbolj_oddaljen_kraj

def presek(s1, s2):
    s = []
    for element in s1:
        if element in s2:
            s.append(element)

    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):
    skupne_tarce = []
    for kraj, x, y in kraji:
        if ime1 == kraj:
            break

    for kraj2, x2, y2 in kraji:
        if ime2 == kraj2:
            break

    for kraj3, x3, y3 in kraji:
        razdalja_1_3 = math.sqrt((x3 - x) ** 2 + (y3 - y) ** 2)
        razdalja_2_3 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

        if razdalja_1_3 <= domet and razdalja_2_3 <= domet:
            skupne_tarce.append(kraj3)

    return skupne_tarce

