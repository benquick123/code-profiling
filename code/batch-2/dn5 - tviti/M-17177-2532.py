def unikati(s):
    seznam = []
    for x in s:
        if x in seznam:
            pass
        else:
            seznam.append(x)
    return seznam

def avtor(tvit):
    seznam = tvit.split()
    for x in seznam:
        if x.endswith(":"):
            x = x.replace(":", "")
            return x

def vsi_avtorji(tviti):
    avtorji = []
    for x in tviti:
        avtor1 = avtor(x)
        if avtor1 in avtorji:
            pass
        else:
            avtorji.append(avtor1)
    return avtorji

def izloci_besedo(beseda):          #popravljena = re.sub('[^0-9a-zA-Z\-]+', '', beseda)
    while beseda[0].isalnum() == False:
        sprednji = beseda.replace(beseda[0], "")
        beseda = sprednji
    zadnji = beseda[::-1]
    while zadnji[0].isalnum() == False:
        zadnji = zadnji.replace(zadnji[0], "")
    rezultat = zadnji[::-1]
    return rezultat


def se_zacne_z(tvit, c):
    sezn = []
    tvt = tvit.split()
    for x in tvt:
        if x.startswith(c):
            besede = izloci_besedo(x)
            sezn.append(besede)
    return sezn

def zberi_se_zacne_z(tviti, c):
    seznam2 = []
    for x in tviti:
        bg = se_zacne_z(x, c)
        seznam2.extend(bg)
    sez = unikati(seznam2)
    return sez

def vse_afne(tviti):
    g = zberi_se_zacne_z(tviti, "@")
    return g

def vsi_hashtagi(tviti):
    gg = zberi_se_zacne_z(tviti, "#")
    return gg

def vse_osebe(tviti):
    seznam = []
    x = vsi_avtorji(tviti)
    seznam.extend(x)
    xx = vse_afne(tviti)
    seznam.extend(xx)
    gg = unikati(seznam)
    gg.sort()
    return gg

def custva(tviti, hashtagi):
    pogoj = []
    for i in tviti:
        tagi = se_zacne_z(i, "#")
        for ii in hashtagi:
            for gg in tagi:
                if ii == gg:
                    c = avtor(i)
                    pogoj.append(c)
    pogoj.sort()
    return unikati(pogoj)

def se_poznata(tviti, oseba1, oseba2):
    afne = []
    bafne = []
    for i in tviti:
        if avtor(i) == oseba1:
            afne = se_zacne_z(i, "@")
        if avtor(i) == oseba2:
            bafne = se_zacne_z(i, "@")
    if oseba1 in bafne:
        return True
    elif oseba2 in afne:
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

