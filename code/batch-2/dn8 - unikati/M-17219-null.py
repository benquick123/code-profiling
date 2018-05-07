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

def opredeli_smer(smer):
    nsmer = ""
    if smer == "N":
        nsmer = "^"
    if smer == "E":
        nsmer = ">"
    if smer == "W":
        nsmer = "<"
    if smer == "S":
        nsmer = "v"
    return nsmer

def izvedi(ime_datoteke):
    sez = []
    trenutna = (0, 0, 'N')
    sez.append(trenutna)

    dat = open(ime_datoteke)
    for vrstica in dat:
        ukaz = vrstica[:1]
        if ukaz == "D":
            ukaz = "R"
        if ukaz == "N":
            stevilka1 = vrstica.split(" ")
            stevilka = int(stevilka1[1].replace("\n", ""))
            # Za X smer
            if trenutna[2] == "W" or trenutna[2] == "E":
                trenutna = (premik(stevilka, trenutna[0], trenutna[1], trenutna[2]))
                sez.append(trenutna)
            # Za Y smer
            if trenutna[2] == "N" or trenutna[2] == "S":
                trenutna = (premik(stevilka, trenutna[0], trenutna[1], trenutna[2]))
                sez.append(trenutna)
        else:
            sez.append(premik(ukaz, trenutna[0], trenutna[1], trenutna[2]))
            trenutna = premik(ukaz, trenutna[0], trenutna[1], trenutna[2])
    dat.close()
    return sez

def opisi_stanje(x, y, smer):
    return ("{:3}:{:<4}{}".format(x, y, opredeli_smer(smer)))


def prevedi(ime_vhoda, ime_izhoda):
    izvedeno = izvedi(ime_vhoda)
    dat = open(ime_izhoda, "w")

    for trojka in izvedeno:
        x = trojka[0]
        y = trojka[1]
        smer = trojka[2]
        dat.write("{}\n".format(opisi_stanje(x, y, smer)))

    dat.close()



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
