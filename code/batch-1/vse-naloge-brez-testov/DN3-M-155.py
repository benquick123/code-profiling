kraji = [
    ('Brežice', 68.66, 7.04), ('Lenart', 85.20, 78.75),
    ('Rateče', -65.04, 70.04),
    ('Ljutomer', 111.26, 71.82), ('Rogaška Slatina', 71.00, 42.00),
    ('Ribnica', 7.10, -10.50),
    ('Dutovlje', -56.80, -6.93), ('Lokve', -57.94, 19.32),
    ('Vinica', 43.81, -38.43),
    ('Brtonigla', -71.00, -47.25), ('Kanal', -71.00, 26.25),
    ('Črnomelj', 39.05, -27.93),
    ('Trbovlje', 29.61, 35.07), ('Beltinci', 114.81, 80.54),
    ('Domžale', -2.34, 31.50),
    ('Hodoš', 120.70, 105.00), ('Škofja Loka', -23.64, 35.07),
    ('Velike Lašče', 0.00, 0.00),
    ('Velenje', 33.16, 54.29), ('Šoštanj', 29.61, 57.75),
    ('Laško', 42.60, 33.29),
    ('Postojna', -29.54, -5.25), ('Ilirska Bistrica', -27.19, -27.93),
    ('Radenci', 100.61, 84.00), ('Črna', 15.41, 66.57),
    ('Radeče', 39.05, 24.57),
    ('Vitanje', 47.36, 57.75), ('Bled', -37.84, 56.07),
    ('Tolmin', -63.90, 36.75),
    ('Miren', -72.14, 7.04), ('Ptuj', 87.61, 61.32),
    ('Gornja Radgona', 97.06, 89.25),
    ('Plave', -73.34, 21.00), ('Novo mesto', 37.91, -3.47),
    ('Bovec', -76.89, 52.50),
    ('Nova Gorica', -69.79, 12.29), ('Krško', 60.35, 14.07),
    ('Cerknica', -18.89, -3.47),
    ('Slovenska Bistrica', 66.31, 57.75), ('Anhovo', -72.14, 22.78),
    ('Ormož', 107.71, 61.32),
    ('Škofije', -59.14, -27.93), ('Čepovan', -60.35, 22.78),
    ('Murska Sobota', 108.91, 87.57),
    ('Ljubljana', -8.24, 22.78), ('Idrija', -43.74, 17.54),
    ('Radlje ob Dravi', 41.46, 82.32),
    ('Žalec', 37.91, 43.79), ('Mojstrana', -49.70, 64.79),
    ('Log pod Mangartom', -73.34, 59.54), ('Podkoren', -62.69, 70.04),
    ('Kočevje', 16.61, -21.00), ('Soča', -69.79, 52.50),
    ('Ajdovščina', -53.25, 5.25),
    ('Bohinjska Bistrica', -48.49, 47.25), ('Tržič', -22.44, 56.07),
    ('Piran', -75.69, -31.50),
    ('Kranj', -20.09, 43.79), ('Kranjska Gora', -60.35, 68.25),
    ('Izola', -68.59, -31.50),
    ('Radovljica', -31.95, 54.29), ('Gornji Grad', 13.06, 49.03),
    ('Šentjur', 54.46, 40.32),
    ('Koper', -63.90, -29.72), ('Celje', 45.01, 42.00),
    ('Mislinja', 42.60, 66.57),
    ('Metlika', 48.56, -19.21), ('Žaga', -81.65, 49.03),
    ('Komen', -63.90, -1.68),
    ('Žužemberk', 21.30, 0.00), ('Pesnica', 74.55, 80.54),
    ('Vrhnika', -23.64, 14.07),
    ('Dravograd', 28.40, 78.75), ('Kamnik', -1.14, 40.32),
    ('Jesenice', -40.19, 64.79),
    ('Kobarid', -74.55, 43.79), ('Portorož', -73.34, -33.18),
    ('Muta', 37.91, 82.32),
    ('Sežana', -54.39, -13.96), ('Vipava', -47.29, 1.79),
    ('Maribor', 72.21, 75.28),
    ('Slovenj Gradec', 31.95, 71.82), ('Litija', 14.20, 22.78),
    ('Na Logu', -62.69, 57.75),
    ('Stara Fužina', -52.04, 47.25), ('Motovun', -56.80, -52.50),
    ('Pragersko', 73.41, 57.75),
    ('Most na Soči', -63.90, 33.29), ('Brestanica', 60.35, 15.75),
    ('Savudrija', -80.44, -34.96), ('Sodražica', 0.00, -6.93),
]


