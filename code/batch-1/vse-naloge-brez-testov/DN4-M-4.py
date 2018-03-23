# Tu pišite svoje funkcije:
from math import *
def koordinate(ime,kraji):
    for kraj,x,y in kraji:
        if(kraj == ime):
            return x, y

def razdalja_koordinat(x1,y1,x2,y2):
    return(sqrt(pow(x1-x2,2)+pow(y1-y2,2)))


def razdalja(ime1,ime2,kraji):
    k1=koordinate(ime1,kraji)
    k2=koordinate(ime2,kraji)
    return razdalja_koordinat(k1[0],k1[1],k2[0],k2[1])

def v_dometu(ime,domet,kraji):
    seznam=[]
    for kraj,x,y in kraji:
        if(razdalja(ime,kraj,kraji)<= domet  and kraj != ime):
            seznam.append(kraj)
    return seznam

def najbolj_oddaljeni(ime,imena,kraji):
    najKraj=imena[0],0
    for i in imena:
        if(razdalja(ime,i,kraji)>najKraj[1]):
            najKraj = i ,razdalja(ime,i,kraji)
    return najKraj[0]

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime,v_dometu(ime,domet,kraji),kraji)

def presek(s1,s2):
    seznam=[]
    for i in s1:
        for j in s2:
            if(j==i):
                seznam.append(j)
    return seznam


def skupno_zalivanje(ime1, ime2, domet, kraji):
    return presek(v_dometu(ime1,domet,kraji),v_dometu(ime2,domet,kraji))




