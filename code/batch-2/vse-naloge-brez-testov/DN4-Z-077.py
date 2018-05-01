# Tu pišite svoje funkcije:
import math

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return x, y

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    kraji_v_dometu = []
    for name, x, y in kraji:
        if 0 < razdalja(ime, name, kraji) <= domet:
            kraji_v_dometu.append(name)
    return kraji_v_dometu


def najbolj_oddaljeni(ime, imena, kraji):
    max_distance = None
    max_name = ""
    for name, x, y in kraji:
        if name in imena:
            distance = razdalja(ime, name, kraji)
            if max_distance is None or max_distance < distance:
                max_distance = distance
                max_name = name
    return max_name


def zalijemo(ime, domet, kraji):
    max_distance = None
    max_name = ""
    for name, x, y in kraji:
        distance = razdalja(ime, name, kraji)
        if distance <= domet and(max_distance is None or max_distance < distance):
            max_distance = distance
            max_name = name
    return max_name


def presek(s1, s2):
    common = []
    for e in s1:
        if e in s2:
            common.append(e)
    return common

def skupno_zalivanje(ime1, ime2, domet, kraji):
    v_dometu_1 = []
    v_dometu_2 = []
    for name, x, y in kraji:
        distance = razdalja(ime1, name, kraji)
        distance2 = razdalja(ime2, name, kraji)
        if distance <= domet:
            v_dometu_1.append(name)
        if distance2 <= domet:
            v_dometu_2.append(name)
    return presek(v_dometu_1, v_dometu_2)



