from math import sqrt
def koordinate(ime,kraji):
    for ime1,x,y in kraji:
        if ime1 == ime:
            return(x,y)
def razdalja_koordinat(x1, y1, x2, y2):
    razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return razdalja
def razdalja(ime1, ime2, kraji):
    for ime,x,y in kraji:
        if koordinate == ime1:
            x1 = x
            y1 = y
        if koordinate == ime2:
            x2 = x
            y2 = y
            razdalja = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return razdalja
def v_dometu(ime,domet,kraji):
    xs = [ ]
    for ime1,x,y in kraji:
        if ime == ime1:
            x1 = x
            y1 = y
    for ime1,x,y in kraji:
        razdalja = sqrt((x - x1) ** 2 + (y - y1) ** 2)
        if razdalja <= domet and ime != ime1:
            xs.append(ime1)
    return xs
def najbolj_oddaljeni(ime, imena, kraji):
    najvecja_razdalja = 0
    for ime1,x,y in kraji:
        if ime1 == ime:
            x1 = x
            y1 = y
    for ime2 in imena:
        for ime1,x,y in kraji:
            if ime1 == ime2:
                x2 = x
                y2 = y
        razdalja = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if razdalja > najvecja_razdalja:
            najvecja_razdalja = razdalja
            naj_oddaljen = ime2

    return naj_oddaljen
def zalijemo(ime, domet, kraji):
    naj_razdalja = 0
    for ime1,x,y in kraji:
        if ime1 == ime:
            x1 = x
            y1 = y
    for ime1,x,y in kraji:
        razdalja = sqrt((x - x1) ** 2 + (y - y1) ** 2)
        if razdalja < domet and ime != ime1 and razdalja> naj_razdalja:
            naj_razdalja = razdalja
            naj_oddaljen = ime1
    return naj_oddaljen
