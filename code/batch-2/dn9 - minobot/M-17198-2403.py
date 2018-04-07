def premik(ukaz, x, y, smer):
    smeri = "NESW"
    premiki = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    ismer = smeri.index(smer)
    if ukaz.strip() == "DESNO":
        smer = smeri[(ismer + 1) % 4]
    elif ukaz.strip() == "LEVO":
        smer = smeri[(ismer - 1) % 4]
    else:
        dx, dy = premiki[ismer]
        x += dx * int(ukaz.strip().split()[1])
        y += dy * int(ukaz.strip().split()[1])
    return x, y, smer



#NALOGE ABLBLBLBBLBLBL
def izvedi(ime_datoteke):
    array=[]
    x=0
    y=0
    smer ="N"
    array.append((x,y,smer))
    for vrstica in open(ime_datoteke):
        array.append(premik(vrstica.strip(),x,y,smer))
        x=premik(vrstica,x,y,smer)[0]
        y=premik(vrstica,x,y,smer)[1]
        smer =premik(vrstica,x,y,smer)[2]
    return array


def opisi_stanje(x,y,smer):
    znak = ""
    if smer == "N":
        znak="^"
    elif smer == "S":
        znak="v"
    elif smer == "W":
        znak="<"
    else:
        znak=">"
    return("{x:>3}:{y:<3}{znak:>2}".format(x=x,y=y,znak=znak))

def prevedi(ime_vhoda,ime_izhoda):
    ukazi=izvedi(ime_vhoda)
    out=open(ime_izhoda,'w+')
    for ukaz in ukazi:
        out.write(opisi_stanje(ukaz[0],ukaz[1],ukaz[2])+"\n")
    

def opisi_stanje_2(x,y,smer):
    puscica = ""
    if smer == "N":
        puscica="^"
    elif smer == "S":
        puscica="v"
    elif smer == "W":
        puscica="<"
    else:
        puscica=">"
    x="("+str(x)
    return("{puscica}{x:>5}:{y})".format(puscica=puscica,x=x,y=y))


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
