import collections

def nogavice(s):
    u = []
    t = collections.Counter(s)
    for nogavica,stevilo in t.items():
        if stevilo % 2 != 0:
            u.append(nogavica)
    return u


def bingo(listki,vrstni_red):
    u = []
    v = []
    z = []
    for a in listki[0]:
        if a in vrstni_red:
            u.append(a)
            listki[0].remove(a)
    for a in listki[1]:
        if a in vrstni_red:
            v.append(a)
            listki[1].remove(a)
    for a in listki[2]:
        if a in vrstni_red:
            z.append(a)
            listki[2].remove(a)

    if len(u)>len(v) and len(u)>len(z):
        return u
    if len(z) > len(u) and len(z) > len(v):
        return z
    if len(v) > len(u) and len(v) > len(z):
        return v





def selitve(zacetek, datoteka_selitev, kraj):
    s = set()
    for vrstica in open(datoteka_selitev):
        for beseda in vrstica.split():
            for mesto, oseba in zacetek:
                if mesto == kraj:
                    s.add(oseba)
                if beseda[-1]==kraj:
                    if beseda == mesto:
                        s.add(oseba)
    return s




def brez_para(nogavica, nogavice):
    u = []
    if not nogavice:
        return True
    for a in nogavice:
        if nogavica==a:
            u.append(a)
    if len(u)%2 != 0:
        return True
    else:
        return False

class Sledilnik:
    def __init__(self,zacetek):
        self.zacetek = zacetek
    def kje_zivi(self,oseba):
        return self.zacetek[0]
    def prebivalci(self,kraj):
        i = 0
        s = set()
        for a in self.zacetek:
            if a[i][0] == a[i+1][0]:
                s.add(a[i][1])
    def preseli(self,oseba,kraj):
        for a in self.zacetek:
            if oseba == a[1]:
                if kraj == a[0]:
                    self.zacetek[a]=kraj,oseba
    def preseli_vse(self,odkod,kam):
        for a in self.zacetek:
            if a[0] == odkod:
                self.zacetek.pop()
    def selitev(self):
        v = 0



import unittest

class Test01Nogavice(unittest.TestCase):
    def test_nogavice(self):
        self.assertEqual(nogavice([1, 2, 3, 2, 3, 1, 3, 1, 1, 1, 1]), [3])
        self.assertEqual(nogavice([1, 2, 3, 2, 3, 3, 4, 1]), [3, 4])
        self.assertEqual(nogavice([1, 4, 2, 3, 2, 3, 3, 1]), [4, 3])
        self.assertEqual(nogavice([1, 1, 4, 1, 3, 1]), [4, 3])
        self.assertEqual(nogavice([1, 4, 2, 3, 2, 3, 3, 4, 3, 1]), [])
        self.assertEqual(nogavice([100, 512, 1]), [100, 512, 1])
        self.assertEqual(nogavice([]), [])
        self.assertEqual(nogavice([123]), [123])

        n = [1, 2, 3, 2]
        self.assertEqual(nogavice(n), [1, 3])
        self.assertEqual(n, [1, 2, 3, 2])


class Test02Bingo(unittest.TestCase):
    def test_bingo(self):
        listki = [[4, 1, 2, 3, 5], [6, 1, 2, 3, 4], [7, 6, 4, 3, 2]]
        self.assertEqual(bingo(listki, [1, 2, 3, 4, 5, 6, 7]), [4, 1, 2, 3, 5])
        self.assertEqual(bingo(listki, [1, 2, 3, 4, 6, 7, 5]), [6, 1, 2, 3, 4])
        self.assertEqual(bingo(listki, [1, 6, 2, 3, 4, 5, 7]), [6, 1, 2, 3, 4])
        self.assertEqual(bingo(listki, [2, 3, 4, 6, 1, 7, 5]), [6, 1, 2, 3, 4])
        self.assertEqual(bingo(listki, [2, 3, 4, 5, 1, 7, 6]), [4, 1, 2, 3, 5])
        self.assertEqual(bingo(listki, [2, 3, 4, 5, 1, 6, 7]), [4, 1, 2, 3, 5])
        self.assertEqual(bingo(listki, [2, 3, 4, 1, 5, 6, 7]), [4, 1, 2, 3, 5])
        self.assertEqual(bingo(listki, [2, 3, 4, 6, 7, 5, 1]), [7, 6, 4, 3, 2])

        self.assertEqual(bingo(listki, [8, 2, 3, 4, 6, 7]), [7, 6, 4, 3, 2])


