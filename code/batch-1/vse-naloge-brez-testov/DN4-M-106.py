import math
# Tu pišite svoje funkcije:

def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return (x,y)

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1,y1, x2, y2)


def v_dometu(ime, domet, kraji):
    seznam=[]
    x1, y1 = koordinate(ime, kraji)
    for i in range(len(kraji)):
        ime2, x2, y2 = (kraji[i])
        if ime != ime2:
            if domet >= razdalja_koordinat(x1,y1,x2,y2):
                seznam.append(ime2)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    naj_kraj=""
    naj_razdalja=0

    x1, y1 = koordinate(ime, kraji)
    for i in range(len(imena)):
        x2, y2 = koordinate(imena[i], kraji)
        pot = razdalja_koordinat(x1,y1,x2,y2)
        if naj_razdalja < pot:
            naj_razdalja = pot
            naj_kraj=imena[i]
    return naj_kraj

def zalijemo(ime, domet, kraji):
    naj_kraj = ""
    naj_razdalja=0

    x1, y1 = koordinate(ime, kraji)
    for i in range(len(kraji)):
        ime2, x2, y2 = kraji[i]
        print(kraji[i])
        pot = razdalja_koordinat(x1, y1, x2, y2)
        if naj_razdalja < pot < domet:
            naj_razdalja=pot
            naj_kraj = ime2

    return naj_kraj

def presek(s1, s2):
    return list(set(s1) & set(s2))

def skupno_zalivanje(ime1, ime2, domet, kraji):
    s1 = v_dometu(ime1, domet, kraji)
    s2 = v_dometu(ime2, domet, kraji)
    return presek(s1, s2)

