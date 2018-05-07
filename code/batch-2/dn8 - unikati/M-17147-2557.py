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
    f = open(ime_datoteke, 'r')
    terka = ()
    seznam=[]
    trenutni_x=0
    trenutni_y=0
    trenutna_smer='N'
    terka=(trenutni_x,trenutni_y,trenutna_smer)
    seznam.append(terka)
    besedilo = f.readlines()

    for vrstica in besedilo:
        #vrstica=vrstica.strip()
        vrstica=vrstica.strip()
        print(vrstica)
        if vrstica[:3] == "NAP":
            ukaz_splitan = vrstica.split(" ")
            terka=premik(int(ukaz_splitan[1]), trenutni_x, trenutni_y, trenutna_smer)
            trenutni_x=terka[0]
            trenutni_y = terka[1]
            seznam.append(terka)
            #print(vrstica)

        elif vrstica=="DESNO" or vrstica=="LEVO":
            trenutni_ukaz=""

            if vrstica=="DESNO":
                trenutni_ukaz="R"
            elif vrstica=="LEVO":
                trenutni_ukaz="L"

            terka=premik(trenutni_ukaz, trenutni_x,trenutni_y, trenutna_smer)
            trenutna_smer=terka[2]
            seznam.append(terka)
            #print(vrstica)

    f.close()
    return seznam
def opisi_stanje(x,y,smer):
    x_string = str(x)
    y_string = str(y)
    smeri1=['N','E','S','W']
    smeri2=['^','>', 'v', '<']
    smer=smeri2[smeri1.index(smer)]
    return ("{:>3}:{:<4}{}".format(x_string, y_string, smer))




def prevedi(ime_vhoda, ime_izhoda):
    seznamTerk = izvedi(ime_vhoda)
    f = open(ime_izhoda,'w')
    for terka in seznamTerk:
        vrstica=opisi_stanje(terka[0],terka[1],terka[2])+'\n'
        f.write(vrstica)
    f.close()

def opisi_stanje_2(x, y, smer):

    return ""

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
