# Tu pišite svoje funkcije:
from math import *


def koordinate (ime,kraji):
    for name,x,y in kraji:
        if name == ime:
            return (x,y)
    return


def razdalja_koordinat(x1,y1,x2,y2):
    razdalja = sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)
    return razdalja



def razdalja(ime1,ime2,kraji):
    kraj1 = koordinate(ime1,kraji)
    kraj2 = koordinate(ime2,kraji)
    x1,y1 = kraj1
    x2,y2 = kraj2
    razdalja_med_krajema = razdalja_koordinat(x1,y1,x2,y2)
    return razdalja_med_krajema




def v_dometu(ime,domet,kraji):
    kraji_v_dometu = []
    for name,x1,y1 in kraji:
        if name == ime:
            for name2,x,y in kraji:
                razdalja = sqrt(abs(x-x1)**2 + abs(y-y1)**2)
                if razdalja <= domet and name2!= ime:
                    kraji_v_dometu.append(name2)
    return kraji_v_dometu



def najbolj_oddaljeni(ime,imena,kraji):
    naj_razdalja = 0
    naj_kraj = ""
    for name,x1,y1 in kraji:
        if name == ime:
         for name2,x,y in kraji:
            for kraj in imena:
             if kraj == name2:
                    razdalja = sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2)
                    if razdalja> naj_razdalja:
                            naj_kraj = name2
    return naj_kraj



def zalijemo(ime,domet,kraji):
    naj_razdalja = 0
    naj_kraj = ""
    for kraj,x1,y1 in kraji:
        if ime == kraj:
            for name,x,y in kraji:
                razdalja = sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2)
                if razdalja> naj_razdalja and razdalja <= domet:
                    naj_razdalja = razdalja
                    naj_kraj = name
    return naj_kraj


def presek(s1,s2):
    ys = []
    for x in s1:
        for x1 in s2:
            if x == x1:
                ys.append(x1)
    return ys

def skupno_zalivanje(ime1,ime2,domet,kraji):
    skupni_kraji = []
    for kraj1,x,y in kraji:
        if kraj1 == ime1:
            x1 = x
            y1 = y
        if kraj1 == ime2:
            x2 = x
            y2 = y
    for name,x,y, in kraji:
                razdalja1 = sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2)
                razdalja2 = sqrt(abs(x - x2) ** 2 + abs(y - y2) ** 2)
                if razdalja1 <= domet and razdalja2<= domet:
                    skupni_kraji.append(name)
    return skupni_kraji




