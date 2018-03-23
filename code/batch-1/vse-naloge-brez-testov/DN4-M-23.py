# Tu pišite svoje funkcije:
from math import *

# ogrevalne
def koordinate(ime, kraji):
    for val, x, y in kraji:
        if val == ime:
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    AB = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return AB

def razdalja(ime1, ime2, kraji):
    k1 = koordinate(ime1, kraji)
    k2 = koordinate(ime2, kraji)

    if k1 != None and k2 != None:
        return razdalja_koordinat(k1[0], k1[1], k2[0], k2[1])

# obvezna
def v_dometu(ime, domet, kraji):
    kraj = []

    for val, x, y in kraji:
        if val == ime:
            x1 = x
            y1 = y

    for val, x, y in kraji:
        if val != ime:
            AB = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
            if AB <= domet:
                kraj.append(val)

    return kraj

def najbolj_oddaljeni(ime, imena, kraji):
    x1, y1 = 0, 0
    topAB = 0
    topKraj = ""

    for val, x, y in kraji:
        if val == ime:
            x1, y1 = x, y

    for kraj in imena:
        for val, x, y in kraji:
            if kraj == val:
                AB = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                if topAB <= AB:
                    topKraj = kraj
                    topAB = AB
    return topKraj

def zalijemo(ime, domet, kraji):
    x1, y1 = 0, 0
    topAB = 0
    topKraj = ""

    for val, x, y in kraji:
        if val == ime:
            x1, y1 = x, y

    for val, x, y in kraji:
        if ime != val:
            AB = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
            if topAB <= AB <= domet:
                topKraj = val
                topAB = AB

    return topKraj

# dodatna
def presek(s1, s2):
    p = []

    for val1 in s1:
        for val2 in s2:
            if val1 == val2:
                p.append(val1)
    return p


def skupno_zalivanje(ime1, ime2, domet, kraji):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    skupniKraj = []

    for val, x, y in kraji:
        if val == ime1:
            x1 = x
            y1 = y
        elif val == ime2:
            x2 = x
            y2 = y

    for val, x, y in kraji:
        if val != ime1 and val != ime2:
            AB1 = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
            AB2 = sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
            if AB1 <= domet and AB2 <= domet:
                skupniKraj.append(val)

    return skupniKraj

