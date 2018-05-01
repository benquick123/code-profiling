# Tu pišite svoje funkcije:
import math


def koordinate(ime, kraji):

    for kraj, x, y in kraji:
        if ime == kraj:  # primerjanje niza ime s nizom kraj iz terke
            return x, y        # vrnemo terko s koordinatama x in y


def razdalja_koordinat(x1, y1, x2, y2):

    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))   # pitagorov izrek za koordinate x1, y1 in x2, y2


def razdalja(ime1, ime2, kraji):

    kraj1 = koordinate(ime1, kraji)
    kraj2 = koordinate(ime2, kraji)

    return razdalja_koordinat(kraj1[0], kraj1[1], kraj2[0], kraj2[1])


def v_dometu(ime, domet, kraji):

    # deklaracija seznama za shranjevanje imen
    imena = []

    x0, y0 = koordinate(ime, kraji)

    # iskanje krajev v dometu
    for kraj1, x1, y1 in kraji:
        dist = math.sqrt(((x0 - x1) ** 2) + ((y0 - y1) ** 2))
        if dist <= domet and kraj1 != ime:
            imena.append(kraj1)

    return imena


def najbolj_oddaljeni(ime, imena, kraji):

    x0, y0 = koordinate(ime, kraji)
    naj_oddaljen = 0
    ime_naj_oddalj = ""

    for kraj, x1, y1 in kraji:
        if kraj in imena:  # primerjanje kraja s seznamom imena
            dist0 = math.sqrt(((x0 - x1) ** 2) + ((y0 - y1) ** 2))  # pitagorov izrek
            if naj_oddaljen < dist0:
                naj_oddaljen = dist0
                ime_naj_oddalj = kraj

    return ime_naj_oddalj


def zalijemo(ime, domet, kraji):

    return najbolj_oddaljeni(ime, v_dometu(ime, domet, kraji), kraji)


def presek(s1, s2):

    presek_elem = []

    for i in range(0, len(s1)):
        if s1[i] in s2:  # primerjanje elementa na indeksu i v seznamu s1 s vsemi elementi v seznamu s2
            presek_elem.append(s1[i])  # dodajanje elementa v preseku v seznam presek_elem

    return presek_elem


def skupno_zalivanje(ime1, ime2, domet, kraji):

    return presek(v_dometu(ime1, domet, kraji), v_dometu(ime2, domet, kraji))


