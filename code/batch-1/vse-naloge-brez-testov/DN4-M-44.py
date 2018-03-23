from math import *

#OGREVALNE NALOGE

def koordinate(ime, kraji):
    for kraj, x , y in kraji:
        if kraj == ime:
            return kraj, x , y
        else:
            return None


def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja


def razdalja(ime1, ime2, kraji):
    for ime, x1, y1 in kraji:
        if ime == ime1:
            break
    for ime, x2, y2 in kraji:
        if ime == ime2:
            break
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja


#OBVEYNI DEL

def v_dometu(ime, domet, kraji):
    s = []
    for kraj, x1 ,y1 in kraji:
        if kraj == ime:
            break
    for kraj, x ,y in kraji:
        razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if 0 < razdalja <= domet:
            s.append(kraj)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    for kraj, x1 , y1 in kraji:
        if kraj == ime:
            break
    naj_razdalja = 0
    naj_ime = ""
    for kraj in imena:
        for kraj1, x , y in kraji:
            if kraj == kraj1:
                razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                if naj_razdalja < razdalja:
                    razdalja = naj_razdalja
                    kraj = naj_ime

    return naj_ime

def zalijemo(ime, domet, kraji):
    for kraj, x1, y1 in kraji:
        if kraj == ime:
            break
    naj_razdalja = 0
    naj_kraj = ""
    for kraj, x, y in kraji:
        razdalja = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if razdalja <= domet:
            if razdalja > naj_razdalja:
                razdalja = naj_razdalja
                kraj = naj_kraj

    return naj_kraj


#DODATNI DEL

def presek(s1, s2):
    s3 = []
    for element in s1:
        if element in s2:
            s3.append(element)

    return s3


def skupno_zalivanje(ime1, ime2, domet, kraji):
    for kraj, x1, y1 in kraji:
        if kraj == ime1
            break

    for kraj, x2, y2 in kraji:
        if kraj == ime2
            break

    s1 = []
    s2 = []
    s3 = []
    for kraj, x, y in kraji:
        razdalja_1 = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if razdalja_1 <= domet:
            s1.append(kraj)


    for kraj, x, y in kraji:
        razdalja_2 = sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
        if razdalja_2 <= domet:
            s2.append(kraj)


    for ime_kraja in s1:
        if ime_kraja in s2:
            s3.append(ime_kraja)

    return s3



































