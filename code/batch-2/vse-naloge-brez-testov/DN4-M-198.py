# Tu pišite svoje funkcije:
from math import *
#Ogrevalne
def koordinate(ime, kraji):#vrne kordinate kraja v terki
    for kraj,x0,y0 in kraji:
        if kraj == ime:
            return(x0,y0)
    return None


def razdalja_koordinat(x1, y1, x2, y2):#vrne razdaljo med dvema kordinatoma
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def razdalja(ime1, ime2, kraji):
    kor1=koordinate(ime1,kraji)
    kor2=koordinate(ime2,kraji)
    return razdalja_koordinat(kor1[0],kor1[1],kor2[0],kor2[1])
#print(razdalja("Brežice","Lenart",kraji))

#Obvezne
def v_dometu(ime, domet, kraji):
    kraji2=[]
    for kraj in kraji:
        if razdalja(kraj[0],ime,kraji) <= domet:
            if kraj[0] !=ime:
                kraji2.append(kraj[0])
    return kraji2
#print(v_dometu("Brežice",30,kraji))

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    naj_kraj = ""
    for kraj in imena:
        if razdalja(kraj,ime,kraji)>naj_razdalja:
            naj_razdalja = razdalja(kraj,ime,kraji)
            naj_kraj = kraj
    return naj_kraj
#print(najbolj_oddaljeni("Ljubljana", ["Domžale", "Kranj", "Maribor", "Vrhnika"], kraji))


def zalijemo(ime, domet, kraji):
    naj_razdalja = 0
    naj_kraj = ""
    for kraj in kraji:
        if razdalja(kraj[0],ime,kraji)<=domet:
            if razdalja(kraj[0],ime,kraji)>naj_razdalja:
                naj_razdalja = razdalja(kraj[0],ime,kraji)
                naj_kraj = kraj[0]
    return naj_kraj
#print(zalijemo("Litija",60,kraji)) 


#Dodatne
def presek(s1, s2):
    s3=[]
    for i in s1:
        for j in s2:
            if i == j:
                s3.append(i)
    return s3
#print(presek([2,1,3,6,8],[3,4,2,8,0]))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    kraji2 = []
    for kraj in kraji:
        if razdalja(ime1,kraj[0],kraji)<=domet:
            if razdalja(ime2,kraj[0],kraji)<=domet:
                kraji2.append(kraj[0])
    return kraji2
#print(skupno_zalivanje("Ljubljana","Bled",30,kraji))
    

