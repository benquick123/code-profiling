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



def migracije(ime_datoteke):
    with open(ime_datoteke) as file:
        vrstice = file.read().splitlines()
    vrstice = [vrstica.split(": ") for vrstica in vrstice]
    vrstice = [[int(stevilo), ostalo.split(" -> ")] for stevilo, ostalo in vrstice]
    odhodi = {value1: 0 for key, [value1, value2] in vrstice}
    prihodi = {value2: 0 for key, [value1, value2] in vrstice}
    for stevilo, [value1, value2] in vrstice:
        odhodi[value1] += stevilo
    for stevilo, [value1, value2] in vrstice:
        prihodi[value2] += stevilo

    return max(odhodi, key=odhodi.get), max(prihodi, key=prihodi.get)


def roboti(navodila, s):
   slovar = {key: (0,0) for key in range(s)}
   koords = {"S": (0, 1), "J": (0, -1), "V": (1, 0), "Z": (-1, 0)}
   for num, ukaz in enumerate(navodila):
       x, y = koords[ukaz]
       x2, y2 = slovar[num%len(slovar)]
       slovar[num % len(slovar)] = (x+x2, y+y2)
   return [value for value in slovar.values()]





def zakladi(navodila):
   r = Robot()
   obiskano = set()
   zakladi = 1
   ukazi = list(navodila)
   ukazi = [int(ukaz) if ukaz != "L" and ukaz != "D" else ukaz for ukaz in ukazi]
   for ukaz in ukazi:
       if isinstance(ukaz, int):
           r.naprej(ukaz)
           x,y = r.koordinate()
           if (abs(x)+abs(y))%7 == 0 and (x,y) not in obiskano:
               obiskano.add((x, y))
               zakladi += 1
       elif ukaz == "D":
           r.desno()
       elif ukaz == "L":
           r.levo()
       else:
           print("error")
   return zakladi

class Delitelj:
   def __init__(self, k):
       self.k = k
       self.cena = 0

   def akcija(self, s):
       for num, item in enumerate(s):
           if item%self.k == 0:
               self.cena += item/self.k
               s[num] = item/self.k



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

'''
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

'''
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
