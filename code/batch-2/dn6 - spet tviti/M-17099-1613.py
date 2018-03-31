import unittest


def unikati(s):
    if len(s) == 0:
        return s
    else:
        e = []
        e.append(s[0])
        k = 0
        for se in s:
            for ee in e:
                if(ee == se):
                    k=0
                    break
                else:
                    k=1
            if k:
                e.append(se)
        return e

def avtor(tvit):
    s = ""
    for t in tvit:
        if t == ":":
            break
        else:
            s = s + t
    return s

def vsi_avtorji(tviti):
    avtorji = []
    k = 1
    for tvit in tviti:
        a = avtor(tvit)
        avtorji.append(a)
        avtorji = unikati(avtorji)
    return avtorji

def izloci_besedo(beseda):
    mesta = []
    for i in range(0, len(beseda)):
        if beseda[i].isalnum():
            mesta.append(i)
    return beseda[mesta[0]:mesta[len(mesta)-1]+1]

def se_zacne_z(tvit, c):
    beseda = ""
    b = []
    k = 0
    for i in range(0,len(tvit)-1):
        if tvit[i] == c:
            k = 1
        if k:
            if tvit[i] == " ":
                k = 0
                beseda = izloci_besedo(beseda)
                b.append(beseda)
                beseda = ""
            beseda += tvit[i]

            if i + 2 == len(tvit):
                beseda += tvit[i + 1]
                beseda = izloci_besedo(beseda)
                b.append(beseda)
    return b

def zberi_se_zacne_z(tviti, c):
    b = []
    a = []
    for i in range(0, len(tviti)):
        if se_zacne_z(tviti[i],c):
            b.append(se_zacne_z(tviti[i],c))
    for bes in b:
        for besede in bes:
            a.append(besede)
    a = unikati(a)
    return a

def vse_afne(tviti):
    s = zberi_se_zacne_z(tviti, "@")
    return s

def vsi_hashtagi(tviti):
    s = zberi_se_zacne_z(tviti, "#")
    return s

def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti) + vse_afne(tviti)
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        h = se_zacne_z(tvit, "#")
        for hash in hashtagi:
            for lojt in h:
                if hash == lojt:
                    avtorji.append(avtor(tvit))
    avtorji = unikati(avtorji)
    avtorji.sort()
    return avtorji

def se_poznata(tviti, oseba1, oseba2):
    poznata = False
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            os = se_zacne_z(tvit, "@")
            for osebe in os:
                if oseba2 == osebe:
                    poznata = True

        if avtor(tvit) == oseba2:
            os = se_zacne_z(tvit, "@")
            for osebe in os:
                if oseba1 == osebe:
                    poznata = True
    return poznata

def besedilo(tvit):
    k = 0
    bes = ""
    for i in range(len(tvit)):
        if(tvit[i - 2] == ":"):
            k = 1
        if k:
            bes += tvit[i]
    return bes


def zadnji_tvit(tviti):
    zad = {}
    for tvit in tviti:
        av = avtor(tvit)
        zad[av] = besedilo(tvit)
    return zad

def prvi_tvit(tviti):
    prvi = {}
    k = 1
    for tvit in tviti:
        av = avtor(tvit)
        for ime in prvi:
            if ime == av:
                k = 0
                break
            else:
                k = 1
        if k:
            prvi[av] = besedilo(tvit)
            k = 0
    return prvi

def prestej_tvite(tviti):
    st = {}
    k = 0
    for tvit in tviti:
        av = avtor(tvit)
        for ime in st:
            if ime == av:
                k = 1
                break
            else:
                k = 0
        if k:
            st[av] += 1
        else:
            st[av] = 1
    return st

def omembe(tviti):
    s = {}
    for tvit in tviti:
        if avtor(tvit) not in s:
            s.update({avtor(tvit): []})

    for tvit in tviti:
        for os in se_zacne_z(tvit, '@'):
            s[avtor(tvit)].append(os)

    return s

def neomembe(ime, omembe):
    s = []
    for om in omembe:
        if om not in omembe[ime]:
            if om != ime:
                s.append(om)
    return s


def se_poznata(ime1, ime2, omembe):
    poznata = False
    for ome in omembe:
        if ome == ime1:
            for o in omembe[ime1]:
                if o == ime2:
                    poznata = True

        if ome == ime2:
            for o in omembe[ime2]:
                if o == ime1:
                    poznata = True
    return poznata

def hashtagi(tviti):
    hashtegi = vsi_hashtagi(tviti)
    sez = []
    s = {}
    for hash in hashtegi:
        for tvit in tviti:
            b = se_zacne_z(tvit, "#")
            for bb in b:
                if bb == hash:
                    sez.append(avtor(tvit))
        s[hash] = sorted(sez)
        sez = []

    return s







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


