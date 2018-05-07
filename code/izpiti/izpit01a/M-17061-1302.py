def migracije(ime_datoteke):
    def odstrani_prazen_prostor(s):
        crke=True
        nov_string = ""
        c = 0
        while c < len(s):
            if s[c] == " " or not s[c].isalnum():
                c += 1
                continue


            else:

                nov_string = nov_string + s[c]
                crke = True
                c += 1
            if crke and c < len(s) - 3:
                nov_string = nov_string + s[c]
                crke = True
                c += 1

        return nov_string
    def izloci_podatke(vrstica):
        stevilo = int(vrstica.split(":")[0])

        napol = vrstica.split("->")
        odhod = odstrani_prazen_prostor(napol[0].split(":")[1])
        prihod = odstrani_prazen_prostor(napol[1])

        return stevilo, odhod, prihod

    file = open(ime_datoteke)

    migracije_dict = {}

    for line in file:
        stevilo, odhod, prihod = izloci_podatke(line)

        if odhod not in migracije_dict: migracije_dict[odhod]={"odhodi": 0, "prihodi": 0}
        else:
            migracije_dict[odhod]["odhodi"]+=stevilo
        if prihod not in migracije_dict: migracije_dict[prihod] ={"odhodi": 0, "prihodi": 0}
        else:
            migracije_dict[odhod]["prihodi"] += stevilo




    file.close()
    return migracije_dict


def zakladi(navodila):
    def preveri_zaklad(r):
        if r.razdalja()%7==0:
            return True
    robot = Robot()
    navodila_seznam = list(navodila)
    print(navodila_seznam)
    if not navodila_seznam: return 1
    najdeni_zakladi = 1
    zgodovina_koordinat = [(0,0)]
    for n in navodila_seznam:
        try:
            razdalja = int(n)
            robot.naprej(razdalja)
            if not robot.koordinate() in zgodovina_koordinat and preveri_zaklad(robot):
                najdeni_zakladi+=1
                zgodovina_koordinat.append(robot.koordinate())
        except:
            if n=="D":
                robot.desno()
                if not robot.koordinate() in zgodovina_koordinat and preveri_zaklad(robot):
                    najdeni_zakladi += 1
                    zgodovina_koordinat.append(robot.koordinate())
            if n=="L":
                robot.levo()
                if not robot.koordinate() in zgodovina_koordinat and preveri_zaklad(robot):
                    najdeni_zakladi += 1
                    zgodovina_koordinat.append(robot.koordinate())
    return najdeni_zakladi


def roboti(navodila, n):
    navodila_seznam = list(navodila)
    vsi_roboti = []
    for r in range(n):
        vsi_roboti.append(Robot())
    c = 0
    for navodilo in navodila_seznam:
        if c == n:
            c = 0

        if navodilo=="V":
            vsi_roboti[c].x+=1
        if navodilo == "J":
            vsi_roboti[c].y -= 1
        if navodilo == "Z":
            vsi_roboti[c].x -= 1
        if navodilo == "S":
            vsi_roboti[c].y += 1

        c += 1

    koordinate = []
    for r in vsi_roboti:
        koordinate.append((r.koordinate()))
    return koordinate


def brez_ponavljanja(s):
    pass

class Delitelj:
    def __init__(self, k):
        self.kolicnik = k
        self.cena = 0
    def akcija(self,s):
        c=0
        while c<len(s):
            if s[c]%self.kolicnik==0:
                s[c]=s[c]/self.kolicnik
                self.cena+=s[c]
            c+=1


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
