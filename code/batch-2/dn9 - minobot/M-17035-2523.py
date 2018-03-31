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
    datoteka = open(ime_datoteke)
    seznam = [(0,0,"N")]
    counter = 0
    for vse in datoteka:
        if vse.startswith("DESNO"):
            x,y,smer = seznam[counter]
            nekaj = premik("R",x,y,smer)
            seznam.append(nekaj)
            counter += 1
        if vse.startswith("LEVO"):
            x, y, smer = seznam[counter]
            nekaj = premik("L", x, y, smer)
            seznam.append(nekaj)
            counter += 1
        if vse.startswith("NAPREJ"):
            x,y,smer = seznam[counter]
            drugo = vse.split(" ")
            nekaj = premik(int(drugo[1]),x,y,smer)
            seznam.append(nekaj)
            counter += 1
    return(seznam)

def opisi_stanje(x,y,smer):
    if smer == "N":
        stanje = "^"
    if smer == "E":
        stanje = ">"
    if smer == "S":
        stanje = "v"
    if smer == "W":
        stanje = "<"
    return("{X:3}:{Y:<3} {S}".format(X=x, Y=y, S=stanje))

def prevedi(ime_vhoda,ime_izhoda):
    seznam = izvedi(ime_vhoda)
    datoteka = open(ime_izhoda, "w")
    for vse in seznam:

        x,y,smer = vse
        opis = opisi_stanje(x,y,smer)
        datoteka.write(opis + "\n")
    datoteka.close()



def opisi_stanje_2(x,y,smer):
    if smer == "N":
        stanje = "^"
    if smer == "E":
        stanje = ">"
    if smer == "S":
        stanje = "v"
    if smer == "W":
        stanje = "<"
    x = "(" + str(x)
    return("{S} {X:>4}:{Y})".format(X=x, Y=y, S=stanje))


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
