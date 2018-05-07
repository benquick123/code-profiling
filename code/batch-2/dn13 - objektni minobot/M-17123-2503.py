class Minobot:
    def __init__(self):
        kompas = ["N", "E", "S", "W"]
        self.x, self.y = 0, 0
        self.sprememba_pozicije = 1
        self.trenutna_pozicija = kompas[self.sprememba_pozicije]
        self.izvrseno = []
    def koordinate(self):
        kx, ky = self.x, self.y
        #print(self.trenutna_pozicija)
        #print("koordinate:",(kx,ky))
        #print("izvrseno:", self.izvrseno)
        return (kx,ky)

    def naprej(self, d):
        if self.trenutna_pozicija == "N":
            self.y+= d
        if self.trenutna_pozicija == "E":
            self.x+= d
        if self.trenutna_pozicija == "S":
            self.y-= d
        if self.trenutna_pozicija == "W":
            self.x-= d
        #print("naprej", d)
        self.izvrseno.append(d)
        #print("izvrseno:", self.izvrseno)
        return (self.x,self.y)

    def desno(self):
        kompas = ["N", "E", "S", "W"]
        self.sprememba_pozicije+= 1
        if self.sprememba_pozicije == 4:
            self.sprememba_pozicije = 0
        self.trenutna_pozicija = kompas[self.sprememba_pozicije]
        self.izvrseno.append("desno")
        #print("desno:", self.sprememba_pozicije)
        #print("izvrseno:", self.izvrseno)

    def levo(self):
        kompas = ["N", "E", "S", "W"]
        self.sprememba_pozicije-= 1
        if self.sprememba_pozicije == -4:
            self.sprememba_pozicije = 0
        self.trenutna_pozicija = kompas[self.sprememba_pozicije]
        self.izvrseno.append("levo")
        #print("levo:", self.sprememba_pozicije)
        #print("izvrseno:", self.izvrseno)

    def razdalja(self):
        manhattanska = abs(self.x) + abs(self.y)
        return manhattanska

    def razveljavi(self):
        if self.trenutna_pozicija == "E":
            self.x-= self.izvrseno[-1]
            self.izvrseno.pop(-1)
            #print(self.izvrseno)
        if self.trenutna_pozicija == "S":
            self.y-= self.izvrseno[-1]
            self.izvrseno.pop(-1)
            #print(self.izvrseno)
        if self.izvrseno[-1] == "levo" and self.trenutna_pozicija == "E":
            self.trenutna_pozicija = "S"
            self.izvrseno.pop(-1)
            #print(self.izvrseno)


import unittest
class TestObvezna(unittest.TestCase):
    def test_minobot(self):
        a = Minobot()
        b = Minobot()

        self.assertEqual(a.koordinate(), (0, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 0)
        self.assertEqual(b.razdalja(), 0)

        a.naprej(1)
        self.assertEqual(a.koordinate(), (1, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 1)
        self.assertEqual(b.razdalja(), 0)

        a.naprej(2)
        self.assertEqual(a.koordinate(), (3, 0))
        self.assertEqual(b.koordinate(), (0, 0))
        self.assertEqual(a.razdalja(), 3)
        self.assertEqual(b.razdalja(), 0)

        b.naprej(2)
        self.assertEqual(a.koordinate(), (3, 0))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 3)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # zdaj je obrnjen dol
        a.naprej(4)
        self.assertEqual(a.koordinate(), (3, -4))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 7)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen je levo
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -4))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 6)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen je gor
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -3))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 5)
        self.assertEqual(b.razdalja(), 2)

        a.desno()  # obrnjen desno
        a.naprej(3)
        self.assertEqual(a.koordinate(), (5, -3))
        self.assertEqual(b.koordinate(), (2, 0))
        self.assertEqual(a.razdalja(), 8)
        self.assertEqual(b.razdalja(), 2)

        b.levo()  # obrnjen gor
        b.naprej(3)
        self.assertEqual(b.koordinate(), (2, 3))
        self.assertEqual(b.razdalja(), 5)

        b.levo()  # obrnjen levo
        b.naprej(3)
        self.assertEqual(b.koordinate(), (-1, 3))
        self.assertEqual(b.razdalja(), 4)

        a.naprej(5)
        self.assertEqual(a.koordinate(), (10, -3))
        self.assertEqual(a.razdalja(), 13)


class TestDodatna(unittest.TestCase):
    def test_undo(self):
        a = Minobot()
        a.desno()  # gleda dol
        a.naprej(4)
        a.levo()  # gleda desno
        a.naprej(1)
        a.naprej(2)

        self.assertEqual(a.koordinate(), (3, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (1, -4))
        a.naprej(1)
        self.assertEqual(a.koordinate(), (2, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (1, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.naprej(1)
        self.assertEqual(a.koordinate(), (1, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.razveljavi()  # spet gleda dol
        self.assertEqual(a.koordinate(), (0, -4))
        a.naprej(2)
        self.assertEqual(a.koordinate(), (0, -6))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, -4))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(3)
        self.assertEqual(a.koordinate(), (0, -3))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # spet gleda desno
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(3)
        self.assertEqual(a.koordinate(), (3, 0))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.naprej(2)
        self.assertEqual(a.koordinate(), (2, 0))
        a.razveljavi()
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))
        a.razveljavi()  # se ne usuje
        self.assertEqual(a.koordinate(), (0, 0))


if __name__ == "__main__":
    unittest.main()
