import math
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if kraj == ime:
            return x, y

def razdalja_koordinat(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

def razdalja(ime1, ime2, kraji):
    kraj1 = koordinate(ime1, kraji)
    kraj2 = koordinate(ime2, kraji)
    return razdalja_koordinat(kraj1[0], kraj1[1], kraj2[0], kraj2[1])

def v_dometu(ime, domet, kraji):
    krajj = []
    for kraj, x, y in kraji:
        razdalja = math.sqrt(math.pow((x - koordinate(ime, kraji)[0]), 2) + math.pow((y - koordinate(ime, kraji)[1]), 2))
        if razdalja <= domet and ime != kraj:
            krajj.append(kraj)
    return krajj

def najbolj_oddaljeni(ime, imena, kraji):
    najRazdalja = 0
    for kraj in imena:
        razdalja = math.sqrt(math.pow((koordinate(kraj, kraji)[0] - koordinate(ime, kraji)[0]), 2) + math.pow((koordinate(kraj, kraji)[1] - koordinate(ime, kraji)[1]), 2))
        if razdalja > najRazdalja:
            najKraj = kraj
            najRazdalja = razdalja
    return najKraj

def zalijemo(ime, domet, kraji):
    a = ["", 0, 0]
    for list in kraji:
        razdalja = math.sqrt(math.pow((list[1] - koordinate(ime, kraji)[0]), 2) + math.pow((list[2] - koordinate(ime, kraji)[1]), 2))
        if razdalja > a[1] and razdalja <= domet:
            a[1] = razdalja
            a[0] = list[0]
    return a[0]

def presek(s1, s2):
    gg = []
    for ime in s1:
        for list in s2:
            if ime == list:
                gg.append(list)
    return gg

def skupno_zalivanje(ime1, ime2, domet, kraji):
    kraj = []
    for list in kraji:
        razdalja1 = math.sqrt(math.pow((list[1] - koordinate(ime1, kraji)[0]), 2) + math.pow((list[2] - koordinate(ime1, kraji)[1]), 2))
        razdalja2 = math.sqrt(math.pow((list[1] - koordinate(ime2, kraji)[0]), 2) + math.pow((list[2] - koordinate(ime2, kraji)[1]), 2))
        if razdalja1 <= domet and razdalja2 <= domet:
            kraj.append(list[0])
    return kraj


