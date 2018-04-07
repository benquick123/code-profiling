def unikati(s):
    u = []
    for a in s:
        if a not in u:
            u.append(a)
    return u

def avtor(tvit):
    avtor = []
    for a in tvit:
        if a == ":" :
            break
        avtor.append(a)
    return ''.join(avtor)

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def izloci_besedo(beseda):
    besedaList = list(beseda)
    while not besedaList[0].isalnum():
        del besedaList[0]
    i = len(besedaList) - 1
    while not besedaList[i].isalnum():
        del besedaList[i]
        i -= 1
    return ''.join(besedaList)

def se_zacne_z(tvit, c):
    beseda = []
    tvitBesede = []
    i=0
    while i < len(tvit):
        if i == 0:
            if tvit[i] == c:
                j = i
                while tvit[j] != " ":
                    beseda.append(tvit[j])
                    j += 1
                tvitBesede.append(izloci_besedo(beseda))
                i = j-1
        elif tvit[i] == " ":
            if tvit[i+1] == c:
                j = i+1
                while j != len(tvit) and tvit[j] != " ":
                    beseda.append(tvit[j])
                    j += 1
                tvitBesede.append(izloci_besedo(beseda))
                i = j -1
        del beseda[:]
        i += 1
    return tvitBesede

def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede.extend(se_zacne_z(tvit, c))
    return unikati(besede)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    osebe = []
    osebe.extend(vsi_avtorji(tviti))
    osebe.extend(vse_afne(tviti))
    osebe.sort
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    besede = []
    avtorji = []
    for i, tvit in enumerate(tviti):
        besede = se_zacne_z(tvit,"#")
        for a in besede:
            if a in hashtagi:
                avtorji.append(avtor(tvit))
    avtorji = unikati(avtorji)
    avtorji.sort()
    return avtorji

def se_poznata(tviti, oseba1, oseba2):
    tvitList = []
    for i, tvit in enumerate(tviti):
        tvitList.append(tvit)
        if avtor(tvit) == oseba1:
            if oseba2 in vse_afne(tvitList):
                return True
        if avtor(tvit) == oseba2:
            if oseba1 in vse_afne(tvitList):
                return True
        del tvitList[:]
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

