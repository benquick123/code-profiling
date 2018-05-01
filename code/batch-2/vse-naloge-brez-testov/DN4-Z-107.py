import math
def koordinate(ime, kraji):
    for name, x, y in kraji:
        if name == ime:
            return (x, y)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    kraj_ena = koordinate(ime1, kraji)
    kraj_dva = koordinate(ime2, kraji)
    return razdalja_koordinat(kraj_ena[0], kraj_ena[1], kraj_dva[0], kraj_dva[1])


def v_dometu(ime, domet, kraji):
    seznam = []
    for name, x, y in kraji:
        distance = razdalja(ime, name, kraji)
        if 0.0 < distance <= domet:
            seznam.append(name)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    max_oddaljeni = imena[0]
    max_razdalja = razdalja(ime, imena[0], kraji)
    for name in imena:
        if razdalja(ime, name, kraji) > max_razdalja:
            max_oddaljeni = name
            max_razdalja = razdalja(ime, name, kraji)
    return max_oddaljeni

def zalijemo(ime, domet, kraji):
    max_oddaljeni = None
    max_razdalja = 0
    for name, x, y in kraji:
        distance = razdalja(ime, name, kraji)
        if distance > max_razdalja and distance <= domet:
            max_oddaljeni = name
            max_razdalja = distance
    return max_oddaljeni

def presek(s1, s2):
    seznam = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                seznam.append(e1)
    return seznam

def lahko_zalije(ime1, ime2, domet, kraji):
    if razdalja(ime1, ime2, kraji) <= domet:
        return True
    else:
        return False

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    for name, x, y in kraji:
        if lahko_zalije(ime1, name, domet, kraji) and lahko_zalije(ime2, name, domet, kraji):
            seznam.append(name)
    return seznam

