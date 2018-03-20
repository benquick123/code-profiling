
import unittest

#Naloga5

def unikati(s):
    tab = []
    for x in s:
        if x not in tab:
            tab.append(x)
    return tab

def avtor(tvit):
    tmp = tvit.split(' ')
    return tmp[0][:-1]

def vsi_avtorji(tviti):
    tab = []
    for tvit in tviti:
        a = avtor(tvit)
        if a not in tab:
            tab.append(a)
    return tab

def izloci_besedo(beseda):
    i = 0
    while i != len(beseda):
        if i == 0 and not beseda[i].isalnum(): #znaki pred osrednjim delom
            beseda = beseda[i+1:]
            i = i - 1
        elif i == len(beseda)-1 and not beseda[i].isalnum(): #znaki po osrednjem delu
            beseda = beseda[:i]
            i = i - 2
        i = i + 1
    return beseda

def se_zacne_z(tvit, c):
    tab = []
    tmp = tvit.split(' ')
    for x in tmp:
        if x[0] == c:
           tab.append(izloci_besedo(x[1:]))
    return tab

def zberi_se_zacne_z(tviti, c):
    tab = []
    for tvit in tviti:
        tmp = se_zacne_z(tvit, c)
        for x in tmp:
            tab.append(x)
    return unikati(tab)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    tab = []
    tmp = vsi_avtorji(tviti)
    for x in tmp:
        tab.append(x)
    tmp = vse_afne(tviti)
    for x in tmp:
        tab.append(x)
    tab = unikati(tab)
    tab.sort()
    return tab

def custva(tviti, hashtagi):
    tab = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in vsi_hashtagi(tvit.split(" ")):
                tab.append(avtor(tvit))
    tab = unikati(tab)
    tab.sort()
    return tab

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1 and oseba2 in vse_afne(tvit.split(" ")):
            return True
    return False

#Naloga6

def besedilo(tvit):
    tab = tvit.split()
    tab.remove(avtor(tvit)+":")
    tmp = " ".join(tab)
    return tmp

def zadnji_tvit(tviti):
    slo = {}
    for tvt in tviti:
        if not avtor(tvt) in slo:
            slo[avtor(tvt)] = set()
        slo[avtor(tvt)] = besedilo(tvt)
    return slo

def prvi_tvit(tviti):
    slo = {}
    for tvt in tviti:
        if not avtor(tvt) in slo:
            slo[avtor(tvt)] = set()
            slo[avtor(tvt)] = besedilo(tvt)
    return slo

def prestej_tvite(tviti):
    slo = {}
    for tvt in tviti:
        if not avtor(tvt) in slo:
            slo[avtor(tvt)] = set()
            slo[avtor(tvt)] = 1
        else:
            slo[avtor(tvt)] += 1
    return slo

def omembe(tviti):
    slo = {}
    for tvt in tviti:
        if not avtor(tvt) in slo:
            slo[avtor(tvt)] = set()
            slo[avtor(tvt)] = vse_afne(tvt.split())
        else:
            slo[avtor(tvt)] += (vse_afne(tvt.split()))
    return slo

def neomembe(ime, omembe):
    slo = []
    for ime1, vrednost1 in omembe.items():
        for ime2, vrednost2 in omembe.items():
            if ime == ime1 and ime1 != ime2 and ime2 not in vrednost1:
                slo.append(ime2)
    return slo

def se_poznata(ime1, ime2, omembe):
    for avtor, vrednost in omembe.items():
        if (ime1 == avtor and ime2 in vrednost) or (ime2 == avtor and ime1 in vrednost):
            return True
    return False

def hashtagi(tviti):
    slo = {}
    for tvit in tviti:
        for hashtag in vsi_hashtagi(tvit.split()):
            if hashtag not in slo.keys():
                slo[hashtag] = set()
                slo[hashtag] = [avtor(tvit)]
            else:
                slo[hashtag] += [avtor(tvit)]
                slo[hashtag] = sorted(slo[hashtag])
    return slo


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


