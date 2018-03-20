def unikati(s):
    seznam=[]
    for neki in s:
        if neki not in seznam:
            seznam.append(neki)
    return seznam

def avtor(tvit):
    ime=tvit.split()
    imeNovo=ime[0].replace(":","")
    return imeNovo

def vsi_avtorji(tviti):
    seznam=[]
    for neki in tviti:
        ime=avtor(neki)
        if ime not in seznam:
            seznam.append(ime)
    return seznam

def izloci_besedo(beseda):
    beseda = list(beseda)
    while (ord(beseda[0]) < 48 or ord(beseda[0]) > 57) and (ord(beseda[0]) < 65 or ord(beseda[0]) > 90) and (ord(beseda[0]) < 97 or ord(beseda[0]) > 122):
        del (beseda[0])
    i = len(beseda) - 1
    while (ord(beseda[i]) < 48 or ord(beseda[i]) > 57) and (ord(beseda[i]) < 65 or ord(beseda[i]) > 90) and (ord(beseda[i]) < 97 or ord(beseda[i]) > 122):
        del (beseda[i])
        i = i - 1
    beseda = "".join(beseda)
    return beseda

def se_zacne_z(tvit, c):
    tvit=tvit.split()
    seznam=[]
    for neki in tvit:
        if neki[0] == c:
            novaBes=izloci_besedo(neki)
            seznam.append(novaBes)
    return seznam

def zberi_se_zacne_z(tviti,c):
    sez=[]
    for neki in tviti:
        neki=neki.split()
        for neki2 in neki:
            if neki2[0] == c:
                novaBes = izloci_besedo(neki2)
                sez.append(novaBes)
    return unikati(sez)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    novSeznam=[]
    novSeznam=vse_afne(tviti)+vsi_avtorji(tviti)
    novSeznam=unikati(novSeznam)
    novSeznam.sort()
    return novSeznam

def custva(tviti,hashtagi):
    seznam=[]
    for neki in tviti:
        neki = neki.split()
        for neki2 in hashtagi:
            if "#"+neki2 in neki:
                seznam.append(avtor(neki[0]))
    seznam=unikati(seznam)
    seznam.sort()
    return seznam

def se_poznata(tviti,oseba1,oseba2):
    for neki in tviti:
        if avtor(neki) == oseba1:
            if "@"+oseba2 in neki:
                return True
    for neki in tviti:
        if avtor(neki) == oseba2:
            if "@"+oseba1 in neki:
                return True
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

