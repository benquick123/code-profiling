# UNIKATI -dela-
def unikati(s):
    sez = []
    for e in s:
        if e not in sez:
            sez.append(e)
    return sez

# AVTOR -dela-
def avtor(tvit):
    at = tvit.split()[0]
    ime = ""
    for l in at:
        if l.isalpha():
            ime += l
    return ime

# VSI AVTORJI -dela-
def vsi_avtorji(tviti):
    sez = []
    for a in tviti:
        tr_avtor = avtor(a)
        if tr_avtor not in sez:
            sez.append(tr_avtor)
    return sez

# IZLOCI BESEDO -dela-
def izloci_besedo(beseda):
    while len(beseda) > 0 and not beseda[0].isalnum():
        beseda = beseda[1:]
    while len(beseda) > 0 and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

# SE ZACNE -dela-
def se_zacne_z(tvit, c):
    sez = []
    for e in tvit.split():
        if e.startswith(c):
            sez.append(izloci_besedo(e))
    return sez

# ZBERI SE ZACNE Z -dela-
def zberi_se_zacne_z(tviti, c):
    sez = []
    new_sez = []
    for e in tviti:
        new_sez.append(se_zacne_z(e, c))
    for e in new_sez:
        for i in e:
            if i != None and i not in sez:
                sez.append(i)
    return sez

# VSE AFNE -dela-
def vse_afne(tviti):
    c = "@"
    seznam = zberi_se_zacne_z(tviti, c)
    return seznam

# VSI HASHTAGI -dela-
def vsi_hashtagi(tviti):
    c = "#"
    seznam = zberi_se_zacne_z(tviti, c)
    return seznam


# VSE OSEBE -dela-
def vse_osebe(tviti):
    sez_oseb = []
    sez1 = vsi_avtorji(tviti)
    sez2 = zberi_se_zacne_z(tviti, "@")
    for e in sez1:
        if e not in sez_oseb:
            sez_oseb.append(e)
    for i in sez2:
        if i not in sez_oseb:
            sez_oseb.append(i)
    sez_oseb = sorted(sez_oseb)
    return sez_oseb





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

