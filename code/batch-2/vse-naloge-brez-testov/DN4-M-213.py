from math import *

def koordinate(ime, kraji,): #1
    s = []
    for kraj, x, y in kraji:
        if ime == kraj:
            s.append(x)
            s.append(y)
            break

    if len(s) > 0:
        return tuple(s)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):#2
    rezultat = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return rezultat

def razdalja(ime1, ime2, kraji):#2
    k1 = koordinate(ime1, kraji)
    k2 = koordinate(ime2, kraji)

    rezultat_koordinat = razdalja_koordinat(k1[0], k1[1], k2[0], k2[1])
    return rezultat_koordinat


def v_dometu(ime, domet, kraji):#4
    s = []
    for ime0, x0, y0 in kraji:
        if ime0 == ime:
            break
    for ime, x, y in kraji:
        razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if 0 < razdalja <= domet:
            s.append(ime)
    return s

def najbolj_oddaljeni(ime, imena, kraji):#5
    for ime0, x, y in kraji:
        if ime == ime0:
            iz = []
            iz.append(x)
            iz.append(y)
            for ime0, x, y in kraji:
                for izbran in imena:
                    if izbran == ime0:
                        naj_raz = 0
                        razdalja = sqrt(((iz[0] - x) ** 2) + ((iz[1] - y) ** 2))
                        if razdalja > naj_raz:
                            naj_raz = razdalja
                            naj_kraj = izbran
    return naj_kraj



def zalijemo(ime, domet, kraji):#6
        naj_razdalja = 0
        for ime0, x, y in kraji:
            if ime == ime0:
                x0 = x
                y0 = y
                break
        for ime, x, y in kraji:
            razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
            if naj_razdalja < razdalja <= domet:
                naj_razdalja = razdalja
                naj_kraj = ime
        return naj_kraj


