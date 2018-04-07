import math

################################ WARM UP FUNCTIONS ####################################

### Function gives back coordinates of the city we choose.
def koordinate(ime, kraji):
    for imena in kraji:
        for data in imena:
            if ime == data:
                return imena[1], imena[2]

### Function gives back distance between coordinates of two points.
def razdalja_koordinat(x1, y1, x2, y2):
    distance = abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return distance

### Function gives back distance between two cities that we choose.
def razdalja(ime1, ime2, kraji):

### Function uses previous function "koordinate" to provide coordinates of chosen cities.
    koordinate1 = koordinate(ime1, kraji)
    koordinate2 = koordinate(ime2, kraji)

### When we have coordinates of cities we can use previous function "razdalja_koordinat" to calculate distance between chosen cities.
    distance = razdalja_koordinat(koordinate1[0], koordinate1[1], koordinate2[0], koordinate2[1])
    return distance

################################ OBLIGATORY FUNCTIONS ####################################

### Function gives back list of cities that chosen city can water with selected range.
def v_dometu(ime, domet, kraji):
    seznam = []
    for imena in kraji:

### We make sure that teh city will not try to water itself.
        if imena[0] != ime:

### We use previous function "razdalja" to calculate distances of each city in the dictionary.
            distance = razdalja(ime, imena[0], kraji)

### If distance is in selected range, we append city to the list that this function will return.
            if distance <= domet:
                seznam.append(imena[0])
    return seznam

### Function gives back the name of the city with maximum distance from the selected list of cities in relation to chosen city,
def najbolj_oddaljeni(ime, imena, kraji):

### We set the starting point of maximum distance to 0 and name to none, so we can replace them later with calculated values.
    maksimum = 0
    oddaljen_kraj = None

### In selected list of cities we calculate the distance of each in relation to the chosen city using previous function "razdalja".
    for data in imena:
        distance = razdalja(ime, data, kraji)

### If calculated distance is bigger than selected maximum, we replace the value of maximum with bigger distance and name with the name of the city that has bigger value.
        if distance > maksimum:
            maksimum = distance
            oddaljen_kraj = data
    return oddaljen_kraj

### Function gives back name of most distant city that a chosen city with selected range can water.
def zalijemo(ime, domet, kraji):

### We set the starting point of maximum distance to 0 and name to none, so we can replace them later with calculated values.
    maksimum = 0
    oddaljen_kraj = None

### We determine cities in the selected range of chosen cities with previous function "v_dometu".
    domet = v_dometu(ime, domet, kraji)

### For each city in selected range we calculate distance from chosen city with previous function "razdalja".
    for izbrani in domet:
        distance = razdalja(ime, izbrani, kraji)

### If calculated distance is bigger than selected maximum, we replace the value of maximum with bigger distance and name with the name of the city that has bigger value.
        if distance > maksimum:
            maksimum = distance
            oddaljen_kraj = izbrani
    return oddaljen_kraj

################################ EXTRA FUNCTIONS ####################################

### Function gives back list of elements that are appearing in both of chosen lists.
def presek(s1, s2):
    seznam = []
    for elements in s1:
        if elements in s2:
            seznam.append(elements)
    return seznam


### Function gives back list of cities that can be watered by both of chosen cities with selected range.
def skupno_zalivanje(ime1, ime2, domet, kraji):

### We determine cities in the selected range of chosen cities with previous function "v_dometu".
    domet1 = v_dometu(ime1, domet, kraji)
    domet2 = v_dometu(ime2, domet, kraji)

### We use previous function "presek" to determine cities that are in range of the first chosen city as of the second chosen city.
    skupaj = presek(domet1, domet2)
    return skupaj


################################ UNITTEST ####################################

