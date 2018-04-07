from math import sqrt

def najoddaljenkrajvdometu(lokacija, domet, kraji):
    najoddaljenkraj = vsikrajivdometu(lokacija, domet, kraji)[-1]
    return najoddaljenkraj

def razdaljamedkrajema(kraj1, kraj2):
    kraj1x = kraj1[1]
    kraj1y = kraj1[2]
    kraj2x = kraj2[1]
    kraj2y = kraj2[2]
    razdaljaX = abs(kraj1x - kraj2x)
    razdaljaY = abs(kraj1y - kraj2y)
    razdalja = sqrt(razdaljaX ** 2 + razdaljaY ** 2)
    return razdalja

def vsikrajivdometu(lokacija, domet, kraji):
    x = lokacija[1]
    y = lokacija[2]
    krajivdosegu = []
    for imekraja, krajX, krajY in kraji:
        razdaljaX = abs(x - krajX)
        razdaljaY = abs(y - krajY)
        if (razdaljaX > domet or razdaljaY > domet or razdaljaX == razdaljaY == 0):
            # V tem primeru lokacija zagotovo ni v dometu in ga lahko ignoriramo
            continue
        else:
            razdalja = sqrt(razdaljaX ** 2 + razdaljaY ** 2)
            if (razdalja <= domet):
                krajivdosegu.append((imekraja, krajX, krajY, razdalja))
    # Sortiraj po razdalji naraščajoče
    sortirano = sorted(krajivdosegu, key=lambda x: x[3])
    # Nočem razdalje imet v vrnjenem seznamu
    return [(kraj[0], kraj[1], kraj[2]) for kraj in sortirano]

def skupnikrajivdometu(kraj1 ,kraj2, domet):
    vdosegukraja1 = vsikrajivdometu(kraj1, domet, kraji)
    vdosegukraja2 = vsikrajivdometu(kraj2, domet, kraji)
    # Vrne seznam skupnih krajev
    return list(set(vdosegukraja1) & set(vdosegukraja2))

def najblizjikrajcilju(kraji, cilj):
    najblizjikraj = None
    i = 0
    for kraj in kraji:
        razdalja =razdaljamedkrajema(kraj, cilj)
        if(i == 0):
            najmrazdalja = razdalja
        if(razdalja <= najmrazdalja):
            najmrazdalja = razdalja
            najblizjikraj = kraj
        i += 1
    return najblizjikraj

def najdikraj(imekraja, kraji):
    return [kraj for kraj in kraji if kraj[0] == imekraja][0]

#----------------------------------------------------------------------------------------------------------------------#

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

# Obvezna naloga

imekraja = "Ljubljana"
domet = 30

# Na tem mestu dopiši program

izvirnikraj = najdikraj(imekraja, kraji)
print(izvirnikraj)
najkrajvdometu = najoddaljenkrajvdometu(izvirnikraj, domet, kraji)
print("Najbolj oddaljen kraj od '"
      +imekraja
      +"', ki ga lahko doseže vodni top z dometom",
      domet, "je '"+najkrajvdometu[0]
      +"' in sicer na razdalji",
      razdaljamedkrajema(izvirnikraj, najkrajvdometu))

# Dodatna naloga (kdor želi)

imekraj1 = "Ljubljana"
imekraj2 = "Bled"
domet = 30

# In tu dopiši program

kraj1 = najdikraj(imekraj1, kraji)
kraj2 = najdikraj(imekraj2, kraji)
skupni = skupnikrajivdometu(kraj1, kraj2, domet)
print ("Skupni kraji v dometu:")
for kraj in skupni:
    print("\t", kraj[0])

# Čisto dodatna naloga

imekraj1 = "Koper"
imekraj2 = "Maribor"
domet = 30

# In tu pride program
'''
Ta rešitev je pomanjkljiva, ker lahko pride do neskončnih zank.
Moral bi si več prebrat o algoritmih za iskanje poti kot so Dijkstrin in A*.
'''
start = najdikraj(imekraj1, kraji)
cilj = najdikraj(imekraj2, kraji)
pot = []
trenutenkraj = start
prispelnacilj = False
while(trenutenkraj != cilj):
    vsivdometutrenutnega = vsikrajivdometu(trenutenkraj, domet, kraji)
    for kraj in vsivdometutrenutnega:
        if(kraj == cilj):
            pot.append(kraj)
            prispelnacilj = True
    if(prispelnacilj == True):
        trenutenkraj = cilj
    else:
        neprehojenikraji = list(set(vsivdometutrenutnega) - set(pot))
        # Kraj najbližje cilju, ki še ni bil prehojen
        krajnajblizjecilju = najblizjikrajcilju(neprehojenikraji, cilj)
        # Tu bi še moral dodat preverjanje če so vsi kraji v dometu že bili prehojeni
        trenutenkraj = krajnajblizjecilju
        pot.append(trenutenkraj)
print("Pot od",start[0], "do", cilj[0], ":")
print("\t", start[0])
for kraj in pot:
    print("\t", kraj[0])



