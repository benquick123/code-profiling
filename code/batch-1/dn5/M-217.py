# -*- coding: utf-8 -*-
import unittest


def unikati(li):
    unikati = []
    for item in li:
        if (item not in unikati):
            unikati.append(item)
    return unikati


def avtor(tvit):
    splitted = tvit.split(":")
    avtor = splitted[0]
    return avtor


def vsi_avtorji(tviti):
    vsi = []
    for tvit in tviti:
        vsi.append(avtor(tvit))

    vsi_uni = unikati(vsi)
    return vsi_uni


def izloci_besedo(beseda):
    bes = list(beseda)
    # od spredi
    for letter in bes:
        if (letter.isalnum()):
            break
        else:
            bes = list(filter(lambda a: a != letter, bes))

    # od zadi
    for letter in bes[::-1]:
        if (letter.isalnum()):
            break
        else:
            bes = list(filter(lambda a: a != letter, bes))
    out = "".join(bes)
    return out


def se_zacne_z(tvit, x):
    res = []
    rez = []
    splitted = tvit.split(" ")
    for beseda in splitted:
        bes = list(beseda)
        for letter in bes:
            if (letter == x):
                res.append("".join(beseda))
    res_uni = unikati(res)
    for word in res_uni:
        rez.append(izloci_besedo(word))
    return rez


def zberi_se_zacne_z(tviti, x):
    vsi = []
    for tvit in tviti:
        vsi = vsi + se_zacne_z(tvit, x)

    vsi = unikati(vsi)
    return vsi


def vse_afne(tviti):
    denom = "@"
    return (zberi_se_zacne_z(tviti, denom))


def vsi_hashtagi(tviti):
    denom = "#"
    return (zberi_se_zacne_z(tviti, denom))


def vse_osebe(tviti):
    out = []
    out = out + vsi_avtorji(tviti) + zberi_se_zacne_z(tviti, "@")
    out = unikati(out)
    out = sorted(out)
    return out


def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        avtort = avtor(tvit)
        tags = se_zacne_z(tvit, "#")
        for tag in hashtagi:
            if (tag in tags):
                avtorji.append(avtort)

    avtorji = unikati(avtorji)
    avtorji = sorted(avtorji)
    return avtorji


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        avtort = avtor(tvit)
        if (avtort == oseba1):
            omembe = se_zacne_z(tvit, "@")
            if (oseba2 in omembe):
                return True
            else:
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

