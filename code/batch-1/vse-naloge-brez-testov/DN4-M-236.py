import math

#Ogrevalne funkcije
from pymysql.converters import convert_timedelta


def koordinate(ime, kraji):
    for kraj in kraji:
        if ime == kraj[0]:
            x = kraj[1]
            y = kraj[2]
            return x, y

def razdalja_koordinat(x1, y1, x2, y2):
    p1 = (x1, y1)
    p2 = (x2, y2)
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def razdalja(ime1, ime2, kraji):
    xy1 = koordinate(ime1, kraji)
    xy2 = koordinate(ime2, kraji)
    return razdalja_koordinat(xy1[0], xy1[1], xy2[0], xy2[1])

#Obvezni del

def v_dometu(ime, domet, kraji):
    zalije = []
    for kraj in kraji:
        if razdalja(ime, kraj[0], kraji) <= domet and kraj[0] != ime:
            zalije.append(kraj[0])
    return zalije

def najbolj_oddaljeni(ime, imena, kraji):
    naj_raz = 0
    for kraj in imena:
        raz = razdalja(ime, kraj, kraji)
        if naj_raz < raz:
            naj_raz = raz
            naj_kraj = kraj
    return naj_kraj

def zalijemo(ime, domet, kraji):
    naj_raz = 0
    for kraj in kraji:
        raz = razdalja(ime, kraj[0], kraji)
        if naj_raz < raz <= domet:
            naj_raz = raz
            naj_kraj = kraj[0]
    return naj_kraj

def presek(s1, s2):
    presek = []
    for element in s1:
        if element in s2:
            presek.append(element)
    return presek

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return presek(s1, s2)







