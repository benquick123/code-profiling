# Tu pišite svoje funkcije:
from math import *


def koordinate(ime, kraji):
    for mesta, x, y in kraji:
        if ime == mesta:
            return x, y


def razdalja_koordinat(x1, y1, x2, y2):
    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    razdalja = sqrt(x + y)
    return razdalja


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja_krajev = razdalja_koordinat(x1, y1, x2, y2)
    return razdalja_krajev

def v_dometu(ime, domet, kraji):
    v_dometu = []
    for mesto, x, y in kraji:
        v = razdalja(ime, mesto, kraji)
        if 0 < v <= domet:
            v_dometu.append(mesto)
    return v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    najrazdalja = 0
    najmesto = 0
    for mesto in imena:
        oddaljenost = razdalja(ime, mesto, kraji)
        if oddaljenost > najrazdalja:
            najrazdalja = oddaljenost
            najmesto = mesto
    return najmesto

def zalijemo(ime, domet, kraji):
    najrazdalja = 0
    najmesto = 0
    for mesto, x, y in kraji:
        v = razdalja(ime, mesto, kraji)
        if najrazdalja < v <= domet:
            najrazdalja = v
            najmesto = mesto
    return najmesto

def presek(s1, s2):
    elementi = []
    for element1 in s1:
        for element2 in s2:
            if element1 == element2:
                elementi.append(element1)
    return elementi

def skupno_zalivanje(ime1, ime2, domet, kraji):
    prvo = v_dometu(ime1,domet, kraji)
    drugo = v_dometu(ime2, domet, kraji)
    skupno = presek(prvo, drugo)
    return skupno

