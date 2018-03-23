# Tu pišite svoje funkcije:
from math import *

def koordinate(ime, kraji):
    for (mesto, x0, y0) in kraji:
        if ime == mesto:
            return x0, y0
####################################################
def razdalja_koordinat(x1, y1, x2, y2):
    raz = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return raz
#####################################################
def razdalja(ime1, ime2, kraji):
    im1 = koordinate(ime1, kraji)
    im2 = koordinate(ime2, kraji)
    razd = razdalja_koordinat(im1[0], im1[1], im2[0], im2[1])
    return razd
#####################################################
def v_dometu(ime, domet, kraji):
    kr = []
    ms = koordinate(ime, kraji)
    for (city, x2, y2) in kraji:
        razda = razdalja_koordinat(ms[0], ms[1], x2, y2)
        if razda <= domet:
            naj_kraj = city
            kr.append(naj_kraj)
            if city == ime:
                kr.remove(ime)
    return kr
######################################################
def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for ime, x, y in kraji:
        razdalja = sqrt(x ** 2 + y ** 2)
        if razdalja > naj_razdalja and ime == ime in imena:
            naj_razdalja = razdalja
            naj_kraj = ime
    return naj_kraj
#######################################################
def zalijemo(ime, domet, kraji):
    for mesto, x0, y0 in kraji:
        if mesto == ime:
            break
        naj_razdalja = 0
    for ime, x, y in kraji:
        razdalja = razdalja_koordinat(x0, y0, x , y)
        if naj_razdalja < razdalja <= domet:
            naj_razdalja = razdalja
            naj_kraj = ime
    return naj_kraj
######################################################
def presek(s1, s2):
    s3 = []
    for stevilo in s1:
        if stevilo == stevilo in s2:
            s3.append(stevilo)
    return s3
######################################################
def skupno_zalivanje(ime1, ime2, domet, kraji):
    sez_kraj = []
    for ime, x1, y1 in kraji:
        if ime == ime1:
            x11 = x1
            y11 = y1
    for ime, x2, y2 in kraji:
        if ime == ime2:
            x22 = x2
            y22 = y2
    for ime, x, y in kraji:
        if sqrt((x - x11) ** 2 + (y - y11) ** 2) < domet and sqrt((x - x22) ** 2 + (y - y22) ** 2) < domet:
            sez_kraj.append(ime)
    return sez_kraj
######################################################

