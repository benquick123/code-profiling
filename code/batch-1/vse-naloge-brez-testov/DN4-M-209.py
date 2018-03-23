# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    x = 0
    y = 0
    for kraj in kraji:
        t_ime, t_x, t_y = kraj
        if (t_ime == ime):
            x = t_x
            y = t_y
            return x, y
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2,kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    kraji_v_dometu = []
    for kraj in kraji:
        t_ime, t_x, t_y = kraj
        r = razdalja(ime,t_ime,kraji)
        if (r <= domet and ime != t_ime):
            kraji_v_dometu += [t_ime]
    return kraji_v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    naj_oddaljen_kraj = ""
    naj_razdalja = -1
    for kraj in kraji:
        t_ime, t_x, t_y = kraj
        if t_ime in imena:
            r = razdalja(ime,t_ime,kraji)
            if r > naj_razdalja:
                naj_razdalja = r
                naj_oddaljen_kraj = t_ime
    return naj_oddaljen_kraj

def zalijemo(ime, domet, kraji):
    naj_oddaljen_kraj = ""
    naj_razdalja = -1
    for kraj in kraji:
        t_ime, t_x, t_y = kraj
        r = razdalja(ime,t_ime,kraji)
        if r > naj_razdalja and r <= domet:
            naj_razdalja = r
            naj_oddaljen_kraj = t_ime
    return naj_oddaljen_kraj

def presek(s1, s2):
    s3 = []
    for e in s1:
        if e in s2:
            s3 += [e]
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1,domet,kraji)
    s2 = v_dometu(ime2,domet,kraji)
    return presek(s1,s2)
#OK


