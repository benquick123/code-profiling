import unittest

def najpogostejse_polje(navodila):
    seznam = []
    isti = []
    robot = Robot()
    index = 0
    slovar ={}
    for navodilo in navodila:
        if navodilo == int:
            robot.naprej(navodilo)
        if navodilo == "D":
            robot.desno()
        if navodilo == "L":
            robot.levo()
        k = robot.koordinate()
        seznam.append(k)
    for x in seznam:
        g = isti.count(x)
        slovar[g] = seznam[index]
        index +=1
    gg = max(slovar)
    return slovar[gg]

def navodila(zaporedje):
    seznam = []
    neki = ""
    x = 0
    st = range(0 ,99999)
    for z in zaporedje:
        if z == "D" or "L":
            seznam.append(z)
        if z in st:
            neki + z
            for b in zaporedje[x:]:
                if b in st:
                    neki + b
        if neki != "":
            neki = int(neki)                                 #noče spremenit v intiger
            seznam.append(neki)
        x += 1
    return seznam


def zamenjano(s, menjave):
    seznam = []
    nov = []
    index = 0
    for key in menjave:
        for x in s:
            if x == key:
                seznam.append(x)
            else:
                pass
    for x in seznam:
        g = menjave[x]
        seznam.remove(x)
        seznam[index] += g
        index += 1
    return seznam


def sprazni(s):
    nov = []
    prazen = []
    for n in s:
        if n == prazen:
            nov.append(n)
    return nov


class Carovnik:

    def __init__(self, konstruktor, cena):
        bu = konstruktor.split(" -> ")
        self.stane = cena
        self.cenaa = 0
        self.kaj = bu[0]
        self.v = bu[1]

    def caraj(self, s):
        seznam = []
        for element in s:
            if element == self.kaj:
                seznam.append(self.v)
            else:
                seznam.append(element)
        self.cenaa += self.stane
        return seznam

    def zasluzek(self):
        return self.cenaa




class Robot:
    def __init__(self):
        self.x = self.y = 0
        self.smer = 1

    def desno(self):
        self.smer = (self.smer + 1) % 4

    def levo(self):
        self.smer = (self.smer - 1) % 4

    def naprej(self, d):
        if self.smer == 0:
            self.y += d
        elif self.smer == 1:
            self.x += d
        elif self.smer == 2:
            self.y -= d
        else:
            self.x -= d

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)


class Test01NajpogostejsePolje(unittest.TestCase):
    def test_najpogostejse_polje(self):
        self.assertEqual(najpogostejse_polje("D2DD2"), (0, 0))
        self.assertEqual(najpogostejse_polje("D2DDDDDDDDDD2"), (0, 0))
        self.assertEqual(najpogostejse_polje("D2L3LL3L41DD4D3"), (0, -2))
        self.assertEqual(najpogostejse_polje("D222LL2"), (0, -4))


class Test02Navodila(unittest.TestCase):
    def test_navodila(self):
        self.assertEqual(navodila("LL"), ["L", "L"])
        self.assertEqual(navodila("L4D"), ["L", 4, "D"])
        self.assertEqual(navodila("D41L"), ["D", 41, "L"])
        self.assertEqual(navodila("123D41L"), [123, "D", 41, "L"])
        self.assertEqual(navodila("123D41L1"), [123, "D", 41, "L", 1])
        self.assertEqual(navodila("123D41L15"), [123, "D", 41, "L", 15])
        self.assertEqual(navodila("123DL"), [123, "D", "L"])
        self.assertEqual(navodila("123LD"), [123, "L", "D"])
        self.assertEqual(navodila("LLD123"), ["L", "L", "D", 123])
        self.assertEqual(navodila("LLD1231"), ["L", "L", "D", 1231])
        self.assertEqual(navodila("42"), [42])
        self.assertEqual(navodila("58286938140968" * 10), [int("58286938140968" * 10)])


