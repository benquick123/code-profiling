# Tu pišite svoje funkcije:

from math import *

def koordinate(ime, kraji):
    terka = ()
    for naziv, x, y in kraji:
        if naziv == ime:
            terka = x, y

    if terka:
        return terka

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2-x1)**2 + (y2-y1)**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    d = razdalja_koordinat(x1, y1, x2, y2)
    return d


def v_dometu(ime, domet, kraji):
    seznam = []
    d = 0
    for naziv, x, y in kraji:
        d = razdalja(naziv, ime, kraji)
        if d <= domet and naziv != ime:
            seznam.append(naziv)

    return seznam

def najbolj_oddaljeni (ime, imena, kraji):
    maks = 0
    kraj = ''
    d=0
    for i in imena:
        d = razdalja(ime, i, kraji)
        if d > maks:
            maks = d
            kraj = i

    return kraj

def zalijemo(ime, domet, kraji):
    d = 0
    najvecja_mozna = 0
    i=''
    for naziv, x, y in kraji:
        d = razdalja(naziv, ime, kraji)
        if d < domet and d > najvecja_mozna:
            najvecja_mozna = d
            i=naziv

    return i

