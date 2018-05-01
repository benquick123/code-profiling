#####Ogrevalne naloge########
from math import*
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime==kraj:
            return (x,y)

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja=sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return (razdalja)

def razdalja(ime1, ime2, kraji):
    k1,k2=koordinate(ime1,kraji)
    k3,k4=koordinate(ime2,kraji)
    return(razdalja_koordinat(k1,k2,k3,k4))

#######Obvezna naloga#####

def v_dometu(ime, domet, kraji):
    s=[]
    for kraj, x, y in kraji:
        if razdalja(ime, kraj, kraji) <= domet and ime!=kraj:
            s.append(kraj)
    return(s)

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja=0
    naj_kraj=""
    for ime1 in imena:
        if razdalja(ime, ime1, kraji) > naj_razdalja:
            naj_razdalja = razdalja(ime, ime1, kraji)
            naj_kraj = ime1
    return (naj_kraj)

def zalijemo(ime, domet, kraji):
    naj_razdalja=0
    naj_kraj=""
    for kraj, x, y in kraji:
        if razdalja(ime, kraj, kraji) > naj_razdalja and razdalja(ime, kraj, kraji) <= domet:
            naj_razdalja = razdalja(ime, kraj, kraji)
            naj_kraj=kraj
    return(naj_kraj)

#####Dodatna naloga########
def presek(s1, s2):
    s=[]
    for e in s1:
        for d in s2:
            if d==e:
             s.append(e)
    return(s)

def skupno_zalivanje(ime1, ime2, domet, kraji):
    g=v_dometu(ime1, domet, kraji)
    b=v_dometu(ime2, domet, kraji)
    s=presek(g,b)
    return(s)

