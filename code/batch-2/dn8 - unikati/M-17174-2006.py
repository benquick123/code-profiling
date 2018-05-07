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
    d = open(ime_datoteke).read().split("\n")[:-1]
    x, y = 0, 0
    smer = "N"
    u = [(x, y, smer)]
    for z in d:
        if z[:6] == "NAPREJ":
            d = premik(int(z[7:]), x, y, smer)
            u.append(d)
            x, y, smer = d[0], d[1], d[2]
        else:
            d = premik(("R" if z[0] == "D" else "L"), x, y, smer)
            u.append(d)
            x, y, smer = d[0], d[1], d[2]
    return u


def opisi_stanje(x, y, smer):
    if smer == "N":
        return "{: >3}:{: <3} {}".format(x, y, "^")
    elif smer == "W":
        return "{: >3}:{: <3} {}".format(x, y, "<")
    elif smer == "E":
        return "{: >3}:{: <3} {}".format(x, y, ">")
    else:
        return "{: >3}:{: <3} {}".format(x, y, "v")


def prevedi(ime_vhoda, ime_izhoda):
    s = izvedi(ime_vhoda)
    d = open(ime_izhoda, "w")
    for m in s:
        d.write(opisi_stanje(m[0], m[1], m[2]) + "\n")
    d.close()


def opisi_stanje_2(x, y, smer):
    if smer == "N":
        print("{} {x: >4}:{y: <1}".format("^", x="(" + str(x), y=str(y) + ")"))
        return "{} {x: >4}:{y: <1}".format("^", x="(" + str(x), y=str(y) + ")")
    elif smer == "W":
        print("{} {x: >4}:{y: <1}".format("<", x="(" + str(x), y=str(y) + ")"))
        return "{} {x: >4}:{y: <1}".format("<", x="(" + str(x), y=str(y) + ")")
    elif smer == "E":
        print("{} {x: >4}:{y: <1}".format(">", x="(" + str(x), y=str(y) + ")"))
        return "{} {x: >4}:{y: <1}".format(">", x="(" + str(x), y=str(y) + ")")
    else:
        print("{} {x: >4}:{y: <1}".format("v", x="(" + str(x), y=str(y) + ")"))
        return "{} {x: >4}:{y: <1}".format("v", x="(" + str(x), y=str(y) + ")")


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
        self.assertEqual(opisi_stanje_2(0, 12, "N"), "^   (0:12)")
        self.assertEqual(opisi_stanje_2(111, 0, "E"), "> (111:0)")
        self.assertEqual(opisi_stanje_2(-2, 111, "S"), "v  (-2:111)")
        self.assertEqual(opisi_stanje_2(0, 0, "W"), "<   (0:0)")


if __name__ == "__main__":
    unittest.main()
