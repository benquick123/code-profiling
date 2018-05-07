import re
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
    sez = [(0,0,'N')]
    x= 0
    y=0
    znak = "N"
    datoteka = open(ime_datoteke)
    for vrstica in datoteka:
        a = vrstica
        print(a)
        if a == "DESNO\n":
            r=premik("R",x,y,znak)
            sez.append(r)
            x = r[0]
            y = r[1]
            znak = r[2]
            print(x,y,znak)

        elif a == "LEVO\n":
            e= premik("L", x, y, znak)
            sez.append(e)
            x = e[0]
            y=e[1]
            znak =e[2]
            print(x, y, znak)
        else:
            o= re.findall('\d+', vrstica)
            e = premik(int(o[0]), x, y, znak)
            sez.append(e)
            x = e[0]
            y = e[1]
            znak = e[2]

    datoteka.close()
    return sez
def opisi_stanje(x,y,smer):
    if smer == "N":
        a = '  {:>1}:{:>1}  {:>1}'.format(x, y,'^')
    if smer == "S":
        a = ' {:>1}:{:>1} {:>1}'.format(x, y,'v')
    if smer == "W":
        a = '  {:>1}:{:>1}   {:>1}'.format(x, y,'<')
    if smer == "E":
        a = '{:>1}:{:>1}   {:>1}'.format(x, y,'>')
    return a
def prevedi(ime_vhoda,ime_izhoda):
    a = izvedi(ime_vhoda)
    f = open(ime_izhoda, "w")
    for x in a:
        if x[2] == "N":
            if len(str(x[0]))==1:
                a = ' {:>2}:{:>1}   {:>1}'.format(x[0], x[1], '^')
            if len(str(x[0]))==2:
                a = ' {:>2}:{:>1}   {:>1}'.format(x[0], x[1], '^')
            if len(str(x[1])) == 3:
                a = '  {:>1}:{:>1} {:>1}'.format(x[0], x[1], '^')
        if x[2] == "S":
            if len(str(x[0])) == 1:
                a = '  {:>1}:{:>1}   {:>1}'.format(x[0], x[1], 'v')
            if len(str(x[0])) == 2:
                a = ' {:>1}:{:>1}   {:>1}'.format(x[0], x[1], 'v')
            if len(str(x[1])) == 3:
                a = '  {:>1}:{:>1} {:>1}'.format(x[0], x[1], 'v')
        if x[2] == "W":
            if len(str(x[0])) == 1:
                a = '  {:>1}:{:>1}   {:>1}'.format(x[0], x[1], '<')
            if len(str(x[0])) == 2:
                a = ' {:>1}:{:>1}   {:>1}'.format(x[0], x[1], '<')
            if len(str(x[1])) == 3:
                a = '  {:>1}:{:>1} {:>1}'.format(x[0], x[1], '<')
            if len(str(x[1])) == 3 and len(str(x[0])) == 3:
                a = '{:>1}:{:>1} {:>1}'.format(x[0], x[1], '<')
        if x[2] == "E":
            if len(str(x[0])) == 1:
                a = '  {:>1}:{:>1}   {:>1}'.format(x[0], x[1], '>')
            if len(str(x[0])) == 2:
                a = ' {:>1}:{:>1}   {:>1}'.format(x[0], x[1], '>')
        f.write(a+'\n')
    f.close()


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
