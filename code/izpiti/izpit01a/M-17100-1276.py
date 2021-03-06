def migracije(ime_datoteke):
    datoteka = open("mesta", encoding="UTF8").read().split("\n")

    stevila = []
    iz_kje = []
    kam = []

    for stavek in datoteka:
        for i, znak in enumerate(stavek):
            if znak == ":":
                z = i+1
                stevila.append(int(stavek[0:i]))
            elif znak == "-":
                iz_kje.append(stavek[z+1:i-1])
                kam.append(stavek[i+3:len(stavek)])

    to = zip(stevila, iz_kje, kam)
    print(iz_kje)
    slovar = dict(iz_kje)
    for element in slovar:
        slovar[element] = 0
    for num, kje, kam in to:
        slovar[kje] -= num
        slovar[kam] += num

    max_kraj = str
    min_kraj = str
    max = 0
    min = 0

    for element in slovar:
        if slovar[element] < min:
            min = slovar[element]
            min_kraj = element
        elif slovar[element] > max:
            max = slovar[element]
            max_kraj = element

    return (min_kraj, max_kraj)


def zakladi(navodila):
    obiskana = [(0, 0)]
    zakladi = 0
    robotek = Robot()
    for ukaz in navodila:
        if ukaz == "L":
            robotek.levo()
        elif ukaz == "D":
            robotek.desno()
        else:
            koliko = int(ukaz)
            robotek.naprej(koliko)
            x, y = robotek.koordinate()
            if abs(x + y)%7 == 0 and (x, y) not in obiskana:
                zakladi += 1
                t = (x, y)
                obiskana.append(t)
            else:
                continue

    return zakladi








def roboti(navodila, n):
    robotki = []
    for i in range(n):
        t = (0, 0)
        robotki.append(t)
    i = 0
    while i < len(navodila):
        if navodila[i] == "S":
            x, y = robotki[i%n]
            x += 0
            y += 1
            robotki[i%n] = x, y
            i += 1
        elif navodila[i] == "J":
            x, y = robotki[i % n]
            x += 0
            y += -1
            robotki[i % n] = x, y
            i += 1
        elif navodila[i] == "V":
            x, y = robotki[i % n]
            x += 1
            y += 0
            robotki[i % n] = x, y
            i += 1
        elif navodila[i] ==  "Z":
            x, y = robotki[i % n]
            x += -1
            y += 0
            robotki[i % n] = x, y
            i += 1

    return robotki

def brez_ponavljanja(s):
    prvi = s[0]
    for element in s[1:]:
        if element == prvi:
            return brez_ponavljanja(s[1:])
        else:
            return brez_ponavljanja(s)


class Delitelj():
    def __init__(self, k):
        self.k = k
        self.cena = 0

    def akcija(self, s):
        for i, element in enumerate(s):
            if element%self.k  == 0:
                s[i] = element/self.k
                self.cena += s[i]
            else:
                continue

    def cena(self):
        return self.cena



import unittest


class Robot:
    def __init__(self):
        self.x = self.y = 0
        self.smer = 1



    def desno(self):
        self.smer = (self.smer + 1) % 4

    def levo(self):
        self.smer = (self.smer - 1) % 4

    def naprej(self, d):
        if self.smer == 0:
            self.y += d
        elif self.smer == 1:
            self.x += d
        elif self.smer == 2:
            self.y -= d
        else:
            self.x -= d

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)




