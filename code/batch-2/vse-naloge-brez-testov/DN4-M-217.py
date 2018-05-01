from math import *

# ponesreči, sem prvič oddal, samo ogrevalne naloge. Se opravičujem za napako in zapravljanje vašega časa.

# Ogrevalne naloge
def koordinate(ime,kraji):
    for imeKraja, x, y in kraji:
        if ime == imeKraja:
            return x,y


def razdalja_koordinat(x1, y1, x2, y2):
        return sqrt((x2 - x1) ** 2 + (y2 - y1)**2)


def razdalja(ime1, ime2, kraji):
    x1,y1 = koordinate(ime1,kraji)
    x2,y2 = koordinate(ime2,kraji)

    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime,domet,kraji):
    s = []
    for imeSeznam,x,y in kraji:
        raz = razdalja(ime,imeSeznam,kraji)
        if raz != 0 and raz<=domet:
            s.append(imeSeznam)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    najdlje = 0
    for imeImena in imena:
        raz = razdalja(ime,imeImena,kraji)
        if najdlje < raz:
            najdlje = raz
            najdljeMesto = imeImena
    return najdljeMesto


def zalijemo(ime,domet,kraji):
    kraji_v_dometu = v_dometu(ime,domet,kraji)
    return najbolj_oddaljeni(ime,kraji_v_dometu,kraji)

def presek(s1,s2):
    vrni = []
    for ime in s1:
        for ime1 in s2:
            if ime == ime1:
                vrni.append(ime)
    return vrni

def skupno_zalivanje(ime1, ime2, domet, kraji):
    prvi_kraj_seznam = v_dometu(ime1,domet,kraji)
    drugi_kraj_seznam = v_dometu(ime2,domet,kraji)
    return presek(prvi_kraj_seznam,drugi_kraj_seznam)

