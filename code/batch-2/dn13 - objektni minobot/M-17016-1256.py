from collections import deque
#inicializacija classa


class Minobot:
    #inicializacija osnovnih vrednosti
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = "E"
        self.history = []

    def naprej(self, d):
        #za vsak mozen otation
        if self.rotation == "E":
            self.x = self.x + d
        elif self.rotation == "S":
            self.y = self.y - d
        elif self.rotation == "W":
            self.x = self.x - d
        elif self.rotation == "N":
            self.y = self.y + d

        #doda element v history
        self.history = self.history + [("N", d)]


    def desno(self):

        #list smeri ki ga kasneje rotejta
        smeri = ["N", "E", "S", "W"]

        #dobi indeks smeri ki jo ima zdaj
        index_s = smeri.index(self.rotation)

        #obrne list smeri tako da se zamaknejo za eno v levo
        nove_smeri = [smeri[1], smeri[2], smeri[3], smeri[0]]

        #spremeni trenuten rotation za enega bolj desno
        self.rotation = nove_smeri[index_s]

        # doda element v history
        self.history = self.history + ["R"]


    def levo(self):
        #isti k kot pri desno() samo da rotejta v drugo smer
        smeri = ["N", "E", "S", "W"]
        index_s = smeri.index(self.rotation)
        nove_smeri = [smeri[3], smeri[0], smeri[1], smeri[2]]
        self.rotation = nove_smeri[index_s]
        # doda element v history
        self.history = self.history + ["L"]

    #pomožna funkcija za razveljavi()
    def nazaj(self, d):
        if self.rotation == "E":
            self.x = self.x - d
        elif self.rotation == "S":
            self.y = self.y + d
        elif self.rotation == "W":
            self.x = self.x + d
        elif self.rotation == "N":
            self.y = self.y - d
        self.history = self.history + [("N", d)]

    #ez
    def koordinate(self):
        return self.x, self.y

    #ez
    def razdalja(self):
        return abs(self.x) + abs(self.y)

    #pomožna funkcija za izpisovanje zgodovine
    def ret(self):
        return self.history

    def razveljavi(self):
        #če je kak element v historiju
        if self.history:
            step = self.history.pop()


            if step == "R":
                self.levo()
            elif step == "L":
                self.desno()
            else:
                self.nazaj(step[1])

            #zbrisi zadnjega
            self.history = self.history[:-1]



m = Minobot()
m.desno()
m.naprej(10)
m.levo()

print(m.ret())


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
