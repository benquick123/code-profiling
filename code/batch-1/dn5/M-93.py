import unittest

def unikati(s):
    a=[]
    for x in s:
        if x not in a:
            a.append(x)
    return a

def avtor(tvit):
    tvit=tvit.split(":")
    return tvit[0]

def vsi_avtorji(tviti):
    imena=[]
    for a in tviti:
        a=a.split(":")
        if a[0] not in imena:
            imena.append(a[0])
    return imena

def izloci_besedo(beseda):
    while beseda[0].isalnum()==False:
        beseda=beseda[1:len(beseda)]
    while beseda[-1].isalnum()==False:
        beseda=beseda[:-1]
    return beseda

def se_zacne_z(tvit, c):
    s=[]
    for a in tvit.split():
        if a[0]==c:
            a=izloci_besedo(a)
            s.append(a)
    return s

def zberi_se_zacne_z(tviti, c):
    s=[]
    for tvit in tviti:
        for a in tvit.split():
            if a[0]==c:
                tvit1=izloci_besedo(a)
                if tvit1 not in s:
                    s.append(tvit1)
    return s

def vse_afne(tviti):
    s=[]
    for tvit in tviti:
        for a in tvit.split():
            if a[0]=="@":
                a=izloci_besedo(a)
                if a not in s:
                    s.append(a)
    return s

def vsi_hashtagi(tviti):
    s=[]
    for tvit in tviti:
        for a in tvit.split():
            if a[0]=="#":
                a=izloci_besedo(a)
                if a not in s:
                    s.append(a)
    return s

def vse_osebe(tviti):
    osebe=[]
    for tvit in tviti:
        osebe.append(avtor(tvit))
    osebe+=vse_afne(tviti)
    osebe=unikati(osebe)
    osebe=sorted(osebe)
    return osebe

def custva(tviti, hashtagi):
    s=[]
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                if avtor(tvit) not in s:
                    s.append(avtor(tvit))
    s=sorted(s)
    return s

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if oseba1==avtor(tvit):
            s = []
            for a in tvit.split():
                if a[0] == "@":
                    a = izloci_besedo(a)
                    s.append(a)
                if oseba2 in s:
                    return True
        if oseba2==avtor(tvit):
            s = []
            for a in tvit.split():
                if a[0] == "@":
                    a = izloci_besedo(a)
                    s.append(a)
                if oseba1 in s:
                    return True


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

