import unittest #bucha = nespremenljivka

def unikati(s):
    seznam = []
    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam

def avtor(tvit):
    tweet = ""
    a = 0
    stev = 0
    for x in tvit:
        stev = tvit.find(":")
        while a != stev:
            tweet+=tvit[a]
            a+=1
    return tweet

def vsi_avtorji(tviti):
    a = ""
    seznam = []
    drugi_seznam = []
    for x in tviti:
        seznam.append(x)
        y = x.split(":")
        drugi_seznam.append(y[0])

    return unikati(drugi_seznam)


def izloci_besedo(beseda):
    besedica = ""
    koncno = ""
    for x in beseda:
        if x.isalnum() != True:
            beseda = beseda.replace(x, "")
        else:
            besedica = beseda[::-1]
            break
    for y in besedica:
        if y.isalnum() != True:
            besedica = besedica.replace(y, "")
        else:
            koncno = besedica[::-1]
            break
    return koncno


def se_zacne_z(tvit, c):
    seznam = []
    koncni_seznam = []
    seznam.append(tvit.split())
    for x in seznam:
        for y in x:
            if c in y:
                koncni_seznam.append(izloci_besedo(y))
    return koncni_seznam

def zberi_se_zacne_z(tviti, c):
    a = 0
    seznam = []
    koncni_seznam = []
    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for a in y:
                if c in a:
                    koncni_seznam.append(izloci_besedo(a))
    return unikati(koncni_seznam)

def vse_afne(tviti):
    a = 0
    seznam = []
    koncni_seznam = []
    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for a in y:
                if "@" in a:
                    koncni_seznam.append(izloci_besedo(a))
    drugi = unikati(koncni_seznam)
    return drugi


def vsi_hashtagi(tviti):
    a = 0
    seznam = []
    koncni_seznam = []
    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for a in y:
                if "#" in a:
                    koncni_seznam.append(izloci_besedo(a))
    return unikati(koncni_seznam)

def vse_osebe(tviti):
    seznam = []
    drugi = []
    koncni = []
    zares_koncni = []
    seznam.append(vse_afne(tviti))
    seznam.append(vsi_avtorji(tviti))
    for a in seznam:
        for b in a:
            drugi.append(b)
    koncni = sorted(drugi)
    zares_koncni = (unikati(koncni))
    return zares_koncni

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

