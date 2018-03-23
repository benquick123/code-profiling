import math

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    d = []
    for kraj, x, y in kraji:
        if kraj == ime:
            continue
        if razdalja(ime, kraj, kraji) <= domet:
            d.append(kraj)
    return d

def najbolj_oddaljeni(ime, imena, kraji):
    naj = 0
    for i in imena:
        r = razdalja(i, ime, kraji)
        if r > naj:
            naj_ime = i
            naj = r
    return naj_ime

def zalijemo(ime, domet, kraji):
    naj = 0
    for kraj, x, y in kraji:
        r = razdalja(ime, kraj, kraji)
        if  r <= domet and r > naj:
            naj = r
            naj_ime = kraj
    return naj_ime

def presek(s1, s2):
    s = []
    for a in s1:
        for b in s2:
            if a == b:
                s.append(a)
    return s

def zal(ime, domet, kraji):
    k = []
    for kraj, x, y in kraji:
        if razdalja(ime, kraj, kraji) <= domet:
            k.append(kraj)
    return k

def skupno_zalivanje(ime1, ime2, domet, kraji):
    k1 = zal(ime1, domet, kraji)
    k2 = zal(ime2, domet, kraji)
    return presek(k1, k2)

# Tu pišite svoje funkcije:




