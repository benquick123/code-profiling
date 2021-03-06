tweets = ["sandra: Spet ta dež. #dougcajt",
          "berta: @sandra Delaj domačo za #programiranje1",
          "sandra: @berta Ne maram #programiranje1 #krneki",
          "ana: kdo so te @berta, @cilka, @dani? #krneki",
          "cilka: jst sm pa #luft",
          "sandra: @janko Kaj pocnes?",
          "benjamin: pogrešam ano #zalosten",
          "ema: @benjamin @ana #split #dougcajt #programiranje1? po dvopičju, za začetek?"]


def unikati(s):
    novi = []
    for e in s:
        if e not in novi:
            novi.append(e)
    return novi


# print(unikati(['d','c','b','c']))

def avtor(tvit):
    for e in tvit.split():
        e = e.replace(":", "")
        return e


# print(avtor("ana: kdo so te??"))

def vsi_avtorji(tviti):
    vsi = []
    for tvit in tviti:
        vsi.append(avtor(tvit))
    return unikati(vsi)


# print(vsi_avtorji(["ana: kdo so te??","janc: kdo so te??","junc: kdo so te??","ana: kdo so te??","rin: kdo so te??"]))

def izloci_besedo(beseda):
    if beseda.isalnum():
        return (beseda)
    else:
        for i in beseda.strip():
            if i.isalnum() is True:
                pass
            else:
                if i == "-":
                    pass
                else:
                    beseda = beseda.replace(i, "")
        return beseda


# print(izloci_besedo("@janez-novak!!!!"))

def se_zacne_z(tvit, c):
    rez = []
    for beseda in tvit.split():
        if beseda[0] == c:
            beseda = izloci_besedo(beseda)
            rez.append(beseda)
    return rez


def se_zacne_z_nejceva(tviti, c):
    rez = []
    for tvit in tviti:
        for beseda in tvit.split():
            if beseda[0] == c:
                beseda = izloci_besedo(beseda)
                rez.append(beseda)
    return rez


def zberi_se_zacne_z(tviti, c):
    return unikati(se_zacne_z_nejceva(tviti, c))


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


# print(vsi_hashtagi(tweets))


def vse_osebe(tviti):
    return sorted(unikati(vse_afne(tviti) + vsi_avtorji(tviti)))


def custva(tviti, hashtagi):
    avtorji = []
    for i in hashtagi:
        for tvit in tviti:
            if i in tvit:
                avtorji.append(avtor(tvit))
    return sorted(unikati(avtorji))


# print(custva(tweets, ["dougcajt"]))

def se_poznata1(tviti, oseba1, oseba2):
    if (oseba1 not in vse_osebe(tviti)) | (oseba2 not in vse_osebe(tviti)):
        return False

    for tvit in tviti:
        if avtor(tvit) == oseba1:
            for beseda in tvit.split():
                if oseba2 == izloci_besedo(beseda):
                    return True
        elif avtor(tvit) == oseba2:
            for beseda in tvit.split():
                if oseba1 == izloci_besedo(beseda):
                    return True


# print(se_poznata(tweets, "ana", "benjamin"))

def besedilo(tvit):
    vse = []
    for beseda in tvit.split():
        vse.append(beseda)
    for beseda in tvit.split():

        if beseda[-1] == ":":
            vse.remove(beseda)
            str1 = ' '.join(str(e) for e in vse)
            return str1


# print(besedilo("ana: kdo so te: @berta, @cilka, @dani?"))

def zadnji_tvit(tviti):
    # kljuc = avtor, value = vsebina
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar


# print(zadnji_tvit(tweets)["cilka"])

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) in slovar:
            pass
        else:
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar


def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = 0
    for tvit in tviti:
        if avtor(tvit) in slovar:
            slovar[avtor(tvit)] = slovar[avtor(tvit)] + 1
    return slovar


# print(prestej_tvite(tweets))

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = []
    for tvit in tviti:
        slovar[avtor(tvit)] += se_zacne_z(tvit, "@")
    return slovar


# print(omembe(tweets))

def neomembe(ime, omembe):
  d = []
  for avtor in omembe.keys():
    if (avtor not in omembe[ime]) & (avtor != ime):
      d.append(avtor)
  return d



# print(neomembe("cilka", omembe(tweets)))

def se_poznata(ime1, ime2, omembe):
    trditev = False
    if (ime1 not in omembe.keys()) | (ime2 not in omembe.keys()):
        return trditev
    if ime1 in omembe[ime2]:
        trditev = True
    if ime2 in omembe[ime1]:
        trditev = True
    return trditev


# print(se_poznata("sandra","ema", omembe(tweets)))

def hashtagi(tviti):
    hasher = {}
    for hassh in vsi_hashtagi(tviti):
        hasher[hassh] = sorted(custva(tviti, [hassh]))

    return hasher

# print(hashtagi(tweets))


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














