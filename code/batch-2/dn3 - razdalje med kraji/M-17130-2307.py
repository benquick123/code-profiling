kraji = [
    ('Bre�ice', 68.66, 7.04), ('Lenart', 85.20, 78.75),
    ('Rate�e', -65.04, 70.04),
    ('Ljutomer', 111.26, 71.82), ('Roga�ka Slatina', 71.00, 42.00),
    ('Ribnica', 7.10, -10.50),
    ('Dutovlje', -56.80, -6.93), ('Lokve', -57.94, 19.32),
    ('Vinica', 43.81, -38.43),
    ('Brtonigla', -71.00, -47.25), ('Kanal', -71.00, 26.25),
    ('�rnomelj', 39.05, -27.93),
    ('Trbovlje', 29.61, 35.07), ('Beltinci', 114.81, 80.54),
    ('Dom�ale', -2.34, 31.50),
    ('Hodo�', 120.70, 105.00), ('�kofja Loka', -23.64, 35.07),
    ('Velike La��e', 0.00, 0.00),
    ('Velenje', 33.16, 54.29), ('�o�tanj', 29.61, 57.75),
    ('La�ko', 42.60, 33.29),
    ('Postojna', -29.54, -5.25), ('Ilirska Bistrica', -27.19, -27.93),
    ('Radenci', 100.61, 84.00), ('�rna', 15.41, 66.57),
    ('Rade�e', 39.05, 24.57),
    ('Vitanje', 47.36, 57.75), ('Bled', -37.84, 56.07),
    ('Tolmin', -63.90, 36.75),
    ('Miren', -72.14, 7.04), ('Ptuj', 87.61, 61.32),
    ('Gornja Radgona', 97.06, 89.25),
    ('Plave', -73.34, 21.00), ('Novo mesto', 37.91, -3.47),
    ('Bovec', -76.89, 52.50),
    ('Nova Gorica', -69.79, 12.29), ('Kr�ko', 60.35, 14.07),
    ('Cerknica', -18.89, -3.47),
    ('Slovenska Bistrica', 66.31, 57.75), ('Anhovo', -72.14, 22.78),
    ('Ormo�', 107.71, 61.32),
    ('�kofije', -59.14, -27.93), ('�epovan', -60.35, 22.78),
    ('Murska Sobota', 108.91, 87.57),
    ('Ljubljana', -8.24, 22.78), ('Idrija', -43.74, 17.54),
    ('Radlje ob Dravi', 41.46, 82.32),
    ('�alec', 37.91, 43.79), ('Mojstrana', -49.70, 64.79),
    ('Log pod Mangartom', -73.34, 59.54), ('Podkoren', -62.69, 70.04),
    ('Ko�evje', 16.61, -21.00), ('So�a', -69.79, 52.50),
    ('Ajdov��ina', -53.25, 5.25),
    ('Bohinjska Bistrica', -48.49, 47.25), ('Tr�i�', -22.44, 56.07),
    ('Piran', -75.69, -31.50),
    ('Kranj', -20.09, 43.79), ('Kranjska Gora', -60.35, 68.25),
    ('Izola', -68.59, -31.50),
    ('Radovljica', -31.95, 54.29), ('Gornji Grad', 13.06, 49.03),
    ('�entjur', 54.46, 40.32),
    ('Koper', -63.90, -29.72), ('Celje', 45.01, 42.00),
    ('Mislinja', 42.60, 66.57),
    ('Metlika', 48.56, -19.21), ('�aga', -81.65, 49.03),
    ('Komen', -63.90, -1.68),
    ('�u�emberk', 21.30, 0.00), ('Pesnica', 74.55, 80.54),
    ('Vrhnika', -23.64, 14.07),
    ('Dravograd', 28.40, 78.75), ('Kamnik', -1.14, 40.32),
    ('Jesenice', -40.19, 64.79),
    ('Kobarid', -74.55, 43.79), ('Portoro�', -73.34, -33.18),
    ('Muta', 37.91, 82.32),
    ('Se�ana', -54.39, -13.96), ('Vipava', -47.29, 1.79),
    ('Maribor', 72.21, 75.28),
    ('Slovenj Gradec', 31.95, 71.82), ('Litija', 14.20, 22.78),
    ('Na Logu', -62.69, 57.75),
    ('Stara Fu�ina', -52.04, 47.25), ('Motovun', -56.80, -52.50),
    ('Pragersko', 73.41, 57.75),
    ('Most na So�i', -63.90, 33.29), ('Brestanica', 60.35, 15.75),
    ('Savudrija', -80.44, -34.96), ('Sodra�ica', 0.00, -6.93),
]


from math import *
kraj = "Litija"
domet = 60
razdalja = 0
x1 = 0
y1 = 0
max_radalja = 0
max_ime = 0
for kraj1 in kraji:
    ime, x, y = kraj1

    if ime==kraj:
        print(ime, "je na koordinatah", x, y)
        x1 = x
        y1 = y
        break

for kraj1 in kraji:
    ime, x, y = kraj1
    razdalja = sqrt((x-x1)**2+(y-y1)**2)
    if max_radalja < razdalja <= domet:
        max_radalja = razdalja
        max_ime = ime
print("Iz kraja", kraj, "lahko zalijemo kraj", max_ime, "na razdalji", max_radalja)


# Dodatna naloga (kdor �eli)

kraj1 = "Ljubljana"
kraj2 = "Bled"
domet = 30
x1 = 0
x2 =0
y1 =0
y2 = 0
razdalja1=0
razdalja2 = 0
for kraj in kraji:
    ime, x, y = kraj

    if ime==kraj1:
        x1 = x
        y1 = y

    elif ime==kraj2:
        x2=x
        y2=y


for kraj in kraji:
    ime, x, y = kraj
    razdalja11 = sqrt((x - x1) ** 2 + (y - y1) ** 2)
    razdalja22 = sqrt((x - x2) ** 2 + (y - y2) ** 2)
    if razdalja11<domet and razdalja22<domet:
        print(ime)






