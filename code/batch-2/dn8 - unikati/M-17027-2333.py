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
    s = open(ime_datoteke)
    j = "N"
    o=[(0,0,"N")]
    i=0
    u=0
    for a in s:
        b="".join(a.strip().split(" ")[1:])
        if b:
            b=b
        else:
            b = 0
        b = int(b)
        if a[0] == "D":
            b = "R"
        elif a[0] == "L":
            b = "L"
        k = premik(b, 0, 0, j)
        j = k[2]
        i += k[0]
        u += k[1]
        o.append((i,u,j))
    #print(o)
    return o

def opisi_stanje(x,y,smer):
    string = ""
    if smer == "N":
        string += "{:>3}:{:<3} ^".format(x,y)
    elif smer == "E":
        string += "{:>3}:{:<3} >".format(x, y)
    elif smer == "S":
        string += "{:>3}:{:<3} v".format(x, y)
    elif smer == "W":
        string += "{:>3}:{:<3} <".format(x, y)
    #print(string)
    return string

def prevedi(ime_vhoda, ime_izhoda):
    s = open(ime_izhoda, "w")
    i = izvedi(ime_vhoda)
    #print(i)
    for a in i:
       # print(a)
        k = opisi_stanje(a[0],a[1],a[2])
        print(k)
        s.write(k+"\n")
    s.close()

def opisi_stanje_2(x,y,smer):
    string = ""
    if smer == "N":
        string += "^{:>5}:{})".format(("("+str(x)), y)
    elif smer == "E":
        string += ">{:>5}:{})".format(("("+str(x)), y)
    elif smer == "S":
        string += "v{:>5}:{})".format(("("+str(x)), y)
    elif smer == "W":
        string += "<{:>5}:{})".format(("("+str(x)), y)
    print(string)
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
