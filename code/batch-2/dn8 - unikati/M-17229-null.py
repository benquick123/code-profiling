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
    ukaz = []
    x = 0
    y = 0
    smer = 0
    smeri = "NESW"
    koraki = [(0, 0, "N")]
    for vrstica in open(ime_datoteke):
        vrstica = vrstica.strip()
        if "NAPREJ" in vrstica:
            vrstica = vrstica.split(" ")
            ukaz.append(int(vrstica[1]))
        else:
            ukaz.append(vrstica)
    for n in ukaz:
        if n == "DESNO":
            smer = smer+1
            if smer > 3:
                smer = 0
        elif n == "LEVO":
            smer = smer-1
            if smer < 0:
                smer = 3
        else:
            if smer == 0:
                y = y - n
            elif smer == 1:
                x = x + n
            elif smer == 2:
                y = y + n
            else:
                x = x - n
        koraki.append((x, y, smeri[smer]))
    return koraki



def opisi_stanje(x,y,smer):
    smeri = [("N","^"),("E",">"),("S","v"),("W","<")]
    for a,b in smeri:
        if a == smer:
            return "{x:>3}:{y:<3} {b}".format(x = x,y = y, b=b)

def prevedi(ime_vhoda, ime_izhoda):
    koraki = izvedi(ime_vhoda)
    file = open(ime_izhoda, "w")
    for x,y,s in koraki:
        file.write("{}\n".format(opisi_stanje(x,y,s)))


def opisi_stanje_2(x, y, smer):
    z = ""
    for n in range(3 - len(str(x))):
        z = z + " "
    smeri = [("N","^"),("E",">"),("S","v"),("W","<")]
    for a,b in smeri:
        if a == smer:
            return "%s " % b + z + "(%d:%d)" % (x, y)


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
