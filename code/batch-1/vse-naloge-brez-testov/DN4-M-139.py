from math import *
# Tu pišite svoje funkcije:
def koordinate(ime,kraji):
    for kraj,x,y in kraji:
        if ime == kraj:
            k = (x,y)
            return k

def razdalja_koordinat(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2,kraji)

    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):
    vsi = []
    for kr in kraji:
        if ime == kr[0]:
            x, y = kr[1], kr[2]

    for kr2 in kraji:
        razdalja = sqrt((kr2[1] - x) ** 2 + (kr2[2] - y) ** 2)
        if razdalja <= domet and kr2[0] != ime:
            vsi.append(kr2[0])
    return vsi

def najbolj_oddaljeni(ime, imena, kraji):

    najvec = 0
    x,y = koordinate(ime,kraji)

    for ime in imena:
        for kr2 in kraji:
            if ime == kr2[0]:
                razdalja = razdalja_koordinat(x,y,kr2[1],kr2[2])
                if razdalja > najvec:
                    najvec = razdalja
                    kraj = kr2[0]

    return kraj

def zalijemo(ime, domet, kraji):
    vsi = v_dometu(ime,domet,kraji)

    kraj = najbolj_oddaljeni(ime,vsi,kraji)

    return kraj

