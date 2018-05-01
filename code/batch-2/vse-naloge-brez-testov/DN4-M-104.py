import math

def koordinate(ime, kraji):
    for kraj , kordinata1 , kordinata2 in kraji:
        if ime == kraj:
            terka = (kordinata1, kordinata2)
            return(terka)
    return(None)

def razdalja_koordinat(x1, y1, x2, y2):
    kord1 = x2 - x1
    kord2 = y2 - y1
    razdalja = math.sqrt(kord1 ** 2 + kord2 ** 2)
    return(razdalja)

def razdalja(ime1, ime2, kraji):
    kor1 = koordinate(ime1, kraji)
    kor2 = koordinate(ime2, kraji)
    rezultat = razdalja_koordinat(kor1[0], kor1[1], kor2[0], kor2[1])
    return(rezultat)

def v_dometu(ime, domet, kraji):
    seznam = []

    for kraj, x, y in kraji:
        if kraj == ime:
            break

    for kraj2, x2, y2 in kraji:
        razdalja = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)

        if 0 < razdalja <= domet:
            seznam.append(kraj2)
    return (seznam)

def najbolj_oddaljeni(ime, imena, kraji):
    najdlje = 0
    najdlje_ime = ""

    k1 = 0
    y1 = 0

    for vsak in kraji:
        kraj, kordinata1, kordinata2 = vsak

        if kraj == ime:
            k1 = kordinata1
            y1 = kordinata2

    for vsak in kraji:
        kraj, kordinata1, kordinata2 = vsak

        k2 = kordinata1
        y2 = kordinata2

        kord1 = k2 - k1
        kord2 = y2 - y1

        razdalja = math.sqrt(kord1 ** 2 + kord2 ** 2)

        if razdalja > najdlje and kraj in imena:
            najdlje = razdalja
            najdlje_ime = kraj
    return (najdlje_ime)

def zalijemo(ime, domet, kraji):
    najdlje = 0
    najdlje_ime = ""

    k1 = 0
    y1 = 0

    for vsak in kraji:
        kraj, kordinata1, kordinata2 = vsak

        if ime == kraj:
            print(ime, "je na kordinatah", kordinata1, kordinata2)
            k1 = kordinata1
            y1 = kordinata2

    for vsak in kraji:
        kraj, kordinata1, kordinata2 = vsak

        k2 = kordinata1
        y2 = kordinata2

        kord1 = k2 - k1
        kord2 = y2 - y1

        razdalja = math.sqrt(kord1 ** 2 + kord2 ** 2)

        if razdalja < domet and razdalja > najdlje:
            najdlje = razdalja
            najdlje_ime = kraj
    return(najdlje_ime)

def presek(s1, s2):
    seznam = []
    for i in s1:
        for j in s2:
            if i == j:
                seznam.append(i)
    return (seznam)

def skupno_zalivanje(ime1, ime2, domet, kraji):
    k1 = 0
    y1 = 0
    k2 = 0
    y2 = 0

    seznam = []

    for vsak in kraji:
        ime, kordinata1, kordinata2 = vsak

        if ime == ime1:
            k1 = kordinata1
            y1 = kordinata2

        if ime == ime2:
            k2 = kordinata1
            y2 = kordinata2

    for vsak in kraji:
        ime, kordinata1, kordinata2 = vsak

        kord1 = k1 - kordinata1
        kord2 = y1 - kordinata2
        kordi1 = k2 - kordinata1
        kordi2 = y2 - kordinata2

        razdalja = math.sqrt(kord1 ** 2 + kord2 ** 2)
        razdalja2 = math.sqrt(kordi1 ** 2 + kordi2 ** 2)

        if razdalja < domet and razdalja2 < domet:
            seznam.append(ime)
    return(seznam)

"""====================================================="""

