import collections
import os


def roboti(navodila, n):


    roboti = []
    for x in range(n):
        roboti.append((0, 0))


    dolzina = len(navodila)

    """
    for x in range(dolzina):
        ukaz = navodila[x]
        index_robot = 0
        if index_robot >= n:
            index_robot = 0

        if ukaz == "J":
            roboti[index_robot][1] -= 1
        elif ukaz == "S":
            roboti[index_robot][1] += 1
        elif ukaz == "V":

            roboti[index_robot][0] += 1

        elif ukaz == "Z":
            roboti[index_robot][0] -= 1


        index_robot += 1"""
    print(n)
    print(roboti)
    return roboti


print(roboti("V", 1))



def migracije(ime_datoteke):
    file = open(ime_datoteke)
    izvori = {}

    cilji = {}
    for x in file.readlines():
        vrsta = x.split(":")

        stevilo = int(vrsta[0])

        izvor = vrsta[1].split("->")[0].strip()

        cilj = vrsta[1].split("->")[1].strip()
        cilj = cilj.replace("\n", "")

        if cilj not in cilji:
            cilji[cilj] = stevilo
        else:
            cilji[cilj] = cilji[cilj] + stevilo

        if izvor not in izvori:
            izvori[izvor] = stevilo
        else:
            izvori[izvor] = izvori[izvor] + stevilo

    for x in izvori:
        max_izvori = x
        if izvori[x] > izvori[max_izvori]:
            max_izvori = x

    for x in cilji:
        max_cilji = x
        if cilji[x] > cilji[max_cilji]:
            max_cilji = x

    return max_izvori, max_cilji

def brez_ponavljanja(s):

    return s

class Delitelj:
    def __init__(self, stevilo):
        self.k = stevilo
        self.cena = 0

    def akcija(self, s):
        for x in range(len(s)):
            if s[x] % self.k == 0:

                self.cena += s[x] / self.k
                s[x] =  s[x] / self.k
            else:
                veckratnik = s[x] // self.k
                self.cena += s[x] - veckratnik * self.k
                self.cena += s[x] // self.k

        return s


deli5 = Delitelj(5)

deli5.akcija([5, 8, 9, 10])


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

R = Robot()

def zakladi(navodila):
    st_zakladov = 0
    st_zakladov += 1
    if len(navodila) > 0:

        for x in range(len(navodila) - 1):
            if navodila[x] == "D":
                R.desno()
            elif navodila[x] == "L":
                R.levo()
            else:
                R.naprej(int(navodila[x]))
            if abs(R.x + R.y) % 7 == 0:
                st_zakladov += 1

    return st_zakladov



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
