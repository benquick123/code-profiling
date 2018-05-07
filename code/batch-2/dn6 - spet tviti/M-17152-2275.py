# Obvezni del 1:
def unikati(s):
    nov_unikati = []
    for stevilka in s:
        if stevilka not in nov_unikati:
            nov_unikati.append(stevilka)
    return nov_unikati

# Obvezni del 2:
def avtor(tvit):
    ime = tvit.split(":")
    return ime[0]

# Obvezni del 3:
def vsi_avtorji(tviti):
    avtorji = []
    for ime in tviti:
        avtorji.append(avtor(ime))
    unikat_avtorji = unikati(avtorji)
    return unikat_avtorji

# Obvezni del 4:
def izloci_besedo(beseda):
    if beseda.isalnum():
        return beseda
    else:
        while beseda[0].isalnum() == False:
            beseda = beseda[1:]
        while beseda[-1].isalnum() == False:
            beseda = beseda[:-1]
    return beseda

# Obvezni del 5:
def se_zacne_z(tvit, c):
    besede = []
    tvit = tvit.split()
    for beseda in tvit:
        if beseda[0] == c:
            beseda = izloci_besedo(beseda)
            besede.append(beseda)
    return besede

# Obvezni del 6:
def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede.extend(se_zacne_z(tvit, c))
        unikat_besede = unikati(besede)
    return unikat_besede

# Obvezni del 7:
def vse_afne(tviti):
    return(zberi_se_zacne_z(tviti, "@"))

# Obvezni del 8:
def vsi_hashtagi(tviti):
    return(zberi_se_zacne_z(tviti, "#"))

# Obvezni del 9:
def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti)
    osebe.extend(vse_afne(tviti))
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

# Dodatni del 1:
def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        for a in hashtagi:
            if "#"+a in tvit:
                avtorji.append(avtor(tvit))
            avtorji = unikati(avtorji)
            avtorji.sort()
    return avtorji

# Dodatni del 2:
def se_poznata(tviti, oseba1, oseba2):
    i = 0
    for tvit in tviti:
        if oseba1+":" in tvit and "@"+oseba2 in tvit:
            i += 1
    if i >= 1:
        return True
    else:
        return False

# ====================================================================================
# SPET TVITI: S SLOVARJI

# Obvezna naloga 1:
def besedilo(tvit):
    vsebina = tvit.split(": ", 1)
    return vsebina[1]

# Obvezna naloga 2:
def zadnji_tvit(tviti):
    slovar_tvitov = {}
    for tvit in tviti:
        locen_tvit = tvit.split(": ", 1)
        slovar_tvitov[locen_tvit[0]] = locen_tvit[1]
    return slovar_tvitov

# Obvezna naloga 3:
def prvi_tvit(tviti):
    slovar_tvitov = {}
    for tvit in tviti:
        locen_tvit = tvit.split(": ", 1)
        if locen_tvit[0] not in slovar_tvitov:
            slovar_tvitov[locen_tvit[0]] = locen_tvit[1]
    return slovar_tvitov

# Obvezna naloga 4:
from collections import Counter
def prestej_tvite(tviti):
    avtorji = []
    for tvit in tviti:
        locen_tvit = tvit.split(": ", 1)
        avtorji.append(locen_tvit[0])
    stevec = Counter(avtorji)
    return stevec

# Obvezna naloga 5:
def omembe(tviti):
    avtorji = {}
    for tvit in tviti:
        omembe = []
        locen_tvit = tvit.split(": ", 1)
        afne = se_zacne_z(tvit, "@")
        if locen_tvit[0] not in avtorji:
            avtorji[locen_tvit[0]] = afne
        else:
            avtorji[locen_tvit[0]] += afne
    return avtorji

# Obvezna naloga 6:
def neomembe(ime, omembe):
    i = 0
    osebe = omembe[ime]
    osebe_vse = ["sandra", "benjamin", "cilka", "berta", "ana"]
    while i < len(osebe_vse):
        if osebe_vse[i] in osebe or osebe_vse[i] == ime:
            osebe_vse.remove(osebe_vse[i])
        else:
            i += 1
    return osebe_vse










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


