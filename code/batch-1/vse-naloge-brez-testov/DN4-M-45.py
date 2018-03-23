# Tu pišite svoje funkcije:

from math import *



#Ogrevalne funkcije

def koordinate(ime, kraji):
    kraj_x = 0
    kraj_y = 0
    vsebuje_kraj = 0
    for kraj, x, y in kraji: #poišče koordinate iskanega kraja
        if kraj == ime:
            kraj_x = x
            kraj_y = y
            vsebuje_kraj = 1 #kraj je v seznamu
            break
    if vsebuje_kraj == 0: #če kraja ni, vrne None
        return None
    else: #drugače izpiše koordinate
        return kraj_x, kraj_y

def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)  #izračuna razdaljo med točkama
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji) #s pomočjo prejšnje funkcije dobimo koordinate
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2) #in izračunamo razdaljo



#Obvezni del

def v_dometu(ime, domet, kraji):
    kraji_v_dometu = []
    kraj_x, kraj_y = koordinate(ime, kraji) #koordinate
    for kraj, x, y in kraji:
        razdalja = razdalja_koordinat(kraj_x, kraj_y, x, y)  #razdalja
        if razdalja <= domet and ime != kraj: #če je v dometu in ni isti kraj, ga shrani
            kraji_v_dometu.append(kraj)
    return kraji_v_dometu

def najbolj_oddaljeni(ime, imena, kraji):
    kraj_x, kraj_y = koordinate(ime, kraji)
    max_razdalja = 0
    max_kraj = 0
    for kraj, x, y in kraji:
        if kraj in imena: #če je kraj v seznamu možnih krajev
            razdalja = razdalja_koordinat(kraj_x, kraj_y, x, y)
            if razdalja > max_razdalja: #preveri, če je bolj oddaljen od prejšnjega
                max_razdalja = razdalja
                max_kraj = kraj
    return max_kraj

def zalijemo(ime, domet, kraji):
    kraj_x, kraj_y = koordinate(ime, kraji)
    max_razdalja = 0
    max_kraj = 0
    for kraj, x, y in kraji:
        razdalja = razdalja_koordinat(kraj_x, kraj_y, x, y)
        if razdalja <= domet and razdalja > max_razdalja: #če je kraj v dometu
            max_razdalja = razdalja
            max_kraj = kraj
    return max_kraj



#Dodatni del

def presek(s1, s2):
    presek = []
    for x in s1:
        if x in s2:
            presek.append(x)
    return presek

def skupno_zalivanje(ime1, ime2, domet, kraji):
    skupni_v_dometu = []
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    for kraj, x, y in kraji:
        razdalja1 = razdalja_koordinat(x1, y1, x, y)
        razdalja2 = razdalja_koordinat(x2, y2, x, y)
        if razdalja1 <= domet and razdalja2 <= domet:
            skupni_v_dometu.append(kraj)
    return skupni_v_dometu



#Seznam krajev in testi