class Test03Selitve(unittest.TestCase):
    def setUp(self):
        from random import randint
        self.fname = "f{}".format(randint(10000, 99999))

    def tearDown(self):
        import os
        try:
            os.remove(self.fname)
        except:
            pass

    def test_selitve(self):
        zacetek = [
            ("Ljubljana", "Jana"), ("Šentvid", "Vid"), ("Šempeter", "Peter"),
            ("Maribor", "Bor"), ("Kamnik", "Nik"), ("Libanja", "Anja"),
            ("Županje Njive", "Ive"), ("Koroška Bela", "Ela"),
            ("Jablan", "Lan"), ("Krtina", "Tina"), ("Lepa njiva", "Iva"),
            ("Mala Polana", "Ana"), ("Mojstrana", "Ana"), ("Ozeljan", "Jan"),
            ("Slatina", "Tina"), ("Stomaž", "Tomaž"), ("Šentjanž", "Anže"),
            ("Begunje", "Lan"), ("Odranci", "Ajda"), ("Polževo", "Tim"),
            ("Lozice", "France")]
        fname = self.fname

        with open(fname, "w") as f:
            f.write("""iz "Ljubljana" v "Šentvid"
iz "Šentvid" pa v "Kamnik"
""")
        self.assertEqual(selitve(zacetek, fname, "Kamnik"), {"Jana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ljubljana"), set())
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})
        self.assertEqual(selitve(zacetek, fname, "Mojstrana"), {"Ana"})

        with open(fname, "w") as f:
            f.write("""iz "Mala Polana" v "Šentvid"
in iz "Kamnik" v "Šentvid"
""")
        self.assertEqual(selitve(zacetek, fname, "Šentvid"), {"Ana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})

        with open(fname, "w") as f:
            f.write("""Najprej grejo iz "Mala Polana" v "Šentvid".
            Iz "Kamnik" pa tudi v "Šentvid".
            Pa še iz "Koroška Bela" odidejo v "Ozeljan".
            Potem pa iz "Šentvid" v "Maribor" (kwa?!).
""")
        self.assertEqual(selitve(zacetek, fname, "Maribor"), {"Ana", "Vid", "Nik", "Bor"})
        self.assertEqual(selitve(zacetek, fname, "Šentvid"), set())

        with open(fname, "w") as f:
            f.write("""najprej iz "Mala Polana" grejo v "Šentvid"
iz "Kamnik" pa tudi v "Šentvid"
""")
        self.assertEqual(selitve(zacetek, fname, "Šentvid"), {"Ana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})

        with open(fname, "w") as f:
            f.write('''iz "Ljubljana" v "Begunje"
iz "Šentvid" v "Kamnik"
iz "Mojstrana" v "Begunje"
iz "Kamnik" v "Koroška Bela"
iz "Begunje" v "Polževo"''')

        self.assertEqual(selitve(zacetek, fname, "Ljubljana"), set())
        self.assertEqual(selitve(zacetek, fname, "Begunje"), set())
        self.assertEqual(selitve(zacetek, fname, "Šentvid"), set())
        self.assertEqual(selitve(zacetek, fname, "Kamnik"), set())
        self.assertEqual(selitve(zacetek, fname, "Koroška Bela"), {"Vid", "Nik", "Ela"})
        self.assertEqual(selitve(zacetek, fname, "Mojstrana"), set())
        self.assertEqual(selitve(zacetek, fname, "Begunje"), set())
        self.assertEqual(selitve(zacetek, fname, "Polževo"), {"Jana", "Ana", "Tim", "Lan"})
        self.assertEqual(selitve(zacetek, fname, "Mala Polana"), {"Ana"})

        with open(fname, "w") as f:
            f.write('''iz "Ljubljana" v "Begunje"
iz "Kamnik" v "Ljubljana"
''')
        self.assertEqual(selitve(zacetek, fname, "Ljubljana"), {"Nik"})
        self.assertEqual(selitve(zacetek, fname, "Begunje"), {"Lan", "Jana"})
        self.assertEqual(selitve(zacetek, fname, "Kamnik"), set())


class Test04BrezPara(unittest.TestCase):
    def test_brez_para(self):
        class Nogavice(list):
            def __getitem__(self, i):
                if not isinstance(i, int) or i == 0:
                    return super().__getitem__(i)
                else:
                    raise IndexError(
                        "Dostopajte le do prvega elementa ali do ostanka")

            def __iter__(self):
                raise ValueError("Brez zanke for, prosim. Hvala.")

        self.assertFalse(brez_para(39, Nogavice([41, 39, 39, 41, 41, 39, 39])))
        self.assertTrue(brez_para(41, Nogavice([41, 39, 39, 41, 41, 39, 39])))
        self.assertTrue(brez_para(1, Nogavice([1, 2, 3, 4, 2, 3, 4])))
        self.assertTrue(brez_para(2, Nogavice([1, 2, 3, 4, 1, 3, 4])))
        self.assertTrue(brez_para(3, Nogavice([1, 2, 4, 1, 2, 3, 4])))
        self.assertTrue(brez_para(4, Nogavice([1, 2, 4, 1, 2, 3])))


class Test05Sledilnik(unittest.TestCase):
    def test_sledilnik(self):
        zacetek = [
            ("Ljubljana", "Jana"), ("Šentvid", "Vid"), ("Šempeter", "Peter"),
            ("Maribor", "Bor"), ("Kamnik", "Nik"), ("Libanja", "Anja"),
            ("Županje Njive", "Ive"), ("Koroška Bela", "Ela"),
            ("Jablan", "Lan"), ("Krtina", "Tina"), ("Lepa njiva", "Iva"),
            ("Mojstrana", "Ana"), ("Ozeljan", "Jan"),
            ("Slatina", "Tina"), ("Stomaž", "Tomaž"), ("Šentjanž", "Anže"),
            ("Odranci", "Ajda"), ("Polževo", "Tim"),
            ("Lozice", "France")]

        sledilnik = Sledilnik(zacetek)
        sledilnik2 = Sledilnik([("Mala Polana", "Ana"), ("Begunje", "Lan")])

        self.assertEqual(sledilnik.selitev(), 0)
        self.assertIsNone(sledilnik.preseli("Jana", "Ljubljana"))
        self.assertEqual(sledilnik.selitev(), 1)
        self.assertEqual(sledilnik.kje_zivi("Jana"), "Ljubljana")
        self.assertEqual(sledilnik.prebivalci("Ljubljana"), {"Jana"})

        self.assertIsNone(sledilnik.preseli("Jana", "Šentvid"))
        self.assertEqual(sledilnik.selitev(), 2)
        self.assertEqual(sledilnik.kje_zivi("Jana"), "Šentvid")
        self.assertEqual(sledilnik.prebivalci("Ljubljana"), set())
        self.assertEqual(sledilnik.prebivalci("Šentvid"), {"Jana", "Vid"})

        self.assertIsNone(sledilnik.preseli("France", "Slatina"))
        self.assertEqual(sledilnik.selitev(), 3)
        self.assertEqual(sledilnik.kje_zivi("France"), "Slatina")
        self.assertEqual(sledilnik.prebivalci("Lozice"), set())
        self.assertEqual(sledilnik.prebivalci("Slatina"), {"France", "Tina"})

        self.assertIsNone(sledilnik.preseli_vse("Slatina", "Mojstrana"))
        self.assertEqual(sledilnik.selitev(), 5)
        self.assertEqual(sledilnik.kje_zivi("France"), "Mojstrana")
        self.assertEqual(sledilnik.kje_zivi("Tina"), "Mojstrana")
        self.assertEqual(sledilnik.prebivalci("Slatina"), set())
        self.assertEqual(sledilnik.prebivalci("Mojstrana"), {"Ana", "France", "Tina"})

        self.assertIsNone(sledilnik.preseli_vse("Mojstrana", "Šentvid"))
        self.assertEqual(sledilnik.selitev(), 8)
        self.assertEqual(sledilnik.kje_zivi("France"), "Šentvid")
        self.assertEqual(sledilnik.kje_zivi("Tina"), "Šentvid")
        self.assertEqual(sledilnik.kje_zivi("Ana"), "Šentvid")
        self.assertEqual(sledilnik.prebivalci("Mojstrana"), set())
        self.assertEqual(sledilnik.prebivalci("Šentvid"), {"Jana", "Vid", "Ana", "France", "Tina"})

        self.assertEqual(sledilnik2.kje_zivi("Ana"), "Mala Polana")
        self.assertEqual(sledilnik2.selitev(), 0)


if __name__ == "__main__":
    unittest.main()
