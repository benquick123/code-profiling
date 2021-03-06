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
    output=[(0, 0, 'N')]
    ukazi=[]
    trenutni_x=trenutni_y=0
    trenutna_smer="N"
    datoteka=open(ime_datoteke)
    for vrstica in datoteka:
        razclenjena_vrstica=vrstica.strip().split()
        ukazi.append(razclenjena_vrstica)
    for niz in ukazi:
        if niz[0]=="DESNO":
            output.append(premik("R",trenutni_x,trenutni_y,trenutna_smer))
            if trenutna_smer=="N":
                trenutna_smer="E"

            elif trenutna_smer=="E":
                trenutna_smer="S"

            elif trenutna_smer=="S":
                trenutna_smer="W"

            elif trenutna_smer=="W":
                trenutna_smer="N"
        if niz[0]=="LEVO":
            output.append(premik("L",trenutni_x,trenutni_y,trenutna_smer))
            if trenutna_smer=="N":
                trenutna_smer="W"

            elif trenutna_smer=="W":
                trenutna_smer="S"

            elif trenutna_smer=="S":
                trenutna_smer="E"

            elif trenutna_smer=="E":
                trenutna_smer="N"
        if niz[0]=="NAPREJ":
            output.append(premik(int(niz[1]),trenutni_x,trenutni_y,trenutna_smer))
            if trenutna_smer=="N":
                trenutni_y=trenutni_y-int(niz[1])

            elif trenutna_smer=="W":
                trenutni_x=trenutni_x-int(niz[1])

            elif trenutna_smer=="S":
                trenutni_y=trenutni_y+int(niz[1])

            elif trenutna_smer=="E":
                trenutni_x=trenutni_x+int(niz[1])
    return output

def opisi_stanje(x, y, smer):
    smeri={"N":"^", "E":">","W":"<","S":"v"}
    return "{x:>3}:{y:<3} {z}".format(x=x,y=y,z=smeri[smer])

def prevedi(ime_vhoda, ime_izhoda):
    ukazi=izvedi(ime_vhoda)
    datoteka=open(ime_izhoda,"w")
    for element in ukazi:
        datoteka.write(opisi_stanje(element[0],element[1],element[2]))
        datoteka.write("\n")
    datoteka.close()


def opisi_stanje_2(x, y, smer):
    smeri={"N":"^", "E":">","W":"<","S":"v"}
    string=""
    if len(str(x))==1:
        string=smeri[smer]+"   ("+str(x)+":"+str(y)+")"
    if len(str(x))==2:
        string=smeri[smer]+"  ("+str(x)+":"+str(y)+")"
    if len(str(x))==3:
        string=smeri[smer]+" ("+str(x)+":"+str(y)+")"
    return string


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
