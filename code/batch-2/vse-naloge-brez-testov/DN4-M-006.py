# Tu pišite svoje funkcije:
from math import sqrt


def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return (x,y)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
        razdalja_x = abs(x1 - x2)
        razdalja_y = abs(y1 - y2)
        razdalja = sqrt((razdalja_x) ** 2 + (razdalja_y) ** 2)

        return razdalja
def razdalja (ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    raz = razdalja_koordinat(x1, y1, x2, y2)
    return raz

def v_dometu (ime, domet, kraji):
    x0, y0 = koordinate(ime, kraji)
    seznam = []
    for imekraja, x, y in kraji:
        raz = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if ime != imekraja and raz <= domet:
            seznam.append(imekraja)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    x0, y0 = koordinate(ime, kraji)
    naj_razdalja = 0
    for ime in imena:
        x, y = koordinate(ime, kraji)
        raz = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if naj_razdalja < raz:
            naj_razdalja = raz
            naj_kraj = ime
    return naj_kraj


def zalijemo(ime, domet, kraji):
    x0, y0 = koordinate(ime, kraji)
    naj_razdalja = 0
    for ime, x, y in kraji:
        raz = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if naj_razdalja < raz <= domet:
            naj_razdalja = raz
            naj_kraj = ime
    return naj_kraj

def skupno_zalivanje(ime1, ime2, domet, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    seznam = []
    for ime, x, y in kraji:
        if sqrt((x - x1) ** 2 + (y - y1) ** 2) < domet and sqrt((x - x2) ** 2 + (y - y2) ** 2) < domet:
            seznam.append(ime)
        return seznam


