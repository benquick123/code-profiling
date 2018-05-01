# Tu pišite svoje funkcije:
def koordinate(ime, kraji):
    for city, height, width in kraji:
        if city == ime:
            x = height
            y = width
            return ((x, y))
    else:
        return (None)


from math import *
def razdalja_koordinat(x1, y1, x2, y2):
    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return (d)


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return (razdalja_koordinat(x1, y1, x2, y2))

def v_dometu(ime, domet, kraji):
    possible_targets = []
    for meta, na_x, na_x in kraji:
        if razdalja(ime, meta, kraji) <= domet and ime != meta:
            possible_targets.append(meta)
    return (possible_targets)

def najbolj_oddaljeni(ime, imena, kraji):
    maxd = 0
    maxPossible = ""
    for possible in imena:
        if razdalja(ime, possible, kraji) > maxd:
            maxd = razdalja(ime, possible, kraji)
            maxPossible = possible
    return (maxPossible)

def zalijemo(ime, domet, kraji):
    maxd = 0
    maxPossible = ""
    for possible, na_x, na_y in kraji:
        att = razdalja(ime, possible, kraji)
        if att > maxd and att <= domet:
            maxd = att
            maxPossible = possible
    return (maxPossible)

def presek(s1, s2):
    presekni = []
    for privremen in s1:
        for privremen2 in s2:
            if privremen == privremen2:
                presekni.append(privremen)
    return (presekni)

def skupno_zalivanje(ime1, ime2, domet, kraji):
    skupna_meta = []
    for meta, na_x, na_y in kraji:
        if razdalja(ime1, meta, kraji) <= domet and razdalja(ime2, meta, kraji) <= domet:
            skupna_meta.append(meta)
    return (skupna_meta )



