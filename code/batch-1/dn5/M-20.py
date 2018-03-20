#### OBVEZNI DEL ####

def unikati(s):
    seznam = []

    for x in s:
        if x not in seznam:
            seznam += [x]

    return seznam

import re
def avtor(tvit):

    beseda = []
    ime = []

    beseda = tvit.split()

    ime = re.sub(r'\W+', '', beseda[0])

    return ime

def vsi_avtorji(tviti):

    avtorji = []

    for x in tviti:
        avtorji += [avtor(x)]

    avtorji = unikati(avtorji)

    return avtorji

from string import punctuation
def izloci_besedo(beseda):

    beseda = beseda.lstrip(punctuation)
    beseda = beseda.rstrip(punctuation)

    return beseda

def se_zacne_z(tvit, c):
    besede = []
    kljucne_besede = []

    besede = tvit.split()

    for x in besede:
        if c in x:
            kljucne_besede += [izloci_besedo(x)]

    return kljucne_besede

def zberi_se_zacne_z(tviti, c):

    kljucne_besede = []

    for tvit in tviti:
        kljucne_besede += se_zacne_z(tvit, c)

    kljucne_besede = unikati(kljucne_besede)

    return kljucne_besede

def vse_afne(tviti):

    kljucne_besede = []
    c = '@'

    kljucne_besede = zberi_se_zacne_z(tviti, c)

    return kljucne_besede

def vsi_hashtagi(tviti):
    kljucne_besede = []
    c = '#'

    kljucne_besede = zberi_se_zacne_z(tviti, c)

    return kljucne_besede

def vse_osebe(tviti):

    osebe = []

    osebe = vsi_avtorji(tviti)
    osebe += vse_afne(tviti)
    osebe = unikati(osebe)
    osebe.sort(key=str.lower)

    return osebe

#### DODATNI DEL ####

def custva(tviti, hashtagi):

    besede = []
    puste_besede = []
    avtorji = []

    for tvit in tviti:
        besede = tvit.split()
        for x in besede:
            puste_besede = [izloci_besedo(x)]
            for y in hashtagi:
                if y in puste_besede:
                    avtorji += [avtor(tvit)]

    avtorji = unikati(avtorji)
    avtorji.sort(key=str.lower)

    return avtorji

def se_poznata(tviti, oseba1, oseba2):

    besede = []

    for tvit in tviti:
        besede = tvit.split()

        if oseba1 == avtor(tvit):
            for x in besede:
                if izloci_besedo(x) == oseba2 and '@' in x:
                    return True
            else:
                return False
















#####################################
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

