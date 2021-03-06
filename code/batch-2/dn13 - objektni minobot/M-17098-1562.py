import unittest

class Minobot():
    def __init__(self):
        self.polje_premikov = [(0,0,2)]

    def naprej(self,d):
        if self.polje_premikov[len(self.polje_premikov)- 1][2] == 1:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1] + d, 1))

        if self.polje_premikov[len(self.polje_premikov)- 1 ][2] == 2:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov)- 1][0] + d,
                                        self.polje_premikov[len(self.polje_premikov)- 1][1], 2))

        if self.polje_premikov[len(self.polje_premikov)- 1][2] == 3:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1] - d, 3))

        if self.polje_premikov[len(self.polje_premikov)- 1][2] == 4:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0] - d,
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 4))


    def desno(self):
        if self.polje_premikov[len(self.polje_premikov) - 1][2] == 1:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 2))

        if self.polje_premikov[len(self.polje_premikov) - 1][2] == 2:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 3))

        if self.polje_premikov[len(self.polje_premikov) - 1][2] == 3:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 4))

        if self.polje_premikov[len(self.polje_premikov) - 1][2] == 4:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 1))

    def levo(self):
        if self.polje_premikov[len(self.polje_premikov) - 1][2] == 1:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 4))

        if self.polje_premikov[len(self.polje_premikov) - 1][2] == 2:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 1))

        if self.polje_premikov[len(self.polje_premikov) - 1][2] == 3:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 2))

        if self.polje_premikov[len(self.polje_premikov) - 1][2] == 4:
            return self.polje_premikov.append((self.polje_premikov[len(self.polje_premikov) - 1][0],
                                        self.polje_premikov[len(self.polje_premikov) - 1][1], 3))

    def koordinate(self):
        return((self.polje_premikov[len(self.polje_premikov) - 1][0], self.polje_premikov[len(self.polje_premikov) - 1][1]))

    def razdalja(self):
        x = abs(self.polje_premikov[len(self.polje_premikov) - 1][0])
        y = abs(self.polje_premikov[len(self.polje_premikov) - 1][1])
        return x + y

    def razveljavi(self):
        if len(self.polje_premikov) > 1:
            self.polje_premikov.pop()


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
