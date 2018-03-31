def unikati(s):
    nov = []
    for el in s:
        if el not in nov:
            nov += [el]
    return nov


def avtor(tvit):
    x = tvit.split(":")
    return x[0]


def vsi_avtorji(tviti):
    x = []
    for el in tviti:
        x += [avtor(el)]
    return unikati(x)


def izloci_besedo(beseda):
    i = 0
    while beseda[i].isalnum() == False:
        beseda = beseda[1:]
    i = len(beseda)-1
    while i >= 0 and beseda[i].isalnum() == False:
        beseda = beseda[:-1]
        i -= 1
    return beseda


def se_zacne_z(tvit, c):
    x = []
    y = tvit.split(" ")
    for el in y:
        if el[0] == c:
            x += [izloci_besedo(el)]
    return x


def zberi_se_zacne_z(tviti, c):
    x = []
    for el in tviti:
        temp = se_zacne_z(el, c)
        for e in temp:
            if e != []:
                x += [e]
    return unikati(x)


def vse_afne(tviti):
    x = []
    for el in tviti:
        t = el.split(" ")
        for e in t:
            if se_zacne_z(e, "@"):
                x += [izloci_besedo(e)]
    return unikati(x)


def vsi_hashtagi(tviti):
    x = []
    for el in tviti:
        t = el.split(" ")
        for e in t:
            if se_zacne_z(e, "#"):
                x += [izloci_besedo(e)]
    return unikati(x)


def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti)+vse_afne(tviti)))

def custva(tviti, hashtagi):
    x = []
    for el in tviti:
        t = el.split(" ")
        j = 1
        while j<len(t):
            if t[j][1:] in hashtagi:
                x.append(t[0][:-1])
            j += 1
    return sorted(unikati(x))


def se_poznata(tviti, oseba1, oseba2):
    if oseba1 in vsi_avtorji(tviti) and oseba2 in vsi_avtorji(tviti):
        for tvit in tviti:
            a = avtor(tvit)
            besede = tvit.split(" ")
            for beseda in besede:
                if izloci_besedo(beseda) == oseba2 and oseba1 == a:
                    return True
                if izloci_besedo(beseda) == oseba1 and oseba2 == a:
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

