from math import *

def koordinate(ime,kraji):
    vrni = None
    for kraj,x,y in kraji:
        if (kraj == ime):
            vrni = (x,y)

    return vrni

def razdalja_koordinat(x1,y1,x2,y2):
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

def razdalja(ime1, ime2, kraji):
    koordinate1 = koordinate(ime1,kraji)
    koordinate2 = koordinate(ime2, kraji)

    return razdalja_koordinat(koordinate1[0],koordinate1[1],koordinate2[0],koordinate2[1])

def v_dometu(ime,domet,kraji):
    seznam  = []

    for kraj,x,y in kraji:
        razdalj = razdalja(kraj,ime,kraji)
        if(razdalj<=domet)and kraj != ime:
            seznam.append(kraj)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    najbolj=""
    razdal = 0

    for kraj in imena:
        trenutna = razdalja(kraj,ime,kraji)
        if(razdal<=trenutna):
            razdal=trenutna
            najbolj=kraj


    return najbolj

#zalijemo(ime, domet, kraji) vrne ime najbolj oddaljenega kraja, ki ga lahko zalije kraj ime, če ima top z dometom domet.

def zalijemo(ime,domet,kraji):
    trenutni = ""
    nov = []
    max = 0
    for k,kx,ky in kraji:

        if(razdalja(k,ime,kraji)<=domet):
            terka = (razdalja(k,ime,kraji),k)
            nov.append(terka)

    for raz, krajcek in nov:

        if(raz>=max):
            max=raz
            trenutni = krajcek

    return trenutni
#presek(s1, s2) prejme dva seznama in vrne seznam elementov, ki se pojavijo v obeh. Vrstni red elementov v vrnjenem seznamu je lahko poljuben.

def presek(s1,s2):
    nov=[]
    for el in s1:
        if el in s2:
            nov.append(el)
    return nov

#skupno_zalivanje(ime1, ime2, domet, kraji) prejme dve imeni krajev, domet vodnih topov, ki ju imajo v teh dveh krajih, in seznam vseh krajev. Vrniti mora seznam vseh krajev, ki jih lahko zalivamo iz obeh krajev.

def skupno_zalivanje(ime1,ime2,domet,kraji):
    return presek(v_dometu(ime1,domet,kraji),v_dometu(ime2,domet,kraji))


