from math import *

def koordinate(ime, kraji):
    koordinate = ()
    for ime_kraji, x, y, in kraji:
        if ime_kraji == ime:
            koordinate += (x, )
            koordinate += (y, )
            return koordinate

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja_koordinat = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja_koordinat

def razdalja(ime1, ime2, kraji):
    prvi = koordinate(ime1, kraji)
    x_prvi = prvi[0]
    y_prvi = prvi[1]
    drugi = koordinate(ime2, kraji)
    x_drugi = drugi[0]
    y_drugi = drugi[1]
    return razdalja_koordinat(x_prvi, y_prvi, x_drugi, y_drugi)

def v_dometu(ime, domet, kraji):
    v_dometu = []
    for ime_kraji, x0, y0 in kraji:
        if ime == ime_kraji:
            break
    for ime_kraji, x, y in kraji:
        razdalja = sqrt((x0 - x) ** 2 + (y0 - y) ** 2)
        if razdalja <= domet and ime_kraji != ime:
            v_dometu.append(ime_kraji)
    return v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for ime_kraji, x0, y0 in kraji:
        if ime == ime_kraji:
            break
    for ime_kraji, x, y in kraji:
        for ime in imena:
            if ime == ime_kraji:
                razdalja = sqrt((x0 - x) ** 2 + (y0 - y) ** 2)
                if razdalja > naj_razdalja:
                    naj_razdalja = razdalja
                    naj_kraj = ime
    return naj_kraj

def zalijemo(ime, domet, kraji):
    for ime_kraji, x0, y0 in kraji:
        if ime == ime_kraji:
            break
    naj_razdalja = 0
    for ime, x, y in kraji:
        razdalja = sqrt((x0 - x) ** 2 + (y0 - y) ** 2)
        if razdalja <= domet:
            if razdalja > naj_razdalja:
                naj_kraj = ime
                naj_razdalja = razdalja
    return naj_kraj

def presek(s1, s2):
    presek = []
    for kraj1 in s1:
        for kraj2 in s2:
            if kraj1 == kraj2:
                presek.append(kraj1)
    return presek

def skupno_zalivanje(ime1, ime2, domet, kraji):
    skupno_zalivanje = []
    for ime, x1, y1 in kraji:
        if ime == ime1:
            break
    for ime, x2, y2 in kraji:
        if ime == ime2:
            break
    for ime, x, y in kraji:
        razdalja1 = sqrt((x - x1) ** 2 + (y - y1) ** 2)
        razdalja2 = sqrt((x - x2) ** 2 + (y - y2) ** 2)
        if razdalja1 <= domet and razdalja2 <= domet:
            skupno_zalivanje.append(ime)
    return skupno_zalivanje