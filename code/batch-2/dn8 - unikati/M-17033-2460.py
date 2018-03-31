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
    vrni = [(0, 0, 'N')]
    ukazi = []
    a = 0
    for vrstice in open(ime_datoteke):
        ukazi.append(vrstice.split())
    for ukaz in ukazi:
        trenutna_smer = vrni[a][2]
        x = vrni[a][0]
        y = vrni[a][1]
        if len(ukaz) == 1:
            if ukaz == ['DESNO']:
                smer = 'R'
                trenutna_pozicija = premik(smer, x, y, trenutna_smer)
                vrni.append(trenutna_pozicija)
            if ukaz == ['LEVO']:
                smer = 'L'
                trenutna_pozicija = premik(smer, x, y, trenutna_smer)
                vrni.append(trenutna_pozicija)

        if len(ukaz)  == 2:
            if trenutna_smer == 'N':
                y = y - int(ukaz[1])
                trenutna_pozicija = x, y, trenutna_smer
                vrni.append(trenutna_pozicija)
            elif trenutna_smer == 'S':
                y = y + int(ukaz[1])
                trenutna_pozicija = x, y, trenutna_smer
                vrni.append(trenutna_pozicija)
            elif trenutna_smer == 'W':
                x = x - int(ukaz[1])
                trenutna_pozicija = x, y, trenutna_smer
                vrni.append(trenutna_pozicija)
            elif trenutna_smer == 'E':
                x = x + int(ukaz[1])
                trenutna_pozicija = x, y, trenutna_smer
                vrni.append(trenutna_pozicija)
        a+=1
    return vrni

def opisi_stanje(x, y, smer):
    smeri = {'N' : ' ^', 'E' : ' >', 'S' : ' v', 'W' : ' <'}
    for smer_ in smeri.items():
        if smer_[0] == smer:
            return("{:3}:{:<3}{:2}".format(x, y, smer_[1]))

def prevedi(ime_vhoda, ime_izhoda):
    vh_dat = izvedi(ime_vhoda)
    file = open(ime_izhoda, "w")
    for element in vh_dat:
        a, b, c, = element
        file.write(opisi_stanje(a, b, c))
        file.write("\n")
    file.close()

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

if __name__ == "__main__":
    unittest.main()
