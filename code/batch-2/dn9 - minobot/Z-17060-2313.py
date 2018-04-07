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
    pravilni_korak = (0,0,'N') #zacnemo na (0,0,'N') po definiciji
    pravilna_pot = [pravilni_korak]
    for vrstice in open(ime_datoteke):
        trenutno_vrstica = vrstice.strip()
        zacetna_koordinata_x = pravilni_korak[0]
        zacetna_koordinata_y = pravilni_korak[1]
        zacetna_smer = pravilni_korak[2]
        if(trenutno_vrstica == 'DESNO'):
            pravilni_korak = premik("R", zacetna_koordinata_x, zacetna_koordinata_y, zacetna_smer)
            pravilna_pot.append(pravilni_korak)
        elif(trenutno_vrstica == 'LEVO'):
            pravilni_korak = premik("L", zacetna_koordinata_x, zacetna_koordinata_y, zacetna_smer)
            pravilna_pot.append(pravilni_korak)
        else:
            #odstranimo NAPREJ in spremenimo v integer
            aktivni_korak = int(trenutno_vrstica.replace("NAPREJ ", ""))
            pravilni_korak = premik(aktivni_korak, zacetna_koordinata_x, zacetna_koordinata_y, zacetna_smer)
            pravilna_pot.append(pravilni_korak)
    return pravilna_pot

def opisi_stanje(x, y, smer):
    if(smer == 'N'):
        smer = '^'
    elif (smer == 'E'):
        smer = '>'
    elif (smer == 'S'):
        smer = 'v'
    elif (smer == 'W'):
        smer = '<'
    return '{:3}:{:<3} {}'.format(x, y, smer)

def prevedi(ime_vhoda, ime_izhoda):
    vhodni_podatek = izvedi(ime_vhoda)
    izhodna_datoteka = open(ime_izhoda, "w")
    for premik_ena in vhodni_podatek:
        lepi_zapis = opisi_stanje(premik_ena[0],premik_ena[1],premik_ena[2])
        izhodna_datoteka.write(lepi_zapis+"\n")

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
