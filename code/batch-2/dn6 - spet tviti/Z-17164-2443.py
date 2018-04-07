def unikati(s):
    nov = []
    for e in s:
        if e not in nov:
            nov.append(e)
    return nov
def avtor(tvit):
    s = tvit.split(':')
    return s[0]
def vsi_avtorji(tviti):
    avtorji = []
    for vrstica in tviti:
        avtorji.append(avtor(vrstica))
    return unikati(avtorji)
def nazaj(beseda):
    return beseda[::-1]
def izloci_besedo(beseda):
    while True:
        for znak in beseda:
            while znak.isalnum() == False:
                beseda = beseda[1:]
                break
            if znak.isalnum() == True:
                beseda = beseda[:]
                break
        for znak in nazaj(beseda):
            while znak.isalnum() == False:
                beseda = beseda[:-1]
                break
            if znak.isalnum() == True:
                beseda = beseda[:]
                break
        return beseda
def se_zacne_z(tvit, c):
    s = []
    for beseda in tvit.split():
        if beseda[0] == c:
            f = izloci_besedo(beseda)
            s.append(f)
    return s
def zberi_se_zacne_z(tviti, c):
    s = []
    sez = []
    for tvit in tviti:
        s.append(se_zacne_z(tvit, c))
    for podsez in s:
        for e in podsez:
            sez.append(e)
    return unikati(sez)
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')
def vse_osebe(tviti):
    s = vsi_avtorji(tviti) + vse_afne(tviti)
    return unikati(sorted(s))

def besedilo(tvit):
    s = tvit.split(":", 1)[1]
    return ''.join(s[1:])

def zadnji_tvit(tviti):
    avtorji = []
    besedila = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
        besedila.append(besedilo(tvit))
    slovar = dict(zip(avtorji,besedila))
    return slovar

def prvi_tvit(tviti):
    slovar = dict()
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

