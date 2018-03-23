# Tu pišite svoje funkcije:
def koordinate(ime, kraji):

    koordinate_kraja = ()

    for kraj, koordinata_x, koordinata_y in kraji:
        if ime == kraj:
            koordinate_kraja += koordinata_x, koordinata_y
            return koordinate_kraja
    else:
        return None


from math import *
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    return razdalja

def razdalja(ime1, ime2, kraji):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    for kraj1 in kraji:
        if ime1 == kraj1[0]:
            x1, y1 = koordinate(ime1, kraji)
            break

    for kraj2 in kraji:
        if kraj2[0] == ime2:
            x2, y2 = koordinate(ime2, kraji)

    return razdalja_koordinat(x1, y1, x2, y2)

def v_dometu(ime, domet, kraji):

    seznam_krajev = []

    for zrtev in kraji:
        tarca = razdalja(ime, zrtev[0], kraji)
        if tarca <= domet and ime != zrtev[0]:
            seznam_krajev.append(zrtev[0])

    return seznam_krajev

def najbolj_oddaljeni(ime, imena, kraji):
    najbolj = 0
    oddaljen_kraj = 0

    for kraj in imena:
        oddaljen_kraj = razdalja(ime, kraj, kraji)

        if najbolj < oddaljen_kraj:
            najbolj = oddaljen_kraj
            ime_najbolj = kraj

    return ime_najbolj

def zalijemo(ime, domet, kraji):

    najbolj = 0
    razdalja_kraja = 0

    for kraj in kraji:
        razdalja_kraja = razdalja(ime, kraj[0], kraji)
        if razdalja_kraja > najbolj and razdalja_kraja <= domet:
            najbolj = razdalja_kraja
            ime_naj_odd = kraj[0]

    return ime_naj_odd

def presek(s1, s2):

    seznam = []

    for i in s1:
        for j in s2:
            if i == j:
                seznam.append(i)

    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam1 = []
    seznam1 = v_dometu(ime1, domet, kraji)

    seznam2 = []
    seznam2 = v_dometu(ime2, domet, kraji)

    seznam = []
    seznam = presek(seznam1, seznam2)

    return seznam



