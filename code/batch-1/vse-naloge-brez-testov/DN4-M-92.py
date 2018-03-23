# Tu pišite svoje funkcije:
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

def koordinate(ime, seznam):
    for kraj, k1, k2 in seznam:
        if kraj == ime:
            return (k1, k2)
    return None
        
print(koordinate("Vitanje", kraji))


from math import *
def razdalja_koordinat(x1, y1, x2, y2):
    return sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)

print(razdalja_koordinat(0,0,1,1))


def razdalja(ime1, ime2, seznam):
    koo1 = koordinate(ime1, seznam)
    koo2 = koordinate(ime2, seznam)
    
    return razdalja_koordinat(koo1[0], koo1[1], koo2[0], koo2[1])

print(razdalja("Ljubljana", "Vipava", kraji))


#v_dometu(ime, domet, kraji) vrne seznam krajev, ki jih lahko zalije kraj ime, če ima top z dometom domet. Kraj ne zaliva sebe.
def v_dometu(ime, domet, kraji):
    v_dosegu = []
    for kraj, k1, k2 in kraji:
        x = razdalja(ime, kraj, kraji)
        if ime != kraj and x<=domet:
            v_dosegu.append(kraj)
    return v_dosegu
            
print(v_dometu("Vipava", 50, kraji))


#najbolj_oddaljeni(ime, imena, kraji) prejme ime nekega kraja, seznam imen nekih krajev (imena) in že običajni seznam terk z imeni in koordinatami krajev. Med kraji v seznamu imena (ne med vsemi kraji, temveč samo med temi!) mora vrniti ime tistega, ki je najbolj oddaljen od kraja ime. Če recimo, pokličemo najbolj_oddaljeni("Ljubljana", ["Domžale", "Kranj", "Maribor", "Vrhnika"], kraji), kjer so kraji vsi kraji iz prejšnje naloge, vrne "Maribor", saj je Maribor med temi štirimi kraji najdalj od Ljubljane

def najbolj_oddaljeni(ime, imena, kraji):
    najr = razdalja(ime, imena[0], kraji)
    najk = imena[0]
    for kraj in imena:
        x = razdalja(ime, kraj, kraji)
        if x > najr:
            najk = kraj
            najr = x
    return najk

print(najbolj_oddaljeni("Ljubljana", ["Domžale", "Kranj", "Maribor", "Vrhnika"], kraji))


#zalijemo(ime, domet, kraji) vrne ime najbolj oddaljenega kraja, ki ga lahko zalije kraj ime, če ima top z dometom domet
def zalijemo(ime, domet, kraji):
    najr = 0
    najk = None
    for ime0, k1, k2 in kraji:
        x = razdalja(ime, ime0, kraji)
        if x <= domet and x > najr and ime0 != ime:
            najr = x
            najk = ime0
    return najk

zalijemo("Vipava", 50, kraji)


#presek(s1, s2) prejme dva seznama in vrne seznam elementov, ki se pojavijo v obeh. Vrstni red elementov v vrnjenem seznamu je lahko poljuben.
def presek(s1, s2):
    skupni = []
    for el in s1:
        if el in s2:
            skupni.append(el)
    return skupni

print(presek([1, 2, 3],[2, 3, 4]))


#skupno_zalivanje(ime1, ime2, domet, kraji) prejme dve imeni krajev, domet vodnih topov, ki ju imajo v teh dveh krajih, in seznam vseh krajev. Vrniti mora seznam vseh krajev, ki jih lahko zalivamo iz obeh krajev.
def skupno_zalivanje(ime1, ime2, domet, kraji):    
    kraji1 = v_dometu(ime1, domet, kraji)
    kraji2 = v_dometu(ime2, domet, kraji)
    
    return presek(kraji1, kraji2)

skupno_zalivanje("Ljubljana", "Vipava", 150, kraji)

