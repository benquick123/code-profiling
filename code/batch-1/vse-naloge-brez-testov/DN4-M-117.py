# Tu pišite svoje funkcije:
from math import *



def v_dometu(ime, domet, kraji):
    for ime_k, x, y in kraji:
        if ime_k == ime:
            x1, y1 = x, y
    seznam = []
    for ime_k, x, y in kraji:
        if sqrt((x1 - x)**2 + (y1 - y)**2) <= domet and ime_k != ime:
            seznam.append(ime_k)
    return seznam


# s = v_dometu("Lenart", 30, kraji)
# print (s)


def najbolj_oddaljeni(ime, imena, kraji):
    for ime_k, x, y in kraji:
        if ime_k == ime:
            x1, y1 = x, y

    naj_razdalja=0
    for ime_k in imena:
        for kraj, x, y in kraji:
            if ime_k == kraj:
                razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if razdalja > naj_razdalja:
            naj_razdalja = razdalja
            k = ime_k
    return k


# k = najbolj_oddaljeni("Ljubljana", ["Domžale", "Kranj", "Maribor", "Vrhnika"], kraji)
# print(k)


def zalijemo(ime, domet, kraji):
    min = 0
    for ime_k, x, y in kraji:
        if ime_k == ime:
            x0 = x
            y0 = y

    for ime, x, y in kraji:
        if sqrt((x0 - x) ** 2 + (y0 - y) ** 2) < domet and sqrt((x0 - x) ** 2 + (y0 - y) ** 2) > min:
            min = sqrt((x0 - x) ** 2 + (y0 - y) ** 2)
            cilj = ime
    return cilj


# zalij = zalijemo("Ljubljana", 30, kraji)
# print(zalij)


def presek(s1, s2):
    seznam = []
    for ime1 in s1:
        for ime2 in s2:
            if ime1 == ime2:
                seznam.append(ime1)

    return seznam


# print(presek(["Ljubljana", "Maribor"], ["Ljubljana"]))


def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    for ime_k, x, y in kraji:
        if ime_k == ime1:
            x1, y1 = x, y
        if ime_k == ime2:
            x2, y2 = x, y
    for ime_k, x, y in kraji:
        if sqrt((x1 - x) ** 2 + (y1 - y) ** 2) < domet and sqrt((x2 - x) ** 2 + (y2 - y) ** 2) < domet:
            seznam.append(ime_k)
    return seznam


# s = skupno_zalivanje("Ljubljana", "Bled", 30, kraji)
# print(s)





#ogrevalne funkcije


def koordinate(ime, kraji):
    najden = False
    for ime_k, x, y in kraji:
        if ime_k == ime:
            k = (x, y)
            najden = True
    if najden == True:
        return k
    else:
        return None


# kor = koordinate("Ljubljana", kraji)
# print (kor)


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2-x1)**2 + (y2-y1)**2)
    return razdalja


def razdalja (ime1, ime2, kraji):
    kor1 = koordinate(ime1, kraji)
    kor2 = koordinate(ime2, kraji)
    raz = razdalja_koordinat(kor1[0], kor1[1], kor2[0], kor2[1])
    return raz


# raz = razdalja("Ljubljana", "Cerknica", kraji)
# print(raz)


