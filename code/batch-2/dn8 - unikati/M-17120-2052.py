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

    situacija= [(0, 0, 'N')]
    x, y, smer= 0, 0, 'N'

    for poteza in datoteka:
        if poteza =='DESNO\n':
            x, y, smer= premik('R', x, y, smer)
        elif poteza == 'LEVO\n':
            x, y, smer=premik('L', x, y, smer)
        else:
            stevilka=int(poteza.replace('NAPREJ ', ''))
            x, y, smer =premik(stevilka, x, y, smer)
        situacija.append((x, y, smer))

    return situacija






def opisi_stanje(x, y, smer):

    desno = ''
    levo = ''
    niz_desno= 3 - len(str(y))
    niz_levo= 3 - len(str(x))


    for i in range(niz_levo):
        levo =levo + ' '

    for i in range(niz_desno):
        desno= desno + ' '

    if smer=='N':
        nova_smer = '^'
    elif smer=='S':
        nova_smer = 'v'
    elif smer=='W':
        nova_smer='<'
    elif smer=='E':
        nova_smer='>'

    return levo + str(x) + ':' + str(y) + desno + ' ' + nova_smer





def prevedi(ime_vhoda, ime_izhoda):

    datoteka =open(ime_vhoda, 'r')
    situacija=izvedi(ime_vhoda)

    for i in range(len(situacija)):
        situacija[i]=opisi_stanje(situacija[i][0], situacija[i][1], situacija[i][2])

    X=open(ime_izhoda,'w')

    for podatek in situacija:
        X.write(str(podatek)+'\n')







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
