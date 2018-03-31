def unikati(s):
    novi_unikati = []
    for unikatni_unikati in s:
        if unikatni_unikati not in novi_unikati:
            novi_unikati.append(unikatni_unikati)
    return novi_unikati


def avtor(tvit):
    ime_avtorja = ''
    for crka1 in tvit:
        if crka1 != ':':
            ime_avtorja = ime_avtorja + crka1
        else:
            break
    return ime_avtorja


def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        if avtor(tvit) not in seznam_avtorjev:
            seznam_avtorjev.append(avtor(tvit))
    return seznam_avtorjev



def izloci_besedo(beseda):
    seznam_besed = ''
    for crka in beseda:
        if True == crka.isalnum() or crka == '-':
            seznam_besed = seznam_besed + crka
    return seznam_besed


def se_zacne_z(tvit, c):
    vrnjene_besede = []
    beseda = ''
    pisemo = 0
    for i in range(len(tvit)):
        if tvit[i].isalnum() == False:
            pisemo = 0
            if beseda != '':
                vrnjene_besede.append(beseda)
            beseda = ''
        if pisemo == 1:
            beseda = beseda + tvit[i]
        if tvit[i] == c:
            pisemo = 1
        if i == len(tvit) - 1 and pisemo == 1:
            pisemo = 0
            if beseda != '':
                vrnjene_besede.append(beseda)
            beseda = ''
    return vrnjene_besede


def zberi_se_zacne_z(tviti, c):
    vrnjeni_tviti = []
    for vsi_tviti in tviti:
        besede_v_enem_tvitu = se_zacne_z(vsi_tviti, c)
        for ena_beseda in besede_v_enem_tvitu:
            if ena_beseda not in vrnjeni_tviti:
                vrnjeni_tviti.append(ena_beseda)
    return vrnjeni_tviti


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')


def vse_osebe(tviti):
    alfa_seznam = []
    a = vsi_avtorji(tviti)
    b = zberi_se_zacne_z(tviti, '@')
    for avtorji in a:
        if avtorji not in alfa_seznam:
            alfa_seznam.append(avtorji)
    for avtorji in b:
        if avtorji not in alfa_seznam:
            alfa_seznam.append(avtorji)
    alfa_seznam.sort()

    return alfa_seznam















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

