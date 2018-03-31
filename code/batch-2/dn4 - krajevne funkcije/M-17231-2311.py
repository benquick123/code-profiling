from math import *

def koordinate(ime, kraji):
    for kraj,x,y in kraji:
        if ime == kraj:
            return x,y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1, kraji)
    x2,y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    good_kraji = []
    x1,y1 = koordinate(ime, kraji)
    for kraj,x2,y2 in kraji:
        if ime == kraj: continue
        if razdalja_koordinat(x1, y1, x2, y2) <= domet:
            good_kraji.append(kraj)
    return good_kraji

def najbolj_oddaljeni(ime, imena, kraji):
    naj_kraj = ime
    naj_raz = 0
    for kraj in imena:
        if ime == kraj: continue
        raz = razdalja(ime, kraj, kraji)
        if raz > naj_raz:
            naj_kraj = kraj
            naj_raz = raz
    return naj_kraj

def zalijemo(ime, domet, kraji):
    naj_kraj = ime
    naj_raz = 0
    x1,y1 = koordinate(ime, kraji)
    for kraj,x2,y2 in kraji:
        if ime == kraj: continue
        raz = razdalja_koordinat(x1, y1, x2, y2)
        if raz <= domet and raz > naj_raz:
            naj_kraj = kraj
            naj_raz = raz
    return naj_kraj

def presek(s1, s2):
    oba = []
    for s in s1:
        if s in s2:
            oba.append(s)
    return oba

def skupno_zalivanje(ime1, ime2, domet, kraji):
    oba_kraji = []
    x1,y1 = koordinate(ime1, kraji)
    x2,y2 = koordinate(ime2, kraji)
    for ime,x,y in kraji:
        raz1 = razdalja_koordinat(x1, y1, x, y)
        raz2 = razdalja_koordinat(x2, y2, x, y)
        if raz1 <= domet and raz2 <= domet:
            oba_kraji.append(ime)
    return oba_kraji