import collections
def prestej_tvite(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return collections.Counter(avtorji)

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        afne = se_zacne_z(tvit, '@')
        if avtor(tvit) in slovar:
            slovar[avtor(tvit)] += afne
        else:
            slovar[avtor(tvit)] = afne
    return slovar


def neomembe(ime, omembe):
    seznam = []
    for pisec in omembe:
        for omenjeni in omembe[pisec]:
            if omenjeni in omembe and omenjeni not in omembe[ime] and ime != omenjeni:
                seznam.append(omenjeni)
    return seznam


def se_poznata(ime1, ime2, omembe):
    for ime, omenjeni in omembe.items():
        if ime == ime1 or ime == ime2:
            for e in omenjeni:
                if e == ime1 or e == ime2:
                    return True
    return False


def hashtagi(tviti):
    slovar = {}
    for tvit in tviti:
        lojtre = se_zacne_z(tvit, '#')
        for lojtra in lojtre:
            #avtorji = avtor(tvit)
            if lojtra in slovar:
                slovar[lojtra] += [avtor(tvit)]
            else:
                slovar[lojtra] = [avtor(tvit)]
    for lojtra, pisci in slovar.items():
        povrsti = sorted(pisci)
        slovar[lojtra] = povrsti
    return slovar

import unittest

class TestObvezna(unittest.TestCase):
    maxDiff = 10000

    def test_1_besedilo(self):
        self.assertEqual(besedilo("sandra: Spet ta dež. #dougcajt"),
                         "Spet ta dež. #dougcajt")
        self.assertEqual(besedilo("ana: kdo so te: @berta, @cilka, @dani? #krneki"),
                         "kdo so te: @berta, @cilka, @dani? #krneki")

    def test_2_zadnji_tvit(self):
        self.assertDictEqual(
            zadnji_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"berta": "@sandra Delaj domačo za #programiranje1",
             "sandra": "@berta Ne maram #programiranje1 #krneki",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten",
             "cilka": "@benjamin @ana #split? po dvopičju, za začetek?"})

        self.assertDictEqual(
            zadnji_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "sandra: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "sandra: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten",
             "sandra": "@benjamin @ana #split? po dvopičju, za začetek?"})

        self.assertDictEqual(
            zadnji_tvit(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki"})

        self.assertEqual(zadnji_tvit([]), {})


    def test_3_prvi_tvit(self):
        self.assertDictEqual(
            prvi_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": "Spet ta dež. #dougcajt",
             "berta": "@sandra Delaj domačo za #programiranje1",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "cilka": "jst sm pa #luft",
             "benjamin": "pogrešam ano #zalosten"})

        self.assertDictEqual(
            prvi_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "sandra: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "sandra: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": "Spet ta dež. #dougcajt",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten"})

        self.assertDictEqual(
            prvi_tvit(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki"})

        self.assertEqual(prvi_tvit([]), {})

    def test_4_prestej_tvite(self):
        self.assertDictEqual(
            prestej_tvite([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": 2, "berta": 1, "ana": 1, "cilka": 2, "benjamin": 1})

        self.assertDictEqual(
            prestej_tvite([
                    "sandra: Spet ta dež. #dougcajt",
                    "sandra: @sandra Delaj domačo za #programiranje1",
                    "sandra: @berta Ne maram #programiranje1 #krneki",
                    "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                    "sandra: jst sm pa #luft",
                    "benjamin: pogrešam ano #zalosten",
                    "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": 5, "ana": 1, "benjamin": 1})

        self.assertDictEqual(
            prestej_tvite(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": 1})

        self.assertEqual(prestej_tvite([]), {})

    def test_5_omembe(self):
        self.assertDictEqual(
            omembe(["sandra: Spet ta dež. #dougcajt",
                    "berta: @sandra Delaj domačo za #programiranje1",
                    "sandra: @berta Ne maram #programiranje1 #krneki",
                    "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                    "cilka: jst sm pa #luft",
                    "benjamin: pogrešam ano #zalosten",
                    "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": ["berta", "benjamin", "ana"],
             "benjamin": [],
             "cilka": [],
             "berta": ["sandra"],
             "ana": ["berta", "cilka", "dani"]}
        )

    def test_6_neomembe(self):
        omembe = {"sandra": ["berta", "benjamin", "ana"],
                  "benjamin": [],
                  "cilka": [],
                  "berta": ["sandra"],
                  "ana": ["berta", "cilka", "dani", "benjamin", "sandra"]}

        self.assertEqual(neomembe("sandra", omembe), ["cilka"])
        self.assertEqual(neomembe("ana", omembe), [])
        self.assertEqual(set(neomembe("benjamin", omembe)), set(omembe) - {"benjamin"})

class TestDodatna(unittest.TestCase):
    def test_1_se_poznata(self):
        omembe = {"sandra": ["berta", "benjamin", "ana"],
                  "benjamin": [],
                  "cilka": [],
                  "berta": ["sandra"],
                  "ana": ["berta", "cilka", "dani"]}

        self.assertTrue(se_poznata("ana", "berta", omembe))
        self.assertTrue(se_poznata("berta", "ana", omembe))
        self.assertTrue(se_poznata("sandra", "benjamin", omembe))
        self.assertTrue(se_poznata("benjamin", "sandra", omembe))

        self.assertFalse(se_poznata("benjamin", "ana", omembe))
        self.assertFalse(se_poznata("ana", "benjamin", omembe))

        self.assertFalse(se_poznata("cilka", "dani", omembe))
        self.assertFalse(se_poznata("pavel", "peter", omembe))

    def test_2_hashtagi(self):
        self.assertDictEqual(
            hashtagi(["sandra: Spet ta dež. #dougcajt",
                      "berta: @sandra Delaj domačo za #programiranje1",
                      "sandra: @berta Ne maram #programiranje1 #krneki",
                      "ana: kdo so te @berta, @cilka, @dani? #krneki",
                      "cilka: jst sm pa #luft",
                      "benjamin: pogrešam ano #zalosten",
                      "ema: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {'dougcajt': ['sandra'],
             'krneki': ['ana', 'sandra'],
             'luft': ['cilka'],
             'programiranje1': ['berta', 'sandra'],
             'split': ['ema'],
             'zalosten': ['benjamin']})


if __name__ == "__main__":
    unittest.main()


