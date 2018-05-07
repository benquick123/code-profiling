from collections import Counter

def migracije(ime_datoteke):
    kraji_odslo = Counter()
    kraji_prislo = Counter()
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        besede = vrstica.split()
        # Odstrani oklepaj
        stevilo = ""
        for c in besede[0]:
            if c != ":":
                stevilo = stevilo + c
        stevilo_int = int(stevilo)

        if besede[2] == "->":
            od = besede[1]
            if len(besede) == 4:
                do = besede[3]
            else:
                do = besede[3] + " " + besede[4]
        else:
            od = besede[1] + " " + besede[2]
            if len(besede) == 5:
                do = besede[4]
            else:
                do = besede[4] + " " + besede[5]

        kraji_odslo[od] += stevilo_int
        kraji_prislo[do] += stevilo_int

    max_odslo = ""
    max_vrednost = 0
    for ime, vrednost in kraji_odslo.items():
        if vrednost > max_vrednost:
            max_vrednost = vrednost
            max_odslo = ime

    max_prislo = ""
    max_vrednost = 0
    for ime, vrednost in kraji_prislo.items():
        if vrednost > max_vrednost:
            max_vrednost = vrednost
            max_prislo = ime

    datoteka.close()
    return (max_odslo, max_prislo)

from math import *

"""
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.kot = 0
        self.prehojeni_zakladi = []
        self.score = 1

    def naprej(self, d):
        rad = radians(self.kot)
        nx = self.x + d * cos(rad)
        ny = self.y + d * sin(rad)
        self.x = int(round(nx))
        self.y = int(round(ny))
        self.preveri_zaklad()

    def desno(self):
        self.kot -= 90

    def levo(self):
        self.kot += 90

    def koordinate(self):
        return self.x, self.y

    def preveri_zaklad(self):
        x, y = self.koordinate()
        if abs(x + y) % 7 == 0 and (x, y) not in self.prehojeni_zakladi:
            self.prehojeni_zakladi.append((x, y))
            self.score += 1

    def get_score(self):
        return self.score
"""

def zakladi(navodila):
    mr_robato = Robot()
    score = 1
    pot = [(0, 0)]
    for c in navodila:
        if c == "D":
            mr_robato.desno()
        elif c == "L":
            mr_robato.levo()
        else:
            mr_robato.naprej(int(c))
        x, y = mr_robato.koordinate()
        if (abs(x) + abs(y)) % 7 == 0 and (x, y) not in pot:
            score += 1
        pot.append((x, y))
    return score

def roboti(navodila, n):
    roboti = []
    for i in range(n):
        roboti.append(Robot())
    for robo_nr in range(n):
        for c in navodila[robo_nr::n]:
            if c == "S":
                if roboti[robo_nr].smer == 1:
                    roboti[robo_nr].levo()
                if roboti[robo_nr].smer == 2:
                    roboti[robo_nr].desno()
                    roboti[robo_nr].desno()
                if roboti[robo_nr].smer == 3:
                    roboti[robo_nr].desno()
            elif c == "J":
                if roboti[robo_nr].smer == 1:
                    roboti[robo_nr].desno()
                if roboti[robo_nr].smer == 4:
                    roboti[robo_nr].desno()
                    roboti[robo_nr].desno()
                if roboti[robo_nr].smer == 3:
                    roboti[robo_nr].levo()
            elif c == "V":
                if roboti[robo_nr].smer == 4:
                    roboti[robo_nr].desno()
                if roboti[robo_nr].smer == 2:
                    roboti[robo_nr].levo()
                if roboti[robo_nr].smer == 3:
                    roboti[robo_nr].levo()
                    roboti[robo_nr].levo()
            elif c == "Z":
                if roboti[robo_nr].smer == 2:
                    roboti[robo_nr].desno()
                if roboti[robo_nr].smer == 1:
                    roboti[robo_nr].levo()
                    roboti[robo_nr].levo()
                if roboti[robo_nr].smer == 4:
                    roboti[robo_nr].levo()
            roboti[robo_nr].naprej(1)
            roboti[robo_nr].smer = 1
    rezultat = []
    for robot in roboti:
        rezultat.append(robot.koordinate())
    return rezultat


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


