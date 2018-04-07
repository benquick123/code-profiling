from collections import defaultdict
#1
def nogavice(s):
    slovar = defaultdict(int)
    seznam = []
    for i in s:
        slovar[i] += 1
    for j in slovar:
        if slovar[j] % 2 != 0:
            seznam.append(j)
    return seznam

#2
def bingo(listki, vrstni_red):
    slovar = defaultdict(int)
    for stevilka in vrstni_red:
        for a, listek in enumerate(listki):
            if stevilka in listek:
                slovar[a] += 1
            if slovar[a] == len(listek):
                return listki[naj_kljuc(slovar)]

def naj_kljuc(d):
    naj_k = None
    naj_v = 0
    for k, v in d.items():
        if v > naj_v:
            naj_k, naj_v = k, v
    return naj_k


#3
def selitve(zacetek, datoteka_selitev, kraj):
    prebivalci = defaultdict(set)
    for vrstica in open(datoteka_selitev):
        _, kje,  _, kam, _ = vrstica.split('"')
        for a, terka in enumerate(zacetek):
            kraj1, oseba = terka
            prebivalci[kraj1].add(oseba)
            if kraj1 == kje:
                zacetek[a] = (kam, oseba)
                prebivalci[kraj1].remove(oseba)
                prebivalci[kam].add(oseba)
    return prebivalci[kraj]


#4
def brez_para(nogavica, nogavice):
    if len(nogavice) < 1:
        return False
    elif len(nogavice) == 1:
        return True
    elif len(nogavice) > 1:
        if nogavica == nogavice[0]:
            return True  + brez_para(nogavica, nogavice[1:])
        else:
            return False + brez_para(nogavica, nogavice[1:])



