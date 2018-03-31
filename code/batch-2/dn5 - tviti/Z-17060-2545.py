random_tviti = ["sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


# 1
def unikati(s):
    lista_unikatov = []
    for vrednost in s:
        if not vrednost in lista_unikatov:
            lista_unikatov.append(vrednost)
    return lista_unikatov;


# 2
def avtor(tvit):
    razdeli_tvit = tvit.split(':')
    return razdeli_tvit[0];


print
avtor("ana: kdo so te @berta, @cilka, @dani? #krneki")


# 3
def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        razdeli_tvit = tvit.split(':')
        avtor = razdeli_tvit[0]
        if not avtor in avtorji:
            avtorji.append(avtor)
    return avtorji;


print
vsi_avtorji(random_tviti)


# 4
def izloci_besedo(beseda):
    chrke = []
    ii = 0
    for chrka in beseda:
        if chrka.isalnum():
            chrke.append(ii)
        ii += 1
    beseda = beseda[min(chrke):max(chrke)+1] # bil napačen pogoj
    return beseda


# 5
def se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede = ""
        zapisuj = False
        for chrka in tvit:
            if chrka == c:
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
        return besede;


# 6
def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        for chrka in tvit:
            if chrka == c:
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
    return besede;


print
zberi_se_zacne_z(random_tviti, "@")


# 7
def vse_afne(tviti):
    besede = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        for chrka in tvit:
            if chrka == "@":
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
    return besede;


# 8
def vsi_hashtagi(tviti):
    besede = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        for chrka in tvit:
            if chrka == "#":
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
    return besede;


print
vsi_hashtagi(random_tviti)


# 9
def vse_osebe(tviti):
    besede = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        avtor = False
        for chrka in tvit:
            if not avtor:
                avtor = True
                zapisuj = True
            if chrka == "@":
                zapisuj = True
                continue
            elif not chrka.isalnum() and beseda:
                if not beseda in besede:
                    besede.append(beseda)
                beseda = ""
                zapisuj = False
            if zapisuj:
                beseda += chrka
        if beseda and not beseda in besede:
            besede.append(beseda)
    besede.sort()
    return besede;


print
vse_osebe(random_tviti)


# 1*
def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        razdeli_tvit = tvit.split(':')
        avtor = razdeli_tvit[0]
        for chrka in tvit:
            if chrka == "#":
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if beseda in hashtagi and avtor not in avtorji:
                    avtorji.append(avtor)
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and beseda in hashtagi and avtor not in avtorji:
            avtorji.append(avtor)
        avtorji.sort()
    return avtorji;


print
custva(random_tviti, ["dougcajt", "krneki"])


# 2*
def se_poznata(tviti, oseba1, oseba2):
    osebi = [oseba1, oseba2]
    znanca = False
    for tvit in tviti:
        beseda = ""
        zapisuj = False
        razdeli_tvit = tvit.split(':')
        avtor = razdeli_tvit[0]
        for chrka in tvit:
            if chrka == "@":
                zapisuj = True
            elif not chrka.isalnum() and beseda:
                if not beseda == avtor and beseda in osebi and avtor in osebi:
                    znanca = True
                    return znanca
                beseda = ""
                zapisuj = False
            elif zapisuj:
                beseda += chrka
        if beseda and not beseda == avtor and beseda in osebi and avtor in osebi:
            znanca = True
    return znanca;


print
se_poznata(random_tviti, "benjamin", "cilka")
print
se_poznata(random_tviti, "berta", "sandra")

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

