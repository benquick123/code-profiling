def unikati(s):
    nov_seznam = []
    for x in s:
        if x not in nov_seznam:
            nov_seznam.append(x)
    return nov_seznam


def avtor(tvit):
    return tvit.split(":")[0]


def vsi_avtorji(tviti):
    seznam2 = []
    for kos in tviti:
        seznam2.append(avtor(kos))
    return unikati(seznam2)


def izloci_besedo(beseda):
    while not beseda[0].isalnum():
            beseda = beseda[1:]
    while not beseda[-1].isalnum():
           beseda = beseda[:-1]
    return beseda


def se_zacne_z(tvit, c):
    seznam4 = []
    for beseda in tvit.split():
        if beseda[0] == c:
            seznam4.append(izloci_besedo(beseda))
    return seznam4


def zberi_se_zacne_z(tviti, c):
    seznam3 =[]
    for x in tviti:
        seznam3 += x.split(" ")
    seznam4 = []
    for beseda in seznam3:
        if beseda[0] == c:
            if izloci_besedo(beseda) in seznam4:
                pass
            else:
                seznam4.append(izloci_besedo(beseda))
    return seznam4


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    seznam_oseb = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    seznam_oseb.sort()
    return seznam_oseb


def custva(tviti, hashtagi):
    seznam1 =[]
    seznam_avtorjev = []
    for x in tviti:
        seznam1 = x.split(" ")
        for beseda in seznam1:
            if beseda[0] == "#":
                if izloci_besedo(beseda) in hashtagi:
                     seznam_avtorjev.append(avtor(x))
    seznam_avtorjev = unikati(seznam_avtorjev)
    seznam_avtorjev.sort()
    return seznam_avtorjev


"""def se_poznata(tviti, oseba1, oseba2):
    seznam1 =[]
    velja = 0
    for x in tviti:
        seznam1 = x.split(" ")
        for beseda in seznam1:
            if beseda[0] == "@":
                if izloci_besedo(beseda) == oseba1 and oseba2 == avtor(x):
                     velja += 1
    seznam2 =[]
    for x in tviti:
        seznam2 = x.split(" ")
        for beseda in seznam2:
            if beseda[0] == "@":
                if izloci_besedo(beseda) == oseba2 and oseba1 == avtor(x):
                     velja += 1
    if velja:
        return True
    else:
        return False"""

#drugi teden

def besedilo(tvit):
    for i in range(len(tvit)):
        if tvit[i] == ":":
            return tvit[(i+2):]


def zadnji_tvit(tviti):
    slovar1 = {}
    for tvit in tviti:
        slovar1[avtor(tvit)] = besedilo(tvit)
    return slovar1


def prvi_tvit(tviti):
    slovar2 = {}
    for tvit in tviti:
        if avtor(tvit) in slovar2:
            pass
        else:
            slovar2[avtor(tvit)] = besedilo(tvit)
    return slovar2

from collections import defaultdict

def prestej_tvite(tviti):
    slovar3 = defaultdict(int)
    for tvit in tviti:
        slovar3[avtor(tvit)] += 1
    return slovar3


def omembe(tviti):
    slovar4 = defaultdict(list)
    for tvit in tviti:
        slovar4[avtor(tvit)] += (se_zacne_z(tvit, "@"))
    return slovar4


def neomembe(ime, omembe):
    seznam_neomenjenih = []
    seznam_omenjenih = omembe.get(ime, "")
    for x in omembe:
        if x not in seznam_omenjenih and x != ime:
            seznam_neomenjenih.append(x)
    return seznam_neomenjenih


def se_poznata(ime1, ime2, omembe):
    seznam_omenjenih = omembe.get(ime1, "")
    seznam_omenjenih2 = omembe.get(ime2, "")
    if ime2 in seznam_omenjenih or ime1 in seznam_omenjenih2:
        return True
    return False


def hashtagi(tviti):
    slovar5 = defaultdict(list)
    seznam = vsi_hashtagi(tviti)
    for hashtag in seznam:
        slovar5[hashtag] = custva(tviti, hashtag)
    return slovar5



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