class Test01Migracije(unittest.TestCase):
    def test_migracije(self):
        import os
        from random import randint
        fn = "m".format(randint(10000, 99999))
        try:
            with open(fn, "wt") as f:
                f.write("""8: Maribor -> Ljubljana
3: Maribor -> Nova Gorica
10: Ljubljana -> Maribor
5: Koper -> Nova Gorica
3: Novo mesto -> Nova Gorica
""")
            self.assertEqual(migracije(fn), ("Maribor", "Nova Gorica"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
3: Mb -> Ng
12: Lj -> Mb
5: Kp -> Ng
3: Nm -> Ng""")
            self.assertEqual(migracije(fn), ("Lj", "Mb"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
3: Mb -> Ng""")
            self.assertEqual(migracije(fn), ("Mb", "Lj"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
9: Ng -> Lj""")
            self.assertEqual(migracije(fn), ("Ng", "Lj"))

            with open(fn, "wt") as f:
                f.write("""11: Maribor -> Lj
5: Lj -> Celje
9: Ng -> Celje""")
            self.assertEqual(migracije(fn), ("Maribor", "Celje"))
        finally:
            os.remove(fn)


class Test02Zakladi(unittest.TestCase):
    def test_zakladi(self):
        self.assertEqual(zakladi(""), 1)
        self.assertEqual(zakladi("L"), 1)
        self.assertEqual(zakladi("LLL"), 1)
        self.assertEqual(zakladi("7"), 2)
        self.assertEqual(zakladi("77"), 3)
        self.assertEqual(zakladi("733"), 2)
        self.assertEqual(zakladi("7331"), 3)
        self.assertEqual(zakladi("7D32"), 2)
        self.assertEqual(zakladi("7D322"), 3)
        self.assertEqual(zakladi("7D3221LL"), 3)
        self.assertEqual(zakladi("7D322LL7"), 3)
        self.assertEqual(zakladi("7D322LL77"), 4)
        self.assertEqual(zakladi("7D331"), 3)
        self.assertEqual(zakladi("7D33D1"), 2)
        self.assertEqual(zakladi("7LLL77LLL"), 4)


class Test03Roboti(unittest.TestCase):
    def test_roboti(self):
        self.assertEqual(roboti("V", 1), [(1, 0)])
        self.assertEqual(roboti("Z", 1), [(-1, 0)])
        self.assertEqual(roboti("S", 1), [(0, 1)])
        self.assertEqual(roboti("J", 1), [(0, -1)])

        self.assertEqual(roboti("VZVZ", 2), [(2, 0), (-2, 0)])
        self.assertEqual(roboti("VZVZV", 2), [(3, 0), (-2, 0)])

        self.assertEqual(roboti("SJVZSJVZSJVZ", 4), [(0, 3), (0, -3), (3, 0), (-3, 0)])
        self.assertEqual(roboti("SJVZSJVZSJVZ", 12), 3 * [(0, 1), (0, -1), (1, 0), (-1, 0)])

        self.assertEqual(roboti("S", 3), [(0, 1), (0, 0), (0, 0)])
        self.assertEqual(roboti("", 300), 300 * [(0, 0)])
        self.assertEqual(roboti("SJ" * 100, 200), 100 * [(0, 1), (0, -1)])


class Test04BrezPonavljanja(unittest.TestCase):
    def test_brez_ponavljanja(self):
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 2]), [3, 1, 4, 2])
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 2, 1]), [3, 1, 4, 2, 1])
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 4, 15, 4, 2, 1]), [3, 1, 4, 15, 4, 2, 1])

        self.assertEqual(brez_ponavljanja([3, 42, 42]), [3, 42])
        self.assertEqual(brez_ponavljanja([42, 42, 3]), [42, 3])

        self.assertEqual(brez_ponavljanja([42, 42]), [42])
        self.assertEqual(brez_ponavljanja([42]), [42])
        self.assertEqual(brez_ponavljanja([]), [])


class Test05Delitelj(unittest.TestCase):
    def test_delitelj(self):
        deli1 = Delitelj(1)
        deli3 = Delitelj(3)
        deli5 = Delitelj(5)

        self.assertEqual(deli1.cena, 0)
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        s = [25, 8, 9, 15, 3, 81]

        self.assertIsNone(deli1.akcija(s))
        self.assertEqual(s, [25, 8, 9, 15, 3, 81])
        self.assertEqual(deli1.cena, sum(s))
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli1.akcija(s))
        self.assertEqual(s, [25, 8, 9, 15, 3, 81])
        self.assertEqual(deli1.cena, 2 * sum(s))
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli3.akcija(s))
        self.assertEqual(s, [25, 8, 3, 5, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [5, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, 5 + 1)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [1, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, (5 + 1) + 1)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [1, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, (5 + 1) + 1)

        self.assertIsNone(deli3.akcija(s))
        self.assertEqual(s, [1, 8, 1, 1, 1, 9])
        self.assertEqual(deli3.cena, (3 + 5 + 1 + 27) + (1 + 9))
        self.assertEqual(deli5.cena, (5 + 1) + 1)


if __name__ == "__main__":
    unittest.main()
