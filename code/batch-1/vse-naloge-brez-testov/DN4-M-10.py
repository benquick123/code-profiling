# Tu pišite svoje funkcije:
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if(ime==kraj):
            return (x,y)

from math import*
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja=sqrt((x2-x1)**2 + (y2-y1)**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    a,b=koordinate(ime1,kraji)
    c,d=koordinate(ime2, kraji)
    r=razdalja_koordinat(a,b,c,d)
    return r

def v_dometu(ime, domet, kraji):
    seznam=[]
    for k,x,y in kraji:
        if k!=ime:
            rk=razdalja(k, ime, kraji)
            if (rk<=domet):
                seznam.append(k)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    najK=""
    najS=0
    for i in imena:
        r=razdalja(ime, i, kraji)
        if r>najS:
            najS=r
            najK=i
    return najK

def zalijemo(ime, domet, kraji):
    s=v_dometu(ime,domet, kraji)
    naj=najbolj_oddaljeni(ime, s, kraji)
    return naj


