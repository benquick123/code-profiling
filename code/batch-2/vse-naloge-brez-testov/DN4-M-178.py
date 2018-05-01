from math import *

# Funkcije

def koordinate(ime, kraji):
    for mesto, koordinata_x, koordinata_y in kraji:
        if mesto == ime:
            return (koordinata_x, koordinata_y)
    return None

def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

def razdalja(ime1, ime2, kraji):
    koordinate1 = koordinate(ime1, kraji)
    koordinate2 = koordinate(ime2, kraji)
    return razdalja_koordinat(koordinate1[0] , koordinate1[1], koordinate2[0], koordinate2[1])

def v_dometu(ime, domet, kraji):
    seznam = []
    for mesto, koordinata_x, koordinata_y in kraji:
        if mesto == ime:
            for mesto2, koordinata_x_2, koordinata_y_2 in kraji:
                if mesto2 == mesto:
                    continue
                razdalja = sqrt(pow((koordinata_x_2 - koordinata_x), 2) + pow((koordinata_y_2 - koordinata_y), 2))
                if razdalja <= domet:
                    seznam.append(mesto2)
    return seznam

def najbolj_oddaljeni(ime, imena, kraji):
    najdaljse_mesto_razdalja = 0
    najdaljse_mesto = 0
    for mesto, koordinata_x, koordinata_y in kraji:
        if mesto == ime:
            for mesto_terka in imena:
                for mesto2, koordinata_x_2, koordinata_y_2 in kraji:
                    if(mesto_terka == mesto2):
                        razdalja = sqrt(
                            pow((koordinata_x_2 - koordinata_x), 2) + pow((koordinata_y_2 - koordinata_y), 2))
                        if(razdalja > najdaljse_mesto_razdalja):
                            najdaljse_mesto_razdalja = razdalja
                            najdaljse_mesto = mesto_terka
    return najdaljse_mesto

def zalijemo(ime, domet, kraji):
    razdalja = 0
    najvecje_zalito_mesto = 0
    zalito_mesto = 0
    for mesto, koordinata_x, koordinata_y in kraji:
        if mesto == ime:
            for mesto2, koordinata_x_2, koordinata_y_2 in kraji:
                razdalja = sqrt(pow((koordinata_x_2 - koordinata_x), 2) + pow((koordinata_y_2 - koordinata_y), 2))

                if razdalja < domet:
                    if razdalja > najvecje_zalito_mesto:
                        najvecje_zalito_mesto = razdalja
                        zalito_mesto = mesto2
    return zalito_mesto

def presek(s1, s2):
    seznam = []
    for stevilo1 in s1:
        for stevilo2 in s2:
            if(stevilo2 == stevilo1):
                seznam.append(stevilo1)
    return seznam

def skupno_zalivanje(ime1, ime2, domet, kraji):
    razdalja_1 = 0
    razdalja_2 = 0
    seznam = []
    for mesto_1, koordinata_x_1, koordinata_y_1 in kraji:
        for mesto_2, koordinata_x_2, koordinata_y_2 in kraji:
            if mesto_1 == ime1 and mesto_2 == ime2:

                for mesto_za_zalit, koordinata_x_za_zalit, koordinata_y_za_zalit in kraji:
                    razdalja_1 = sqrt(
                        pow((koordinata_x_za_zalit - koordinata_x_1), 2) + pow((koordinata_y_za_zalit - koordinata_y_1),
                                                                               2))
                    razdalja_2 = sqrt(
                        pow((koordinata_x_za_zalit - koordinata_x_2), 2) + pow((koordinata_y_za_zalit - koordinata_y_2),
                                                                               2))
                    if razdalja_1 < domet and razdalja_2 < domet:
                        seznam.append(mesto_za_zalit)
    return seznam


# Seznam krajev

