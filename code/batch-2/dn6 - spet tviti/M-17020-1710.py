
def unikati(s):
    xs = []
    for element in s:
        if element not in xs:
            xs.append(element)
    return xs


def avtor(tvit):
    niz = ""
    for crka in tvit:
        if crka != ":":
            niz += crka
        else:
            break
    return niz


def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in imena:
            imena.append(ime)
    return imena


def izloci_besedo(beseda):
    if beseda.isalnum() == False:
        for crka in beseda:
            if crka.isalnum() == False:
                beseda = beseda[1:]
            else:
                break
        for crka in beseda:
            indeks = beseda.index(crka) + 1
            if indeks < len(beseda):
                element = beseda[indeks]
            if (crka.isalnum() == False) and (element.isalnum() == False):
                beseda = beseda[:-1]
        return beseda
    else:
        return beseda


def se_zacne_z(tvit, c):
    s = []
    xs = []
    beseda = ""
    for crka in tvit:
        if crka != " ":
            beseda += crka
        else:
            xs.append(beseda)
            beseda = ""
    xs.append(beseda)
    for niz in xs:
        if niz.startswith(c):
            nova_beseda = izloci_besedo(niz)
            s.append(nova_beseda)
    return s


def zberi_se_zacne_z(tviti, c):
    s = []
    niz = 0
    for tvit in tviti:
        if c in tvit:
            seznam = se_zacne_z(tvit, c)
            for niz in seznam:
                if niz not in s:
                    s.append(niz)
    return s


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")



def vse_osebe(tviti):
    seznam = []
    s = vsi_avtorji(tviti)
    xs = vse_afne(tviti)
    for ime in xs + s:
        if ime not in seznam:
            seznam.append(ime)
    seznam.sort()
    return seznam


def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        a = avtor(tvit)
        b = se_zacne_z(tvit, "#")
        for element in b:
            for hashtag in hashtagi:
                if element == hashtag and a not in seznam:
                    seznam.append(a)
        seznam.sort()
    return seznam


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        a = avtor(tvit)
        b = se_zacne_z(tvit, "@")
        for element in b:
            if (a == oseba1 or a == oseba2) and (element == oseba1 or element == oseba2):
                return True
    else:
        return False



def besedilo(tvit):
    niz = ""
    s = tvit.split(": ", 1)
    del s[0]
    for element in s:
        niz += element
    return niz


def zadnji_tvit(tviti):
    d = {}
    for tvit in tviti:
        kljuc = avtor(tvit)
        vrednost = besedilo(tvit)
        d[kljuc] = vrednost
    return d


def prvi_tvit(tviti):
    d = {}
    for tvit in tviti:
        kljuc = avtor(tvit)
        vrednost = besedilo(tvit)
        if kljuc in d:
            continue
        d[kljuc] = vrednost
    return d


from collections import Counter

def prestej_tvite(tviti):
    s = []
    for tvit in tviti:
        oseba = avtor(tvit)
        s.append(oseba)
    d = Counter(s)
    return d


def omembe(tviti):
    d = {}
    for tvit in tviti:
        kljuc = avtor(tvit)
        if kljuc not in d:
            d[kljuc] = []
        vrednosti = se_zacne_z(tvit, "@")
        for vrednost in vrednosti:
            d[kljuc].append(vrednost)
    return d


def neomembe(ime, omembe):
    xs = []
    d = omembe
    s = d[ime]
    pisci = d.keys()
    for oseba in pisci:
        if oseba not in s and oseba != ime:
            xs.append(oseba)
    return xs


def se_poznata(ime1, ime2, omembe):
    s = omembe
    imena = s.keys()
    if ime1 not in imena or ime2 not in imena:
        return False
    if ime2 in s[ime1] or ime1 in s[ime2]:
        return True
    else:
        return False


def hashtagi(tviti):
    d = {}
    s = vsi_hashtagi(tviti)
    for tvit in tviti:
        for hash in s:
            if hash in tvit:
                pisec = avtor(tvit)
                if hash not in d:
                    d[hash] = []
                d[hash].append(pisec)
    for kljuc in d:
        xs = d[kljuc]
        xs.sort()
    return d


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


