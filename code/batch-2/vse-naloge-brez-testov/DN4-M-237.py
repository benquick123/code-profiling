def koordinate(ime, kraji):
    for name,x,y in kraji:
        if name == ime:
            return(x,y)
        elif name == None:
            return None
def razdalja_koordinat(x1, y1, x2, y2):
    import math
    return math.sqrt(math.pow(x2-x1, 2)+ math.pow(y2-y1,2))

def razdalja(ime1, ime2, kraji):
    x_1, y_1 = koordinate(ime1, kraji)
    x_2, y_2 =koordinate(ime2, kraji)
    return razdalja_koordinat(x_1, y_1, x_2, y_2)

def v_dometu(ime, domet, kraji):
    x_1, y_1 = koordinate(ime, kraji)
    mesta = []
    for name, x_2, y_2 in kraji:
        razdalja = razdalja_koordinat(x_1, y_1, x_2, y_2)
        if razdalja <= domet and name != ime:
            mesta.append(name)
    return mesta


def najbolj_oddaljeni(ime, imena, kraji):
    x_1, y_1 = koordinate(ime, kraji)
    naj_oddaljeni = 0
    for name in imena:
        x_2, y_2 = koordinate(name, kraji)
        razdalja = razdalja_koordinat(x_1, y_2, x_2, y_2)
        if naj_oddaljeni<razdalja:
            naj_oddaljeni=razdalja
            naj_oddaljeni_ime = name
    return naj_oddaljeni_ime

def zalijemo(ime, domet, kraji):
    naj_razdalja = 0
    x_1, y_1 = koordinate(ime, kraji)
    for name, x, y in kraji:
        x_2 = x
        y_2 = y
        razdalja = razdalja_koordinat(x_1, y_1, x_2, y_2)
        if razdalja < domet :
            if naj_razdalja < razdalja:
                naj_razdalja = razdalja
                naj_ime = name
    return naj_ime
