# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
        for a, x, y in kraji:
            if a == ime:
                print(ime, x, y)
                return(x,y)


def razdalja_koordinat(x1, y1, x2, y2):
        raz = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
        return raz

def razdalja(ime1,ime2,kraji):
        x1,y1 = koordinate(ime1, kraji)
        x2,y2 = koordinate(ime2, kraji)
        raz=razdalja_koordinat(x1,y1,x2,y2)
        return raz



def v_dometu(ime, domet, kraji):
    k = []
    for a, x, y in kraji:
        if a == ime:
            x1 = x
            y1 = y
    for a, x, y in kraji:
        raz = sqrt(pow(x1 - x, 2) + pow(y1 - y, 2))
        # print(raz)
        if raz<=domet and a!=ime:
            k.append(a)
    print(k)
    return k



def najbolj_oddaljeni(ime, imena, kraji):
    for a,x,y in kraji:
        if a==ime:
            x1=x
            y1=y
    naj_kraj=""
    naj=0
    for a in imena:
        for s,x,y in kraji:
            if a==s:
             x2=x
             y2=y
        raz = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        if raz > naj:
            naj=raz
            naj_kraj=a
    print(naj_kraj)
    return naj_kraj

def zalijemo(ime, domet, kraji):
    naj_kraj=""
    naj=0
    for a, x, y in kraji:
        if a == ime:
            x1 = x
            y1 = y
    for a, x, y in kraji:
        raz = sqrt(pow(x1 - x, 2) + pow(y1 - y, 2))
        if raz > naj and raz <= domet:
            naj=raz
            naj_kraj=a
    print(naj_kraj)
    return naj_kraj



def presek(s1,s2):
    sez= []
    for a in s1:
        for b in s2:
            if a==b:
                sez.append(a)

    print(sez)
    return sez



def skupno_zalivanje(ime1,ime2,domet,kraji):
    sez= []
    x1,y1 = koordinate(ime1, kraji)
    x2,y2 = koordinate(ime2, kraji)
    for ime, x, y in kraji:
        if ime != ime1 and ime != ime2:
            raz1 = razdalja_koordinat(x,y,x1,y1)
            if raz1 <= domet:
                raz2=razdalja_koordinat(x,y,x2,y2)
                if raz2<= domet:
                    sez.append(ime)
                    print(sez)
    print(sez)
    return sez







