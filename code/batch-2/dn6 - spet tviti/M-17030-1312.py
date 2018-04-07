#star program
import unittest
def unikati(s):
    seznam= []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam
def avtor(tvit):
    tvit = tvit.split()
    ime = tvit[0]
    ime = ime.split()
    ime = list(map(lambda x: x[:-1], ime))
    ime = ime.pop()
    return(ime)
def vsi_avtorji(tviti):
    imena = []
    for i in tviti:
        i = i.split()
        ime = i[0]
        ime = ime.split()
        ime = list(map(lambda x: x[:-1], ime))
        ime = ime.pop()
        if ime not in imena:
            imena.append(ime)
    return(imena)
def izloci_besedo(beseda):
    import re
    beseda = re.sub('[^0-9a-zA-Z--]+', '', beseda)
    return beseda
def se_zacne_z(tvit, c):
    import re
    seznam=[]
    tvit = tvit.split()
    for beseda in tvit:
        if beseda[0] == c:
            beseda = re.sub('[^0-9a-zA-Z--]+', '', beseda)
            seznam.append(beseda)
    return (seznam)
def zberi_se_zacne_z(tviti, c):
    imena = []
    for tvit in tviti:
        import re
        tvit = tvit.split()
        for beseda in tvit:
            if beseda[0] == c:
                beseda = re.sub('[^0-9a-zA-Z--]+', '', beseda)
                if beseda not in imena:
                    imena.append(beseda)
    return (imena)
def vse_afne(tviti):
    seznam=zberi_se_zacne_z(tviti,c="@")
    return seznam
def vsi_hashtagi(tviti):
    seznam=zberi_se_zacne_z(tviti,c="#")
    return seznam
def vse_osebe(tviti):
    vse_osebe=[]
    seznam=vsi_avtorji(tviti)
    drugi_seznam=vse_afne(tviti)
    for ime in seznam:
        if ime not in drugi_seznam:
            drugi_seznam.append(ime)
    drugi_seznam.sort()
    return drugi_seznam
#nov program
import collections
def besedilo(tvit):
    tvit=tvit.split(" ",1)[1]
    return (tvit)
def zadnji_tvit(tviti):
    zadnji_tviti = {}
    ime1 = " "
    for tvit in tviti:
        za_ime = tvit.split()
        ime = za_ime[0]
        ime = ime.split()
        ime = list(map(lambda x: x[:-1], ime))
        ime = ime.pop()
        tvit = tvit.split(" ", 1)[1]
        if ime != ime1:
            zadnji_tviti[ime] = tvit
        else:
            del zadnji_tviti[ime]
            zadnji_tviti[ime] = tvit
        ime1 = ime
    return (zadnji_tviti)
def prvi_tvit(tviti):
    zadnji_tviti = {}
    for tvit in tviti:
        za_ime = tvit.split()
        ime = za_ime[0]
        ime = ime.split()
        ime = list(map(lambda x: x[:-1], ime))
        ime = ime.pop()
        tvit = tvit.split(" ", 1)[1]
        if ime in zadnji_tviti:
            print()
        else:
            zadnji_tviti[ime] = tvit
    return (zadnji_tviti)
def prestej_tvite(tviti):
    seznam_imen = []
    for tvit in tviti:
        za_ime = tvit.split()
        ime = za_ime[0]
        ime = ime.split()
        ime = list(map(lambda x: x[:-1], ime))
        ime = ime.pop()
        seznam_imen.append(ime)
    stevilo = collections.Counter(seznam_imen)
    return stevilo
def omembe(tviti):
    besedilo_values = collections.defaultdict(list)
    for tvit in tviti:
        avtorji = avtor(tvit)
        besedilo_values[avtorji].extend(se_zacne_z(tvit, "@"))
    return besedilo_values
def neomembe(ime, omembe):
    prazen_slovar = []
    for oseba, vrednost in omembe.items():
        if oseba not in omembe[ime] and oseba != ime:
            prazen_slovar.append(oseba)
    return prazen_slovar
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
if __name__ == "__main__":
    unittest.main()


