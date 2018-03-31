def migracije(ime_datoteke):
    filename = ime_datoteke
    slovar_ven = {}
    slovar_not = {}
    with open(filename) as file_object:
        lines = file_object.readlines()
    seznam = []
    for vrstica in lines:

       #print(line.split()) # 8, MB, ->, LJ
        emi, imi = 0, 0
        this_line = vrstica.strip()
        seznam.append((this_line))
    for line in seznam:
        slovar_ven[line.split()[1]] = 0
        slovar_not[line.split()[3]] = 0

    for line in seznam:

        #dobim cifro v int
        cifra = ""
        for j in line.split()[0]:
            if j == ":": #zaradi nekega razloga mi tu noce cifre jemat, saj misli d da je dvopicje se noti
                slovar_ven[line[1]] += int(cifra)
                slovar_not[line[3]] += int(cifra)
            else: cifra += j
    max_ven = 0
    max_ven_place = ""
    for key in slovar_ven:
        if slovar_ven >= max_ven:
            max_ven = slovar_ven[key]
            if key == "Nova":
                max_ven_place == "Nova Gorica"
            else:
                max_ven_place = key

    max_not = 0
    max_not_place = ""
    for key in slovar_not:
        if slovar_not >= max_not:
            max_not = slovar_not[key]
            if key == "Nova":
                max_not_place == "Nova Gorica"
            else:
                max_not_place = key
    return (max_ven_place, max_not_place)





    return (slovar_ven, slovar_not)



class Robot():
    def __init__(self):
        self.x, self.y = 0, 0
        self.direction = "E"
        self.directions = "NESW"
        self.ismer = self.directions.index(self.direction)

    def naprej(self, d):
        if self.direction == "N":
            self.y += d
        if self.direction == "E":
            self.x += d
        if self.direction == "S":
            self.y -= d
        if self.direction == "W":
            self.x -= d

    def desno(self):
        self.direction = self.directions[(self.ismer + 1) % 4]
        self.ismer = self.directions.index(self.direction)

    def levo(self):
        self.direction = self.directions[(self.ismer - 1) % 4]
        self.ismer = self.directions.index(self.direction)

    def koordinate(self):
        return (self.x, self.y)

    def zakladi(self, navodila):
        self.zakladi = 1 # (0, 0)

        for ex in navodila:

            if ex == "D":
                self.desno()
            if ex == "L":
                self.levo()
            else:
                self.naprej(int(ex))
                if abs(self.x + self.y) % 7 == 0:
                    self.zakladi += 1
        return self.zakladi

def roboti(navodila, n): # "JSVZZVJ"
    slovarx, slovary = {}, {}

    while n!=0:
        slovarx[n] = 0
        slovary[n] = 0
        n = n - 1


    for i, ex in enumerate(navodila):
        cifra = 0
        kljuc = 1
        while cifra <= len(navodila):


            if ex == "S":
                slovary[kljuc] += 1
            if ex == "V":
                slovarx[kljuc] += 1
            if ex == "J":
                slovary[kljuc] -= 1
            if ex == "Z":
                slovarx[kljuc] -= 1
            if kljuc < 3:
                kljuc = kljuc + 1
            else:
                kljuc = 1
            cifra+=1
    seznam = []
    for n in range(1,3):
        seznam.append((slovarx[n], slovary[n]))

    return seznam

class Deljitelj():
    def __init__(self, k):
        self.glavno = k
        self.cena = 0

    def akcija(self, s):
        for st in s:
            if st % self.glavno == 0:
                self.cena+=int(st/self.glavno)
    def cena(self):
        return self.cena

def brez_ponavljanja(s):

    for i, ele in enumerate(s):
        if i-1 < len(s):
            if ele == s[i+1]:
                del s[i+1]
                return brez_ponavljanja(s)

#racunalnik je konstantno laggal (cetrtino vsega izpita je bil zmrznjen), dvakrat mi je pycharm tudi crashal


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
