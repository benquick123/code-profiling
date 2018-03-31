def besedilo(tvit):
    return tvit.split(": ", 1)[1]

def avtor(tvit):
    return tvit[:tvit.find(":")]

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        besedilo_tvita = besedilo(tvit)
        slovar[avtor_tvita] = besedilo_tvita
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        if avtor_tvita not in slovar:
            besedilo_tvita = besedilo(tvit)
            slovar[avtor_tvita] = besedilo_tvita
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        if avtor_tvita not in slovar:
            slovar[avtor_tvita] = 1
        else:
            slovar[avtor_tvita] += 1
    return slovar

def omembe_v_tvitih(tviti):
    return zberi_se_zacne_z(tviti, "@")

def zberi_se_zacne_z(tviti, c):
    rezultati = []
    for tvit in tviti:
        rezultati += se_zacne_z(tvit, c)
    return unikati(rezultati)

def se_zacne_z(tvit, c):
    vse_besede = tvit.split()
    rezultati = []
    for beseda in vse_besede:
        if beseda[0] == c:
            rezultati.append(izloci_besedo(beseda))
    return rezultati

def unikati(s):
    unikati = []
    for element in s:
        if element not in unikati:
            unikati.append(element)
    return unikati

def izloci_besedo(beseda):
    while(not beseda[0].isalnum()):
        beseda = beseda[1:]
    while(not beseda[-1].isalnum()):
        beseda = beseda[:-1]
    return beseda

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)

def tviti_avtorja(tviti, ime):
    rezultati = []
    for tvit in tviti:
        if avtor(tvit) == ime:
            rezultati.append(tvit)
    return rezultati

def omembe(tviti):
    slovar = {}
    avtorji = vsi_avtorji(tviti)
    for avtor in avtorji:
        avtorjevi_tviti = tviti_avtorja(tviti, avtor)
        slovar[avtor] = omembe_v_tvitih(avtorjevi_tviti)
    return slovar

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def neomembe(ime, omembe):
    izpadli_avtorji = omembe[ime]
    izpadli_avtorji.append(ime)
    avtorji = []
    for ime, besedilo in omembe.items():
        if ime not in avtorji:
            avtorji.append(ime)
    return([ime for ime in avtorji if ime not in izpadli_avtorji])

def se_poznata(imeX, imeY, omembe):
    poznani_osebeX = []
    poznani_osebeY = []
    if imeX in omembe:
        poznani_osebeX = omembe[imeX]
    if imeY in omembe:
        poznani_osebeY = omembe[imeY]
    x_pozna_y = False
    y_pozna_x = False
    if imeY in poznani_osebeX:
        x_pozna_y = True
    if imeX in poznani_osebeY:
        y_pozna_x = True
    poznata_se = x_pozna_y or y_pozna_x
    return poznata_se

def hashtagi(tviti):
    slovar_hashtagov = {}
    vsi_hashi = vsi_hashtagi(tviti)
    for tvit in tviti:
        for hashtag in vsi_hashi:
            if hashtag in tvit:
                avtor_tvita = avtor(tvit)
                if hashtag in slovar_hashtagov:
                    slovar_hashtagov[hashtag].append(avtor_tvita)
                else:
                    slovar_hashtagov[hashtag] = [avtor_tvita]
                slovar_hashtagov[hashtag] = sorted(slovar_hashtagov[hashtag])
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


