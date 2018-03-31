import unittest
from collections import defaultdict
def nogavice(s):
    sez = []
    d = defaultdict(int)
    for x in s:
        if x not in d:
            d[x] = 1

        elif d[x] == 2:
            d[x] = 0
        else:
            e = d[x] + 1
            d[x] = e
    for x in d:
        if d[x] == 1:
            sez.append(d[x])

    return sez
def brez_para(nogavica, nogavice):
    d = defaultdict(int)
    a = False

    if nogavice[0] not in d:
        d[nogavica] = 1
        del nogavice[0]
        brez_para(nogavica,nogavice)
    elif d[nogavica] == 2:
        d[nogavica] = 0
        del nogavice[0]
        brez_para(nogavica, nogavice)
    else:
        e = d[nogavica] + 1
        d[nogavica] = e
        del nogavice[0]
        brez_para(nogavica, nogavice)
    for x in d:
        if d[x] == 1:
            a = False
    return a
def selitve(zacetek, datoteka_selitve, kraj):
    d = defaultdict(int)
    for x in open(datoteka_selitve):
        z= x.split()
        for x in z:
            if "" in x:
                r = x.strip()



class Sledilnik:
    def __init__(self, zacetek,):
        self.zacetek = zacetek


    def prebivalci(self, kraj):
        sez= []
        for x in self.zacetek:
            if x[0] == kraj:
                sez.append(x[1])
        return sez
    def kje_zivi(self, oseba):
        for x in self.zacetek:
            if x[1] == oseba:
                break
        return self.zacetek[1]
    def preseli(self, oseba, kraj):
        for x in self.zacetek:
            if x[1] == oseba:
                x[0] = kraj
                break


def bingo(listki, vrstni_red):
    d = defaultdict(list)
    for l in vrstni_red:
        for x,y,s in zip(listki[0],listki[1],listki[2]):
            if x == l:
                d[1] = x
            if d[1] == vrstni_red:
                sez = d[1]
                break
            if y == l:
                d[2] = y
            if d[2] == vrstni_red:
                sez = d[2]
                break
            if s == l:
                d[3] = s
            if d[3] == vrstni_red:
                sez= d[3]
                break
        break

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

