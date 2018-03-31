import math

def koordinate(ime, kraji):
    for kraj , kordinata1 , kordinata2 in kraji:
        if ime == kraj:
            terka = (kordinata1, kordinata2)
            return(terka)
    return(None)

def razdalja_koordinat(x1, y1, x2, y2):
    kord1 = x2 - x1
    kord2 = y2 - y1
    razdalja = math.sqrt(kord1 ** 2 + kord2 ** 2)
    return(razdalja)

def razdalja(ime1, ime2, kraji):
    kor1 = koordinate(ime1, kraji)
    kor2 = koordinate(ime2, kraji)
    rezultat = razdalja_koordinat(kor1[0], kor1[1], kor2[0], kor2[1])
    return(rezultat)

def v_dometu(ime, domet, kraji):
    seznam = []

    for kraj, x, y in kraji:
        if kraj == ime:
            break

    for kraj2, x2, y2 in kraji:
        razdalja = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)

        if 0 < razdalja <= domet:
            seznam.append(kraj2)
    return (seznam)

def najbolj_oddaljeni(ime, imena, kraji):
    najdlje = 0
    najdlje_ime = ""

    k1 = 0
    y1 = 0

    for vsak in kraji:
        kraj, kordinata1, kordinata2 = vsak

        if kraj == ime:
            k1 = kordinata1
            y1 = kordinata2

    for vsak in kraji:
        kraj, kordinata1, kordinata2 = vsak

        k2 = kordinata1
        y2 = kordinata2

        kord1 = k2 - k1
        kord2 = y2 - y1

        razdalja = math.sqrt(kord1 ** 2 + kord2 ** 2)

        if razdalja > najdlje and kraj in imena:
            najdlje = razdalja
            najdlje_ime = kraj
    return (najdlje_ime)

def zalijemo(ime, domet, kraji):
    najdlje = 0
    najdlje_ime = ""

    k1 = 0
    y1 = 0

    for vsak in kraji:
        kraj, kordinata1, kordinata2 = vsak

        if ime == kraj:
            print(ime, "je na kordinatah", kordinata1, kordinata2)
            k1 = kordinata1
            y1 = kordinata2

    for vsak in kraji:
        kraj, kordinata1, kordinata2 = vsak

        k2 = kordinata1
        y2 = kordinata2

        kord1 = k2 - k1
        kord2 = y2 - y1

        razdalja = math.sqrt(kord1 ** 2 + kord2 ** 2)

        if razdalja < domet and razdalja > najdlje:
            najdlje = razdalja
            najdlje_ime = kraj
    return(najdlje_ime)

def presek(s1, s2):
    seznam = []
    for i in s1:
        for j in s2:
            if i == j:
                seznam.append(i)
    return (seznam)

def skupno_zalivanje(ime1, ime2, domet, kraji):
    k1 = 0
    y1 = 0
    k2 = 0
    y2 = 0

    seznam = []

    for vsak in kraji:
        ime, kordinata1, kordinata2 = vsak

        if ime == ime1:
            k1 = kordinata1
            y1 = kordinata2

        if ime == ime2:
            k2 = kordinata1
            y2 = kordinata2

    for vsak in kraji:
        ime, kordinata1, kordinata2 = vsak

        kord1 = k1 - kordinata1
        kord2 = y1 - kordinata2
        kordi1 = k2 - kordinata1
        kordi2 = y2 - kordinata2

        razdalja = math.sqrt(kord1 ** 2 + kord2 ** 2)
        razdalja2 = math.sqrt(kordi1 ** 2 + kordi2 ** 2)

        if razdalja < domet and razdalja2 < domet:
            seznam.append(ime)
    return(seznam)

"""====================================================="""

