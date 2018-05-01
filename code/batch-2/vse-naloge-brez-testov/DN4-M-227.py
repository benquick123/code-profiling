# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    list = []
    for kraj, x, y in kraji:
        if kraj == ime:
            list.append(x)
            list.append(y)
            terka = tuple(list)
            return terka
    else:
        return None


def razdalja_koordinat(x1, y1, x2, y2):
    d = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    return d


def razdalja(ime1, ime2, kraji):
    terka1 = koordinate(ime1, kraji)
    terka2 = koordinate(ime2, kraji)
    raz = razdalja_koordinat(terka1[0], terka1[1], terka2[0], terka2[1])
    return raz


def v_dometu(ime, domet, kraji):
    list = []
    for kraj, x, y in kraji:
        if kraj == ime:
            x0 = x
            y0 = y
            break
    for kraj, x, y in kraji:
        d = sqrt(pow((x - x0), 2) + pow((y - y0), 2))
        if d <= domet and kraj != ime:
            list.append(kraj)
    return list


def najbolj_oddaljeni(ime, imena, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            x0 = x
            y0 = y
            break

    najdalj = 0

    for i in imena:
        for kraj, x, y in kraji:
            if i == kraj:
                d = sqrt(pow((x - x0), 2) + pow((y - y0), 2))
                if d > najdalj:
                    najdalj = d
                    kraj0 = kraj
    return kraj0


def zalijemo(ime, domet, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            x0 = x
            y0 = y
            break

    najdalj = 0

    for kraj, x, y in kraji:
        d = sqrt(pow((x - x0), 2) + pow((y - y0), 2))
        if d <= domet:
            if d > najdalj:
                najdalj = d
                kraj1 = kraj
    return kraj1


def presek(s1, s2):
    nov = []
    for el in s1:
        if el in s2:
            nov.append(el)
    return nov


def skupno_zalivanje(ime1, ime2, domet, kraji):
    list = []
    for kraj, x, y in kraji:
        if kraj == ime1:
            x1 = x
            y1 = y
        if kraj == ime2:
            x2 = x
            y2 = y

    for kraj, x, y in kraji:
        d1 = sqrt(pow((x - x1), 2) + pow((y - y1), 2))
        d2 = sqrt(pow((x - x2), 2) + pow((y - y2), 2))
        if d1 <= domet and d2 <= domet:
            list.append(kraj)
    return list



