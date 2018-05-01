from math import sqrt

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime :
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 =koordinate(ime1, kraji)
    x2, y2 =koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)


def v_dometu(ime, domet, kraji):
    s=[]
    for kraj, x1, y1 in kraji:
        if razdalja(ime, kraj, kraji) <= domet and ime != kraj:
            s.append(kraj)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    naj_kraj = ''
    naj_razd = 0
    for kraj in imena:
        i =razdalja(ime, kraj, kraji)
        if i > naj_razd:
            naj_kraj = kraj
            naj_razd = i
    return naj_kraj

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji )

def presek(s1, s2):
    return [x for x in s1 if x in s2 ]

def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))