kraji = [
    ('Brežice', 68.66, 7.04), ('Lenart', 85.20, 78.75), ('Rateče', -65.04, 70.04),
    ('Ljutomer', 111.26, 71.82), ('Rogaška Slatina', 71.00, 42.00), ('Ribnica', 7.10, -10.50),
    ('Dutovlje', -56.80, -6.93), ('Lokve', -57.94, 19.32), ('Vinica', 43.81, -38.43),
    ('Brtonigla', -71.00, -47.25), ('Kanal', -71.00, 26.25), ('Črnomelj', 39.05, -27.93),
    ('Trbovlje', 29.61, 35.07), ('Beltinci', 114.81, 80.54), ('Domžale', -2.34, 31.50),
    ('Hodoš', 120.70, 105.00), ('Škofja Loka', -23.64, 35.07), ('Velike Lašče', 0.00, 0.00),
    ('Velenje', 33.16, 54.29), ('Šoštanj', 29.61, 57.75), ('Laško', 42.60, 33.29),
    ('Postojna', -29.54, -5.25), ('Ilirska Bistrica', -27.19, -27.93),
    ('Radenci', 100.61, 84.00), ('Črna', 15.41, 66.57), ('Radeče', 39.05, 24.57),
    ('Vitanje', 47.36, 57.75), ('Bled', -37.84, 56.07), ('Tolmin', -63.90, 36.75),
    ('Miren', -72.14, 7.04), ('Ptuj', 87.61, 61.32), ('Gornja Radgona', 97.06, 89.25),
    ('Plave', -73.34, 21.00), ('Novo mesto', 37.91, -3.47), ('Bovec', -76.89, 52.50),
    ('Nova Gorica', -69.79, 12.29), ('Krško', 60.35, 14.07), ('Cerknica', -18.89, -3.47),
    ('Slovenska Bistrica', 66.31, 57.75), ('Anhovo', -72.14, 22.78), ('Ormož', 107.71, 61.32),
    ('Škofije', -59.14, -27.93), ('Čepovan', -60.35, 22.78), ('Murska Sobota', 108.91, 87.57),
    ('Ljubljana', -8.24, 22.78), ('Idrija', -43.74, 17.54), ('Radlje ob Dravi', 41.46, 82.32),
    ('Žalec', 37.91, 43.79), ('Mojstrana', -49.70, 64.79),
    ('Log pod Mangartom', -73.34, 59.54), ('Podkoren', -62.69, 70.04),
    ('Kočevje', 16.61, -21.00), ('Soča', -69.79, 52.50), ('Ajdovščina', -53.25, 5.25),
    ('Bohinjska Bistrica', -48.49, 47.25), ('Tržič', -22.44, 56.07), ('Piran', -75.69, -31.50),
    ('Kranj', -20.09, 43.79), ('Kranjska Gora', -60.35, 68.25), ('Izola', -68.59, -31.50),
    ('Radovljica', -31.95, 54.29), ('Gornji Grad', 13.06, 49.03), ('Šentjur', 54.46, 40.32),
    ('Koper', -63.90, -29.72), ('Celje', 45.01, 42.00), ('Mislinja', 42.60, 66.57),
    ('Metlika', 48.56, -19.21), ('Žaga', -81.65, 49.03), ('Komen', -63.90, -1.68),
    ('Žužemberk', 21.30, 0.00), ('Pesnica', 74.55, 80.54), ('Vrhnika', -23.64, 14.07),
    ('Dravograd', 28.40, 78.75), ('Kamnik', -1.14, 40.32), ('Jesenice', -40.19, 64.79),
    ('Kobarid', -74.55, 43.79), ('Portorož', -73.34, -33.18), ('Muta', 37.91, 82.32),
    ('Sežana', -54.39, -13.96), ('Vipava', -47.29, 1.79), ('Maribor', 72.21, 75.28),
    ('Slovenj Gradec', 31.95, 71.82), ('Litija', 14.20, 22.78), ('Na Logu', -62.69, 57.75),
    ('Stara Fužina', -52.04, 47.25), ('Motovun', -56.80, -52.50), ('Pragersko', 73.41, 57.75),
    ('Most na Soči', -63.90, 33.29), ('Brestanica', 60.35, 15.75),
    ('Savudrija', -80.44, -34.96), ('Sodražica', 0.00, -6.93),
]


# Vnosi in izpisi

ime = "Ljubljana"
print(koordinate(ime, kraji), "\n")

x1 = 4
y1 = 3
x2 = 7
y2 = 2
print("Razdalja med točkama je:", razdalja_koordinat(int(x1), int(y1), int(x2), int(y2)), "\n")

ime1 = "Ljubljana"
ime2 = "Celje"
print("Razdalja med krajema je:", razdalja(ime1, ime2, kraji), "\n")

domet = 40
ime = "Slovenj Gradec"
print(v_dometu(ime, domet, kraji), "\n")

ime = "Ljubljana"
imena = ["Domžale", "Kranj", "Maribor", "Vrhnika"]
print(najbolj_oddaljeni(ime, imena, kraji), "\n")

domet = 40
ime = "Maribor"
print(zalijemo(ime, domet, kraji), "\n")

s1 = [4, 3, 44, 15, 20, 18, 101]
s2 = [6, 44, 18, 8, 33, 20, 31]
print("Skupna števila obeh seznamov so:", presek(s1, s2), "\n")

ime1 = "Celje"
ime2 = "Slovenj Gradec"
domet = 30
print(skupno_zalivanje(ime1, ime2, domet, kraji), "\n")


# Tester

