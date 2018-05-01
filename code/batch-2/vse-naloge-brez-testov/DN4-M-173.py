from math import *

# Tu pišite svoje funkcije:

def koordinate(ime, kraji):
    for naslov, x, y in kraji:
        if naslov == ime:
            a = (x,y)
            return a
    return None


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2-x1)**2 + (y2-y1)**2)
    return razdalja


def razdalja(ime1, ime2, kraji):
    x_1, y_1 = koordinate(ime1, kraji)
    x_2, y_2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x_1, y_1, x_2, y_2)


def v_dometu(ime, domet, kraji):
    seznam = []
    for mesto, x, y in kraji:
        if razdalja(ime, mesto, kraji) - domet <= 0.5 and ime != mesto:
            seznam.append(mesto)
    return seznam


def najbolj_oddaljeni(ime, imena, kraji):
    f, g = koordinate(ime, kraji)                   #koordinati kraja, ki mu iščemo najbolj oddaljenega
    s, p = koordinate(imena[0], kraji)              #priredimo koordinati prevega zapisanega kraja
    najvecja = razdalja_koordinat(f, g, s, p)       #največja razdalja oddaljenosti kraja od podanega mesta
    najvecja_kraj = imena[0]                        #ime kraja, ki je najbolj oddaljen od podanega mesta
    for element in imena:
        s, p = koordinate(element, kraji)
        d = razdalja_koordinat(s, p, f, g)
        if najvecja < d:
            najvecja_kraj = element
            najvecja = d

    return najvecja_kraj


def zalijemo(ime, domet, kraji):
    maks_kraj = 0
    maks_kraj_ime = ""
    x1, y1 = koordinate(ime, kraji)
    for element, x, y in kraji:
        if maks_kraj < razdalja_koordinat(x1, y1, x, y) < domet:
            maks_kraj = razdalja_koordinat(x1, y1, x, y)
            maks_kraj_ime = element
    return maks_kraj_ime


def presek(s1, s2):
    seznam = []
    for element1 in s1:
        for element2 in s2:
            if element1 == element2:
                seznam.append(element1)
    return seznam


def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    for element, x_3, y_3 in kraji:
        if razdalja_koordinat(x1, y1, x_3, y_3) - domet < 1 and razdalja_koordinat(x2, y2, x_3, y_3) - domet < 1:
            seznam.append(element)
    return seznam



