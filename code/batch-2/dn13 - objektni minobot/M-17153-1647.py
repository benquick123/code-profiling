# Napiši razred Minobot. Ta sicer ne bo imel več nobene zveze z minami, imel pa bo zvezo z nalogo Minobot, ki smo jo reševali pred časom.
# Minobot se v začetku nahaja na koordinatah (0, 0) in je obrnjen na desno.
# Koordinatni sistem je takšen kot pri matematiki: koordinata y narašča navzgor.
# Razred Minobot ima naslednje metode.
#   naprej(d) gre za d naprej v podani smeri;
#   desno() se obrne za 90 stopinj v desno;
#   levo() se obrne za 90 stopinj levo;
#   koordinate() vrne trenutne koordinate (x in y)
#   razdalja() vrne pravokotno razdaljo (Manhattansko razdaljo) do koordinat (0, 0): če se robot nahaja na (5, -3), je razdalja do (0, 0) enaka 8.
#   Če, recimo izvedemo
#       a = Minobot()
#       a.levo()
#       a.naprej(4)
#       a.desno()
#       a.naprej(3)
#       print(a.koordinate())
#       se izpiše (3, 4).

class Minobot:

    def __init__(self):
        self.koord = (0, 0)
        self.stran = 0
        self.spr1 = 360
        self.spr2 = 0

    def naprej(self, d):
        x, y = self.koord
        if self.stran == 0:
            x += d
            self.koord = (x, y)
        elif self.stran == 90:
            y += d
            self.koord = (x, y)
        elif self.stran == 180:
            x -= d
            self.koord = (x, y)
        elif self.stran == 270:
            y -= d
            self.koord = (x, y)

    def desno(self):
        self.stran = self.spr1 - 90
        self.spr1 -= 90

        if self.spr1 == 0:
            self.spr1 = 360

    def levo(self):
        self.stran = self.spr2 + 90
        self.spr2 += 90

        if self.spr2 == 360:
            self.spr2 = 0

    def koordinate(self):
        return self.koord

    def razdalja(self):
        zx, zy = self.koord
        kx, ky = (0, 0)
        return abs(kx - zx) + abs(ky - zy)


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
