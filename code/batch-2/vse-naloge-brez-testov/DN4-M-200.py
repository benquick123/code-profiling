from math import *

def koordinate(ime, kraji):
    if kraji:
        for mesto, x_kor, y_kor in kraji:
            if mesto == ime:
                return (x_kor, y_kor)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    return abs(sqrt((x2 - x1)**2 + (y2 - y1)**2))

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    seznam_krajev_v_dometu = []
    x1, y1 = koordinate(ime, kraji)
    for do_mesta, x2, y2 in kraji:
        if do_mesta == ime:
            continue
        elif razdalja(ime, do_mesta, kraji) <= domet:
            seznam_krajev_v_dometu.append(do_mesta)
    return seznam_krajev_v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    najbolj_oddaljeno_mesto = ''
    naj_razdalja = 0
    for mesto_iz_seznama in imena:
        razdalja_izmed_mest = razdalja(ime, mesto_iz_seznama, kraji)
        if razdalja_izmed_mest > naj_razdalja:
            naj_razdalja = razdalja_izmed_mest
            najbolj_oddaljeno_mesto = mesto_iz_seznama
    return najbolj_oddaljeno_mesto

def zalijemo(ime, domet, kraji):
    naj_razdalja = 0
    naj_kraj = ''
    for mesto, x2, y2 in kraji:
        razdalja_izmed_mest = razdalja(ime, mesto, kraji)
        if naj_razdalja < razdalja_izmed_mest <= domet:
            naj_razdalja = razdalja_izmed_mest
            naj_kraj = mesto
    return naj_kraj

def presek(s1, s2):
    return list(set(s1) & set(s2))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))