#5
class Sledilnik:
    def __init__(self, zacetek):
        self.zacetek = {}
        for kraj, oseba in zacetek:
            self.zacetek[oseba] = kraj

        self.selitve = 0

    def kje_zivi(self, oseba):
        return self.zacetek[oseba]

    def prebivalci(self, kraj):
        seznam_prebivalcev = set()
        for k, v in self.zacetek.items():
            if v == kraj:
                seznam_prebivalcev.add(k)
                self.selitve += 1
        return seznam_prebivalcev

    def preseli(self, oseba, kraj):
        self.zacetek[oseba] = kraj
        self.selitve += 1

    def preseli_vse(self, odkod, kam):
        for k, v in self.zacetek.items():
            if v == odkod:
                self.zacetek[k] = kam
                self.selitve += 1
    def selitev(self):
        return self.selitve


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
            ("Ljubljana", "Jana"), ("Ĺ entvid", "Vid"), ("Ĺ empeter", "Peter"),
            ("Maribor", "Bor"), ("Kamnik", "Nik"), ("Libanja", "Anja"),
            ("Ĺ˝upanje Njive", "Ive"), ("KoroĹˇka Bela", "Ela"),
            ("Jablan", "Lan"), ("Krtina", "Tina"), ("Lepa njiva", "Iva"),
            ("Mala Polana", "Ana"), ("Mojstrana", "Ana"), ("Ozeljan", "Jan"),
            ("Slatina", "Tina"), ("StomaĹľ", "TomaĹľ"), ("Ĺ entjanĹľ", "AnĹľe"),
            ("Begunje", "Lan"), ("Odranci", "Ajda"), ("PolĹľevo", "Tim"),
            ("Lozice", "France")]
        fname = self.fname

        with open(fname, "w") as f:
            f.write("""iz "Ljubljana" v "Ĺ entvid"
iz "Ĺ entvid" pa v "Kamnik"
""")
        self.assertEqual(selitve(zacetek, fname, "Kamnik"), {"Jana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ljubljana"), set())
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})
        self.assertEqual(selitve(zacetek, fname, "Mojstrana"), {"Ana"})

        with open(fname, "w") as f:
            f.write("""iz "Mala Polana" v "Ĺ entvid"
in iz "Kamnik" v "Ĺ entvid"
""")
        self.assertEqual(selitve(zacetek, fname, "Ĺ entvid"), {"Ana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})

        with open(fname, "w") as f:
            f.write("""Najprej grejo iz "Mala Polana" v "Ĺ entvid".
            Iz "Kamnik" pa tudi v "Ĺ entvid".
            Pa Ĺˇe iz "KoroĹˇka Bela" odidejo v "Ozeljan".
            Potem pa iz "Ĺ entvid" v "Maribor" (kwa?!).
""")
        self.assertEqual(selitve(zacetek, fname, "Maribor"), {"Ana", "Vid", "Nik", "Bor"})
        self.assertEqual(selitve(zacetek, fname, "Ĺ entvid"), set())

        with open(fname, "w") as f:
            f.write("""najprej iz "Mala Polana" grejo v "Ĺ entvid"
iz "Kamnik" pa tudi v "Ĺ entvid"
""")
        self.assertEqual(selitve(zacetek, fname, "Ĺ entvid"), {"Ana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})

        with open(fname, "w") as f:
            f.write('''iz "Ljubljana" v "Begunje"
iz "Ĺ entvid" v "Kamnik"
iz "Mojstrana" v "Begunje"
iz "Kamnik" v "KoroĹˇka Bela"
iz "Begunje" v "PolĹľevo"''')

        self.assertEqual(selitve(zacetek, fname, "Ljubljana"), set())
        self.assertEqual(selitve(zacetek, fname, "Begunje"), set())
        self.assertEqual(selitve(zacetek, fname, "Ĺ entvid"), set())
        self.assertEqual(selitve(zacetek, fname, "Kamnik"), set())
        self.assertEqual(selitve(zacetek, fname, "KoroĹˇka Bela"), {"Vid", "Nik", "Ela"})
        self.assertEqual(selitve(zacetek, fname, "Mojstrana"), set())
        self.assertEqual(selitve(zacetek, fname, "Begunje"), set())
        self.assertEqual(selitve(zacetek, fname, "PolĹľevo"), {"Jana", "Ana", "Tim", "Lan"})
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
            ("Ljubljana", "Jana"), ("Ĺ entvid", "Vid"), ("Ĺ empeter", "Peter"),
            ("Maribor", "Bor"), ("Kamnik", "Nik"), ("Libanja", "Anja"),
            ("Ĺ˝upanje Njive", "Ive"), ("KoroĹˇka Bela", "Ela"),
            ("Jablan", "Lan"), ("Krtina", "Tina"), ("Lepa njiva", "Iva"),
            ("Mojstrana", "Ana"), ("Ozeljan", "Jan"),
            ("Slatina", "Tina"), ("StomaĹľ", "TomaĹľ"), ("Ĺ entjanĹľ", "AnĹľe"),
            ("Odranci", "Ajda"), ("PolĹľevo", "Tim"),
            ("Lozice", "France")]

        sledilnik = Sledilnik(zacetek)
        sledilnik2 = Sledilnik([("Mala Polana", "Ana"), ("Begunje", "Lan")])

        self.assertEqual(sledilnik.selitev(), 0)
        self.assertIsNone(sledilnik.preseli("Jana", "Ljubljana"))
        self.assertEqual(sledilnik.selitev(), 1)
        self.assertEqual(sledilnik.kje_zivi("Jana"), "Ljubljana")
        self.assertEqual(sledilnik.prebivalci("Ljubljana"), {"Jana"})

        self.assertIsNone(sledilnik.preseli("Jana", "Ĺ entvid"))
        self.assertEqual(sledilnik.selitev(), 2)
        self.assertEqual(sledilnik.kje_zivi("Jana"), "Ĺ entvid")
        self.assertEqual(sledilnik.prebivalci("Ljubljana"), set())
        self.assertEqual(sledilnik.prebivalci("Ĺ entvid"), {"Jana", "Vid"})

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

        self.assertIsNone(sledilnik.preseli_vse("Mojstrana", "Ĺ entvid"))
        self.assertEqual(sledilnik.selitev(), 8)
        self.assertEqual(sledilnik.kje_zivi("France"), "Ĺ entvid")
        self.assertEqual(sledilnik.kje_zivi("Tina"), "Ĺ entvid")
        self.assertEqual(sledilnik.kje_zivi("Ana"), "Ĺ entvid")
        self.assertEqual(sledilnik.prebivalci("Mojstrana"), set())
        self.assertEqual(sledilnik.prebivalci("Ĺ entvid"), {"Jana", "Vid", "Ana", "France", "Tina"})

        self.assertEqual(sledilnik2.kje_zivi("Ana"), "Mala Polana")
        self.assertEqual(sledilnik2.selitev(), 0)


if __name__ == "__main__":
    unittest.main()


