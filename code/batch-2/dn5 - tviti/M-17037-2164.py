def unikati(s):
    unikatek = []
    for i in range(len(s)):
        if s[i] in unikatek:
            continue
        else:
            unikatek.append(s[i])
    return unikatek


def avtor(tvit):
    return tvit.split()[0].split(":")[0]


def vsi_avtorji(tviti):
    tviterji = []
    for t in range(len(tviti)):
        if avtor(tviti[t]) not in tviterji:
            tviterji.append(avtor(tviti[t]))
    return tviterji


def izloci_besedo(beseda):
    while beseda[0].isalnum() == False:
        beseda = beseda[1: len(beseda)]
    while beseda[-1].isalnum() == False:
        beseda = beseda[0: len(beseda) - 1]
    return beseda


def se_zacne_z(tvit, c):
    tvit = tvit.split()
    vse_resitve = []
    for beseda in range(len(tvit)):
        if tvit[beseda][0] == c:
            vse_resitve.append(izloci_besedo(tvit[beseda]))
        else:
            continue
    return vse_resitve


def zberi_se_zacne_z(tviti, c):
    at = []
    for t in range(len(tviti)):
        at.extend(se_zacne_z(tviti[t], c))
    return unikati(at)



def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")



def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    vsi_veckrat = []
    vsi_veckrat += vsi_avtorji(tviti) + vse_afne(tviti)
    vsi_veckrat = unikati(vsi_veckrat)
    vsi_veckrat.sort()
    return vsi_veckrat


""" -----------------------------------------------------------------------------------------------------------"""

def custva(tviti, hashtagi):
    custveni_ljudje = []
    for w in range(len(hashtagi)):
        for t in range(len(tviti)):
            for z in range(len(tviti[t].split())):
                if hashtagi[w] in tviti[t].split()[z]:
                    custveni_ljudje.append(avtor(tviti[t]))
    custveni_ljudje.sort()
    return unikati(custveni_ljudje)




def se_poznata(tviti, oseba1, oseba2):
    for t in range(len(tviti)):
        if oseba1 == avtor(tviti[t]) or oseba2 == avtor(tviti[t]):
            if (oseba1 in tviti[t] and "@"+oseba2 in tviti[t]) or ("@"+oseba1 in tviti[t] and oseba2 in tviti[t]):
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
        self.assertEqual(zberi_se_zacne_z(self.tviti, "#"),
                         ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_vse_afne(self):
        self.assertEqual(vse_afne(self.tviti), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])

    def test_vsi_hashtagi(self):
        self.assertEqual(vsi_hashtagi(self.tviti),
                         ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

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
