import collections

def unikati(s):
    seznam=[]
    for neki in s:
        if neki not in seznam:
            seznam.append(neki)
    return seznam

def avtor(tvit):
    ime=tvit.split()
    imeNovo=ime[0].replace(":","")
    return imeNovo

def vsi_avtorji(tviti):
    seznam=[]
    for neki in tviti:
        ime=avtor(neki)
        if ime not in seznam:
            seznam.append(ime)
    return seznam

def izloci_besedo(beseda):
    beseda = list(beseda)
    while (ord(beseda[0]) < 48 or ord(beseda[0]) > 57) and (ord(beseda[0]) < 65 or ord(beseda[0]) > 90) and (ord(beseda[0]) < 97 or ord(beseda[0]) > 122):
        del (beseda[0])
    i = len(beseda) - 1
    while (ord(beseda[i]) < 48 or ord(beseda[i]) > 57) and (ord(beseda[i]) < 65 or ord(beseda[i]) > 90) and (ord(beseda[i]) < 97 or ord(beseda[i]) > 122):
        del (beseda[i])
        i = i - 1
    beseda = "".join(beseda)
    return beseda

def se_zacne_z(tvit, c):
    tvit=tvit.split()
    seznam=[]
    for neki in tvit:
        if neki[0] == c:
            novaBes=izloci_besedo(neki)
            seznam.append(novaBes)
    return seznam

def zberi_se_zacne_z(tviti,c):
    sez=[]
    for neki in tviti:
        neki=neki.split()
        for neki2 in neki:
            if neki2[0] == c:
                novaBes = izloci_besedo(neki2)
                sez.append(novaBes)
    return unikati(sez)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    novSeznam=[]
    novSeznam=vse_afne(tviti)+vsi_avtorji(tviti)
    novSeznam=unikati(novSeznam)
    novSeznam.sort()
    return novSeznam

def custva(tviti,hashtagi):
    seznam=[]
    for neki in tviti:
        neki = neki.split()
        for neki2 in hashtagi:
            if "#"+neki2 in neki:
                seznam.append(avtor(neki[0]))
    seznam=unikati(seznam)
    seznam.sort()
    return seznam

def se_poznata(tviti,oseba1,oseba2):
    for neki in tviti:
        if avtor(neki) == oseba1:
            if "@"+oseba2 in neki:
                return True
    for neki in tviti:
        if avtor(neki) == oseba2:
            if "@"+oseba1 in neki:
                return True
    return False

def besedilo(tvit):
    ime = tvit.split()
    del (ime[0])
    return " ".join(ime)

def zadnji_tvit(tviti):
    zadTvit={}
    for tvrit in tviti:
        ime=avtor(tvrit)
        zadTvit[ime]=besedilo(tvrit)
    return zadTvit

def prvi_tvit(tviti):
    zadTvit = {}
    for tvrit in tviti:
        ime = avtor(tvrit)
        if ime not in zadTvit:
            zadTvit[ime] = besedilo(tvrit)
    return zadTvit

def prestej_tvite(tviti):
    stevTvit = {}
    stevTvit = collections.defaultdict(int)
    for tvrit in tviti:
        ime=avtor(tvrit)
        stevTvit[ime]+=1
    return stevTvit

def omembe(tviti):
    stevTvit = collections.defaultdict(list)
    for tvrit in tviti:
        ime = avtor(tvrit)
        stevTvit.setdefault(ime, [])
        for imeOmen in se_zacne_z(tvrit,"@"):
            stevTvit[ime].append(imeOmen)
    return stevTvit

def neomembe(ime,omembe):
    ime=ime.lower()
    seznam=omembe
    seznam2=[]
    for neki in seznam:
        if neki == ime:
            for kljuc in seznam:
                if kljuc not in seznam[neki] and kljuc != ime:
                    seznam2.append(kljuc)
    return seznam2

def se_poznata(ime1,ime2, omembe):
    if ime1 in omembe.get(ime2,""):
        return True
    if ime2 in omembe.get(ime1,""):
        return True
    return False

def hashtagi(tviti):
    seznam = collections.defaultdict(list)
    for neki in tviti:
        ime=avtor(neki)
        for kljuc in se_zacne_z(neki,"#"):
            seznam[kljuc].append(ime)
            seznam[kljuc].sort()
    return seznam


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


