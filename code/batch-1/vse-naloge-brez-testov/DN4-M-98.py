# Tu pišite svoje funkcije:
from math import *
# Ogrevalne naloge:

def koordinate (ime, kraji):
    koordinati = list()
    for ime_kraja, x, y in kraji:
        if ime == ime_kraja:
            koordinati.insert(0, x)
            koordinati.insert(1, y)
            koordinati = tuple(koordinati)
            return koordinati
    if koordinati == 0:
        return None

def razdalja_koordinat (x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja

def razdalja (ime1, ime2, kraji):
    koordinati1 = koordinate(ime1, kraji)
    koordinati2 = koordinate(ime2, kraji)
    razdalja_krajev = razdalja_koordinat(koordinati1[0], koordinati1[1], koordinati2[0], koordinati2[1])
    return razdalja_krajev

# Obvezni del

def v_dometu(ime, domet, kraji):
    krajiVDometu = []
    for ime_kraja, x1, y1 in kraji:
        if ime == ime_kraja:
            break

    for ime_kraja1, x2, y2 in kraji:
        if ime == ime_kraja1:
            continue
        razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if razdalja <= domet:
            krajiVDometu.append(ime_kraja1)
    return krajiVDometu

def najbolj_oddaljeni(ime, imena, kraji):
    for ime_kraja, x1, y1 in kraji:
        if ime_kraja == ime:
            break

    najvecja_razdalja = 0
    for i in imena:
        for ime1, x2, y2 in kraji:
            if ime1 == i:
                razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if razdalja > najvecja_razdalja:
                    najvecja_razdalja = razdalja
                    najbolj_oddaljen = ime1
    return najbolj_oddaljen

def zalijemo(ime, domet, kraji):
    for ime_kraja, x1, y1 in kraji:
        if ime_kraja == ime:
            break
    najvecja_razdalja = 0
    for ime2, x2, y2 in kraji:
        razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if najvecja_razdalja < razdalja <= domet:
            najvecja_razdalja = razdalja
            najbolj_oddaljen = ime2

    return najbolj_oddaljen

# Dodatni del

def presek(s1, s2):
    seznam = []
    for i in s1:
        for j in s2:
            if j == i:
                seznam.append(j)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam = []
    for i in range(len(kraji)):
        ime, x, y = kraji[i]
        if ime == ime1:
            x1 = x
            y1 = y
        if ime == ime2:
            x2 = x
            y2 = y

    for k in range(len(kraji)):
        ime, x, y = kraji[k]
        razdalja1 = sqrt((x - x1) ** 2 + (y - y1) ** 2)
        razdalja2 = sqrt((x - x2) ** 2 + (y - y2) ** 2)

        if razdalja1 <= domet and razdalja2 <= domet:
            seznam.append(ime)
    return seznam


