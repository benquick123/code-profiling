from math import *

# Ogrevalna naloga
def koordinate(ime, kraji):
    koncna = None
    for kraj,x,y in kraji:
        if kraj == ime:
            koncna = (x,y)
    return koncna

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def razdalja(ime1, ime2, kraji):
    kraj1 = koordinate(ime1,kraji)
    kraj2 = koordinate(ime2,kraji)
    return razdalja_koordinat(kraj1[1],kraj1[0],kraj2[1],kraj2[0])

# Obvezna naloga
def v_dometu(ime, domet, kraji):
    zaliti = []
    x0 = koordinate(ime,kraji)[0]
    y0 = koordinate(ime,kraji)[1]
    naj_razdalja = 0
    for ime, x, y in kraji:
        razdalja = sqrt((x - x0) ** 2 + (y - y0) ** 2)
        if naj_razdalja < razdalja <= domet:
            zaliti.append(ime)
    return zaliti

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    naj_kraj = ""
    for i in imena:
        if naj_razdalja < razdalja(ime,i,kraji):
            naj_razdalja = razdalja(ime,i,kraji)
            naj_kraj = i
    return naj_kraj

def zalijemo(ime, domet, kraji):
    krajii = v_dometu(ime,domet,kraji)
    return najbolj_oddaljeni(ime,krajii,kraji)

# Dodatna naloga
def presek(s1, s2):
    return list(set(s1) & set(s2))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    vsi_kraji = []
    ko1 = koordinate(ime1,kraji)
    ko2 = koordinate(ime2,kraji)
    for ime, x, y in kraji:
        if sqrt((x - ko1[0]) ** 2 + (y - ko1[1]) ** 2) < domet and sqrt((x - ko2[0]) ** 2 + (y - ko2[1]) ** 2) < domet:
            vsi_kraji.append(ime)
    return vsi_kraji