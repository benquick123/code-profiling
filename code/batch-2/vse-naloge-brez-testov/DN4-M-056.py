from math import *
# Tu pišite svoje funkcije:
### OGREVALNI DEL
# prva naloga
def koordinate(ime, kraji):
    i = 0
    for im,x,y in kraji:
        if im == ime:
            i = 1
            terka = (x,y)
    if i == 1:
        return(terka)
    else:
        return None
#druga naloga:
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return razdalja
#tretja naloga:
def razdalja(ime1,ime2,kraji):
    ko1 = koordinate(ime1, kraji)
    ko2 = koordinate(ime2, kraji)
    r = razdalja_koordinat(ko1[0], ko1[1],ko2[0], ko2[1])
                
    return r
#OBVEZNI DEL:
#prva:
def v_dometu(ime, domet, kraji):
    sez = []
    for ime2,x,y in kraji:
        if ime2 != ime:
            r = razdalja(ime, ime2, kraji)
            if r <= domet:
                sez.append(ime2)
    return(sez)
#druga:
def najbolj_oddaljeni(ime, imena, kraji):
    i = 0
    maks = 0
    for ime2 in imena:
        a = razdalja(ime,ime2,kraji)
        if a > i:
            i = a
            maks = ime2
    return(maks)
#tretja:
def zalijemo(ime, domet, kraji):
    i = 0
    maks = 0
    for ime2,x,y in kraji:
        a = razdalja(ime, ime2, kraji)
        if a > i and a < domet:
            i = a
            maks = ime2
    return (maks)
#DODATNA:
def presek(s1, s2):
    sez = []
    for i in s1:
        for k in s2:
            if k == i:
                sez.append(k)
    return(sez)
def skupno_zalivanje(ime1, ime2, domet, kraji):
    sez = []
    ko1 = koordinate(ime1, kraji)
    ko2 = koordinate(ime2, kraji)
    r = razdalja_koordinat(ko1[0], ko1[1], ko2[0], ko2[1])
    for im,x,y in kraji:
        r1 = razdalja_koordinat(ko1[0], ko1[1], x, y)
        r2 = razdalja_koordinat(ko2[0], ko2[1], x, y)
        if r1 <= domet and r2 <= domet:
            sez.append(im)
    return(sez)

