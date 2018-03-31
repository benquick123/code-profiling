def unikati(s):
    nov = []
    for a in s:
        if a not in nov:
            nov.append(a)
    return nov

def avtor(tvit):
    x = tvit.split(":")
    return x[0]

def vsi_avtorji(tviti):
    nov = []
    for x in tviti:
        y = avtor(x)
        if y not in nov:
            nov.append(y)
    return nov

def izloci_besedo(beseda):
    for i in range(2):
        for a in beseda:
            if a.isalnum() == False:
                beseda = beseda[1:len(beseda)]
            else:
                break
        beseda = beseda[::-1]
    return beseda

def se_zacne_z(tvit, c):
    izpis=[]
    n = tvit.split(" ")
    for x in n:
        if c in x:
            x=izloci_besedo(x)
            izpis.append(x)
    return izpis

def zberi_se_zacne_z(tviti, c):
    izpis = []
    for a in tviti:
        if c in a:
            x = se_zacne_z(a, c)
            izpis.extend(x)
    izpis = unikati(izpis)
    return izpis

def vse_afne(tviti):
    izpis=[]
    for y in tviti:
        n = y.split(" ")
        for x in n:
            if "@" in x:
                x = izloci_besedo(x)
                if x not in izpis:
                    izpis.append(x)
    return izpis

def vsi_hashtagi(tviti):
    izpis = []
    for y in tviti:
        n = y.split(" ")
        for x in n:
            if "#" in x:
                x = izloci_besedo(x)
                if x not in izpis:
                    izpis.append(x)
    return izpis

def vse_osebe(tviti):
    izpis=[]
    x = vse_afne(tviti)
    x.extend(vsi_avtorji(tviti))
    izpis = unikati(x)
    izpis.sort()
    return izpis

def custva(tviti, hashtagi):
    izpis = []
    for i in hashtagi:
        for tvit in tviti:
            if i in tvit:
                izpis.append(avtor(tvit))
    izpis = unikati(izpis)
    izpis.sort()
    return izpis

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        x = (avtor(tvit))
        if x == oseba1:
            if oseba2 in tvit and oseba2 in vse_osebe(tviti):
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

