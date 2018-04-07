import unittest
import string


def unikati(s):
    stevila = []
    for i in s:
        if i not in stevila:
            stevila.append(i)
    return stevila


def avtor(tvit):
    crke = ""
    for i in tvit:
        if i == ":":
            break
        else:
            crke += i
    return crke


def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        func = avtor(tvit)
        if func not in avtorji:
            avtorji.append(func)
    return avtorji


def izloci_besedo(beseda):
    i = 0
    s = 0
    for crka in beseda:
        if crka.isalnum():
            break
        i += 1
    for crka in beseda[::-1]:
        if crka.isalnum():
            break
        s += 1
    return beseda[i:len(beseda)-s]


def se_zacne_z(tvit, c):
    tvit = tvit.split()
    nov_sez = []
    for beseda in tvit:
        if beseda[0] == c:
            nov_sez.append(izloci_besedo(beseda))
    return nov_sez


def zberi_se_zacne_z(tviti, c):
    novi_sez = []
    for tvit in tviti:
        func = se_zacne_z(tvit, c)
        for i in func:
            if i not in novi_sez:
                novi_sez.append(i)
    return novi_sez


def vse_afne(tviti):
    sez = []
    for tvit in tviti:
        func = se_zacne_z(tvit, "@")
        for element in func:
            if element not in sez:
                sez.append(element)
    return sez


def vsi_hashtagi(tviti):
    sez = []
    for tvit in tviti:
        func = se_zacne_z(tvit, "#")
        for element in func:
            if element not in sez:
                sez.append(element)
    return sez


def vse_osebe(tviti):
    nov_sez = []
    for tvit in tviti:
        func1 = avtor(tvit)
        if func1 not in nov_sez:
            nov_sez.append(func1)
    func2 = vse_afne(tviti)
    for element in func2:
        if element not in nov_sez:
            nov_sez.append(element)
    return sorted(nov_sez)
    # return sorted(sez_oseb)


def custva(tviti, hashtagi):
    sez_avtorjev = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if (hashtag in tvit)and avtor(tvit) not in sez_avtorjev:
                sez_avtorjev.append(avtor(tvit))
    return sorted(sez_avtorjev)


def se_poznata(tviti, oseba1, oseba2):
    """ to bi delal..če bi mela oseba lahko samo en tvit :D """
    # tvit_dict = {avtor(tvit): tvit for tvit in tviti}
    # try:
    #     if "@" + oseba2 in tvit_dict[oseba1]:
    #         return True
    #     elif "@" + oseba1 in tvit_dict[oseba2]:
    #         return True
    # except KeyError:
    #     return False
    # return False
    for tvit in tviti:
        if tvit.startswith(oseba1):
            if oseba2 in se_zacne_z(tvit, "@"):
                return True
        if tvit.startswith(oseba2):
            if oseba1 in se_zacne_z(tvit, "@"):
                return True
    return False


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


