from math import *

# Tu pišite svoje funkcije:
def koordinate(ime, kraji):
    for imeKraja, x, y in kraji:
        if imeKraja == ime:
            return (x, y)

def razdalja_koordinat(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    razdalja = sqrt(x**2 + y**2)
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):
    seznamKrajev = []
    #pridobi koordinate izbranega kraja
    x1, y1 = koordinate(ime, kraji)
    for imeKraja, x2, y2 in kraji:
        #preveri ali je razdalaja med dvema krajema manjsa od dometa
        if razdalja(ime, imeKraja, kraji) <= domet and ime != imeKraja:
            seznamKrajev.append(imeKraja)
    return seznamKrajev

def najbolj_oddaljeni(ime, imena, kraji):
    najboljOddaljeni = ""
    maxRazdalja = 0
    x1, y1 = koordinate(ime, kraji)
    for imeKraja in imena:
        trenutnaRazdalja = razdalja(ime, imeKraja, kraji)
        if trenutnaRazdalja > maxRazdalja:
            maxRazdalja = trenutnaRazdalja
            najboljOddaljeni = imeKraja
    return najboljOddaljeni

def  zalijemo(ime, domet, kraji):
    najboljOddaljeni = ""
    maxRazdalja = 0
    x1, y1 = koordinate(ime, kraji)
    for imeKraja, x, y in kraji:
        if  domet > razdalja(ime, imeKraja, kraji) > maxRazdalja:
            maxRazdalja = razdalja(ime, imeKraja, kraji)
            najboljOddaljeni = imeKraja
    return najboljOddaljeni

def presek(s1, s2):
    skupniSeznam = []
    for element in s1:
        if element in s2:
            skupniSeznam.append(element)
    return skupniSeznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    skupniSeznam = []
    for imeKraja, x, y in kraji:
        if razdalja(ime1, imeKraja, kraji) < domet and razdalja(ime2, imeKraja,kraji) < domet:
            skupniSeznam.append(imeKraja)
    return skupniSeznam

