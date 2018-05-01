import math

def koordinate(ime, kraji):
    for a, x, y in kraji:
        if a == ime:
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)                        #razdalja = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(1/2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    c = razdalja_koordinat(x1, y1, x2, y2)
    return c

def v_dometu(ime, domet, kraji):
    dosezeni = []
    x1, y1 = koordinate(ime, kraji)
    for a, x, y in kraji:
        razdalja = razdalja_koordinat(x1, y1, x, y)
        if a != ime:
            if razdalja <= domet:
                dosezeni.append(a)
    return dosezeni

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    razdalja = 0
    x, y = koordinate(ime, kraji)
    a = ''
    for k in imena:
        x1, y1 = koordinate(k, kraji)
        razdalja = razdalja_koordinat(x, y, x1, y1)
        if naj_razdalja < razdalja:
            naj_razdalja = razdalja
            a = k
    return a

def zalijemo(ime, domet, kraji):
    a = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, a, kraji)

def presek(s1, s2):
    koncen = []
    for a in s1:
        for b in s2:
            if a == b:
                koncen.append(b)
    return koncen

def skupno_zalivanje(ime1, ime2, domet, kraji):
    prvi = v_dometu(ime1, domet, kraji)
    drugi = v_dometu(ime2, domet, kraji)
    return presek(prvi, drugi)



