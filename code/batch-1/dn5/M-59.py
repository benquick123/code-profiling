import unittest

def unikati(s):
    if len(s) == 0:
        return s
    else:
        e = []
        e.append(s[0])
        k = 0
        for se in s:
            for ee in e:
                if(ee == se):
                    k=0
                    break
                else:
                    k=1
            if k:
                e.append(se)
        return e

def avtor(tvit):
    s = ""
    for t in tvit:
        if t == ":":
            break
        else:
            s = s + t
    return s

def vsi_avtorji(tviti):
    avtorji = []
    k = 1
    for tvit in tviti:
        a = avtor(tvit)
        avtorji.append(a)
        avtorji = unikati(avtorji)
    return avtorji

def izloci_besedo(beseda):
    mesta = []
    for i in range(0, len(beseda)):
        if beseda[i].isalnum():
            mesta.append(i)
    return beseda[mesta[0]:mesta[len(mesta)-1]+1]

def se_zacne_z(tvit, c):
    beseda = ""
    b = []
    k = 0
    for i in range(0,len(tvit)-1):
        if tvit[i] == c:
            k = 1
        if k:
            if tvit[i] == " ":
                k = 0
                beseda = izloci_besedo(beseda)
                b.append(beseda)
                beseda = ""
            beseda += tvit[i]

            if i + 2 == len(tvit):
                beseda += tvit[i + 1]
                beseda = izloci_besedo(beseda)
                b.append(beseda)
    return b

def zberi_se_zacne_z(tviti, c):
    b = []
    a = []
    for i in range(0, len(tviti)):
        if se_zacne_z(tviti[i],c):
            b.append(se_zacne_z(tviti[i],c))
    for bes in b:
        for besede in bes:
            a.append(besede)
    a = unikati(a)
    return a

def vse_afne(tviti):
    s = zberi_se_zacne_z(tviti, "@")
    return s

def vsi_hashtagi(tviti):
    s = zberi_se_zacne_z(tviti, "#")
    return s

def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti) + vse_afne(tviti)
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        h = se_zacne_z(tvit, "#")
        for hash in hashtagi:
            for lojt in h:
                if hash == lojt:
                    avtorji.append(avtor(tvit))
    avtorji = unikati(avtorji)
    avtorji.sort()
    return avtorji

def se_poznata(tviti, oseba1, oseba2):
    poznata = False
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            os = se_zacne_z(tvit, "@")
            for osebe in os:
                if oseba2 == osebe:
                    poznata = True

        if avtor(tvit) == oseba2:
            os = se_zacne_z(tvit, "@")
            for osebe in os:
                if oseba1 == osebe:
                    poznata = True
    return poznata


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

