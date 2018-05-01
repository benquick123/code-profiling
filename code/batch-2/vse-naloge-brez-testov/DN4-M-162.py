from math import *


def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            terka_koordinata = (x, y)
            return terka_koordinata
    else:
        return None


def razdalja_koordinat(x1, y1, x2, y2):
    r = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return r


def razdalja(ime1, ime2, kraji):
    (a1, b1) = koordinate(ime1, kraji)
    (a2, b2) = koordinate(ime2, kraji)
    if a1 is not None and a2 is not None and b1 is not None and b2 is not None:
        return razdalja_koordinat(a1, b1, a2, b2)
    else:
        return None


def v_dometu(ime, domet, kraji):
    kraji_v_dometu = []
    for kraj1, x1, y1 in kraji:
        if kraj1 == ime:
            for kraj2, x2, y2 in kraji:
                razmak = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if razmak <= domet and kraj2 != kraj1:
                    kraji_v_dometu.append(kraj2)
    return kraji_v_dometu


def najbolj_oddaljeni(ime, imena, kraji):
    (x2, y2) = koordinate(ime, kraji)
    naj_razmak = 0
    naj_kraj = []
    for kraj_imena in imena:
        for kraj, x1, y1 in kraji:
            if kraj == kraj_imena:
                razmak = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if naj_razmak < razmak:
                    naj_razmak = razmak
                    naj_kraj = kraj
    return naj_kraj


def zalijemo(ime, domet, kraji):
    (x2, y2) = koordinate(ime, kraji)
    priblizan_razmak = 0
    naj_kraj = []
    for kraj, x1, y1 in kraji:
        razmak = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if priblizan_razmak < razmak < domet:
            priblizan_razmak = razmak
            naj_kraj = kraj
    return naj_kraj


def presek(s1, s2):
    seznam = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                seznam.append(e1)
    return seznam


def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    if koordinate(ime1, kraji) and koordinate(ime2, kraji) is not None:
        (a1, b1) = koordinate(ime1, kraji)
        (a2, b2) = koordinate(ime2, kraji)
        for kraj, x, y in kraji:
            if ime1 != kraj and ime2 != kraj:
                r1 = sqrt((x - a1) ** 2 + (y - b1) ** 2)
                r2 = sqrt((x - a2) ** 2 + (y - b2) ** 2)
                if r1 < domet and r2 < domet:
                    seznam.append(kraj)
    return seznam



