import unittest

#1. Naloga
####################################################################################

def najpogostejse_polje(navodila):
    robot = Robot()
    polja = {(0,0) : 1}
    max_polje = (0,0)
    for i in navodila:
        if i != 'D' and i != 'L':
            robot.naprej(int(i))
            (x, y) = robot.koordinate()
            if (x, y) not in polja:
                polja[(x,y)] = 1
            else:
                polja[(x,y)] += 1
        elif i == 'L':
            robot.levo()
        else:
            robot.desno()
    for tmp_x, tmp_y in polja:
        if polja[(tmp_x, tmp_y)] > polja[max_polje]:
            max_polje = (tmp_x, tmp_y)
    return max_polje
#########################################################################################

#2. Naloga
#########################################################################################
def navodila(zaporedje):
    ret_list = []
    tmp_list = []
    for i in zaporedje:
        is_num = False
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            tmp_list.append(i)
            is_num = True
        if not is_num:
            if tmp_list:
                tmp_list = "".join(tmp_list)
                ret_list.append(int(tmp_list))
                tmp_list = []
                ret_list.append(i)
            else:
                ret_list.append(i)

    if tmp_list:
        tmp_list = "".join(tmp_list)
        ret_list.append(int(tmp_list))
    return ret_list
#########################################################################################

#3. Naloga
#########################################################################################
def zamenjano(s, menjave):
    ret_list = []
    for oseba in s:
        if oseba not in menjave:
            ret_list.append(oseba)
            continue
        ret_list.append(menjave[oseba])
    return ret_list

def zamenjaj(s, menjave):
    tmp = zamenjano(s, menjave)
    s[:] = tmp

#########################################################################################

#4. Naloga
#########################################################################################
def sprazni(s):
    ret_list = []
    if not s:
        return ret_list
    for i in s:
        if i != None:
            ret_list.append(sprazni(i))
    return ret_list
#########################################################################################



#5. Naloga
#########################################################################################
class Carovnik:
    def __init__(self, ponudba, cena):
        ponudba = ponudba.split()
        self.iz = ponudba[0]
        self.v = ponudba[2]
        self.cena = cena
        self.profit = 0
    def caraj(self, s):
        ret_list = []
        for i in s:
            if i == self.iz:
                ret_list.append(self.v)
                self.profit += self.cena
            else:
                ret_list.append(i)
        return ret_list
    def zasluzek(self):
        return self.profit
#########################################################################################

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

