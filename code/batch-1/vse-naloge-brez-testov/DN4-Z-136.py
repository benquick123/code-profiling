

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
           return x,y

from math import *
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2,kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    s = []
    x1, y1 = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        if domet >= razdalja_koordinat(x1, y1, x, y):
                if kraj != ime:
                    s.append(kraj)
    return s

#v_dometu(ime, domet, kraji) vrne seznam krajev, ki jih lahko zalije kraj ime, če ima top z dometom domet. Kraj ne zaliva sebe.

def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    naj_kraj = []
    for i in imena:
        razdalja_i = razdalja(ime, i,kraji)
        if razdalja_i > naj_razdalja:
            naj_razdalja = razdalja_i
            naj_kraj = i
    return naj_kraj

#zalijemo(ime, domet, kraji) vrne ime najbolj oddaljenega kraja, ki ga lahko zalije kraj ime, če ima top z dometom domet.
#uporabi funkcijo v dometu

def zalijemo(ime, domet, kraji):
    return najbolj_oddaljeni(ime, v_dometu(ime, domet,kraji),kraji)


#presek(s1, s2) prejme dva seznama in vrne seznam elementov, ki se pojavijo v obeh. Vrstni red elementov v vrnjenem seznamu je lahko poljuben.

def presek(s1, s2):
    s = []
    for element in s1:
        if element in s2:
            s.append(element)
    return s



