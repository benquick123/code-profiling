import math
def koordinate(ime, kraji):
    for y,x,z in kraji:
        if y == ime:
            return x, z
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1, = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    rezultat = razdalja_koordinat(x1, y1, x2, y2)
    return rezultat

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
    x, y =  koordinate(ime, kraji)
    c = ""
    for b in imena:
        x1, y1 = koordinate(b, kraji)
        razdalja = razdalja_koordinat(x, y, x1, y1)
        if naj_razdalja < razdalja:
            naj_razdalja = razdalja
            c = b
    return c

def zalijemo(ime, domet, kraji):
    a = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, a, kraji)




