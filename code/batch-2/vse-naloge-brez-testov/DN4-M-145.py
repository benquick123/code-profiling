# Tu pišite svoje funkcije:
from math import *
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if(kraj==ime):
            return x,y

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1,y1=koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1,y1,x2,y2)

def v_dometu(ime, domet, kraji):
    lahko_zaliva = []
    for ime_kraja, x, y in kraji:
        if ime_kraja == ime:
            x_kraja = x
            y_kraja = y
    for ime_kraja2, x, y in kraji:
        razdalja_krajev = sqrt((x - x_kraja) ** 2 + (y - y_kraja) ** 2)
        if(razdalja_krajev<=domet):
            if(ime_kraja2!=ime):
                lahko_zaliva.append(ime_kraja2)
    return lahko_zaliva

def najbolj_oddaljeni(ime, imena, kraji):
    for ime_kraja, x, y in kraji:
        if (ime == ime_kraja):
            x_kraj = x
            y_kraj = y
    z_razdalja = 0
    oddaljen= ""
    for ime in imena:
        for ime_kraja2, x,y in kraji:
            if(ime == ime_kraja2):
                razdalja = sqrt((x - x_kraj) ** 2 + (y - y_kraj) ** 2)
                if(razdalja>=z_razdalja):
                    z_razdalja=razdalja
                    oddaljen = ime_kraja2
    return oddaljen

def zalijemo(ime, domet, kraji):
    for ime_kraja, x, y in kraji:
        if (ime == ime_kraja):
            x_kraj = x
            y_kraj = y
    z_razdalja = 0
    for ime_kraja2, x, y in kraji:
        razdalja = sqrt((x - x_kraj) ** 2 + (y - y_kraj) ** 2)
        if(razdalja<=domet):
            if(razdalja>=z_razdalja):
                z_razdalja=razdalja
                z_kraj=ime_kraja2
    return z_kraj

#---------------------- DODATNA NALOGA ----------------------
def presek(s1, s2):
    return list(set(s1) & set(s2))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    for ime_kraja, x, y in kraji:
        if (ime1 == ime_kraja):
            kraj1_x=x
            kraj1_y=y
        if (ime2 == ime_kraja):
            kraj2_x=x
            kraj2_y=y
    skupni_kraji=[]
    for ime_kraja2, x, y in kraji:
        razdalja_med1 = sqrt((kraj1_x - x) ** 2 + (kraj1_y - y) ** 2)
        razdalja_med2 = sqrt((kraj2_x - x) ** 2 + (kraj2_y - y) ** 2)
        if (razdalja_med1 <= 30 and razdalja_med2 <= 30):
            skupni_kraji.append(ime_kraja2)
    return skupni_kraji

