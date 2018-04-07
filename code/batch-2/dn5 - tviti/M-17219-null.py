def unikati(s):
    sez = []
    for x in s:
        if x not in sez:
            sez.append(x)
    return sez

def avtor(tvit):
    spl = tvit.split(" ")
    ime = spl[0]

    return ime[:-1]

def vsi_avtorji(tviti):
    i = 0
    sez = []
    for x in tviti:
        novi = tviti[i].split(" ")
        ime1 = novi[0]
        ime2 = ime1[:-1]

        if ime2 not in sez:
            sez.append(ime2)
        i += 1
    return sez

def izloci_besedo(beseda):
    for x in beseda:
        if not x.isalnum():
            beseda = beseda.replace(x, "")
        else:
            break

    ime_rev = beseda[::-1]

    for x in ime_rev:
        if not x.isalnum():
            ime_rev = ime_rev.replace(x, "")
        else:
            break

    imeF = ime_rev[::-1]
    return imeF

def se_zacne_z(tvit, c):
    i = 0
    sez = []

    for y in tvit.split(" "):
        if y.startswith(c):
            koš = "!@#$=:?,."

            for smet in koš:
                y = y.replace(smet, "")
            if y not in sez:
                sez.append(y)
        i += 1
    return sez

def zberi_se_zacne_z(tviti, c):
    i = 0
    sez = []
    for x in tviti:
        for y in x.split(" "):
            if y.startswith(c):
                koš = "!@#$=:?,."

                for smet in koš:
                    y = y.replace(smet, "")
                if y not in sez:
                    sez.append(y)
            i += 1
    return sez

def vse_afne(tviti):
    i = 0
    sez = []
    for x in tviti:
        for y in x.split(" "):
            if y.startswith("@"):
                koš = "!@#$=:?,."

                for smet in koš:
                    y = y.replace(smet, "")
                if y not in sez:
                    sez.append(y)
            i += 1
    return sez

def vsi_hashtagi(tviti):
    i = 0
    sez = []
    for x in tviti:
        for y in x.split(" "):
            if y.startswith("#"):
                koš = "!@#$=:?,."

                for smet in koš:
                    y = y.replace(smet, "")
                if y not in sez:
                    sez.append(y)
            i += 1
    return sez

def vse_osebe(tviti):

    sez = []

    for x in vsi_avtorji(tviti):
        sez.append(x)

    for y in vse_afne(tviti):
        if y not in sez:
            sez.append(y)

    sez.sort()

    return sez

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

