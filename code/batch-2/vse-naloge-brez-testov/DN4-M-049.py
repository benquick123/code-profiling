from math import *

def koordinate(ime, kraji):
    for mesto, x, y in kraji:
        if mesto == ime:
            return x, y

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    prvi = koordinate(ime1, kraji)
    drugi = koordinate(ime2, kraji)

    x1, y1 = prvi
    x2, y2 = drugi
    return (razdalja_koordinat(x1, y1, x2, y2))
def v_dometu(ime, domet, kraji):
    mesto1 = koordinate(ime, kraji)
    x1, y1 = mesto1

    s = []
    for mesto2, x2, y2 in kraji:
        if mesto2 != ime and razdalja_koordinat(x1, y1, x2, y2) <= domet:
            s.append(mesto2)
    return(s)

def najbolj_oddaljeni(ime, imena, kraji):
    mesto1 = koordinate(ime, kraji)
    x1, y1 = mesto1

    naj_razdalja = 0
    naj_kraj = ""

    for imeKraja in imena:
        for mesto, x2, y2 in kraji:
            if imeKraja == mesto:
                if naj_razdalja < razdalja_koordinat(x1, y1, x2, y2):
                    naj_razdalja = razdalja_koordinat(x1, y1, x2, y2)
                    naj_kraj = imeKraja

    return naj_kraj

def zalijemo(ime, domet, kraji):
    mesto1 = koordinate(ime, kraji)
    x1, y1 = mesto1

    naj_razdalja = 0
    naj_kraj = ""

    for mesto, x2, y2 in kraji:
        if naj_razdalja < razdalja_koordinat(x1, y1, x2, y2) and razdalja_koordinat(x1, y1, x2, y2) < domet:
            naj_razdalja = razdalja_koordinat(x1, y1, x2, y2)
            naj_kraj = mesto

    return naj_kraj

def presek(s1, s2):
    return list(set(s1) & set(s2))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    prvi = koordinate(ime1, kraji)
    drugi = koordinate(ime2, kraji)

    return list(set(v_dometu(ime1, domet, kraji)) & set(v_dometu(ime2, domet, kraji)))



