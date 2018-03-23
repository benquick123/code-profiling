# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for place, kor1, kor2 in kraji:
        if place == ime:
            return(kor1, kor2)

def razdalja_koordinat(x1, y1, x2, y2):
    distance = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return (distance)

def razdalja(ime1, ime2, kraji):
    a = koordinate(ime1, kraji)
    b = koordinate(ime2, kraji)
    return (razdalja_koordinat(a[0], a[1], b[0], b[1]))

def v_dometu(ime, domet, kraji):
    ys = []
    num = 0
    for place, kor1, kor2 in kraji:
        if place == ime:
            for place2, x, y in kraji:
                distance = sqrt((kor1 - x) ** 2 + (kor2 - y) ** 2)
                if distance <= domet:
                    far = distance

                    if far > num:
                        naj = place2
                        ys.append(naj)
            return ys

def najbolj_oddaljeni(ime, imena, kraji):
    naj = imena[0]
    for x in imena:
        if razdalja(ime, x, kraji) > razdalja(ime, naj, kraji):
            naj = x
    return naj

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)

def presek(s1, s2):
    ys = []
    for a in s1:
        for b in s2:
            if a == b:
                ys.append(a)
    return ys

def skupno_zalivanje(ime1, ime2, domet, kraji):
    place1 = v_dometu(ime1, domet, kraji)
    place2 = v_dometu(ime2, domet, kraji)
    return presek(place1, place2)


