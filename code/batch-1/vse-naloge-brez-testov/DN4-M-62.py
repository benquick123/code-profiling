# Tu pišite svoje funkcije:

from math import sqrt

def koordinate(ime, kraji):
    for kraj in kraji:
        if(kraj[0] == ime):
            return kraj[1], kraj[2]
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja_x = abs(x1 - x2)
    razdalja_y = abs(y1 - y2)
    razdalja = sqrt(razdalja_x ** 2 + razdalja_y ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    kraj1 = koordinate(ime1, kraji)
    kraj2 = koordinate(ime2, kraji)
    razdalja = razdalja_koordinat(kraj1[0], kraj1[1], kraj2[0], kraj2[1])
    return razdalja

def v_dometu(ime, domet, kraji):
    seznam_krajev = []
    kraj_x, kraj_y = koordinate(ime, kraji)
    for kraj in kraji:
        if(ime == kraj[0]):
            continue
        razdalja = razdalja_koordinat(kraj_x, kraj_y, kraj[1], kraj[2])
        if(razdalja <= domet):
            seznam_krajev.append(kraj[0])
    return seznam_krajev

def najbolj_oddaljeni(ime, imena, kraji):
    naj_oddaljen = None
    naj_razdalja = 0
    kraj_x, kraj_y = koordinate(ime, kraji)
    for kraj in kraji:
        if(kraj[0] in imena):
            razdalja = razdalja_koordinat(kraj_x, kraj_y, kraj[1], kraj[2])
            if(razdalja >= naj_razdalja):
                naj_oddaljen = kraj[0]
                naj_razdalja = razdalja
    return naj_oddaljen

def zalijemo(ime, domet, kraji):
    kraji_v_dometu = v_dometu(ime, domet, kraji)
    naj_oddaljeni = najbolj_oddaljeni(ime, kraji_v_dometu, kraji)
    return naj_oddaljeni

def presek(s1, s2):
    return list(set(s1).intersection(s2))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    v_dometu_1 = v_dometu(ime1, domet, kraji)
    v_dometu_2 = v_dometu(ime2, domet, kraji)
    return presek(v_dometu_1, v_dometu_2)


