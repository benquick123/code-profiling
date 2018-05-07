def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz == "R":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz == "L":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * ukaz
        y += dy * ukaz
    return x, y, smer

def izvedi(ime_datoteke):
    datoteka = open(ime_datoteke, encoding="UTF8").read().split("\n")

    ukazi = []
    for item in datoteka:
        g = item.lstrip()
        ukazi.append(g)

    x = 0
    y = 0
    smer = "N"
    pot = []
    pot.append((x, y, smer))

    for ukaz in ukazi:
        if ukaz == "DESNO":
            del_poti = premik("R", x, y, smer)
            x, y, smer = del_poti
            pot.append(del_poti)

        elif ukaz == "LEVO":
            del_poti = premik("L", x, y, smer)
            x, y, smer = del_poti
            pot.append(del_poti)

        elif "NAPREJ" in ukaz:
            tabelca = ukaz.split("NAPREJ")
            stevilo = int(tabelca[1])

            del_poti = premik(stevilo, x, y, smer)
            x, y, smer = del_poti
            pot.append(del_poti)

    return pot

def opisi_stanje(x, y, smer):
    if smer == "N":
        puscica = "^"

    elif smer == "S":
        puscica = "v"

    elif smer == "E":
        puscica = ">"

    elif smer == "W":
        puscica = "<"

    dvopicje = ":"
    odgovor = ("{x:>3}{dvopicje}{y:<3}".format(x=x, y=y, dvopicje=dvopicje)) + " " + puscica

    return odgovor

def prevedi(ime_vhoda, ime_izhoda):
    izvor = izvedi(ime_vhoda)
    cilj = open(ime_izhoda, "w")
    for item in izvor:
        x, y, smer = item
        dodatek = opisi_stanje(x, y, smer)+"\n"
        cilj.write(dodatek)

    cilj.close()

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        puscica = "^"

    elif smer == "S":
        puscica = "v"

    elif smer == "E":
        puscica = ">"

    elif smer == "W":
        puscica = "<"

    dvopicje = ":"
    prazno = 3 - len(str(x))
    dodatek = prazno * " "
    odgovor = puscica+" "+dodatek+("{}{x:>}{dvopicje}{y:<}".format("(",x=x, y=y, dvopicje=dvopicje))+")"

    return odgovor


import unittest
class TestObvezna(unittest.TestCase):
    def test_branje(self):
        self.assertEqual(
            izvedi("primer.txt"),
            [(0, 0, 'N'), (0, 0, 'E'), (12, 0, 'E'), (12, 0, 'S'), (12, 2, 'S'),
             (12, 2, 'E'), (15, 2, 'E'), (15, 2, 'N'), (15, 2, 'W')]
        )
        self.assertEqual(
            izvedi("ukazi.txt"),
            [(0, 0, 'N'), (0, 0, 'E'), (1, 0, 'E'), (1, 0, 'S'), (1, 0, 'W'),
             (0, 0, 'W'), (0, 0, 'S'), (0, 0, 'E'), (1, 0, 'E'), (1, 0, 'S'),
             (1, 3, 'S'), (1, 3, 'E'), (2, 3, 'E'), (2, 3, 'S'), (2, 3, 'W')]
        )

    def test_opisi_stanje(self):
        self.assertEqual(opisi_stanje(0, 12, "N"), "  0:12  ^")
        self.assertEqual(opisi_stanje(111, 0, "E"), "111:0   >")
        self.assertEqual(opisi_stanje(-2, 111, "S"), " -2:111 v")
        self.assertEqual(opisi_stanje(0, 0, "W"), "  0:0   <")

    def test_prevedi(self):
        from random import randint
        import os
        ime = "izhod{:05}.txt".format(randint(0, 99999))
        try:
            self.assertIsNone(prevedi("primer.txt", ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:0   >
 12:0   >
 12:0   v
 12:2   v
 12:2   >
 15:2   >
 15:2   ^
 15:2   <""")

            self.assertIsNone(prevedi("ukazi.txt", ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:0   >
  1:0   >
  1:0   v
  1:0   <
  0:0   <
  0:0   v
  0:0   >
  1:0   >
  1:0   v
  1:3   v
  1:3   >
  2:3   >
  2:3   v
  2:3   <""")
        finally:
            os.remove(ime)

        vime = "vhod{:05}.txt".format(randint(0, 99999))
        open(vime, "wt").write("NAPREJ 23\nLEVO\nNAPREJ 17\n")
        try:
            self.assertIsNone(prevedi(vime, ime))
            self.assertEqual(open(ime).read().rstrip(), """  0:0   ^
  0:-23 ^
  0:-23 <
-17:-23 <""")
        finally:
            os.remove(ime)
            os.remove(vime)


class TestDodatna(unittest.TestCase):
    def test_opisi_stanje(self):
        self.assertEqual(opisi_stanje_2(0, 12, "N"),   "^   (0:12)")
        self.assertEqual(opisi_stanje_2(111, 0, "E"),  "> (111:0)")
        self.assertEqual(opisi_stanje_2(-2, 111, "S"), "v  (-2:111)")
        self.assertEqual(opisi_stanje_2(0, 0, "W"),    "<   (0:0)")


if __name__ == "__main__":
    unittest.main()
