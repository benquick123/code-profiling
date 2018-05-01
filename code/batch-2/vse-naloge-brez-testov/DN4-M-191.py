__author__ = 'Haris'

from math import *

def koordinate(ime,kraji):
    for kraj,x,y in kraji:
        if ime==kraj:
            return x,y

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

def razdalja(ime1, ime2, kraji):
    (x1,y1)=koordinate(ime1,kraji)
    (x2,y2)=koordinate(ime2,kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    seznam=[]
    (x1,y1)=koordinate(ime,kraji)
    for kraj,x2,y2 in kraji:
        if ime != kraj and razdalja_koordinat(x1, y1, x2, y2) <= domet:
            seznam.append(kraj)
    return seznam

"""
def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = test_razdalja = 0
    naj_kraj=""
    (x1,y1)=koordinate(ime,kraji)
    for kraj in imena:
        for kraj,x2,y2 in kraji:
            if k == kraj:
                test_razdalja=razdalja_koordinat(x1, y1, x2, y2)
                if test_razdalja>naj_razdalja:
                    naj_razdalja=test_razdalja
                    naj_kraj=kraj
    return naj_kraj
"""

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = test_razdalja = 0
    naj_kraj=""
    (x1,y1)=koordinate(ime,kraji)
    for kraj,x2,y2 in kraji:
        if kraj in imena:
            test_razdalja=razdalja_koordinat(x1, y1, x2, y2)
            if test_razdalja>naj_razdalja:
                naj_razdalja=test_razdalja
                naj_kraj=kraj
    return naj_kraj

def zalijemo(ime, domet, kraji):
    (x1,y1)=koordinate(ime,kraji)
    naj_razdalja=test_razdalja=0
    naj_kraj=""
    for kraj,x2,y2 in kraji:
        test_razdalja=razdalja_koordinat(x1, y1, x2, y2)
        if test_razdalja<=domet and test_razdalja>naj_razdalja:
            naj_razdalja=test_razdalja
            naj_kraj=kraj
    return naj_kraj

def presek(s1,s2):
    seznam=[]
    for element in s1:
        if element in s2:
            seznam.append(element)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam=[]
    (x1,y1)=koordinate(ime1,kraji)
    (x3,y3)=koordinate(ime2,kraji)
    for kraj,x2,y2 in kraji:
        if razdalja_koordinat(x1, y1, x2, y2)<=domet and razdalja_koordinat(x3, y3, x2, y2)<=domet:
            seznam.append(kraj)
    return seznam



