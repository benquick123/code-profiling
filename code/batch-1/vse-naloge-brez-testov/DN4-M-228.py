# Tu pišite svoje funkcije:

### Ogrevalne naloge ###

def koordinate(ime, kraji):
    koordinate = None
    for kraj, x0, y0 in kraji:
        if kraj == ime:
            koordinate = (x0, y0)
    return koordinate

def razdalja_koordinat(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def razdalja(ime1, ime2, kraji):
    koordinate1, koordinate2 = koordinate(ime1, kraji), koordinate(ime2, kraji)
    return razdalja_koordinat(*koordinate1, *koordinate2)

### Obvezne naloge ###

def v_dometu(ime, domet, kraji):
    v_dometu = []
    for kraj, x, y in kraji:
        if 0 < razdalja(ime, kraj, kraji) <= domet:
            v_dometu.append(kraj)
    return v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    najbolj_oddaljeni = ""
    naj_razdalja = 0
    for imena in imena:
        if razdalja(ime, imena, kraji) > naj_razdalja:
            naj_razdalja = razdalja(ime, imena, kraji)
            najbolj_oddaljeni = imena
    return najbolj_oddaljeni

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)

### Dodatne naloge ###

def presek(s1, s2):
    presek = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                presek.append(e2)
    return presek

def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))

### Testi ###

