def unikati(s):
    s1=[]
    for i in s:
        if i not in s1:
            s1.append(i)
    return s1

def avtor(tvit):
    tvit=tvit.split()
    return tvit[0].strip(":")

def vsi_avtorji(tviti):
    avtorji=[]
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def izloci_besedo(beseda):
    while beseda[0].isalnum() == 0:
        beseda=beseda.strip(beseda[0])
    while beseda[-1].isalnum() == 0:
        beseda=beseda.strip(beseda[-1])
    return beseda

def se_zacne_z(tvit, c):
    list = []
    tvit = tvit.split()
    for beseda in tvit:
        if beseda[0] == str(c):
            list.append(izloci_besedo(beseda))
    return list

def zberi_se_zacne_z(tviti, c):
    s=[]
    for tvit in tviti:
         s+=(se_zacne_z(tvit,c))
    return unikati(s)

def vse_afne(tviti):
    s = []
    for tvit in tviti:
        s += (se_zacne_z(tvit, "@"))
    return unikati(s)

def vsi_hashtagi(tviti):
    s = []
    for tvit in tviti:
        s += (se_zacne_z(tvit, "#"))
    return unikati(s)

def vse_osebe(tviti):
    osebe=[]
    osebe += vsi_avtorji(tviti)
    osebe += vse_afne(tviti)
    return sorted(unikati(osebe))

def custva(tviti,hashtagi):
    custvene_osebe=[]
    s=[]
    for tvit in tviti:
        tvit=tvit.split()
        for beseda in tvit:
            for hashtag in hashtagi:
                if beseda == "#"+hashtag:
                    custvene_osebe.append(tvit[0])
    for custvena_oseba in custvene_osebe:
        s.append(izloci_besedo(custvena_oseba))
    return sorted(unikati(s))

def se_poznata(tviti,oseba1,oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            for beseda in se_zacne_z(tvit,"@"):
                if beseda == oseba2:
                    return True
        elif avtor(tvit) == oseba2:
            for beseda in se_zacne_z(tvit,"@"):
                if beseda == oseba1:
                    return True

import unittest

class TestTviti(unittest.TestCase):
    tviti = [
        "sandra: Spet ta deĹľ. #dougcajt",
        "berta: @sandra Delaj domaÄŤo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogreĹˇam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopiÄŤju, za zaÄŤetek?",
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
        self.assertEqual(avtor("janez: pred dvopiÄŤjem avtor, potem besedilo"), "janez")
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
        "sandra: Spet ta deĹľ. #dougcajt",
        "berta: @sandra Delaj domaÄŤo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogreĹˇam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopiÄŤju, za zaÄŤetek?",
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
