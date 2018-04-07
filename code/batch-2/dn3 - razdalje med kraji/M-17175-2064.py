import math

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

# Funkcija za izračun razdalje med dvema točkama
def razdalja(x1, x2, y1, y2):
    return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))

zalivalec1_ime = "Ljubljana"
zalivalec1_domet = 30
zalivalec1 = None

# Najdi zalivalca 1
for kraj in kraji:
    ime, x, y = kraj
    if zalivalec1_ime in kraj:
        zalivalec1 = kraj
        print(ime, 'je na koordinatah', x, y)
        break

# Najdi max oddaljen kraj od zalivalca 1
max_oddaljen_kraj = ('', zalivalec1[1], zalivalec1[2])
for kraj in kraji:
    kraj_ime, x1, y1 = kraj
    if kraj != zalivalec1:
        zalivalec1_ime, x2, y2 = zalivalec1
        razd = razdalja(x1, x2, y1, y2)
        if razd <= zalivalec1_domet and razd > razdalja(max_oddaljen_kraj[1], x2, max_oddaljen_kraj[2], y2):
            max_oddaljen_kraj = kraj

if max_oddaljen_kraj[0]:
    print('Iz kraja', zalivalec1_ime, 'lahko zalijemo kraj', max_oddaljen_kraj[0], 'na razdalji', razdalja(max_oddaljen_kraj[1], zalivalec1[1], max_oddaljen_kraj[2], zalivalec1[2]))

zalivalci_imena = ("Ljubljana", "Bled")
zalivalci = []
zalivalci_domet = 30

# Najdi zalivalce v tabeli krajev
for kraj in kraji:
    ime, x, y = kraj
    for zalivalec_ime in zalivalci_imena:
        if zalivalec_ime in kraj:
            zalivalci.append(kraj)

# Najdemo, katere kraje lahko zalivalca družno zalivata
for kraj in kraji:
    kraj_ime, x1, y1 = kraj

    # Preskočimo kraje zalivalce.
    if kraj not in zalivalci:
        # Za vsakega zalivalca pogledamo, če je tarča v njegovem dometu
        for zalivalec in zalivalci:
            zalivalec_ime, x2, y2 = zalivalec

            razd = razdalja(x1, x2, y1, y2)
            if razd > zalivalci_domet:
                break
        # Če se zgornja zanka izvede brez breaka, torej če
        # lahko vsi zalivalci dosežejo tarčo ... potem izpišemo
        # ime tarče (kraja)
        else:
            print(kraj_ime)
            continue