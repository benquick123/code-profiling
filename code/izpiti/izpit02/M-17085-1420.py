def nogavice(s):
    seznam_brez_para=[]
    vrednosti=[]
    ponovitve=0
    stevec=1
    dolzina=len(s)
    for vrednost in s:
        if vrednost not in vrednosti:
            vrednosti.append(vrednost)
            while(stevec<=dolzina):
                if s[stevec]==vrednost:
                    ponovitve+=1
                stevec+=1
            if ponovitve%2 !=0:
                seznam_brez_para.append(vrednost)
            ponovitve=0
        stevec=vrednost.index() + 1
    return vrednosti

def bingo(listki, vrstni_red):
    zmagovalni=0 # sem bom shranil index zmagovalnega listka, ki ga bom nakoncu samo izpisal
    kopija=listki.copy()
    for stevilka in vrstni_red:
        for listek in kopija:
            for vrednost in listek:
                if vrednost==stevilka:
                    listek[vrednost].delete() #nisem se mogel spomniti kako bi izbrisali element iz seznama
        if len(listek)==0:
            zmagovalni=listek.index

    return listki[zmagovalni]

def selitve(zacetek, datoteka_selitev, kraj):
    mnozica=set()
    for vrstica in datoteka_selitev.open():
        vrstica.split("")

def brez_para(nogavica, nogavice):
    stevilo_ponovitev=0
    for koceta in nogavice:
        if koceta==nogavica:
            stevilo_ponovitev+1
    if stevilo_ponovitev%2!=0:
        return True
    else:
        return False
    #nisem imel časa da bi zgruntal rekurzijo... naloga bi mogla delovati, ampak žal mi je zmanjkalo časa da bi jo rešil z rekurzijo.
    #upam na vsaj nekaj točk :)


#to nalogo sem si zamislil tako, da če se oseba odseli nekam, jo preselimo,
# odstranimo tisto vrednost osebe s prejsnjim krajem, in dodamo vrednost z novim krajem
# in to vrednost dodamo v tisti seznam ki ga imamo podanega
class Sledilnik():
    def __init__(self, iz_kje):
        self.vrednosti=iz_kje
        self.stevilo=0 # koliko preselitev se je zgodilo

    def kje_zivi(self, oseba):
        for element in self.vrednosti:
            if oseba== element[1]:
                return element[0]

    def prebivalci(self, kraj):
        mnozica=set()
        for element in self.vrednosti:
            if element[0]==kraj:
                mnozica.add(element[1])

    def preseli(self, oseba, kraj):
        for element in self.vrednosti:
            if element[1]==oseba:
                self.vrednosti[element].drop #zbrišemo prejšnje nahajanje osebe
        self.vrednosti.append((kraj, oseba)) # dodamo novo
        self.stevilo+= 1

    def preseli_vse(self, odkod, kam):
        for element in self.vrednosti:
            if element[0]==odkod:
                self.vrednosti[element].drop # zbrišemo prejšnje nahajanje osebe
                self.vrednosti.append((kam, element[1])) # dodamo novo za use tiste ki so se preselili v nov kraj

    def selitev(self):
        return self.stevilo
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

