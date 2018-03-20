import unittest

def unikati(s):

    seznam = []

    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam




def avtor(tvit):

    rez_tweet = ""

    avt = 0
    stevc = 0

    for x in tvit:
        stevc = tvit.find(":")
        while avt != stevc:
            rez_tweet+=tvit[avt]
            avt+=1
    return rez_tweet




def vsi_avtorji(tviti):

    a = ""

    prvi_seznam = []
    drugi_seznam = []

    for x in tviti:
        prvi_seznam.append(x)
        y = x.split(":")
        drugi_seznam.append(y[0])

    return unikati(drugi_seznam)




def izloci_besedo(beseda):

    xxx = ""
    koncno = ""

    for x in beseda:
        if x.isalnum() != True:
            beseda = beseda.replace(x, "")
        else:
            xxx = beseda[::-1]
            break

    for y in xxx:
        if y.isalnum() != True:
            xxx = xxx.replace(y, "")
        else:
            koncno = xxx[::-1]
            break

    return koncno





def se_zacne_z(tvit, c):

    seznam = []
    drugi_seznam = []

    seznam.append(tvit.split())

    for x in seznam:
        for y in x:
            if c in y:
                drugi_seznam.append(izloci_besedo(y))
    return drugi_seznam




def zberi_se_zacne_z(tviti, c):

    x = 0

    seznam = []
    koncni_seznam = []

    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for x in y:
                if c in x:
                    koncni_seznam.append(izloci_besedo(x))
    return unikati(koncni_seznam)





def vse_afne(tviti):

    ax = 0

    seznam = []
    drugi_seznam = []

    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for x in y:
                if "@" in x:
                    drugi_seznam.append(izloci_besedo(x))
    drugi = unikati(drugi_seznam)
    return drugi






def vsi_hashtagi(tviti):

    xx = 0

    seznam = []
    koncni_seznam = []

    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for xx in y:
                if "#" in xx:
                    koncni_seznam.append(izloci_besedo(xx))
    return unikati(koncni_seznam)





def vse_osebe(tviti):

    seznam = []
    drugi_seznam = []
    tretji_seznam = []
    cetrti_seznam = []

    seznam.append(vse_afne(tviti))
    seznam.append(vsi_avtorji(tviti))

    for a in seznam:
        for b in a:
            drugi_seznam.append(b)
    tretji_seznam = sorted(drugi_seznam)
    cetrti_seznam = (unikati(tretji_seznam))
    return cetrti_seznam








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

    '''
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

    '''
if __name__ == "__main__":
    unittest.main()

