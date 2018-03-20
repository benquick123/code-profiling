tviti = {"berta": "@sandra Delaj domačo za #programiranje1",
 "sandra": "@berta Ne maram #programiranje1 #krneki",
 "ana": "kdo so te: @berta, @cilka, @dani? #krneki"}

from collections import Counter
def unikati(s):
    str = []
    for i in s:
        if i not in str:
            str.append(i)
    return str


def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)


def izloci_besedo(beseda):

    zac = ""
    n = 0
    while n < len(beseda) - 1:
        if beseda[n].isalnum() == False:
            zac = zac + beseda[n]
        else:
            break
        n += 1

    m = len(beseda) - 1
    kon = ""
    while m > 0:
        if beseda[m].isalnum() == False:
            kon = kon + beseda[m]
        else:
            break
        m -= 1

    return beseda.replace(zac, "").replace(kon, "")


def se_zacne_z(tvit, c):
    besede = tvit.split()
    pravebesede = []

    for beseda in besede:
        if(beseda[0] == c):
            pravebesede.append(izloci_besedo(beseda))

    return pravebesede


def besedilo(tvit):
    return  tvit.split(": ", 1)[1]


def zadnji_tvit(tviti):
    zadnji_tviti = {}
    for tvit in tviti:
        avtor = tvit.split(": ")[0]
        besedilo_tvita = besedilo(tvit)
        zadnji_tviti[avtor] = besedilo_tvita
    return zadnji_tviti

def prvi_tvit(tviti):
    prvi_tviti = {}
    for tvit in tviti:
        avtor = tvit.split(": ")[0]
        besedilo_tvita = besedilo(tvit)
        if avtor not in prvi_tviti:
            prvi_tviti[avtor] = besedilo_tvita
    return prvi_tviti

def prestej_tvite(tviti):
    presteti_tviti = {}
    for tvit in tviti:
        avtor = tvit.split(": ")[0]
        presteti_tviti[avtor] = presteti_tviti.get(avtor, 0)+1

    return presteti_tviti

def omembe(tviti):
    omembe = {}
    for tvit in tviti:
        avtor = tvit.split(": ")[0]
        omemba = se_zacne_z(tvit, "@")
        if(omemba != []):
            if(avtor not in omembe):
                omembe[avtor] = omemba
            else:
                for tvit in omemba:
                    omembe[avtor].append(tvit)
        else:
            omembe[avtor] = []

    return omembe


def neomembe(ime, omembe):
    neomembe = omembe
    omenjene_osebe = []
    neomenjene_osebe = []

    for oseba in neomembe[ime]:
        omenjene_osebe.append(oseba)

    for oseba in omembe.keys():
        if(oseba == ime):
            continue
        if(oseba not in omenjene_osebe):
            neomenjene_osebe.append(oseba)

    return neomenjene_osebe

def se_poznata(ime1, ime2, omembe):
    omenjene_osebe = omembe

    if(ime1 in omenjene_osebe):
        for oseba in omenjene_osebe[ime1]:
            if(oseba == ime2):
                return True
        else:
            if(ime2 in omenjene_osebe):
                for oseba_2 in omenjene_osebe[ime2]:
                    if oseba_2 == ime1:
                        return True
    else:
        if(ime2 in omenjene_osebe):
            for oseba_2 in omenjene_osebe[ime2]:
                if(oseba_2 == ime1):
                    return True
    return False

def hashtagi(tviti):
    hashtagi = {}
    for tvit in tviti:
        avtor = avtor(tvit)
        hashtag_collection = se_zacne_z(tvit, "#")


        for single_hashtag in hashtag_collection:
            if (single_hashtag not in hashtagi):
                hashtagi[single_hashtag] = avtor.split()
            else:
                hashtagi[single_hashtag].append(avtor)
        for hash in hashtagi:
            x = hashtagi[hash]
            x = sorted(x)
            hashtagi[hash] = x
    return hashtagi






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


