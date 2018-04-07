#Funckije v pomoč:

def unikati(s):
    prazen_seznam = []

    for i in s:                         # for i in s pomeni, da se i premika po vrednostih seznama s, NE PO INDEKSIH!
        if i not in prazen_seznam:
            prazen_seznam.append(i)

    return prazen_seznam

def izloci_besedo(beseda):
    for i in beseda:
        if not beseda[0].isalnum():
            beseda = beseda[1:]
        else:
            break

    od_zadaj = len(beseda) - 1              #od_zadaj je stevec iz desne proti levi ki se premika po besedi, -1 ker se indeksiranje zacne z 0
                                            # in konca z eno manj kot je dejansko dolg niz
    while od_zadaj >= 0:
        if not beseda[od_zadaj].isalnum():
            beseda = beseda[:od_zadaj]
        else:
            break
        od_zadaj-=1

    return beseda

def se_zacne_z(tvit, c):
    prazen_seznam = []
    rezultat = []
    prazen_seznam = tvit.split(" ")
    for s in prazen_seznam:
        if s[0] == c:
            rezultat.append(izloci_besedo(s))

    return rezultat

def zberi_se_zacne_z(tviti, c):
    rez = []
    for i in tviti:
        rez.extend(se_zacne_z(i,c))         # extend zdruzi dva seznama, ne uporabljaj "append"!!!

    return unikati(rez)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

############################

def get_tviti(tviti):
    seznam_tvitov = []
    for tvit in tviti:
        seznam_tvitov.append(tvit)

    return seznam_tvitov

############################

def besedilo(tvit):
    razlom = tvit.split(": ", 1)
    return razlom[1]

def avtor(tvit):
    razlom = tvit.split(": ", 1)
    return razlom[0]

def zadnji_tvit(tviti):
    prazen_slovar = collections.defaultdict(str)

    for tvit in tviti:
        besedilo_tvita = besedilo(tvit)
        avtor_tvita = avtor(tvit)
        prazen_slovar[avtor_tvita] = besedilo_tvita

    return prazen_slovar

def prvi_tvit(tviti):
    prazen_slovar = collections.defaultdict(str)

    for tvit in tviti:
        besedilo_tvita = besedilo(tvit)
        avtor_tvita = avtor(tvit)

        if prazen_slovar[avtor_tvita] == "":
            prazen_slovar[avtor_tvita] = besedilo_tvita

    return prazen_slovar

def prestej_tvite(tviti):
    prazen_slovar = collections.defaultdict(int)

    for tvit in tviti:
        besedilo_tvita = besedilo(tvit)
        avtor_tvita = avtor(tvit)
        prazen_slovar[avtor_tvita] += 1

    return prazen_slovar

def omembe(tviti):
    prazen_slovar = collections.defaultdict(list)

    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        prazen_slovar[avtor_tvita].extend(se_zacne_z(tvit, "@"))

    return prazen_slovar

def neomembe(ime, omembe):
    prazen_slovar = []
    for oseba, vrednost in omembe.items():
        if oseba not in omembe[ime] and oseba != ime:
            prazen_slovar.append(oseba)

    return prazen_slovar

def se_poznata(ime1, ime2, omembe):
    for oseba, vrednost in omembe.items():
        if oseba == ime1 and ime2 in vrednost:
            return True
        elif oseba == ime2 and ime1 in vrednost:
            return True

    return False

def hashtagi(tviti):
    prazen_slovar = collections.defaultdict(list)
    seznam_hashtagov = vsi_hashtagi(tviti)
    for hash in seznam_hashtagov:
        for tvit in tviti:
            for split in se_zacne_z(tvit, "#"):
                if split == hash:
                    prazen_slovar[hash].append(avtor(tvit))

    for kljuc, vrednost in prazen_slovar.items():
        prazen_slovar[kljuc] = sorted(vrednost)

    return prazen_slovar


import unittest
import collections

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


