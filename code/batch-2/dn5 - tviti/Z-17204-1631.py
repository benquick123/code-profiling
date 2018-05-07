def unikati(s):
    nov = []
    for x in s:
        if x not in nov:
            nov.append(x)
    return nov

def avtor(tvit):
    for beseda in tvit.split():
        if ":" in beseda:
            return beseda[:-1]

def vsi_avtorji(tviti):
    sez = []
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in sez:
            sez.append(ime)
    return sez

def izloci_besedo(beseda):
    spredaj = False
    zadaj = False
    while spredaj == False:
        if not beseda[0].isalnum():
            beseda = beseda[1:]
        else:
            spredaj = True
            break
    while zadaj == False:
        if not beseda[-1].isalnum():
            beseda = beseda[:-1]
        else:
            zadaj = True
            break
    return beseda

def se_zacne_z(tvit, c):
    sez = []
    for beseda in tvit.split():
        if beseda.startswith(c):
            beseda = izloci_besedo(beseda)
            sez.append(beseda)
    return sez

def zberi_se_zacne_z(tviti, c):
    sez = []
    vse = " ".join(tviti)
    sez += se_zacne_z(vse,c)
    return unikati(sez)

def vse_afne(tviti):
    afne = zberi_se_zacne_z(tviti, "@")
    return afne

def vsi_hashtagi(tviti):
    hash = zberi_se_zacne_z(tviti, "#")
    return hash

#Vrne po abecedi urejen seznam vseh oseb, ki nastopajo v tvitih - bodisi kot avtorji, ali omenjene v tvitih. Vsaka oseba naj se pojavi le enkrat.
def vse_osebe(tviti):
    sez = []
    sez += vsi_avtorji(tviti)
    sez += vse_afne(tviti)
    sez = unikati(sez)
    return sorted(sez)

def custva(tviti, hashtagi):
    sez = []
    for tvit in tviti:
        for hash in hashtagi:
            if hash in tvit:
                sez.append(avtor(tvit))
    return sorted(unikati(sez))

def se_poznata(tviti, oseba1, oseba2):
    poznanstvo = False
    tviti1 = []
    tviti2 = []
    for x in tviti:
        if oseba1 == avtor(x):
            tviti1.append(x)
            if oseba2  in vse_afne(tviti1):
                poznanstvo = True
    for y in tviti:
        if oseba2 == avtor(y):
            tviti2.append(y)
            if oseba1 in vse_afne(tviti2):
                poznanstvo = True
    return poznanstvo




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

