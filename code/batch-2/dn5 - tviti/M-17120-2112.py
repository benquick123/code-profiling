def unikati(s):
    seznam = []
    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam


def avtor(tvit):
    x = tvit.find(":")
    return tvit[:x]


def vsi_avtorji(tviti):
    seznam = []
    for oseba in tviti:
        x = avtor(oseba)
        seznam.append(x)
    koncni_seznam = unikati(seznam)
    return koncni_seznam


def izloci_besedo(beseda):
    for x in beseda:
        if not x.isalnum():
            beseda=beseda[1:]
        else:
            break
    for x in beseda[::-1]:
        if not x.isalnum():
            beseda=beseda[:-1]
        else:
            break
    return beseda


def se_zacne_z(tvit, c):
    seznam = []
    tviti=tvit.split()
    for x in tviti:
        for y in x:
            if y==c:
                beseda=izloci_besedo(x)
                seznam.append(beseda)
    return seznam


def zberi_se_zacne_z(tviti, c):
    seznam = []
    for x in tviti:
        beseda=se_zacne_z(x,c)
        for x in beseda:
            seznam.append(x)
    seznam=unikati(seznam)
    return seznam


def vse_afne(tviti):
    seznam = []
    for x in tviti:
        beseda=se_zacne_z(x,"@")
        for x in beseda:
            seznam.append(x)
    seznam=unikati(seznam)
    return seznam


def vsi_hashtagi(tviti):
    seznam = []
    for x in tviti:
        beseda=se_zacne_z(x,"#")
        for x in beseda:
            seznam.append(x)
    seznam=unikati(seznam)
    return seznam


def vse_osebe(tviti):
    seznam=[]
    for tvit in tviti:
        ime=avtor(tvit)
        if ime:
            seznam.append(ime)
    afne=vse_afne(tviti)
    for ime in afne:
        seznam.append(ime)
    seznam=unikati(seznam)
    seznam.sort()
    return seznam


def custva(tviti, hashtagi):
    seznam=[]
    for x in tviti:
        for y in hashtagi:
            hashi=se_zacne_z(x,"#")
            for z in hashi:
                if z==y:
                    ime=avtor(x)
                    if ime!=[]:
                        seznam.append(ime)
    seznam=unikati(seznam)
    seznam.sort()
    return seznam


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        ime=avtor(tvit)
        afna=se_zacne_z(tvit,"@")
        for x in afna:
            if ime == oseba1 and x == oseba2 or ime == oseba2 and x == oseba1:
                return True
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

