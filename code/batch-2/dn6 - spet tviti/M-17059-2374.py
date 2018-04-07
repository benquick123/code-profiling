import unittest

def avtor(tviti):
    a = tviti.split(":")
    return a[0]

def besedilo(tviti):
    a = tviti.split(" ")
    a.remove(a[0])
    return ' '.join(a)
#a = {}
def zadnji_tvit(tviti):
    a = {}
    for tvit in tviti:
        a[avtor(tvit)] = besedilo(tvit)
    return a

def prvi_tvit(tviti):
    a = {}
    for tvit in tviti:
        if avtor(tvit) not in a:
            a[avtor(tvit)] = besedilo(tvit)
    return a

def prestej_tvite(tviti):
    a = {}
    for tvit in tviti:
        if avtor(tvit) in a:
            a[avtor(tvit)] = a[avtor(tvit)]+1
        else:
            a[avtor(tvit)] = 1
    return a

def izloci_besedo(beseda):
    beseda = list(beseda)
    a = ""
    i = 0
    for znak in beseda:
        if 0 < ord(znak) < 48 or 57 < ord(znak) < 65 or 91 < ord(znak) < 97 or ord(znak) > 123:
            if ord(znak) != 45:
                beseda[i] = 0
        i += 1
    a = a.join(str(item) for item in beseda)

    return a.strip('0')

def se_zacne_z(tvit, c):
    tvit = tvit.split()
    a = []
    for beseda in tvit:
        if beseda[0] == c:
            a.append(izloci_besedo(beseda))
    return a

def omembe(tviti):
    a = {}
    b = []
    for tvit in tviti:
        b = se_zacne_z(tvit, '@')
        if avtor(tvit) in a:
            a[avtor(tvit)] += b
        else:
            a[avtor(tvit)] = b
    return a

def neomembe(ime, omembe):
        a = []
        slovar = {}
        for i in omembe:
            if i not in a:
                a.append(i)

        b = omembe[ime]
        c = []

        for i in a:
            if i not in b and i != ime:
                c.append(i)
        return c

def se_poznata(ime1, ime2, omembe):
    a = []
    b = []
    if ime1 in omembe:
        a = omembe[ime1]
    if ime2 in omembe:
        b = omembe[ime2]
    if ime2 in a or ime1 in b:
        return True
    else:
        return False

def izloci_besedo(beseda):
    beseda = list(beseda)
    a = ""
    i = 0
    for znak in beseda:
        if 0 < ord(znak) < 48 or 57 < ord(znak) < 65 or 91 < ord(znak) < 97 or ord(znak) > 123:
            if ord(znak) != 45:
                beseda[i] = 0
        i += 1
    a = a.join(str(item) for item in beseda)

    return a.strip('0')

def custva(tviti, hashtag):
    a = []
    for stavek in tviti:
        s = stavek.split()
        hastag = "#"+hashtag
        for i in s:
            i = izloci_besedo(i)
            i = "#"+i
            if hastag == i:
                a.append(avtor(stavek))
    return sorted(unikati(a))

def unikati(s):
    if s == []:
        return s
    h = [s[0]]
    for i in s:
        for t in h:
            if i != t and i not in h:
                h.append(i)
    return h

def hashtagi(tviti):
    a = []
    slovar = {}
    for tvit in tviti:
        for hastag in se_zacne_z(tvit, "#"):
            if hastag not in a:
                a.append(hastag)

    for hastag in a:
        gg = custva(tviti, hastag)
        slovar[hastag] = gg

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


