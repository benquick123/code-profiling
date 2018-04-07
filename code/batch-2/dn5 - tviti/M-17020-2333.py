
def unikati(s):
    xs = []
    for element in s:
        if element not in xs:
            xs.append(element)
    return xs


def avtor(tvit):
    niz = ""
    for crka in tvit:
        if crka != ":":
            niz += crka
        else:
            break
    return niz


def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in imena:
            imena.append(ime)
    return imena


def izloci_besedo(beseda):
    if beseda.isalnum() == False:
        for crka in beseda:
            if crka.isalnum() == False:
                beseda = beseda[1:]
            else:
                break
        for crka in beseda:
            indeks = beseda.index(crka) + 1
            if indeks < len(beseda):
                element = beseda[indeks]
            if (crka.isalnum() == False) and (element.isalnum() == False):
                beseda = beseda[:-1]
        return beseda
    else:
        return beseda


def se_zacne_z(tvit, c):
    s = []
    xs = []
    beseda = ""
    for crka in tvit:
        if crka != " ":
            beseda += crka
        else:
            xs.append(beseda)
            beseda = ""
    xs.append(beseda)
    for niz in xs:
        if niz.startswith(c):
            nova_beseda = izloci_besedo(niz)
            s.append(nova_beseda)
    return s


def zberi_se_zacne_z(tviti, c):
    s = []
    niz = 0
    for tvit in tviti:
        if c in tvit:
            seznam = se_zacne_z(tvit, c)
            for niz in seznam:
                if niz not in s:
                    s.append(niz)
    return s


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")



def vse_osebe(tviti):
    seznam = []
    s = vsi_avtorji(tviti)
    xs = vse_afne(tviti)
    for ime in xs + s:
        if ime not in seznam:
            seznam.append(ime)
    seznam.sort()
    return seznam


def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        a = avtor(tvit)
        b = se_zacne_z(tvit, "#")
        for element in b:
            for hashtag in hashtagi:
                if element == hashtag and a not in seznam:
                    seznam.append(a)
        seznam.sort()
    return seznam


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        a = avtor(tvit)
        b = se_zacne_z(tvit, "@")
        for element in b:
            if (a == oseba1 or a == oseba2) and (element == oseba1 or element == oseba2):
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

