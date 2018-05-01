# Tu pišite svoje funkcije:

from math import *

# def. koordinate

def koordinate(ime, kraji):
    kraj = ime
    for ime, x, y in kraji:
        if kraj == ime:
            return (x, y)
    else:
        return None

# def. razdalja_koordinat

def razdalja_koordinat(x1, y1, x2, y2):
    raz = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return (raz)

# def. razdalja

def razdalja(ime1, ime2, kraji):
    kraj1 = koordinate (ime1, kraji)
    kraj2 = koordinate(ime2, kraji)
    raz = razdalja_koordinat(kraj1[0], kraj1[1],  kraj2[0], kraj2[1])
    return (raz)


# OBVEZNI DEL

# def. v_dometu

def v_dometu(ime, domet, kraji):
    s = []
    kraj = ime
    for ime, x, y in kraji:
        if ime == kraj:
            ime1 = ime
            x1 = x
            y1 = y

    for ime, x, y in kraji:
        raz = razdalja_koordinat(x, y, x1, y1)
        if raz <= domet and ime1 != ime:
            s.append(ime)
    return (s)

# def. najbolj_oddaljeni

def najbolj_oddaljeni(ime, imena, kraji):
    kraj = ime
    naj_raz = 0
    for ime, x, y in kraji:
        if ime == kraj:
            ime1 = ime
            x1 = x
            y1 = y

    for imex in imena:
        for ime, x, y in kraji:
            if imex == ime:
                raz = razdalja_koordinat(x, y, x1, y1)
                if raz > naj_raz:
                    naj_ime = ime
                    naj_raz = raz
    return (naj_ime)

# def. zalijemo

def zalijemo (ime, domet, kraji):
    kraj = ime
    naj_raz = 0
    for ime, x, y in kraji:
        if ime == kraj:
            ime1 = ime
            x1 = x
            y1 = y

    for ime, x, y in kraji:
        raz = razdalja_koordinat(x, y, x1, y1)
        if naj_raz < raz and raz < domet:
            naj_ime = ime
            naj_raz = raz
    return (naj_ime)






