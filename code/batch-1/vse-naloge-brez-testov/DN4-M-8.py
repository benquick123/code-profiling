from math import *
def koordinate(ime, kraji):
    for kraj, kor_x, kor_y in kraji:
        if kraj == ime:
            return (kor_x,kor_y)


def razdalja_koordinat(x1, y1, x2, y2):
    return (sqrt(((x2-x1)**2) + ((y2-y1)**2)))

def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1, kraji)
    x2,y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):
    seznam_v_dometu = []
    for kraj, kor_x, kor_y in kraji:
        if razdalja(ime,kraj,kraji) <= domet and kraj != ime:
            seznam_v_dometu.append(kraj)
    return seznam_v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    seznam = []
    for kraj in imena:
        for mesto, kor_x, kor_y in kraji:
            if mesto == kraj:
                seznam.append([mesto,kor_x,kor_y])
    najdaljsa = 0
    for trenutni in seznam:
        if razdalja(ime,trenutni[0],kraji) > najdaljsa:
            najdaljsa = razdalja(ime,trenutni[0],kraji)
            kraj = trenutni[0]
    return kraj

def zalijemo(ime, domet, kraji):
    seznam = v_dometu(ime, domet, kraji)
    najbolj_oddaljen = 0
    for kraj in seznam:
        if razdalja(ime, kraj, kraji) > najbolj_oddaljen:
            najbolj_oddaljen = razdalja(ime, kraj, kraji)
            ime_naj = kraj
    return ime_naj

def presek(s1, s2):
    s3 = []
    for i in s1:
        for j in s2:
            if j == i and j not in s3:
                s3.append(j)
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    kraj1 = v_dometu(ime1, domet, kraji)
    kraj2 = v_dometu(ime2, domet, kraji)
    skupni = presek(kraj1, kraj2)
    return skupni














