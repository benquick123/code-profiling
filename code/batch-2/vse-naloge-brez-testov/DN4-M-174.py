# Tu pišite svoje funkcije:
from math import sqrt


def koordinate(ime, kraji):
    for i,x,y in kraji:
        if ime==i:
            return (x,y)
    else:
        return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(((x1-x2)**2)+((y1-y2)**2))

def razdalja(ime1, ime2, kraji):
    x1,y1=koordinate(ime1,kraji)
    x2,y2=koordinate(ime2,kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):
    zaliti=[]
    x1,y1=koordinate(ime,kraji)
    for i,x2,y2 in kraji:
        if i!=ime:
            if razdalja_koordinat(x1,y1,x2,y2)<=domet:
                zaliti+=(i,)
    return zaliti

def najbolj_oddaljeni(ime, imena, kraji):
    najdlje=ime
    x1,y1=koordinate(ime,kraji)
    for i in imena:
        x2,y2=koordinate(i,kraji)
        if razdalja_koordinat(x1,y1,x2,y2)> \
                razdalja_koordinat(x1,y1,koordinate(najdlje,kraji)[0],koordinate(najdlje,kraji)[1]):
            najdlje=i
    return najdlje

def zalijemo(ime, domet, kraji):
    najdlje=ime
    x1,y1=koordinate(ime,kraji)
    for i,x2,y2 in kraji:
        razdalja_tr=razdalja_koordinat(x1,y1,x2,y2)
        najdlje_k=koordinate(najdlje,kraji)
        if razdalja_tr<=domet and razdalja_tr> razdalja_koordinat(x1,y1,najdlje_k[0],najdlje_k[1]):
            najdlje=i
    return najdlje

def presek(s1, s2):
    s3=[]
    for x in s1:
        for y in s2:
            if x==y:
                s3+=(x,)
    return s3

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1=v_dometu(ime1,domet,kraji)
    s2=v_dometu(ime2,domet,kraji)
    s3=presek(s1,s2)
    return s3

