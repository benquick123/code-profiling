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
    ukazi = []
    for vrstica in open(ime_datoteke):
        if vrstica.strip() == "DESNO":
            ukazi.append("R")
        elif vrstica.strip() == "LEVO":
            ukazi.append("L")
        else:
            ukazi.append(int(vrstica.split()[-1]))
    stanja = [(0, 0, "N")]
    stanje = 0
    for ukaz in ukazi:
        stanja.append(premik(ukaz, stanja[stanje][0], stanja[stanje][1], stanja[stanje][2]))
        stanje += 1
    return stanja

def izpisi_stanje(x, y, znak):
    return "{0:>3}:{1:<4}{2}".format(x, y, znak)

def opisi_stanje(x, y, smer):
    if smer == "N":
        return izpisi_stanje(x, y, "^")
    elif smer == "S":
        return izpisi_stanje(x, y, "v")
    elif smer == "E":
        return izpisi_stanje(x, y, ">")
    else:
        return izpisi_stanje(x, y, "<")

def prevedi(ime_vhoda, ime_izhoda):
    nova_datoteka = open(ime_izhoda, "w")
    for x, y, smer in izvedi(ime_vhoda):
        nova_datoteka.write(opisi_stanje(x, y, smer) + "\n")

def izpisi_stanje_2(x, y, znak):
    return "{0}{1:>5}:{2})".format(znak, "(" + str(x), y)

def opisi_stanje_2(x, y, smer):
    if smer == "N":
        return izpisi_stanje_2(x, y, "^")
    elif smer == "S":
        return izpisi_stanje_2(x, y, "v")
    elif smer == "E":
        return izpisi_stanje_2(x, y, ">")
    else:
        return izpisi_stanje_2(x, y, "<")


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