import unittest
class TestKraji(unittest.TestCase):
    vsi_kraji = [
        ('Brežice', 68.66, 7.04),
        ('Lenart', 85.20, 78.75),
        ('Rateče', -65.04, 70.04),
        ('Ljutomer', 111.26, 71.82),
        ('Rogaška Slatina', 71.00, 42.00),
        ('Ribnica', 7.10, -10.50),
        ('Dutovlje', -56.80, -6.93),
        ('Lokve', -57.94, 19.32),
        ('Vinica', 43.81, -38.43),
        ('Brtonigla', -71.00, -47.25),
        ('Kanal', -71.00, 26.25),
        ('Črnomelj', 39.05, -27.93),
        ('Trbovlje', 29.61, 35.07),
        ('Beltinci', 114.81, 80.54),
        ('Domžale', -2.34, 31.50),
        ('Hodoš', 120.70, 105.00),
        ('Škofja Loka', -23.64, 35.07),
        ('Velike Lašče', 0.00, 0.00),
        ('Velenje', 33.16, 54.29),
        ('Šoštanj', 29.61, 57.75),
        ('Laško', 42.60, 33.29),
        ('Postojna', -29.54, -5.25),
        ('Ilirska Bistrica', -27.19, -27.93),
        ('Radenci', 100.61, 84.00),
        ('Črna', 15.41, 66.57),
        ('Radeče', 39.05, 24.57),
        ('Vitanje', 47.36, 57.75),
        ('Bled', -37.84, 56.07),
        ('Tolmin', -63.90, 36.75),
        ('Miren', -72.14, 7.04),
        ('Ptuj', 87.61, 61.32),
        ('Gornja Radgona', 97.06, 89.25),
        ('Plave', -73.34, 21.00),
        ('Novo mesto', 37.91, -3.47),
        ('Bovec', -76.89, 52.50),
        ('Nova Gorica', -69.79, 12.29),
        ('Krško', 60.35, 14.07),
        ('Cerknica', -18.89, -3.47),
        ('Slovenska Bistrica', 66.31, 57.75),
        ('Anhovo', -72.14, 22.78),
        ('Ormož', 107.71, 61.32),
        ('Škofije', -59.14, -27.93),
        ('Čepovan', -60.35, 22.78),
        ('Murska Sobota', 108.91, 87.57),
        ('Ljubljana', -8.24, 22.78),
        ('Idrija', -43.74, 17.54),
        ('Radlje ob Dravi', 41.46, 82.32),
        ('Žalec', 37.91, 43.79),
        ('Mojstrana', -49.70, 64.79),
        ('Log pod Mangartom', -73.34, 59.54),
        ('Podkoren', -62.69, 70.04),
        ('Kočevje', 16.61, -21.00),
        ('Soča', -69.79, 52.50),
        ('Ajdovščina', -53.25, 5.25),
        ('Bohinjska Bistrica', -48.49, 47.25),
        ('Tržič', -22.44, 56.07),
        ('Piran', -75.69, -31.50),
        ('Kranj', -20.09, 43.79),
        ('Kranjska Gora', -60.35, 68.25),
        ('Izola', -68.59, -31.50),
        ('Radovljica', -31.95, 54.29),
        ('Gornji Grad', 13.06, 49.03),
        ('Šentjur', 54.46, 40.32),
        ('Koper', -63.90, -29.72),
        ('Celje', 45.01, 42.00),
        ('Mislinja', 42.60, 66.57),
        ('Metlika', 48.56, -19.21),
        ('Žaga', -81.65, 49.03),
        ('Komen', -63.90, -1.68),
        ('Žužemberk', 21.30, 0.00),
        ('Pesnica', 74.55, 80.54),
        ('Vrhnika', -23.64, 14.07),
        ('Dravograd', 28.40, 78.75),
        ('Kamnik', -1.14, 40.32),
        ('Jesenice', -40.19, 64.79),
        ('Kobarid', -74.55, 43.79),
        ('Portorož', -73.34, -33.18),
        ('Muta', 37.91, 82.32),
        ('Sežana', -54.39, -13.96),
        ('Vipava', -47.29, 1.79),
        ('Maribor', 72.21, 75.28),
        ('Slovenj Gradec', 31.95, 71.82),
        ('Litija', 14.20, 22.78),
        ('Na Logu', -62.69, 57.75),
        ('Stara Fužina', -52.04, 47.25),
        ('Motovun', -56.80, -52.50),
        ('Pragersko', 73.41, 57.75),
        ('Most na Soči', -63.90, 33.29),
        ('Brestanica', 60.35, 15.75),
        ('Savudrija', -80.44, -34.96),
        ('Sodražica', 0.00, -6.93),
    ]

    class CountCalls:
        def __init__(self, f):
            self.f = f
            self.call_count = 0

        def __call__(self, *args, **kwargs):
            self.call_count += 1
            return self.f(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        global koordinate, razdalja_koordinat
        try:
            koordinate = cls.CountCalls(koordinate)
        except:
            pass
        try:
            razdalja_koordinat = cls.CountCalls(razdalja_koordinat)
        except:
            pass

    def test_1_koordinate(self):
        kraji = [
            ('Brežice', 68.66, 7.04),
            ('Lenart', 85.20, 78.75),
            ('Rateče', -65.04, 70.04),
            ('Ljutomer', 111.26, 71.82)
        ]

        self.assertEqual(koordinate("Brežice", kraji), (68.66, 7.04))
        self.assertEqual(koordinate("Lenart", kraji), (85.20, 78.75))
        self.assertEqual(koordinate("Rateče", kraji), (-65.04, 70.04))
        self.assertEqual(koordinate("Ljutomer", kraji), (111.26, 71.82))
        self.assertIsNone(koordinate("Ljubljana", kraji))

        kraji = [('Brežice', 68.66, 7.04)]
        self.assertEqual(koordinate("Brežice", kraji), (68.66, 7.04))
        self.assertIsNone(koordinate("Lenart", kraji))

        kraji = []
        self.assertIsNone(koordinate("Brežice", kraji))

    def test_1_range_len(self):
        class NoGetItem(list):
            def __getitem__(*x):
                raise IndexError("Nauči se (pravilno) uporabljati zanko for!")

        kraji = NoGetItem([('Brežice', 68.66, 7.04), ('Lenart', 85.20, 78.75),
                           ('Rateče', -65.04, 70.04)])
        self.assertEqual(koordinate("Brežice", kraji), (68.66, 7.04))
        self.assertEqual(koordinate("Lenart", kraji), (85.20, 78.75))
        self.assertEqual(koordinate("Rateče", kraji), (-65.04, 70.04))
        self.assertIsNone(koordinate("Ljubljana", kraji))

    def test_2_razdalja_koordinat(self):
        self.assertEqual(razdalja_koordinat(0, 0, 1, 0), 1)
        self.assertEqual(razdalja_koordinat(0, 0, 0, 1), 1)
        self.assertEqual(razdalja_koordinat(0, 0, -1, 0), 1)
        self.assertEqual(razdalja_koordinat(0, 0, 0, -1), 1)
        self.assertEqual(razdalja_koordinat(1, 0, 0, 0), 1)
        self.assertEqual(razdalja_koordinat(0, 1, 0, 0), 1)
        self.assertEqual(razdalja_koordinat(-1, 0, 0, 0), 1)
        self.assertEqual(razdalja_koordinat(0, -1, 0, 0), 1)

        self.assertEqual(razdalja_koordinat(1, 2, 4, 6), 5)
        self.assertEqual(razdalja_koordinat(1, 2, -2, 6), 5)
        self.assertEqual(razdalja_koordinat(1, 2, 4, -2), 5)
        self.assertEqual(razdalja_koordinat(1, 2, -2, -2), 5)

        from math import sqrt
        self.assertAlmostEqual(razdalja_koordinat(1, 2, 0, 1), sqrt(2))

    def test_3_razdalja_krajev(self):
        kraji = [
            ('Brežice', 10, 20),
            ('Lenart', 13, 24),
            ('Rateče', 17, 20),
            ('Ljutomer', 8, 36)
        ]

        from math import sqrt
        self.assertEqual(razdalja("Brežice", "Lenart", kraji), 5)
        self.assertEqual(razdalja("Lenart", "Brežice", kraji), 5)
        self.assertEqual(razdalja("Brežice", "Rateče", kraji), 7)
        self.assertAlmostEqual(razdalja("Lenart", "Rateče", kraji), sqrt(32))
        self.assertEqual(razdalja("Lenart", "Ljutomer", kraji), 13)

        koordinate.call_count = razdalja_koordinat.call_count = 0
        razdalja("Brežice", "Lenart", kraji)
        self.assertEqual(
            koordinate.call_count, 2,
            "Funkcija `razdalja` mora dvakrat poklicati `koordinate`")
        self.assertEqual(
            razdalja_koordinat.call_count, 1,
            "Funkcija `razdalja` mora enkrat poklicati `razdalja`")

    def test_4_v_dometu(self):
        kraji = [
            ('Lenart', 13, 24),
            ('Brežice', 10, 20),  # Lenart <-> Brežice = 5
            ('Rateče', 17, 20),   # Lenart <-> Rateče = 5.66
            ('Ljutomer', 8, 36)   # Lenart <-> Ljutomer = 13
        ]
        self.assertEqual(v_dometu("Lenart", 5, kraji), ["Brežice"])
        self.assertEqual(v_dometu("Lenart", 3, kraji), [])
        self.assertEqual(set(v_dometu("Lenart", 6, kraji)), {"Brežice", "Rateče"})

        kraji = self.vsi_kraji
        self.assertEqual(set(v_dometu("Ljubljana", 20, kraji)), {'Vrhnika', 'Domžale', 'Kamnik', 'Škofja Loka'})

    def test_5_najbolj_oddaljeni(self):
        kraji = [
            ('Lenart', 13, 24),
            ('Brežice', 10, 20),  # Lenart <-> Brežice = 5
            ('Rateče', 17, 20),   # Lenart <-> Rateče = 5.66
            ('Ljutomer', 8, 36)   # Lenart <-> Ljutomer = 13
        ]
        self.assertEqual(najbolj_oddaljeni("Lenart", ["Brežice", "Rateče"], kraji), "Rateče")
        self.assertEqual(najbolj_oddaljeni("Lenart", ["Brežice"], kraji), "Brežice")

        kraji = self.vsi_kraji
        self.assertEqual(najbolj_oddaljeni("Ljubljana", ["Domžale", "Kranj", "Maribor", "Vrhnika"], kraji), "Maribor")

    def test_6_zalijemo(self):
        self.assertEqual(zalijemo("Ljubljana", 30, self.vsi_kraji), "Cerknica")

    def test_7_presek(self):
        self.assertEqual(presek([1, 5, 2], [3, 1, 4]), [1])
        self.assertEqual(presek([1, 5, 2], [3, 0, 4]), [])
        self.assertEqual(presek([1, 5, 2], []), [])
        self.assertEqual(presek([], [3, 0, 4]), [])
        self.assertEqual(presek([], []), [])
        self.assertEqual(set(presek([1, 5, 2], [2, 0, 5])), {2, 5})

        self.assertEqual(presek(["Ana", "Berta", "Cilka"], ["Cilka", "Dani", "Ema"]), ["Cilka"])

    def test_8_skupno_zalivanje(self):
        self.assertEqual(set(skupno_zalivanje("Bled", "Ljubljana", 30, self.vsi_kraji)),
                         {"Kranj", "Škofja Loka"})


if __name__ == "__main__":
    unittest.main()

