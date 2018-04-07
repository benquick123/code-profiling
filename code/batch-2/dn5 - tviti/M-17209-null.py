def unikati(s):
    nov = []
    for x in s:
        if not x in nov:
            nov.append(x)
    return nov

def avtor(tvit):
    ime = ""
    for x in tvit:
        if x == ":":
            break
        ime += x
    return ime

def vsi_avtorji(tviti):
    seznam = []
    for x in tviti:
        ime = avtor(x)
        if not ime in seznam:
            seznam.append(ime)
    return seznam

def izloci_besedo(beseda):
    nova = ""
    i = 0
    while i < len(beseda) - 1:
        if beseda[i].isalnum():
            levi = i
            break
        i += 1
    #print(levi)
    j = len(beseda) - 1
    while j > 0:
        if beseda[j].isalnum():
            desni = j
            break
        j -= 1
    #print(desni)
    return beseda[levi : desni + 1]

#print(izloci_besedo("@ana"))

def se_zacne_z(tvit,c):
    besede = []
    for x in tvit.split(" "):
        if x[0] == c:
            besede.append(izloci_besedo(x))
    return besede
#print(se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#"))

def zberi_se_zacne_z(tviti,c):
    vse = []
    for tvit in tviti:
        rez = se_zacne_z(tvit,c)
        for x in rez:
            if not x in vse:
                vse.append(x)
    return vse

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    imena = []
    for x in tviti:
        for parce in x.split(" "):
            if ":" in parce or "@" in parce:
                beseda = izloci_besedo(parce)
                if not beseda in imena:
                    imena.append(beseda)
    return sorted(imena)

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        besede = tvit.split(" ")
        nov = []
        for parce in besede:
            beseda = izloci_besedo(parce)
            nov.append(beseda)
        for x in hashtagi:
            if x in nov:
                if not avtor(tvit) in avtorji:
                    avtorji.append(avtor(tvit))
    return sorted(avtorji)

def se_poznata(tviti,oseba1,oseba2):
    avtorji = vsi_avtorji(tviti)
    if oseba1 in avtorji and oseba2 in avtorji:
        for tvit in tviti:
            besede = []
            for x in tvit.split(" "):
                besede.append(izloci_besedo(x))
            if (besede[0] == oseba1 and oseba2 in besede
                and oseba1) or (besede[0] == oseba2 and oseba1 in besede):
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
