def besedilo(tvit):
    besedilo = tvit.split(":", 1)[1]
    besedilo2 = besedilo.lstrip()
    return besedilo2

def zadnji_tvit(tviti):
    t = {}
    for tvit in tviti:
        avtor = tvit.split(":", 1)[0]
        besedilot = besedilo(tvit)
        t[avtor] = besedilot
    return t

def prvi_tvit(tviti):
    t = {}
    for tvit in tviti:
        avtor = tvit.split(":", 1)[0]
        besedilot = besedilo(tvit)
        if avtor not in t:
            t[avtor] = besedilot
    return t

def prestej_tvite(tviti):
    t = {}
    for tvit in tviti:
        avtor = tvit.split(":", 1)[0]
        if avtor not in t:
            t[avtor] = 0
        t[avtor] += 1
    return t






def unikati(s):  #1,3
    u = []
    for e in s:
        if e not in u:
            u.append(e)
    return u

def izloci_besedo(beseda): #1,1
    for znak in beseda:
        if znak.isalnum():
            break
        else:
            beseda = beseda.lstrip(znak[0])
    for znak in beseda[::-1]:
        if znak.isalnum():
            break
        else:
            beseda = beseda.rstrip(znak[-1])
    return beseda


def zberi_se_zacne_z(tvit, c): #1,2
    a = []
    vrni = []
    besede = tvit.split()
    for beseda in besede:
        if beseda[0] == c:
            beseda = izloci_besedo(beseda)
            a.append(beseda)
            vrni = unikati(a)
    return vrni

def vse_afne(tviti):  #1,4
    c = "@"
    b = zberi_se_zacne_z(tviti, c)
    return b

def omembe(tviti): #1
    t = {}
    for tvit in tviti:
        avtor = tvit.split(":", 1)[0]
        besedilo = tvit.split(":", 1)[1]
        besedilot = vse_afne(besedilo)
        if avtor not in t:
            t[avtor] = []
        t[avtor] += besedilot
    return t

def neomembe(name, mention): #2
    s = []
    for avtor in mention:
        if name != avtor:
            if avtor not in mention[name]:
                s.append(avtor)
    return s

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


