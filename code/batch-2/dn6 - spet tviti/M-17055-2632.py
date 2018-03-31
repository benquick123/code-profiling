def unikati(s):

    a = []
    for i in s:
        if i in a:
            pass
        else:
            a.append (i)
    return a

def avtor(tvit):
    return tvit.split(":")[0]


"""
    b = tvit.split()
    for i in b:
        if i.find(":") > 0:
            i = i.replace(":","")
            return i
"""



def vsi_avtorji(tviti):
    a = []
    for i in tviti:
        b = avtor(i)
        a.append(b)
    c = unikati(a)
    return c

def izloci_besedo(beseda):
    #beseda = "!#$%\"=%/%()/Ben-jamin'"
    b = 0
    while beseda[b].isalnum() == False:
        a = beseda.replace(beseda[b],"")
        beseda = a

    besedilo = beseda[::-1]
    while besedilo[b].isalnum() == False:
        besedilo = besedilo.replace(besedilo[b],"")

    c = besedilo[::-1]
    return c

def se_zacne_z(tvit, c):
    a = []
    tvit = tvit.split()
    for i in tvit:
        for x in i:
            if x == c:
                i = i.replace(c, "")
                i = izloci_besedo(i)
                a.append(i)
    return a

def zberi_se_zacne_z(tviti, c):
    a = []

    for i in tviti:
        i = i.split()
        for x in i:
            if c in x:
                d = x.replace(c, "")
                d = izloci_besedo(d)
                if d in a:
                    pass
                else:
                    a.append(d)
    return a

def vse_afne(tviti):
    b = zberi_se_zacne_z(tviti,"@")
    return b

def vsi_hashtagi(tviti):
     a = zberi_se_zacne_z(tviti,"@" and "#")
     return a

def vse_osebe(tviti):
    a = []

    b = vsi_avtorji(tviti)
    if b not in a:
        a.extend(b)

    c = vse_afne(tviti)
    for i in c:
        if i in a:
            pass
        else:
            a.append(i)

    a.sort()
    print(a)
    return a

def custva(tviti, hashtagi):
    a = []
    for i in tviti:
        for e in hashtagi:
            if e in i:
                if i.find(e) > 0:
                    h = i.replace(":", "")
                    c = h.split()
                    if c[0] not in a:
                        a.append(c[0])
    a.sort()
    return a


#--------------------------------------------------------
def besedilo(tvit):
    a = 1
    for i in tvit:
        if i == ":":
            a = a + 1
            return tvit[a:]
        a += 1

def zadnji_tvit(tviti):
    f = {}
    for c in tviti:
        a = avtor(c)
        b = besedilo(c)
        f[a]= b
    return f

def prvi_tvit(tviti):
    f = {}
    for c in tviti:
        a = avtor(c)
        b = besedilo(c)
        if a not in f:
            f[a]= b
    return f

def prestej_tvite(tviti):
    a = {}
    for i in tviti:
        b = avtor(i)
        if b not in a:
            a[b] = 0
        a[b] += 1
    return a

def omembe(tviti):
    a = {}
    for i in tviti:
        if avtor(i) not in a:
            a[avtor(i)]= []
        a[avtor(i)].extend(se_zacne_z(i,"@"))
    return a

def neomembe(ime, omembe):
    b = []
    a = omembe[ime]

    for i in omembe:
        if i != ime:
            b.append(i)

    #return (x for x in b if x not in a)
    return [x for x in b if x not in a]

def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe:
        omembe[ime1] = []
    if ime2 not in omembe:
        omembe[ime2] = []
    a = omembe[ime1]
    b = omembe[ime2]
    if ime1 in b or ime2 in a:
        return True
    return False

def hashtagi(tviti):
    z = {}

    for tvit in tviti:
        a = avtor(tvit)
        h = se_zacne_z(tvit,"#")

        for has in h:
            if has not in z:
                z[has]= a.split()
            else:
                z[has].append(a)
        z[has]= sorted(z[has])

    return z



































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