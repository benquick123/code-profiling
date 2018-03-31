def unikati(s):
    seznam_unikatov = list()
    for element in s:
        if element not in seznam_unikatov:
            seznam_unikatov.append(element)
    return seznam_unikatov


def avtor(tvit):
    ime = ""
    for znak in tvit:
        if znak == ':':
            break
        ime += znak
    return ime

def vsi_avtorji(tviti):
    seznam_avtorjev = list()
    for en_tvit in tviti:
        seznam_avtorjev.append(avtor(en_tvit))
    return unikati(seznam_avtorjev)

def izloci_besedo(beseda):
    while not beseda[0].isalnum():
        beseda = beseda[1:]
        if len(beseda) == 0:
            return ''
    while not beseda[-1].isalnum():
        beseda = beseda[:-1]
        if len(beseda) == 0:
            return ''
    return beseda

def se_zacne_z(tvit, c):
    seznam_besed = list()
    besede_v_tvitu = str.split(tvit)
    for beseda in besede_v_tvitu:
        if(beseda[0] == c):
            seznam_besed.append(izloci_besedo(beseda))
    return seznam_besed

def zberi_se_zacne_z(tviti, c):
    seznam_unikatnih_besed = list()
    for tvit in tviti:
        seznam_unikatnih_besed += se_zacne_z(tvit, c)
    return unikati(seznam_unikatnih_besed)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    return sorted(unikati(vsi_avtorji(tviti) + vse_afne(tviti)))

def custva(tviti, hashtagi):
    seznam_avtorjev = list()
    for tvit in tviti:
        for hashtag in se_zacne_z(tvit, '#'):
            if hashtag in hashtagi:
                seznam_avtorjev.append(avtor(tvit))
    return sorted(unikati(seznam_avtorjev))

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1 and oseba2 in se_zacne_z(tvit, '@'):
            return True
        if avtor(tvit) == oseba2 and oseba1 in se_zacne_z(tvit, '@'):
            return True
    return False

#===================================================================

import collections

def besedilo(tvit):
    for i in range(len(tvit)):
        if tvit[i] == ':':
            return tvit[i+2:]
    return None

def zadnji_tvit(tviti):
    slovar_zadnjih_tvitov = collections.defaultdict(str)
    for tvit in tviti:
        slovar_zadnjih_tvitov[avtor(tvit)] = besedilo(tvit)
    return slovar_zadnjih_tvitov

def prvi_tvit(tviti):
    slovar_zadnjih_tvitov = collections.defaultdict(str)
    for tvit in tviti[::-1]:
        slovar_zadnjih_tvitov[avtor(tvit)] = besedilo(tvit)
    return slovar_zadnjih_tvitov

def prestej_tvite(tviti):
    slovar_zadnjih_tvitov = collections.defaultdict(int)
    for tvit in tviti:
        slovar_zadnjih_tvitov[avtor(tvit)] += 1
    return slovar_zadnjih_tvitov

def omembe(tviti):
    slovar_zadnjih_tvitov = collections.defaultdict(list)
    for tvit in tviti:
        slovar_zadnjih_tvitov[avtor(tvit)] += se_zacne_z(tvit, '@')
    return slovar_zadnjih_tvitov

def neomembe(ime, omembe):
    neomenjeni = list()
    for ime_osebe in omembe:
        if ime_osebe not in omembe[ime] and ime_osebe != ime:
            neomenjeni.append(ime_osebe)
    return neomenjeni

def se_poznata(ime1, ime2, omembe):
    if ime2 in omembe:
        if ime1 in omembe[ime2]:
            return True
    if ime1 in omembe:
        if ime2 in omembe[ime1]:
            return True
    return False

def hashtagi(tviti):
    slovar_hashtagov = collections.defaultdict(list)
    for tvit in tviti:
        if len(se_zacne_z(tvit, '#')) >= 1:
            for hashtag in se_zacne_z(tvit, '#'):
                slovar_hashtagov[hashtag].append(avtor(tvit))
    for imena in slovar_hashtagov:
        slovar_hashtagov[imena] = sorted(slovar_hashtagov[imena])
    return slovar_hashtagov

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


