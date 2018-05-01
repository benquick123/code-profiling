# Tu pišite svoje funkcije:
from math import*

def koordinate(ime, kraji):
    for terka in kraji:
        mesto, x, y=terka
        if ime==mesto:
            return (x, y)


def razdalja_koordinat(x1, y1, x2, y2):
        a=sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2)
        return a

def razdalja(ime1, ime2, kraji):
    for mesto, x, y in kraji:
        x1,y1=koordinate(ime1, kraji)
        x2, y2=koordinate(ime2, kraji)
        a=razdalja_koordinat(x1, y1, x2, y2)
        return a

def v_dometu(ime, domet, kraji):
    a=[]
    for mesto, x, y in kraji:
        x1, y1 = koordinate(ime, kraji)
        razdalja = sqrt(((x - x1) ** 2) + (y - y1) ** 2)
        if domet >= razdalja and ime!=mesto:
            a.append(mesto)
    return a

def najbolj_oddaljeni(ime, imena, kraji):
    a=0
    vas=0
    b=0
    x1, y1 = koordinate(ime, kraji)
    for kraj in imena:
        for mesto, x, y in kraji:
            if mesto==kraj:
                razdalja = sqrt(((x - x1) ** 2) + (y - y1) ** 2)
                if razdalja>b:
                    b=razdalja
                    vas=kraj
    return vas

def zalijemo(ime, domet, kraji):
    a=0
    for mesto, x, y in kraji:
        x1, y1 = koordinate(ime, kraji)
        razdalja = sqrt(((x - x1) ** 2) + (y - y1) ** 2)
        if domet >= razdalja:
            if razdalja>a:
                a=razdalja
                vas=mesto
    return vas

def presek(s1, s2):
    x=[]
    for a in s1:
        for b in s2:
            if a==b:
                x.append(a)
    return x

def skupno_zalivanje(ime1, ime2, domet, kraji):
    a = []
    for mesto, x, y in kraji:
        x1, y1 = koordinate(ime1, kraji)
        razdalja = sqrt(((x - x1) ** 2) + (y - y1) ** 2)
        if razdalja <= domet:
            mesto1 = mesto
            x2, y2 = koordinate(ime2, kraji)
            razdalja1 = sqrt(((x - x2) ** 2) + (y - y2) ** 2)
            if razdalja1 <= domet:
                mesto2 = mesto
                if mesto1 == mesto2:
                    a.append(mesto1)
    return a

