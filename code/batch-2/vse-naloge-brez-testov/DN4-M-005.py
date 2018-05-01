# Tu pišite svoje funkcije:
from math import *

# koordinate
def koordinate(ime, kraji):
    for mesto, x, y in kraji:
        if mesto == ime:
            return (x, y)

# razdalja koordinat
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja

# razdalja
def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja_med_imenoma = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja_med_imenoma

# domet
def v_dometu(ime, domet, kraji):
    seznam = []
    x_ime, y_ime = koordinate(ime, kraji)
    for mesto, x, y in kraji:
        razdalja_med_krajema = razdalja_koordinat(x_ime, y_ime, x, y)
        if 0 < razdalja_med_krajema <= domet:
            seznam.append(mesto)
    return seznam

# najbolj oddaljen
def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    naj_oddaljen_kraj = ""
    for mesto in imena:
        razdalja_med_krajema = razdalja(ime, mesto, kraji)
        if razdalja_med_krajema > naj_razdalja:
            naj_razdalja = razdalja_med_krajema
            naj_oddaljen_kraj = mesto
    return naj_oddaljen_kraj

# zalijemo
def zalijemo(ime, domet, kraji):
    naj_razdalja = 0
    kraj = ""
    for mesto, x, y in kraji:
        razdalja_med_obema = razdalja(ime, mesto, kraji)
        if naj_razdalja < razdalja_med_obema <= domet:
            naj_razdalja = razdalja_med_obema
            kraj = mesto
    return kraj

# presek
def presek(s1, s2):
    return list(set(s1).intersection(s2))

# skupno zalivanje
def skupno_zalivanje(ime1, ime2, domet, kraji):
    zalivanje_krajev = []
    for mesto, x, y in kraji:
        razdalja1 = razdalja(ime1, mesto, kraji)
        razdalja2 = razdalja(ime2, mesto, kraji)
        if razdalja1 <= domet and razdalja2 <= domet:
            zalivanje_krajev.append(mesto)
    return zalivanje_krajev


