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

#########################################
#            POMOŽNA FUNKCIJA           #
#########################################

def prevedi_smer(smer):
    """
    Vrni smer v obliki:
    ^, >, v, < za smeri
    N, E, S, W

    Args:
        smer (string): smer v obliki N, E, S, W

    Returns:
        string: smer v obliki ^, >, v, <
    """
    if smer == 'N':
        return '^'
    elif smer == 'E':
        return '>'
    elif smer == 'S':
        return 'v'
    else:
        return '<'

#########################################
#                OBVEZNE                #
#########################################

def izvedi(ime_datoteke):
    file = open(ime_datoteke)
    datoteka = file.read().splitlines()
    x = 0
    y = 0
    smer = 'N'
    s = [(x, y, smer)]
    for ukaz in datoteka:
        if ukaz == 'DESNO':
            ukaz = 'R'
        elif ukaz == 'LEVO':
            ukaz = 'L'
        else:
            ukaz = int(ukaz.split()[1])
        x, y, smer = premik(ukaz, x, y, smer)
        s.append((x, y, smer))
    file.close()
    return s

def opisi_stanje(x, y, smer):
    smer = prevedi_smer(smer)
    return "{:>3}:{:<3} {}".format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    stanja = izvedi(ime_vhoda)
    pisanje = open(ime_izhoda, 'w')
    for x, y, smer in stanja:
        pisanje.write(opisi_stanje(x, y, smer) + "\n")
    pisanje.close()

#########################################
#                DODATNA                #
#########################################

def opisi_stanje_2(x, y, smer):
    smer = prevedi_smer(smer)
    x_oklepaj = "({}".format(x)
    return "{} {:>4}:{})".format(smer, x_oklepaj, y)

#########################################
#                 TESTI                 #
#########################################

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
