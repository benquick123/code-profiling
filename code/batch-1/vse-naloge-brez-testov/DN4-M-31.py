# Tu pišite svoje funkcije:
from math import sqrt
def koordinate(ime, kraji):
    for ime_kraja,x,y in kraji:
        if(ime_kraja == ime):
            return (x,y)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1,kraji)
    x2,y2 = koordinate(ime2,kraji)

    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):
    s = []
    for ime_k,x,y in kraji:
        if(ime_k != ime):
            if razdalja(ime_k, ime, kraji) <= domet:
                s.append(ime_k)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for ime_k in imena:
        if razdalja(ime, ime_k, kraji) > naj_razdalja:
            naj_razdalja = razdalja(ime, ime_k, kraji)
            naj_mesto = ime_k
    return naj_mesto

def zalijemo(ime, domet, kraji):
    kraji_v_dometu = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, kraji_v_dometu, kraji)

def presek(s1, s2):
    seznam_skupen = []
    for seznam1 in s1:
        for seznam2 in s2:
            if seznam1 == seznam2:
                seznam_skupen.append(seznam2)
    return seznam_skupen

def skupno_zalivanje(ime1,ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return presek(s1, s2)
