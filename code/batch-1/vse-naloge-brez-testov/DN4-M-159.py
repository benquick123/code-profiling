# Tu pišite svoje funkcije:
from math import sqrt
def koordinate(ime, kraji):
    for ime_krajev, x, y in kraji:
        if ime == ime_krajev:
            return x, y
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)

    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    seznam = []
    x1, y1 = koordinate(ime, kraji)
    for ime_krajev, x2, y2 in kraji:
        dolzina = razdalja_koordinat(x1, y1, x2, y2)
        if dolzina <= domet and dolzina != 0:
            seznam.append(ime_krajev)

    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    naj_kraj = ""
    naj_dolzina = 0
    x1, y1 = koordinate(ime, kraji)
    for kraj in imena:
        for imena_krajev, x2, y2 in kraji:
            dolzina = razdalja_koordinat(x1, y1, x2, y2)
            if kraj == imena_krajev and dolzina > naj_dolzina:
                naj_dolzina = dolzina
                naj_kraj = kraj
    return naj_kraj

def zalijemo(ime, domet, kraji):
    naj_kraj = ""
    naj_dolzina = 0
    x1, y1 = koordinate(ime, kraji)
    for imena_krajev, x2, y2 in kraji:
        dolzina = razdalja_koordinat(x1, y1, x2, y2)
        if naj_dolzina < dolzina < domet:
            naj_dolzina = dolzina
            naj_kraj = imena_krajev
    return naj_kraj

def presek(s1, s2):
    seznam = []
    for x in s1:
        for y in s2:
            if y == x:
                seznam.append(x)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    for ime, x, y in kraji:
        dolzina1 = razdalja(ime1, ime, kraji)
        dolzina2 = razdalja(ime2, ime, kraji)
        if dolzina1 <= domet and dolzina2 <= domet and ime != ime1 and ime != ime2:
            seznam.append(ime)
    return seznam