from math import *

# Obvezna naloga

kraj = "Ljubljana"
domet = 30

# Na tem mestu dopiši program

# poišči koordinate mesta, izpiši mesto in koordinate
kraj_x = kraj_y = 0
for mesto, x, y in kraji:
    if mesto == kraj:
        print(mesto, "je na koordinatah", x, y)
        kraj_x, kraj_y = x, y

# izračunaj razdaljo med izbranim krajem in mestom iz seznam; poglej, če ga lahko zadanemo
naj_razdalja = 0
zadeto_mesto = ''
for mesto, x, y in kraji:
    razdalja = sqrt((kraj_x - x)**2 + (kraj_y - y)**2)
    if naj_razdalja < razdalja < domet:
        naj_razdalja = razdalja
        zadeto_mesto = mesto
print("Iz kraja", kraj, "lahko zalijemo kraj", zadeto_mesto, "na razdalji", naj_razdalja)

# Dodatna naloga (kdor želi)

kraj1 = "Ljubljana"
kraj2 = "Bled"
domet = 30

# In tu dopiši program

# poišči in shrani koordinate obeh krajev
kraj1_x = kraj1_y = 0
kraj2_x = kraj2_y = 0
for mesto, x, y in kraji:
    if mesto == kraj1:
        kraj1_x, kraj1_y = x, y
    if mesto == kraj2:
        kraj2_x, kraj2_y = x, y

# izpiši mesta, ki jih kraja lahko družno zalivata
for mesto, x, y in kraji:
    razdalja_kraj1 = sqrt((kraj1_x - x)**2 + (kraj1_y - y)**2)
    razdalja_kraj2 = sqrt((kraj2_x - x)**2 + (kraj2_y - y)**2)
    if razdalja_kraj1 < domet and razdalja_kraj2 < domet:
        print(mesto)

# Čisto dodatna naloge

kraj1 = "Koper"
kraj2 = "Maribor"
domet = 30

# In tu pride program

"""Program ne deluje čisto pravilno ... za optimalno rešitev je verjetno potrebno uporabiti kakšen bolj sofisticiran
"informed search" algoritem, kot je na primer "A-star algorithm", katerega pa ne znam implementirati.
Čeprav mi ni uspela rešitev, moram reči, da sem se precej naučil ob reševanju te naloge.
V programu je pojasnjeno, kako sem poenostavil nalogo, da je rešljiva."""

kraj1 = "Koper"
kraj2 = "Maribor"
domet = 30

# ustvari slovar sosednjih mest, v katera lahko pridemo; razdalja mora biti manjša od 30
slovar = {}
for root_kraj, root_x, root_y in kraji:
    children = []
    for child_kraj, child_x, child_y in kraji:
        razdalja_do_sosednjih_mest = sqrt((root_x - child_x) ** 2 + (root_y - child_y) ** 2)
        """Na tem mestu sem problem poenostavil:
        Potrebno je oceniti spodnjo mejo koraka (omejiti število sosednjih mest), če želimo, da se program izvede v sprejemljivem času,
        in da ne zmanjka pomnilnika; jaz sem izbral 20; 
        s tem pogram odstrani sosedja mesta, ki so preblizu in bi jih bilo v večini primerov nesmiselno prečkati"""
        spodnja_meja = 20
        if spodnja_meja < razdalja_do_sosednjih_mest < domet:
            children.append(child_kraj)
    slovar[root_kraj] = children

# ustvari seznam, ki vsebuje sezname poti
poti = [[kraj1, ]]
najkrajsa_pot = False
for pot in poti:
    # shrani zadnji kraj poti
    zadnji_kraj = pot[-1]

    # Preveri, v katera mesta greš lahko naprej iz zadnjega kraja poti, shrani novo pot
    for mesto in slovar[zadnji_kraj]:
        nova_pot = list(pot)
        nova_pot.append(mesto)

        # Poglej, da ne greš nazaj v isto mesto
        if len(nova_pot) != len(set(nova_pot)):
            continue

        # Poglej, če si že prišel do cilja; to bo avtomatsko najkrajša pot, ker iščemo poti z dodajanjem mest
        if nova_pot[-1] == kraj2:
            for mesto in nova_pot:
                print(mesto)
            najkrajsa_pot = True
            break
        else:
            # dodaj novo pot v seznam poti, če nisi prišel do cilja
            poti.append(nova_pot)

    # Prekini, če si prišel do cilja
    if najkrajsa_pot:
        break