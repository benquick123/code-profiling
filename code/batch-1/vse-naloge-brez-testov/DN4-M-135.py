from math import *

#Ogrevalna naloga:

def koordinate(ime, kraji):
    for mesto, x,y in kraji:
        if ime == mesto:
            terka = (x, y)
            return terka
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    raz = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return raz

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2,y2 = koordinate(ime2,kraji)
    izracun = razdalja_koordinat(x1,y1,x2,y2)
    return izracun

#Obvezna naloga:

def v_dometu(ime, domet, kraji):
    sez = []
    zadnji_domet = 0
    for mesto, x2,y2 in kraji:
        if mesto != ime:
            raz = razdalja(ime,mesto,kraji)
            if raz <= domet:
                zadnji_domet = raz
                sez.append(mesto)
    return sez

def najbolj_oddaljeni(ime, imena, kraji):
    naj_domet = 0
    lokacija = None
    for mesto,x2,y2 in kraji:
        if mesto in imena:
            raz = razdalja(ime,mesto,kraji)

            if raz > naj_domet:
                naj_domet = raz
                lokacija = mesto
    return lokacija

def zalijemo(ime, domet, kraji):
    naj_kraj = None
    zadnji_domet = 0
    for mesto, x2, y2 in kraji:
        if mesto != ime:
            raz = razdalja(ime, mesto, kraji)
            if raz <= domet:
                if raz >= zadnji_domet:
                    zadnji_domet = raz
                    naj_kraj = mesto
    return naj_kraj


def presek(s1, s2):
    a = set(s1)
    b = set(s2)
    k = a & b
    sez = []
    for i in k:
        sez.append(i)
    return sez

def skupno_zalivanje(ime1, ime2, domet, kraji):
    prvi = v_dometu(ime1,domet, kraji)
    drugi = v_dometu(ime2,domet,kraji)
    rez = presek(prvi,drugi)
    return rez




