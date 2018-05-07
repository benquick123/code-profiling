import os

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
    output = [(0, 0, 'N')]


    f=""
    if ".txt" in ime_datoteke:
        f = ime_datoteke
    else:
        f = ime_datoteke+".txt"
    file = open(f, "r")

    x, y, smer = 0, 0, "N"

    for line in file.readlines():
        vrstica = line.split(" ")

        command = vrstica[0][0]
        ukaz = ""
        naprej = 0
        if command == "D":
            ukaz = "R"
        elif command == "L":
            ukaz = "L"
        else:
            ukaz =  "N"
            naprej = int(vrstica[1])

        """
        if ukaz == "N":
            print(naprej, x, y, smer)
        else:
            print(ukaz, x, y, smer)
"""

        if ukaz == "N":
            x, y, smer = (premik(naprej, x, y, smer))
            output.append((x, y, smer))
        else:
            x, y, smer = (premik(ukaz, x, y, smer))
            output.append((x, y, smer))
    return output

def opisi_stanje(x, y, smer):
    smeri = "NESW"
    puscice = "^>v<"

    ismer = smeri.index(smer)
    puscica = puscice[ismer]

    x = str(x)
    y = str(y)

    #   12:0   ^

    return "{:>3}:{:<4}{}".format(x, y, puscica)

def prevedi(ime_vhoda, ime_izhoda):

    if ".txt" not in ime_vhoda:
        ime_vhoda = ime_vhoda+".txt"

    if ".txt" not in ime_izhoda:
        ime_izhoda = ime_izhoda+".txt"

    i = open(ime_izhoda, "w")

    output = izvedi(ime_vhoda)

    for x, y, smer in output:
        #print(x, y, smer)
        i.write(opisi_stanje(x, y, smer) + "\n")

    i.close()

def opisi_stanje_2(x, y, smer):
    smeri = "NESW"
    puscice = "^>v<"

    ismer = smeri.index(smer)
    puscica = puscice[ismer]

    x = str(x)
    y = str(y)
    #^   (0:12)

    print(x)

    if (len(x) == 1):
        return "{:<4}({}:{})".format(puscica, x, y)
    elif (len(x) == 2):
        return "{:<3}({}:{})".format(puscica, x, y)
    elif (len(x) == 3):
        return "{:<2}({}:{})".format(puscica, x, y)


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
