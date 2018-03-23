# Tu pišite svoje funkcije:

from math import *


def koordinate(ime, kraji):
    kraj_obstaja = False
    for ime_kraja, x, y in kraji:
        if ime_kraja == ime:
            kraj_obstaja = True
            break
    if kraj_obstaja:
        return x, y
    return None


def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def razdalja(ime1, ime2, kraji):
    kraj1_x, kraj1_y = koordinate(ime1, kraji)
    kraj2_x, kraj2_y = koordinate(ime2, kraji)
    return razdalja_koordinat(kraj1_x, kraj1_y, kraj2_x, kraj2_y)


def v_dometu(ime, domet, kraji):
    lahko_zalijemo = list()
    for ime_kraja, x, y in kraji:
        if razdalja(ime, ime_kraja, kraji) <= domet and ime_kraja != ime:
            lahko_zalijemo.append(ime_kraja)
    return lahko_zalijemo


def najbolj_oddaljeni(ime, imena, kraji):
    naj_odd = 0
    naj_odd_ime = ""
    for ime_kraja in imena:
        raz = razdalja(ime, ime_kraja, kraji)
        if raz > naj_odd:
            naj_odd = raz
            naj_odd_ime = ime_kraja
    return naj_odd_ime


def zalijemo(ime, domet, kraji):
    naj_odd = 0
    naj_odd_ime = ""
    for ime_kraja, x, y in kraji:
        raz = razdalja(ime, ime_kraja, kraji)
        if raz <= domet and raz > naj_odd:
            naj_odd = raz
            naj_odd_ime = ime_kraja
    return naj_odd_ime


def presek(s1, s2):
    v_obeh = list()
    for element in s2:
        if element in s1:
            v_obeh.append(element)
    return v_obeh

def skupno_zalivanje(ime1, ime2, domet, kraji):
    lahko_zalijemo = list()
    for ime_kraja, x, y in kraji:
        razdalja1 = razdalja(ime1, ime_kraja, kraji)
        razdalja2 = razdalja(ime2, ime_kraja, kraji)
        if razdalja1 <= domet and razdalja2 <= domet and ime_kraja != ime1 and ime_kraja != ime2:
            lahko_zalijemo.append(ime_kraja)
    return lahko_zalijemo




