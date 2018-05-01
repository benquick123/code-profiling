# Tu pišite svoje funkcije:

import math

def koordinate(ime, kraji):
    for kraj, k1, k2 in kraji:
        if ime == kraj:
            return (k1, k2)
    else:
        return None


def razdalja_koordinat(x1, y1, x2, y2):
    odd = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return odd


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    raz = razdalja_koordinat(x1, y1, x2, y2)
    return raz


def v_dometu(ime, domet, kraji):
    kraji_v_dometu = []

    for i, k1, k2 in kraji:
        if razdalja(ime, i, kraji) <= domet and ime != i:
            kraji_v_dometu.append(i)
    return kraji_v_dometu


def najbolj_oddaljeni(ime, imena, kraji):
    trenutno_najoddljeni = 0
    najoddaljeni = ""
    for i in imena:
        if razdalja(ime, i, kraji) > trenutno_najoddljeni:
            najoddaljeni = i
            trenutno_najoddljeni = razdalja(ime, i, kraji)
    return najoddaljeni


def zalijemo(ime, domet, kraji):
    trenutno_najoddaljeni = 0
    se_v_dometu = ""
    for i, k1, k2 in kraji:
        if trenutno_najoddaljeni < razdalja(ime, i, kraji) < domet:
            trenutno_najoddaljeni = razdalja(ime, i, kraji)
            se_v_dometu = i
    return se_v_dometu


def presek(s1, s2):
    r = []
    for i in s1:
        for j in s2:
            if i == j:
                r.append(i)
    return r


def skupno_zalivanje(ime1, ime2, domet, kraji):
    rezultat = []

    for i, k1, k2 in kraji:
        if razdalja(ime1, i, kraji) <= domet and razdalja(ime2, i, kraji) <= domet:
            rezultat.append(i)
    return rezultat





