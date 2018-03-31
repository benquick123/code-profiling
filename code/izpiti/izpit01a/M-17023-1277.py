import unittest
import collections

def migracije(ime_datoteke):
    datoteka = open(ime_datoteke, encoding='utf8')

    seznam_ven = collections.defaultdict(int)
    seznam_noter = collections.defaultdict(int)

    for vrstica in datoteka.readlines():
        vrstica = vrstica.split("->")
        vrstica[0] = vrstica[0].strip()
        vrstica[1] = vrstica[1].strip()
        vrstica = vrstica[0].split(":") + [vrstica[1]]
        vrstica[0] = vrstica[0].strip()
        vrstica[1] = vrstica[1].strip()



        print(vrstica[0],vrstica[1],vrstica[2])

        seznam_ven[vrstica[1]] += int(vrstica[0])
        seznam_noter[vrstica[2]] += int(vrstica[0])

    najv_ven = list(seznam_ven.keys())[0] # mesto
    najv_st = seznam_ven[najv_ven]   #st izseljencev

    for e in seznam_ven:
        mesto = e
        if seznam_ven[mesto] > najv_st:
            najv_ven = mesto
            najv_st = seznam_ven[mesto]

    najv_noter = list(seznam_noter.keys())[0]  # mesto
    najv_st = seznam_noter[najv_noter]  # st izseljencev

    for e in seznam_noter:
        mesto = e
        if seznam_noter[mesto] > najv_st:
            najv_noter = mesto
            najv_st = seznam_noter[mesto]

    #print(najv_ven)
    #print(najv_noter)
    datoteka.close()
    return(najv_ven,najv_noter)

def zakladi(navodila):
    zaklad = 1
    obiskana_polja = [(0,0)]
    moj_robot = Robot()
    for znak in navodila:
        if znak == "L":
            moj_robot.levo()
        elif znak == "D":
            moj_robot.desno()
        else:
            moj_robot.naprej(int(znak))

        if (abs(moj_robot.koordinate()[0]) + abs(moj_robot.koordinate()[1])) % 7 == 0:
            if moj_robot.koordinate() not in obiskana_polja:
                zaklad += 1
                obiskana_polja.append(moj_robot.koordinate())

    return zaklad

def roboti(navodila, n):
    trenutni_robot = 0
    seznam_robotov = []
    for i in range(n):
        seznam_robotov.append((0,0))

    for znak in navodila:
        if znak == "J":
            seznam_robotov[trenutni_robot] = (seznam_robotov[trenutni_robot][0],seznam_robotov[trenutni_robot][1]-1)
        if znak == "S":
            seznam_robotov[trenutni_robot] = (seznam_robotov[trenutni_robot][0], seznam_robotov[trenutni_robot][1] + 1)
        if znak == "Z":
            seznam_robotov[trenutni_robot] = (seznam_robotov[trenutni_robot][0] - 1, seznam_robotov[trenutni_robot][1])
        if znak == "V":
            seznam_robotov[trenutni_robot] = (seznam_robotov[trenutni_robot][0] + 1, seznam_robotov[trenutni_robot][1])

        trenutni_robot = (trenutni_robot+1)%n

    return seznam_robotov

def brez_ponavljanja(s):
    if len(s) == 1:
        return s

    if s == []:
        return s

    if s[0] != brez_ponavljanja(s[1:])[0]:
        return [s[0]] + brez_ponavljanja(s[1:])
    else:
        return brez_ponavljanja(s[1:])

class Delitelj:
    def __init__(self, k):
        self.cena = 0
        self.k = k

    def akcija(self, s):
        i = 0
        for e in s:

            if e % self.k == 0:
                #print(e, k)
                s[i] = e/self.k
                self.cena += s[i]
            i += 1

s = [25,8,15]
deli5 = Delitelj(5)
deli5.akcija(s)
print(s, "moj s")







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
