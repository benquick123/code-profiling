# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):                             #prejme (ime) kraja in seznam krajev (kraji), vrne terko s koordinatama podanega kraja
    for ime_kraja, x, y in kraji:
        if (ime_kraja == ime):
            return x,y

def razdalja_koordinat(x1, y1, x2, y2):                 #dobi koordinate dveh točk in vrne razdaljo med njima
    return(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

def razdalja(ime1, ime2, kraji):                        #prejme imeni dveh krajev in vrne razdaljo med njima
    x1, y1 = koordinate(ime1,kraji)
    x2, y2 = koordinate(ime2,kraji)
    return(razdalja_koordinat(x1, y1, x2, y2))

def v_dometu(ime, domet, kraji):                        #vrne seznam krajev, ki jih lahko zalije kraj (ime), če ima top z nekim dometom
    s=[]
    x1, y1 = koordinate(ime, kraji)
    for ime_kraja, x, y in kraji:
        if 0 < razdalja_koordinat(x,y,x1,y1) <= domet:  #mora biti vecje od nič, sicer kraj zaliva sebe
            s.append(ime_kraja)
    return s

def najbolj_oddaljeni(ime, imena, kraji):               #med kraji v seznamu (imena) vrne ime tistega, ki je najbolj oddaljen od kraja (ime)
    x1,y1 = koordinate(ime, kraji)
    max=0
    for ime_kraja, x, y in kraji:
        if ime_kraja in imena:  #preveri ali je (ime_kraja) v seznamu (imena)
            if (sqrt((x - x1) ** 2 + (y - y1) ** 2)) > max:
                max = (sqrt((x - x1) ** 2 + (y - y1) ** 2))
                naj_o=ime_kraja
    return naj_o

def zalijemo(ime, domet, kraji):                        #vrne ime najbolj oddaljenega kraja, ki ga lahko zalije kraj (ime), če ima top z nekim dometom
    x1,y1 = koordinate(ime,kraji)
    max=0
    for ime_kraja, x, y in kraji:
        if (sqrt((x - x1) ** 2 + (y - y1) ** 2)) <= domet:
            if (sqrt((x - x1) ** 2 + (y - y1) ** 2)) > max:
                max = (sqrt((x - x1) ** 2 + (y - y1) ** 2))
                naj_o = ime_kraja
    return naj_o

def presek(s1, s2):                                     #prejme dva seznama in vrne seznam elementov, ki se pojavijo v obeh
    s=[]
    for a in s1:
        for b in s2:
            if a==b:
                s.append(a)
    return s

def skupno_zalivanje(ime1, ime2, domet, kraji):         #prejme dve imeni krajev, domet in seznam vseh krajev. Vrniti mora seznam vseh krajev, ki jih lahko zalivamo iz obeh krajev
    x1,y1 = koordinate(ime1, kraji)
    x2,y2 = koordinate(ime2, kraji)
    s=[]
    for ime_kraja, x, y in kraji:
        if (sqrt((x - x1) ** 2 + (y - y1) ** 2)) <= domet and (sqrt((x - x2) ** 2 + (y - y2) ** 2)) <= domet:
            s.append(ime_kraja)
    return s


