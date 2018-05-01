# OGREVALNE FUNKCIJE
# Vrnitev koordinat
def koordinate(ime, kraji):
    for kraj, x, y in kraji:
        if ime == kraj:
            return x, y
    return None

# Razdalja koordinat
def razdalja_koordinat(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

# Razdalja dveh krajev
def razdalja(ime1, ime2, kraji):
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    return razdalja_koordinat(x1, y1, x2, y2)

# OBVEZNI DEL
# Seznam krajev v dometu
def v_dometu(ime, domet, kraji):
    imena = []
    x1, y1 = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        raz = ((x1 - x) ** 2 + (y1 - y) ** 2) ** (1 / 2)
        if raz <= domet and raz != 0:
            imena.append(kraj)
    return imena

# Najbolj oddaljen kraj s seznama
def najbolj_oddaljeni(ime, imena, kraji):
    m = 1
    x1, y1 = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        for i in imena:
            if i == kraj:
                x2, y2 = x, y
                raz = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
                if raz > m:
                    m = raz
                    n = kraj
    return n

# Zalijemo kraj
def zalijemo(ime, domet, kraji):
    rz = 1
    x1, y1 = koordinate(ime, kraji)
    for kraj, x, y in kraji:
        raz = ((x1 - x) ** 2 + (y1 - y) ** 2) ** (1 / 2)
        if raz <= domet:
            m, nd = kraj, raz
            if nd > rz:
                rz = nd
                n = m
    return n

# DODATNA NALOGA
# Presek
def presek(s1, s2):
    sez = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
                sez.append(e1)
    return sez

# Skupno zalivanje
def skupno_zalivanje(ime1, ime2, domet, kraji):
    skupaj = []
    x1, y1 = koordinate(ime1, kraji)
    x2, y2 = koordinate(ime2, kraji)
    for kraj, x, y in kraji:
        raz1 = ((x1 - x) ** 2 + (y1 - y) ** 2) ** (1 / 2) <= domet
        raz2 = ((x2 - x) ** 2 + (y2 - y) ** 2) ** (1 / 2) <= domet
        if raz1 and raz2:
            skupaj.append(kraj)
    return skupaj
