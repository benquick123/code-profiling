# Tu pišite svoje funkcije:
from math import *
# Tu pišite svoje funkcije:
#ogrevalne naloge
def koordinate(ime, kraji):
    for i,x,y in kraji:
        if i==ime:
            return x,y
    return None

def razdalja_koordinat(x1, y1,x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def razdalja(ime1, ime2, kraji):
    x1,y1 =koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    razdalja_krajev=razdalja_koordinat(x1,y1,x2,y2)
    return razdalja_krajev
#obvezni del
def v_dometu(ime,domet,kraji):
    seznam = []
    x1,y1=koordinate(ime,kraji)
    for i,x,y in kraji:
        if(razdalja_koordinat(x,y,x1,y1))<=domet:
            if ime != i:
                seznam.append(i)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    maxkraj= ""
    max=0
    xime,yime=koordinate(ime,kraji)
    for i in imena:
        for imekraja,x,y in kraji:
            dolzina = razdalja_koordinat(xime,yime,x,y)
            if i==imekraja and dolzina > max:
                max=dolzina
                maxkraj=i
    return maxkraj


def zalijemo(ime,domet,kraji):
    maxkraj = ""
    max = 0
    xime, yime = koordinate(ime, kraji)
    for imekraja,x,y in kraji:
        dolzina=razdalja_koordinat(xime,yime,x,y)
        if dolzina<domet:
            if dolzina>max:
                max=dolzina
                maxkraj=imekraja
    return maxkraj







