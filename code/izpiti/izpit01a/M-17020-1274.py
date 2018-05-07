
def migracije(ime_datoteke):
    najvec_izselilo = 0
    najvec_priselilo = 0
    naj_izseljen = ""
    naj_priseljen = ""
    izselilo = {}
    priselilo = {}
    for vrstica in open(ime_datoteke, encoding="UTF-8"):
        vrstica.strip()
        stevila = vrstica.split(":")
        stevilo = int(stevila[0])
        kraji = stevila[1]
        kraji = kraji.split("\n")
        kraji = kraji[0]
        k = kraji.split("->")
        izseli = k[0]
        priseli = k[1]
        if izseli not in izselilo:
            izselilo[izseli] = 0
        izselilo[izseli] += stevilo
        if priseli not in priselilo:
            priselilo[priseli] = 0
        priselilo[priseli] += stevilo
    for kraj, stevilo in izselilo.items():
        if stevilo > najvec_izselilo:
            najvec_izselilo = stevilo
            naj_izseljen = kraj
    for kraj, stevilo in priselilo.items():
        if stevilo > najvec_priselilo:
            najvec_priselilo = stevilo
            naj_priseljen = kraj
    return naj_izseljen, naj_priseljen


def zakladi(navodila):
    r = Robot()
    if not navodila:
        return 1
    else:
        polja = 0
        for e in navodila:
            if e == "D":
                r.desno()
            if e == "L":
                r.levo()
            if isinstance(e, int):
                r.naprej(e)
            x0, y0 = r.koordinate()
            if abs(x0 + y0) % 7 == 0:
                polja += 1
                zakladi.append(r.koordinate())
    return polja

def zakladi(navodila):
    z = [(0, 0)]
    r = Robot()
    if not navodila:
        return 1
    else:
        polja = 0
        for e in navodila:
            if e == "D":
                r.desno()
            elif e == "L":
                r.levo()
            else:
                r.naprej(int(e))
            x0, y0 = r.koordinate()
            if abs(x0 + y0) % 7 == 0:
                if r.koordinate() not in z:
                    polja += 1
                    z.append(r.koordinate())
    return len(z)


def roboti(navodila, n):
    x0, y0 = 0, 0
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    stevilo_navodil = int(len(navodila) / n)
    seznam = []
    prvi = navodila[::3]
    drugi = navodila[1::3]
    tretji = navodila[2::3]
    for navodilo in navodila:
        if navodilo in prvi:
            if navodilo == "J":
                y0 -= 1
            if navodilo == "S":
                y0 += 1
            if navodilo == "V":
                x0 += 1
            if navodilo == "Z":
                x0 -= 1
        if navodilo in drugi:
            if navodilo == "J":
                y1 -= 1
            if navodilo == "S":
                y1 += 1
            if navodilo == "V":
                x1 += 1
            if navodilo == "Z":
                x1 -= 1
        if navodilo in tretji:
            if navodilo == "J":
                y2 -= 1
            if navodilo == "S":
                y2 += 1
            if navodilo == "V":
                x2 += 1
            if navodilo == "Z":
                x2 -= 1
    return [(x0, y0), (x1, y1), (x2, y2)]


def brez_ponavljanja(s):
    if s[0] not in s[1:]:
        return s[0] + brez_ponavljanja(s[1:])
    else:
        return brez_ponavljanja(s[1:])

def brez_ponavljanja(s):
    x = []
    if not s:
        return x
    if s[0] not in x:
        x.append(s[0])
        return x + brez_ponavljanja(s[1:])

def brez_ponavljanja(s):
    x = []
    for e in s:
        if e not in x:
            x.append(e)
        return x

class Delitelj:
    def __init__(self, k):
        self.k = k
        self.cena = 0

    def akcija(self, s):
        for e in s:
            if e % self.k == 0:
                kolicnik = e / self.k
                self.cena += kolicnik


class Delitelj:
    def __init__(self, k):
        self.k = k
        self.cena = 0

    def akcija(self, s):
        for i, e in enumerate(s):
            if e % self.k == 0:
                kolicnik = e / self.k
                s.insert(i, e)
                del s[i + 1]
                self.cena += kolicnik

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
