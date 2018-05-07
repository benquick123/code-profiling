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
    rezSez = []
    currentSide = 'N'
    currX = 0
    currY = 0
    rezSez.append((currX, currY, currentSide))
    with open(ime_datoteke) as f:
        for line in f:
            if(line.__contains__("DESNO")):
                currentSide = premik("R", currX, currY, currentSide)[2]
                rezSez.append((currX, currY, currentSide))
            if (line.__contains__("LEVO")):
                currentSide = premik("L", currX, currY, currentSide)[2]
                rezSez.append((currX, currY, currentSide))
            if(line.__contains__("NAPREJ")):
                moveLen = int(line.split()[1])
                currX = premik(moveLen, currX, currY, currentSide)[0]
                currY = premik(moveLen, currX, currY, currentSide)[1]
                rezSez.append((currX, currY, currentSide))
    return rezSez

def opisi_stanje(x, y, smer):
    returnStr = ""
    if x >= 100 or x <= -10:
        returnStr += str(x)
    elif x >= 10 or x <= -1:
        returnStr += " " + str(x)
    else:
        returnStr += "  " + str(x)

    returnStr += ":"

    if y >= 100 or y <= -10:
        returnStr += str(y)
    elif y >= 10 or y <= -1:
        returnStr += str(y) + " "
    else:
        returnStr += str(y) + "  "

    returnStr += " "

    if smer == "N":
        returnStr += "^"
    if smer == "E":
        returnStr += ">"
    if smer == "W":
        returnStr += "<"
    if smer == "S":
        returnStr += "v"

    return returnStr


def prevedi(ime_vhoda, ime_izhoda):
    seznamPremik = izvedi(ime_vhoda)
    newFile = open(ime_izhoda, 'w+')
    for currPremik in seznamPremik:
        newFile.write(opisi_stanje(currPremik[0], currPremik[1], currPremik[2]) + "\n")
    newFile.close()


def opisi_stanje_2(x, y, smer):
    returnStr = ""
    if smer == "N":
        returnStr += "^"
    if smer == "E":
        returnStr += ">"
    if smer == "W":
        returnStr += "<"
    if smer == "S":
        returnStr += "v"

    returnStr += " "

    getX = "(" + str(x)
    for i in range(len(getX), 4):
        returnStr += " "
    returnStr += getX + ":" + str(y) + ")"

    return returnStr




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
