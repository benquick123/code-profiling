def migracije(ime_datoteke):
    listkraji = [("Maribor", 0, 0), ("Ljubljana", 0, 0), ("Nova Gorica", 0, 0), ("Koper", 0, 0), ("Novo Mesto", 0 ,0)]
    datoteka = open(ime_datoteke)
    maxi = ("Ljubljana", -10)
    maxv = ("Ljubljana", -10)
    for vrstica in datoteka:
        zapst = 0
        vrs = vrstica.split(" ")
        prebivalci = int(vrs[0].split(":")[0])
        kraj_izselitve =  vrs[1]
        kraj_vselitve = vrstica.split("->")[1].strip()
        for (kraj, izselitve, vselitve) in listkraji:
            if kraj == kraj_izselitve:
                izselitve += prebivalci
                vselitve -= prebivalci
                listkraji[zapst] = (kraj, izselitve, vselitve)
            if kraj == kraj_vselitve:
                vselitve += prebivalci
                izselitve += prebivalci
                listkraji[zapst] = (kraj, izselitve, vselitve)
            zapst += 1
        for (kraj, izselitve, vselitve) in listkraji:
            if izselitve > maxi[1]:
                maxi = (kraj, izselitve)
            if vselitve > maxv[1]:
                maxv = (kraj, vselitve)

        return (maxi[0], maxv[0])
def migracije(ime_datoteke):
        listkraji = [("Maribor", 0), ("Ljubljana", 0), ("Nova Gorica", 0), ("Koper", 0),
                     ("Novo Mesto", 0)]
        datoteka = open(ime_datoteke)
        maxi = ("Ljubljana", 0)
        maxv = ("Ljubljana", 0)
        for vrstica in datoteka:
            vrs = vrstica.split(" ")
            prebivalci = int(vrs[0].split(":")[0])
            kraj_izselitve = vrs[1]
            kraj_vselitve = vrstica.split("->")[1].strip()
            stevec = 0
            for (kraj, stevilo) in listkraji:
                if kraj == kraj_izselitve:
                    stevilo -= prebivalci
                    listkraji[stevec] = (kraj, stevilo)
                if kraj == kraj_vselitve:
                    stevilo += prebivalci
                    listkraji[stevec] = (kraj, stevilo)
                stevec += 1
        for i in listkraji:
            if i[1] < maxv[1]:
                maxv = i
            if i[1] > maxi[1]:
                maxi = i

            return(maxv[0], maxi[0])

def zakladi(navodila):
    r = Robot
    ins = navodila.split()
    for i in ins:
        if i == "D":
            r.desno()
        elif i == "L":
            r.levo()
        else:
            r.naprej(i)

def roboti(navodila, n):
    robot = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    stevec = 0
    for num in range(0, n):
        robot.append((0,0))
    if navodila == "S":
        (x, y) = robot[stevec]
        robot[stevec] = (x, y + 1)
    elif navodila == "J":
        (x, y) = robot[stevec]
        robot[stevec] = (x, y - 1)
    elif navodila == "V":
        (x, y) = robot[stevec]
        robot[stevec] = (x + 1, y)
    elif navodila == "Z":
        (x, y) = robot[stevec]
        robot[stevec] = (x - 1, y)
    stevec += 1
    if stevec > n:
        stevec = 0
    return robot

class Delitelj:
    def __init__(self, k):
        self.stevilo = k
        self.cena = 0
    def akcija(self, s):
        for stev in s:
            if stev % self.stevilo == 0:
                temp = stev / self.stevilo
                self.cena += temp

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
