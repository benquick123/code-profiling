#coding=utf-8
#from __future__ import unicode_literals

def izvedi(ime_datoteke):

    x,y,s = 0, 0, 'N'
#    robot = (0,0,'N')
    premiki = [(0, 0, 'N')]

    for vrstica in open(ime_datoteke) :
        vrstica = vrstica.strip()

        if vrstica == 'DESNO' :
            vrstica = 'R'
        elif vrstica == 'LEVO' :
            vrstica = 'L'
        else :
            vrstica = int(vrstica.split(' ')[1])

    #    print("VR 222 ", vrstica)
    #    print("Premik ", premik(vrstica, x,y,s))

        x,y,s = premik(vrstica, x,y,s)

    #    print("Robot: ",x,y,s)

        premiki.append((x,y,s))

    return premiki
#    print("PREMIKI:   ", premiki)



def opisi_stanje(x, y, smer):

    # if smer == 'N' :
    # smer = '^'.....

    #    print("x: ", x)
    #    print("y: ", y)
    #    print("smer: ", smer)


    neba = 'NESW'
    pusc = '^>v<'
    smer = pusc[neba.index(smer)]

    #    print("{:>3}:{:<3} {}".format(x,y,smer))

    return "{:>3}:{:<3} {}".format(x,y,smer)



def prevedi(ime_vhoda, ime_izhoda):

    premiki = izvedi(ime_vhoda)

    dat = open(ime_izhoda, 'w')

    for premik in premiki :
    #    print("333")
    #    stanje = opisi_stanje(premik)
    #    print("444")
        dat.write(opisi_stanje(premik[0], premik[1], premik[2]) + "\n")

    dat.close()

def opisi_stanje_2(x, y, smer):

    neba = 'NESW'
    pusc = '^>v<'
    smer = pusc[neba.index(smer)]

    x = str(x)
    y = str(y)

    # print("{} {:>4}:{}".format(smer,"("+x,y+")"))

    return "{} {:>4}:{}".format(smer,"("+x,y+")")


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
