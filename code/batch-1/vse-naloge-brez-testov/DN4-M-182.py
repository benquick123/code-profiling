# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for mesto ,x , y in kraji:
        if (ime== mesto):
            return x,y
    return None
def razdalja_koordinat(x1, y1, x2, y2):
    dolzina_medkraji=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    return dolzina_medkraji
def razdalja(ime1, ime2, kraji):
    x1,y1=koordinate(ime1,kraji)
    x2,y2=koordinate(ime2,kraji)
    razdalja_dometa=razdalja_koordinat(x1, y1, x2, y2)
    return razdalja_dometa
def v_dometu(ime, domet, kraji):
    seznam_mest=[]
    x1 = 0
    y1 = 0
    for mesto, x2, y2 in kraji:
        if (mesto == ime):
            x1 = x2
            y1 = y2
    for mesto, x2, y2 in kraji:
        dolzina = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        if (dolzina <= domet):
            if (dolzina == 0):
                None
            else:
                seznam_mest.append(mesto)
    return seznam_mest
def najbolj_oddaljeni(ime, imena, kraji):
    maksimum = 0
    x1,y1 = koordinate(ime,kraji)
    for kraj in imena:
        for mesta,x2,y2 in kraji:
            if kraj == mesta:
                dolzina = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
                if dolzina>maksimum:
                    maksimum=dolzina
                    maksimalna_dolzina=kraj
    return maksimalna_dolzina

def zalijemo(ime, domet, kraji):
    maksimum = 0
    x1,y1 = koordinate(ime,kraji)
    for mesta, x2, y2 in kraji:
        dolzina = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        if dolzina > maksimum:
            if dolzina<=domet:
                maksimum = dolzina
                maksimalna_dolzina = mesta
    return maksimalna_dolzina

