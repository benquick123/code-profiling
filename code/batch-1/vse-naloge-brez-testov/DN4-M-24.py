# Tu pišite svoje funkcije:
from math import *
import math

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if(ime == kraj):
            iskani_kraj = kraj
            x1 = x
            y1 = y
            return x1, y1
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    x1, y1 = koordinate(ime, kraji)
    seznam = []
    iskani_kraj = ""
    for kraj, x, y in kraji:
        if(ime !=  kraj):
            x2, y2 = x, y
            iskani_kraj = kraj

            if(razdalja_koordinat(x1, y1, x2, y2) <= domet):
                seznam.append(iskani_kraj)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    max_razdalja = 0
    max_kraj = " "
    for mozni_kraj in imena:
        for kraj, x, y in kraji:
            if(mozni_kraj == kraj):
                vmesna_razdalja = razdalja(ime, mozni_kraj, kraji)
                iskani_kraj = mozni_kraj
                if(max_razdalja < vmesna_razdalja):
                    max_razdalja = vmesna_razdalja
                    max_kraj = iskani_kraj

    return  max_kraj

def zalijemo(ime, domet, kraji):
    max_domet = " "
    max_razdalja = 0
    for kraj, x, y in kraji:
        vmesna_razdalja = razdalja(ime, kraj, kraji)
        if(vmesna_razdalja <= domet):
            if(vmesna_razdalja >= max_razdalja):
                max_razdalja = vmesna_razdalja
                max_domet = kraj

    return max_domet

def presek(s1, s2):
    seznam = []
    for x in s1:
        for y in s2:
            if(x == y):
              seznam.append(x)

    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    for kraj, x, y in kraji:
        if(razdalja(ime1, kraj, kraji) <= domet and razdalja(ime2, kraj, kraji) <= domet):
            seznam.append(kraj)

    return seznam






