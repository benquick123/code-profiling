# Tu pišite svoje funkcije:
from math import *


def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return x, y
    else:
        return None


def razdalja_koordinat(x1, y1, x2, y2):

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)


"""
#JAZ BI TAKO, ALI PA DA koordinate() VRNE 2x None, A NIČ OD TEGA NE PRESTANE TESTOV
def razdalja(ime1, ime2, kraji):
    if koordinate(ime1, kraji) is not None and koordinate(ime2, kraji) is not None:
        x1, y1 = koordinate(ime1, kraji)
        x2, y2 = koordinate(ime2, kraji)
        return razdalja_koordinat(x1, y1, x2, y2)
"""

"""
#A BI SE DALO KAKO RAZPAKIRAT V KLICU FUNKCIJE? TO NE DELA
def razdalja(ime1, ime2, kraji):
    return razdalja_koordinat(koordinate(ime1, kraji), koordinate(ime2, kraji))
"""


def v_dometu(ime, domet, kraji):
    seznam = []
    for kraj, _, _ in kraji:
        razdalja0 = razdalja(ime, kraj, kraji)
        if razdalja0 is not None and 0 < razdalja0 <= domet:
            seznam += [kraj]
    return seznam


def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    naj_kraj = None
    for kraj in imena:
        razdalja0 = razdalja(ime, kraj, kraji)
        if razdalja0 > naj_razdalja:
            naj_razdalja = razdalja0
            naj_kraj = kraj
    return naj_kraj


def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)


"""
#JAO SEJ ŽE VSE MAM
def zalijemo(ime, domet, kraji):
    for kraj, _, _ in kraji:
        razdalja0 = razdalja(ime, kraj, kraji)
        naj_razdalja = 0
        if razdalja0 is not None and naj_razdalja < razdalja0 <= domet:
            
    return
"""

def presek(s1, s2):
    presek = []
    for element in s1:
        if element in s2:
            presek += [element]
    return presek


def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))

#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#very beautiful

