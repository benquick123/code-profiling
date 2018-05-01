# Tu pišite svoje funkcije:

#ogrevalni del
from math import*
def koordinate(ime, kraji):
    a = 0
    for kraj, x, y in kraji:
        if ime == kraj:
            a = (x, y)
    if a == 0:
        return
    else:
        return a


def razdalja_koordinat(x1, y1, x2, y2):
    kX = x1 - x2
    kY = y1 - y2
    k = sqrt(kX**2 + kY**2)
    return k

def razdalja(ime1, ime2, kraji):
    prva = koordinate(ime1, kraji)
    druga = koordinate(ime2, kraji)
    mid = prva + druga
    result = razdalja_koordinat(mid[0], mid[1], mid[2], mid[3])
    return result


# vrne seznam krajev, ki jih zalije kraj "ime"
def v_dometu(ime, domet, kraji):
    v_dometu_l = []
    for kraj, x, y in kraji:
        if ime == kraj:
            center = kraj
            centerX = x
            centerY = y
            break
    for kraj, x, y, in kraji:
        kX = centerX - x
        kY = centerY - y
        a = sqrt(kX**2 + kY**2)
        if a <= domet and kraj != center:
            v_dometu_l.append(kraj)
    return v_dometu_l


#obvezni del

#vrne najbolj oddaljen kraj iz seznama od kraja "ime"
def najbolj_oddaljeni(ime, imena, kraji):
    naj_razdalja = 0
    for kraj, x, y in kraji:
        if ime == kraj:
            x1 = x
            y1 = y
            break
    for kraj, x, y in kraji:
        for kraj2 in imena:
            if kraj == kraj2:
                kx = x1 - x
                ky = y1 - y
                razdalja = sqrt(kx**2 + ky**2)
                if razdalja > naj_razdalja:
                    naj_razdalja = razdalja
                    naj_kraj = kraj2
    return naj_kraj

#vrne najbolj oddaljen kraj ki ga lahko zalije kraj "ime" z dometom "domet"
def zalijemo(ime, domet, kraji):
    naj_a = 0
    for kraj, x, y in kraji:
        if ime == kraj:
            centerX = x
            centerY = y
            break
    for kraj, x, y, in kraji:
        kX = centerX - x
        kY = centerY - y
        a = sqrt(kX**2 + kY**2)
        if a < domet and a > naj_a:
            naj_a = a
            naj_kraj = kraj
    return naj_kraj


#prejme dva seznama in vrne seznam elementov, ki se pojavijo v obeh seznamih
def presek(s1, s2):
    double = []
    for s in s1:
        for s0 in s2:
            if s0 == s:
               double.append(s0)
    return double


#prejme dva kraja, domet in vrne seznam krajev ki jih lahko zalivamo z obeh krajev
def skupno_zalivanje(ime1, ime2, domet, kraji):
    a = v_dometu(ime1, domet, kraji)
    b = v_dometu(ime2, domet, kraji)
    c = presek(a, b)
    return c







