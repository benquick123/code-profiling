
import unittest

def besedilo(tvit):
    stev = 0
    for item in tvit:
        stev += 1
        if item == ":":
            break
    return tvit[stev+1:]


def zadnji_tvit(tviti):
    slovar = {}
    niz1 = []
    niz2 = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i not in niz1 and i.endswith(":"):
                niz1.append(i)
                break
    for item in tviti:
        stev = 0
        for i in item:
            stev += 1
            if i == ":":
                niz2.append(item[stev+1:])
                break
    for item in tviti:
        for j in niz2:
            if j in item:
                value = j
                break
        nov = item.split(" ")
        for x in nov:
            for i in niz1:
                if x == i:
                    key = i[:-1]
                    slovar[key] = value
                    break
    return slovar


def prvi_tvit(tviti):
    slovar = {}
    niz1 = []
    niz2 = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i not in niz1 and i.endswith(":"):
                niz1.append(i)
                break
    for item in tviti:
        stev = 0
        for i in item:
            stev += 1
            if i == ":":
                niz2.append(item[stev+1:])
                break
    for item in tviti:
        for j in niz2:
            if j in item:
                value = j
                break
        nov = item.split(" ")
        for x in nov:
            for i in niz1:
                if x == i:
                    key = i[:-1]
                    if key not in slovar:
                        slovar[key] = value
                    break
    return slovar


def prestej_tvite(tviti):
    slovar = {}
    niz1 = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i.endswith(":"):
                niz1.append(i[:-1])
                break
    for i in niz1:
        slovar[i] = slovar.get(i, 0) + 1
    return slovar


def omembe(tviti):
    slovar = {}
    niz1 = []
    niz2 = []
    os = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i not in niz1 and i.endswith(":"):
                niz1.append(i)
                break
    for item in tviti:
        stev = 0
        for i in item:
            stev += 1
            if i == ":":
                niz2.append(item[stev+1:])
                break
    for item in tviti:
        nov = item.split(" ")
        for x in nov:
            if x.startswith("@"):
                os.append(x)
    osebe = []
    for item in tviti:
        for j in niz2:
            if j in item:
                for o in os:
                    if o in item:
                        for t in o:
                            if not t.isalnum():
                                o = o.replace(t, "")
                        if o not in osebe:
                            osebe.append(o)
        nov = item.split(" ")
        for x in nov:
            for i in niz1:
                if x == i:
                    key = i[:-1]
                    slovar[key] = slovar.get(key, []) + osebe
                    osebe = []
                    break
    return slovar


def neomembe(ime, omembe):
    kljuci = []
    kljuci = list(omembe.keys())
    imena = []
    imena = omembe[ime]
    sub = list(set(kljuci) - set(imena))
    sub.remove(ime)
    return sub


def se_poznata(ime1, ime2, omembe):
    imena1 = []
    imena2 = []
    try:
        imena1 = omembe[ime1]
        imena2 = omembe[ime2]
    except:
        return False
    for i in imena1:
        if i == ime2:
            return True
    for j in imena2:
        if j == ime1:
            return True
    return False


def hashtagi(tviti):
    slovar = {}
    niz = []
    n = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i[1:] not in niz and i.startswith("#"):
                niz.append(i[1:])
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i[:-1] not in n and i.endswith(":"):
                n.append(i[:-1])
    for item in tviti:
        for i in n:
            if i + ":" in item:
                for j in niz:
                    if "#" + j in item:
                        for x in j:
                            if not x.isalnum():
                                j = j.replace(x, "")
                        slovar[j] = sorted(slovar.get(j, []) + i.split(" "))
    return slovar


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


