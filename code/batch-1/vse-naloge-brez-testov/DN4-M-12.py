from math import *

def koordinate(ime, kraji):
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


def razdalja_koordinat(x1, y1, x2, y2):
    r = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return r


def razdalja(ime1, ime2, kraji):
    k1 = koordinate(ime1, kraji)
    k2 = koordinate(ime2, kraji)

    rk = razdalja_koordinat(k1[0], k1[1], k2[0], k2[1])
    return rk

def v_dometu(ime, domet, kraji):
    seznam = []
    for kraj, x, y in kraji:
        if ime == kraj:
            izhodisce = []
            izhodisce.append(x)
            izhodisce.append(y)
            for kraj, x, y in kraji:
                razdalja = sqrt(((izhodisce[0] - x) ** 2) + ((izhodisce[1] - y) ** 2))
                if razdalja <= domet and kraj != ime:
                    seznam.append(kraj)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            izhodisce = []
            izhodisce.append(x)
            izhodisce.append(y)
            for kraj, x, y in kraji:
                for izbran in imena:
                    if izbran == kraj:
                        naj_raz = 0
                        razdalja = sqrt(((izhodisce[0] - x) ** 2) + ((izhodisce[1] - y) ** 2))
                        if razdalja > naj_raz:
                            naj_raz = razdalja
                            naj_kraj = izbran
    return naj_kraj

def zalijemo(ime, domet, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            izhodisce = []
            izhodisce.append(x)
            izhodisce.append(y)
            naj_raz = 0
            for kraj, x, y in kraji:
                razdalja = sqrt(((izhodisce[0] - x) ** 2) + ((izhodisce[1] - y) ** 2))
                if razdalja < domet and kraj != ime:
                    if razdalja > naj_raz:
                        naj_raz = razdalja
                        naj_kraj = kraj
    return naj_kraj

def presek(s1, s2):
    s = []
    for sx in s1:
        for sy in s2:
            if sy == sx:
                s.append(sy)
    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):
    skupaj = presek((v_dometu(ime1, domet, kraji)), (v_dometu(ime2, domet, kraji)))
    return skupaj






#TESTI!


