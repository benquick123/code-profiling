# Obvezni del 1:
def unikati(s):
    nov_unikati = []
    for stevilka in s:
        if stevilka not in nov_unikati:
            nov_unikati.append(stevilka)
    return nov_unikati

# Obvezni del 2:
def avtor(tvit):
    ime = tvit.split(":")
    return ime[0]

# Obvezni del 3:
def vsi_avtorji(tviti):
    avtorji = []
    for ime in tviti:
        avtorji.append(avtor(ime))
    unikat_avtorji = unikati(avtorji)
    return unikat_avtorji

# Obvezni del 4:
def izloci_besedo(beseda):
    if beseda.isalnum():
        return beseda
    else:
        while beseda[0].isalnum() == False:
            beseda = beseda[1:]
        while beseda[-1].isalnum() == False:
            beseda = beseda[:-1]
    return beseda

# Obvezni del 5:
def se_zacne_z(tvit, c):
    besede = []
    tvit = tvit.split()
    for beseda in tvit:
        if beseda[0] == c:
            beseda = izloci_besedo(beseda)
            besede.append(beseda)
    return besede

# Obvezni del 6:
def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede.extend(se_zacne_z(tvit, c))
        unikat_besede = unikati(besede)
    return unikat_besede

# Obvezni del 7:
def vse_afne(tviti):
    return(zberi_se_zacne_z(tviti, "@"))

# Obvezni del 8:
def vsi_hashtagi(tviti):
    return(zberi_se_zacne_z(tviti, "#"))

# Obvezni del 9:
def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti)
    osebe.extend(vse_afne(tviti))
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

# Dodatni del 1:
def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        for a in hashtagi:
            if "#"+a in tvit:
                avtorji.append(avtor(tvit))
            avtorji = unikati(avtorji)
            avtorji.sort()
    return avtorji

# Dodatni del 2:
def se_poznata(tviti, oseba1, oseba2):
    i = 0
    for tvit in tviti:
        if oseba1+":" in tvit and "@"+oseba2 in tvit:
            i += 1
    if i >= 1:
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