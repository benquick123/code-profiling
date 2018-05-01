# Tu pišite svoje funkcije:

from math import*

def koordinate(ime, kraji):
    koordinate = None
    for kraj, x, y in kraji:
        if ime == kraj:
            koordinate = (x,y)
    return koordinate

def razdalja_koordinat(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1,y1,x2,y2)


def v_dometu(ime, domet, kraji):
    s = []
    x1,y1 = koordinate(ime, kraji)
    for kraj, x2, y2 in kraji:
         if domet >= razdalja_koordinat(x1,y1,x2,y2) > 0 :
            s.append(kraj)
    return s

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for kraj in imena:
        dolzina = razdalja(ime, kraj, kraji)
        if dolzina > naj_razdalja:
            naj_razdalja = dolzina
            naj_kraj = kraj
    return naj_kraj

def zalijemo(ime, domet, kraji):
    imena = v_dometu(ime, domet, kraji)
    return najbolj_oddaljeni(ime, imena, kraji)




