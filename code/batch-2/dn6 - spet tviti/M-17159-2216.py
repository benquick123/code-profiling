import collections

#STAREEEEEEEEEE FUNKCIJEEEEEEEEEEE
def unikati(s):
    seznam = []
    for element in s:
        if element not in seznam:
            seznam.append(element)
    return seznam


def avtor(tvit):
    ime = ""
    for znak in tvit:
        if znak == ":":
            break
        ime += znak
    return ime


def vsi_avtorji(tviti):
    seznam = []
    for tvit in tviti:
        seznam.append(avtor(tvit))
    return unikati(seznam)


def izloci_besedo(beseda):
    koncna = beseda
    for crka in beseda:
        if crka.isalnum():
            break
        koncna = koncna[1:]

    for crka in beseda[::-1]:
        if crka.isalnum():
            break
        koncna = koncna[:-1]
    return koncna


def se_zacne_z(tvit, c):
    seznam = []
    for beseda in tvit.split():
        if beseda[0] == c:
            seznam.append(izloci_besedo(beseda))
    return seznam


def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        seznam += se_zacne_z(tvit, c)
    return unikati(seznam)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne((tviti))))


#DOOOODAAAAAAATNAAAAAAAAAAAAAAAAAAA prejsn tedn


def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in se_zacne_z(tvit, "#"):
                avtorji.append(avtor(tvit))
                break
    return sorted(unikati(avtorji))

"""
def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            if oseba2 in se_zacne_z(tvit, "@"):
                return True
        if avtor(tvit) == oseba2:
            if oseba1 in se_zacne_z(tvit, "@"):
                return True
"""

#NOVEEEEEE FUNKCIJEEEEEEEEEEEEEEEE

def besedilo(tvit):
    return ":".join(tvit.split(":")[1:])[1:]

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        pisatelj = avtor(tvit)
        if pisatelj not in slovar:
            slovar[pisatelj] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    slovar = collections.defaultdict(int)
    for tvit in tviti:
        slovar[avtor(tvit)] += 1
    return slovar

def omembe(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        slovar[avtor(tvit)] += se_zacne_z(tvit, "@")
    return slovar

def neomembe(ime, omembe):
    seznam = []
    for pisatelj in omembe.keys():
        if pisatelj != ime:
            if pisatelj not in omembe[ime]:
                seznam.append(pisatelj)
    return seznam

#DODATNAAAAAAAAAAAAAAAA TA TEDN

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe.keys():
        if ime2 in omembe[ime1]:
            return True
    if ime2 in omembe.keys():
        if ime1 in omembe[ime2]:
            return True

def hashtagi(tviti):
    slovar = {}
    for tvit in tviti:
        for hashtag in se_zacne_z(tvit, "#"):
            if hashtag in slovar:
                slovar[hashtag].append(avtor(tvit))
                slovar[hashtag].sort()
            else:
                slovar[hashtag] = [avtor(tvit)]
    return slovar


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


