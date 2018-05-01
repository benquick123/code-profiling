# Tu pišite svoje funkcije:
import math


def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return list(zip([x], [y]))[0]


def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2)+(y2-y1)**2)


def razdalja(ime1, ime2, kraji):
    koordinate1 = koordinate(ime1, kraji)
    koordinate2 = koordinate(ime2, kraji)
    return razdalja_koordinat(koordinate1[0], koordinate1[1], koordinate2[0], koordinate2[1])


def v_dometu(ime, domet, kraji):
    seznam_v_dometu = []
    koordinate_glavno_mesto = koordinate(ime, kraji)

    for kraj, x, y in kraji:
        if kraj == ime:
            continue

        razdalja_med_mesti = razdalja_koordinat(x, y, koordinate_glavno_mesto[0], koordinate_glavno_mesto[1])

        if razdalja_med_mesti <= domet:
            seznam_v_dometu.append(kraj)

    return seznam_v_dometu


def najbolj_oddaljeni(ime, imena, kraji):
    max_odd=0

    koordinate_glavno_mesto = koordinate(ime, kraji)

    for ime_kraja in imena:
        koordinate_ime_kraja = koordinate(ime_kraja, kraji)

        razdalja_med_kraji = razdalja_koordinat(koordinate_glavno_mesto[0], koordinate_glavno_mesto[1],
                                                koordinate_ime_kraja[0], koordinate_ime_kraja[1])

        if razdalja_med_kraji > max_odd:
            max_odd = razdalja_med_kraji
            max_kraj = ime_kraja

    return max_kraj


def zalijemo(ime, domet, kraji):
    max_odd = 0

    koordinate_glavno_mesto = koordinate(ime, kraji)

    for kraj, x, y in kraji:
        if kraj == ime:
            continue

        razdalja_med_mesti = razdalja_koordinat(x, y, koordinate_glavno_mesto[0], koordinate_glavno_mesto[1])

        if razdalja_med_mesti <= domet:
            if razdalja_med_mesti > max_odd:
                max_odd = razdalja_med_mesti
                max_kraj = kraj

    return max_kraj


def presek(s1, s2):
    nov_seznam = []

    for i in s1:
        for j in s2:
            if i == j:
                nov_seznam.append(i)
                break

    return nov_seznam


def skupno_zalivanje(ime1, ime2, domet, kraji):
    seznam_krajev = []

    koordinate_glavno_mesto1 = koordinate(ime1, kraji)
    koordinate_glavno_mesto2 = koordinate(ime2, kraji)

    for kraj, x, y in kraji:
        if kraj == ime1 or kraj == ime2:
            continue

        razdalja1 = razdalja_koordinat(x, y, koordinate_glavno_mesto1[0], koordinate_glavno_mesto1[1])
        if razdalja1 <= domet:
            razdalja2 = razdalja_koordinat(x, y, koordinate_glavno_mesto2[0], koordinate_glavno_mesto2[1])
            if razdalja2 <= domet:
                seznam_krajev.append(kraj)

    return seznam_krajev

