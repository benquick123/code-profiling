'''
Author: 63140235
'''

from math import sqrt

# Tu pišite svoje funkcije:
# obvezni del:

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    moji_kraji = []

    for kraj, x, y in kraji:
        if kraj == ime:
            moj_kraj = kraj

    for kraj, x, y in kraji:
        tr_razdalja = razdalja(moj_kraj, kraj, kraji)
        if tr_razdalja <= domet and kraj != moj_kraj:
            moji_kraji.append(kraj)

    return moji_kraji

def najbolj_oddaljeni(ime, imena, kraji):
    max = 0
    for tr_ime in imena:
        tr_razdalja = razdalja(ime, tr_ime, kraji)
        if tr_razdalja > max:
            max = tr_razdalja
            max_kraj = tr_ime

    return max_kraj

def zalijemo(ime, domet, kraji):
    max = 0
    for kraj, x, y in kraji:
        tr_razdalja = razdalja(ime, kraj, kraji)
        if max < tr_razdalja <= domet:
            max = tr_razdalja
            max_kraj = kraj

    return max_kraj


# dodatni del:

def presek(s1, s2):
    seznam = []

    for kraj1 in s1:
        for kraj2 in s2:
            if kraj2 == kraj1:
                seznam.append(kraj1)

    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []

    for kraj, x, y in kraji:
        razdalja1 = razdalja(kraj, ime1, kraji)
        razdalja2 = razdalja(kraj, ime2, kraji)

        if razdalja1 < domet and razdalja2 < domet:
            seznam.append(kraj)

    return seznam


