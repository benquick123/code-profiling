from math import *
#ogrevalna
def koordinate(ime, kraji):

    for ime1, x, y in kraji:
        if ime1 == ime:
            x1 = x
            y1 = y
            c = (x1, y1)
            return c
    return None



def razdalja_koordinat(x1, y1, x2, y2):
    a = sqrt((x2 - x1) ** 2 + (y2 -y1) ** 2)
    return a


def razdalja(ime1, ime2, kraji):
    a = koordinate(ime1, kraji)
    x1, y1 = a
    b = koordinate(ime2, kraji)
    x2, y2 = b
    return razdalja_koordinat(x1, y1, x2, y2)



#obvezna
def v_dometu(ime, domet, kraji):
    s = []
    for ime1, x, y in kraji:
        if ime1 == ime:
            x_kraj = x
            y_kraj = y
            break

    for ime2, x, y in kraji:
        if ime2 == ime:
            continue
        raz = sqrt((x - x_kraj) ** 2 + (y - y_kraj) ** 2)
        if raz <= domet:
           s.append(ime2)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    for ime1, x, y in kraji:
        if ime1 == ime:
            x_kraj = x
            y_kraj = y
            break
    naj_raz = 0
    for i in imena:
        for ime2, x, y in kraji:
            if ime2 == i:
                raz = sqrt((x - x_kraj) ** 2 + (y - y_kraj) ** 2)
                if raz > naj_raz:
                    naj_raz = raz
                    ime3 = ime2
    return ime3

def zalijemo(ime, domet, kraji):
    for ime1, x, y in kraji:
        if ime1 == ime:
            x_kraj = x
            y_kraj = y
            break
    naj_raz = 0
    for ime2, x, y in kraji:
        raz = sqrt((x - x_kraj) ** 2 + (y - y_kraj) ** 2)
        if raz <= domet and naj_raz < raz:
            naj_raz = raz
            ime3 = ime2
    return ime3


#dodatna
def presek(s1, s2):
    s = []
    for i in s1:
        for j in s2:
            if j == i:
                s.append(j)
    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s = []
    for ime, x, y in kraji:
        if ime == ime1:
            x_kraj1 = x
            y_kraj1 = y
            continue
        if ime == ime2:
            x_kraj2 = x
            y_kraj2 = y
            continue
    for ime, x, y in kraji:
        raz1 = sqrt((x - x_kraj1) ** 2 + (y - y_kraj1) ** 2)
        raz2 = sqrt((x - x_kraj2) ** 2 + (y - y_kraj2) ** 2)
        if raz1 <= domet and raz2 <= domet:
            s.append(ime)
    return s







# Tu pišite svoje funkcije:
