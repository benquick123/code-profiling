def unikati(s):
    nov_seznam = []
    for x in s:
        if x in nov_seznam:
            pass
        else:
            nov_seznam.append(x)
    return nov_seznam


def avtor(tvit):
    return tvit.split(":")[0]


def vsi_avtorji(tviti):
    seznam2 = []
    for kos in tviti:
        seznam2.append(avtor(kos))
    return unikati(seznam2)


def izloci_besedo(beseda):
    while not beseda[0].isalnum():
            beseda = beseda[1:]
    while not beseda[-1].isalnum():
           beseda = beseda[:-1]
    return beseda


def se_zacne_z(tvit, c):
    seznam3 = tvit.split(" ")
    seznam4 = []
    for beseda in seznam3:
        if beseda[0] == c:
            seznam4.append(izloci_besedo(beseda))
    return seznam4


def zberi_se_zacne_z(tviti, c):
    seznam3 =[]
    for x in tviti:
        seznam3 += x.split(" ")
    seznam4 = []
    for beseda in seznam3:
        if beseda[0] == c:
            if izloci_besedo(beseda) in seznam4:
                pass
            else:
                seznam4.append(izloci_besedo(beseda))
    return seznam4


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    seznam_oseb = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    seznam_oseb.sort()
    return seznam_oseb


def custva(tviti, hashtagi):
    seznam1 =[]
    seznam_avtorjev = []
    for x in tviti:
        seznam1 = x.split(" ")
        for beseda in seznam1:
            if beseda[0] == "#":
                if izloci_besedo(beseda) in hashtagi:
                     seznam_avtorjev.append(avtor(x))
    seznam_avtorjev = unikati(seznam_avtorjev)
    seznam_avtorjev.sort()
    return seznam_avtorjev


def se_poznata(tviti, oseba1, oseba2):
    seznam1 =[]
    velja = 0
    for x in tviti:
        seznam1 = x.split(" ")
        for beseda in seznam1:
            if beseda[0] == "@":
                if izloci_besedo(beseda) == oseba1 and oseba2 == avtor(x):
                     velja += 1
    seznam2 =[]
    for x in tviti:
        seznam2 = x.split(" ")
        for beseda in seznam2:
            if beseda[0] == "@":
                if izloci_besedo(beseda) == oseba2 and oseba1 == avtor(x):
                     velja += 1
    if velja:
        return True
    else:
        return False



import unittest


class TestTviti(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]

    def test_unikat(self):
        self.assertEqual(unikati([1, 2, 1, 1, 3, 2]), [1, 2, 3])
        self.assertEqual(unikati([1, 3, 2, 1, 1, 3, 2]), [1, 3, 2])
        self.assertEqual(unikati([1, 5, 4, 3, 2]), [1, 5, 4, 3, 2])
        self.assertEqual(unikati([1, 1, 1, 1, 1]), [1])
        self.assertEqual(unikati([1]), [1])
        self.assertEqual(unikati([]), [])
        self.assertEqual(unikati(["Ana", "Berta", "Cilka", "Berta"]), ["Ana", "Berta", "Cilka"])

    def test_avtor(self):
        self.assertEqual(avtor("janez: pred dvopičjem avtor, potem besedilo"), "janez")
        self.assertEqual(avtor("ana: malo krajse ime"), "ana")
        self.assertEqual(avtor("benjamin: pomembne so tri stvari: prva, druga in tretja"), "benjamin")

    def test_vsi_avtorji(self):
        self.assertEqual(vsi_avtorji(self.tviti), ["sandra", "berta", "ana", "cilka", "benjamin", "ema"])
        self.assertEqual(vsi_avtorji(self.tviti[:3]), ["sandra", "berta"])

    def test_izloci_besedo(self):
        self.assertEqual(izloci_besedo("@ana"), "ana")
        self.assertEqual(izloci_besedo("@@ana!!!"), "ana")
        self.assertEqual(izloci_besedo("ana"), "ana")
        self.assertEqual(izloci_besedo("!#$%\"=%/%()/Ben-jamin'"), "Ben-jamin")

    def test_vse_na_crko(self):
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! #Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("ana: kdo so te @berta, @cilka, @dani? #krneki", "@"), ["berta", "cilka", "dani"])

    def test_zberi_na_crko(self):
        self.assertEqual(zberi_se_zacne_z(self.tviti, "@"), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])
        self.assertEqual(zberi_se_zacne_z(self.tviti, "#"), ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_vse_afne(self):
        self.assertEqual(vse_afne(self.tviti), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])

    def test_vsi_hashtagi(self):
        self.assertEqual(vsi_hashtagi(self.tviti), ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_vse_osebe(self):
        self.assertEqual(vse_osebe(self.tviti), ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'])


class TestDodatna(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]

    def test_custva(self):
        self.assertEqual(custva(self.tviti, ["dougcajt", "krneki"]), ["ana", "sandra"])
        self.assertEqual(custva(self.tviti, ["luft"]), ["cilka"])
        self.assertEqual(custva(self.tviti, ["meh"]), [])

    def test_se_poznata(self):
        self.assertTrue(se_poznata(self.tviti, "ana", "berta"))
        self.assertTrue(se_poznata(self.tviti, "ema", "ana"))
        self.assertFalse(se_poznata(self.tviti, "sandra", "ana"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "luft"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "balon"))


if __name__ == "__main__":
    unittest.main()