class Test03Menjave(unittest.TestCase):
    def test_zamenjano(self):
        s = [5, 3, 1, 1, 3, 2, 6]
        t = s[:]
        self.assertEqual(zamenjano(s, {3: 1, 1: 7}), [5, 1, 7, 7, 1, 2, 6])
        self.assertEqual(s, t)

        s = [5, 3, 1, 1, 3, 2, 6]
        t = s[:]
        self.assertEqual(zamenjano(s, {3: 1, 5: 1, 2: 1, 1: 7}), [1, 1, 7, 7, 1, 1, 6])
        self.assertEqual(s, t)

        s = ["Ana", "Ana", "Berta", "Ana", "Cilka"]
        t = s[:]
        self.assertEqual(zamenjano(s, {"Ana": "Peter", "Berta": "Ana"}), ["Peter", "Peter", "Ana", "Peter", "Cilka"])
        self.assertEqual(s, t)

        s = ["Ana", "Ana", "Berta", "Ana", "Cilka"]
        t = s[:]
        self.assertEqual(zamenjano(s, {}), t)
        self.assertEqual(s, t)

        s = []
        self.assertEqual(zamenjano(s, {3: 1, 5: 1, 2: 1, 1: 7}), [])

    def test_zamenjaj(self):
        s = [5, 3, 1, 1, 3, 2, 6]
        self.assertIsNone(zamenjaj(s, {3: 1, 1: 7}))
        self.assertEqual(s, [5, 1, 7, 7, 1, 2, 6])

        s = [5, 3, 1, 1, 3, 2, 6]
        self.assertIsNone(zamenjaj(s, {3: 1, 5: 1, 2: 1, 1: 7}))
        self.assertEqual(s, [1, 1, 7, 7, 1, 1, 6])

        s = ["Ana", "Ana", "Berta", "Ana", "Cilka"]
        self.assertIsNone(zamenjaj(s, {"Ana": "Peter", "Berta": "Ana"}))
        self.assertEqual(s, ["Peter", "Peter", "Ana", "Peter", "Cilka"])

        s = ["Ana", "Ana", "Berta", "Ana", "Cilka"]
        self.assertIsNone(zamenjaj(s, {}))
        self.assertEqual(s, ["Ana", "Ana", "Berta", "Ana", "Cilka"])

        s = []
        self.assertIsNone(zamenjaj(s, {"Ana": "Peter", "Berta": "Ana"}))
        self.assertEqual(s, [])


class Test04Sprazni(unittest.TestCase):
    def test_sprazni(self):
        self.assertEqual(sprazni([None, None, None]), [])
        self.assertEqual(sprazni([[[None, None, None]]]), [[[]]])
        self.assertEqual(sprazni([[[]]]), [[[]]])
        self.assertEqual(sprazni([None, None, [None], [None, None, []], None]), [[], [[]]])


class Test05Carovnik(unittest.TestCase):
    def test_carovnik(self):
        alkemist = Carovnik("svinec -> zlato", 10)
        piroman = Carovnik("les -> pepel", 2)
        feniks = Carovnik("pepel -> svinec", 4)
        stvari = ["svinec", "svinec", "les", "zlato", "svinec"]

        self.assertEqual(alkemist.zasluzek(), 0)
        self.assertEqual(piroman.zasluzek(), 0)
        self.assertEqual(feniks.zasluzek(), 0)

        stvari = feniks.caraj(stvari)
        self.assertEqual(stvari, ["svinec", "svinec", "les", "zlato", "svinec"])
        self.assertEqual(alkemist.zasluzek(), 0)
        self.assertEqual(piroman.zasluzek(), 0)
        self.assertEqual(feniks.zasluzek(), 0)

        stvari = alkemist.caraj(stvari)
        self.assertEqual(stvari, ["zlato", "zlato", "les", "zlato", "zlato"])
        self.assertEqual(alkemist.zasluzek(), 30)
        self.assertEqual(piroman.zasluzek(), 0)
        self.assertEqual(feniks.zasluzek(), 0)

        stvari = piroman.caraj(stvari)
        self.assertEqual(stvari, ["zlato", "zlato", "pepel", "zlato", "zlato"])
        self.assertEqual(alkemist.zasluzek(), 30)
        self.assertEqual(piroman.zasluzek(), 2)
        self.assertEqual(feniks.zasluzek(), 0)

        stvari = piroman.caraj(stvari)
        self.assertEqual(stvari, ["zlato", "zlato", "pepel", "zlato", "zlato"])
        self.assertEqual(alkemist.zasluzek(), 30)
        self.assertEqual(piroman.zasluzek(), 2)
        self.assertEqual(feniks.zasluzek(), 0)

        stvari = feniks.caraj(stvari)
        self.assertEqual(stvari, ["zlato", "zlato", "svinec", "zlato", "zlato"])
        self.assertEqual(alkemist.zasluzek(), 30)
        self.assertEqual(piroman.zasluzek(), 2)
        self.assertEqual(feniks.zasluzek(), 4)

        stvari = alkemist.caraj(stvari)
        self.assertEqual(stvari, ["zlato", "zlato", "zlato", "zlato", "zlato"])
        self.assertEqual(alkemist.zasluzek(), 40)
        self.assertEqual(piroman.zasluzek(), 2)
        self.assertEqual(feniks.zasluzek(), 4)

        druge = ["pepel", "pepel", "svinec", "zlato"]
        druge = feniks.caraj(druge)
        self.assertEqual(druge, ["svinec", "svinec", "svinec", "zlato"])
        self.assertEqual(alkemist.zasluzek(), 40)
        self.assertEqual(piroman.zasluzek(), 2)
        self.assertEqual(feniks.zasluzek(), 12)

        nic = []
        nic = feniks.caraj(nic)
        self.assertEqual(nic, [])
        self.assertEqual(alkemist.zasluzek(), 40)
        self.assertEqual(piroman.zasluzek(), 2)
        self.assertEqual(feniks.zasluzek(), 12)



if __name__ == "__main__":
    unittest.main()

