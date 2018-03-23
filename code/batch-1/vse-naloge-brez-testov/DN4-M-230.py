# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            vrni = (x,y)
            break
    else:
        vrni = None
    return vrni

def razdalja_koordinat(x1, y1, x2, y2):
    razd = sqrt((x2-x1)**2 + (y2-y1)**2)
    return razd

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razd = razdalja_koordinat(x1, y1, x2, y2)
    return razd

def v_dometu(ime, domet, kraji):
    seznam = []
    for ime2, x, y in kraji:
        if ime2 != ime:
            razd = razdalja(ime,ime2, kraji)
            if razd <= int(domet):
                seznam.append(ime2)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    najdalsar = 0 # najdalša razdalja enota 0 razdalja nemore biti negativna
    for ime2 in imena:
        razd = razdalja(ime, ime2, kraji)
        if razd > najdalsar:
            najdalsar = razd # najdaljša razdalja
            najdalsik = ime2 # najdaljši kraj
    return najdalsik        

def zalijemo(ime, domet, kraji):
    najdalsar = 0
    for ime2, _, _ in kraji:
        razd = razdalja(ime, ime2, kraji)
        if najdalsar < razd <= domet:
            najdalsar = razd
            najdalsik = ime2
    return najdalsik

def presek(s1,s2):
    s3 = list(set(s1) & set(s2))
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    for ime3, _, _ in kraji:
        razdalja1 = razdalja(ime3, ime1, kraji)
        razdalja2 = razdalja(ime3, ime2, kraji)
        if razdalja1 <= domet and razdalja2 <= domet:
            seznam.append(ime3)
    return seznam