import unittest
class TestKraji(unittest.TestCase):
    vsi_kraji = [
        ('BreĹľice', 68.66, 7.04),
        ('Lenart', 85.20, 78.75),
        ('RateÄŤe', -65.04, 70.04),
        ('Ljutomer', 111.26, 71.82),
        ('RogaĹˇka Slatina', 71.00, 42.00),
        ('Ribnica', 7.10, -10.50),
        ('Dutovlje', -56.80, -6.93),
        ('Lokve', -57.94, 19.32),
        ('Vinica', 43.81, -38.43),
        ('Brtonigla', -71.00, -47.25),
        ('Kanal', -71.00, 26.25),
        ('ÄŚrnomelj', 39.05, -27.93),
        ('Trbovlje', 29.61, 35.07),
        ('Beltinci', 114.81, 80.54),
        ('DomĹľale', -2.34, 31.50),
        ('HodoĹˇ', 120.70, 105.00),
        ('Ĺ kofja Loka', -23.64, 35.07),
        ('Velike LaĹˇÄŤe', 0.00, 0.00),
        ('Velenje', 33.16, 54.29),
        ('Ĺ oĹˇtanj', 29.61, 57.75),
        ('LaĹˇko', 42.60, 33.29),
        ('Postojna', -29.54, -5.25),
        ('Ilirska Bistrica', -27.19, -27.93),
        ('Radenci', 100.61, 84.00),
        ('ÄŚrna', 15.41, 66.57),
        ('RadeÄŤe', 39.05, 24.57),
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
        ('KrĹˇko', 60.35, 14.07),
        ('Cerknica', -18.89, -3.47),
        ('Slovenska Bistrica', 66.31, 57.75),
        ('Anhovo', -72.14, 22.78),
        ('OrmoĹľ', 107.71, 61.32),
        ('Ĺ kofije', -59.14, -27.93),
        ('ÄŚepovan', -60.35, 22.78),
        ('Murska Sobota', 108.91, 87.57),
        ('Ljubljana', -8.24, 22.78),
        ('Idrija', -43.74, 17.54),
        ('Radlje ob Dravi', 41.46, 82.32),
        ('Ĺ˝alec', 37.91, 43.79),
        ('Mojstrana', -49.70, 64.79),
        ('Log pod Mangartom', -73.34, 59.54),
        ('Podkoren', -62.69, 70.04),
        ('KoÄŤevje', 16.61, -21.00),
        ('SoÄŤa', -69.79, 52.50),
        ('AjdovĹˇÄŤina', -53.25, 5.25),
        ('Bohinjska Bistrica', -48.49, 47.25),
        ('TrĹľiÄŤ', -22.44, 56.07),
        ('Piran', -75.69, -31.50),
        ('Kranj', -20.09, 43.79),
        ('Kranjska Gora', -60.35, 68.25),
        ('Izola', -68.59, -31.50),
        ('Radovljica', -31.95, 54.29),
        ('Gornji Grad', 13.06, 49.03),
        ('Ĺ entjur', 54.46, 40.32),
        ('Koper', -63.90, -29.72),
        ('Celje', 45.01, 42.00),
        ('Mislinja', 42.60, 66.57),
        ('Metlika', 48.56, -19.21),
        ('Ĺ˝aga', -81.65, 49.03),
        ('Komen', -63.90, -1.68),
        ('Ĺ˝uĹľemberk', 21.30, 0.00),
        ('Pesnica', 74.55, 80.54),
        ('Vrhnika', -23.64, 14.07),
        ('Dravograd', 28.40, 78.75),
        ('Kamnik', -1.14, 40.32),
        ('Jesenice', -40.19, 64.79),
        ('Kobarid', -74.55, 43.79),
        ('PortoroĹľ', -73.34, -33.18),
        ('Muta', 37.91, 82.32),
        ('SeĹľana', -54.39, -13.96),
        ('Vipava', -47.29, 1.79),
        ('Maribor', 72.21, 75.28),
        ('Slovenj Gradec', 31.95, 71.82),
        ('Litija', 14.20, 22.78),
        ('Na Logu', -62.69, 57.75),
        ('Stara FuĹľina', -52.04, 47.25),
        ('Motovun', -56.80, -52.50),
        ('Pragersko', 73.41, 57.75),
        ('Most na SoÄŤi', -63.90, 33.29),
        ('Brestanica', 60.35, 15.75),
        ('Savudrija', -80.44, -34.96),
        ('SodraĹľica', 0.00, -6.93),
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
            ('BreĹľice', 68.66, 7.04),
            ('Lenart', 85.20, 78.75),
            ('RateÄŤe', -65.04, 70.04),
            ('Ljutomer', 111.26, 71.82)
        ]

        self.assertEqual(koordinate("BreĹľice", kraji), (68.66, 7.04))
        self.assertEqual(koordinate("Lenart", kraji), (85.20, 78.75))
        self.assertEqual(koordinate("RateÄŤe", kraji), (-65.04, 70.04))
        self.assertEqual(koordinate("Ljutomer", kraji), (111.26, 71.82))
        self.assertIsNone(koordinate("Ljubljana", kraji))

        kraji = [('BreĹľice', 68.66, 7.04)]
        self.assertEqual(koordinate("BreĹľice", kraji), (68.66, 7.04))
        self.assertIsNone(koordinate("Lenart", kraji))

        kraji = []
        self.assertIsNone(koordinate("BreĹľice", kraji))

    def test_1_range_len(self):
        class NoGetItem(list):
            def __getitem__(*x):
                raise IndexError("NauÄŤi se (pravilno) uporabljati zanko for!")

        kraji = NoGetItem([('BreĹľice', 68.66, 7.04), ('Lenart', 85.20, 78.75),
                           ('RateÄŤe', -65.04, 70.04)])
        self.assertEqual(koordinate("BreĹľice", kraji), (68.66, 7.04))
        self.assertEqual(koordinate("Lenart", kraji), (85.20, 78.75))
        self.assertEqual(koordinate("RateÄŤe", kraji), (-65.04, 70.04))
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
            ('BreĹľice', 10, 20),
            ('Lenart', 13, 24),
            ('RateÄŤe', 17, 20),
            ('Ljutomer', 8, 36)
        ]

        from math import sqrt
        self.assertEqual(razdalja("BreĹľice", "Lenart", kraji), 5)
        self.assertEqual(razdalja("Lenart", "BreĹľice", kraji), 5)
        self.assertEqual(razdalja("BreĹľice", "RateÄŤe", kraji), 7)
        self.assertAlmostEqual(razdalja("Lenart", "RateÄŤe", kraji), sqrt(32))
        self.assertEqual(razdalja("Lenart", "Ljutomer", kraji), 13)

        koordinate.call_count = razdalja_koordinat.call_count = 0
        razdalja("BreĹľice", "Lenart", kraji)
        self.assertEqual(
            koordinate.call_count, 2,
            "Funkcija `razdalja` mora dvakrat poklicati `koordinate`")
        self.assertEqual(
            razdalja_koordinat.call_count, 1,
            "Funkcija `razdalja` mora enkrat poklicati `razdalja`")

    def test_4_v_dometu(self):
        kraji = [
            ('Lenart', 13, 24),
            ('BreĹľice', 10, 20),  # Lenart <-> BreĹľice = 5
            ('RateÄŤe', 17, 20),   # Lenart <-> RateÄŤe = 5.66
            ('Ljutomer', 8, 36)   # Lenart <-> Ljutomer = 13
        ]
        self.assertEqual(v_dometu("Lenart", 5, kraji), ["BreĹľice"])
        self.assertEqual(v_dometu("Lenart", 3, kraji), [])
        self.assertEqual(set(v_dometu("Lenart", 6, kraji)), {"BreĹľice", "RateÄŤe"})

        kraji = self.vsi_kraji
        self.assertEqual(set(v_dometu("Ljubljana", 20, kraji)), {'Vrhnika', 'DomĹľale', 'Kamnik', 'Ĺ kofja Loka'})

    def test_5_najbolj_oddaljeni(self):
        kraji = [
            ('Lenart', 13, 24),
            ('BreĹľice', 10, 20),  # Lenart <-> BreĹľice = 5
            ('RateÄŤe', 17, 20),   # Lenart <-> RateÄŤe = 5.66
            ('Ljutomer', 8, 36)   # Lenart <-> Ljutomer = 13
        ]
        self.assertEqual(najbolj_oddaljeni("Lenart", ["BreĹľice", "RateÄŤe"], kraji), "RateÄŤe")
        self.assertEqual(najbolj_oddaljeni("Lenart", ["BreĹľice"], kraji), "BreĹľice")

        kraji = self.vsi_kraji
        self.assertEqual(najbolj_oddaljeni("Ljubljana", ["DomĹľale", "Kranj", "Maribor", "Vrhnika"], kraji), "Maribor")

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
                         {"Kranj", "Ĺ kofja Loka"})


if __name__ == "__main__":
    unittest.main()

