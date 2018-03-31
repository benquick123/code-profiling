# UNIKATI -dela-
def unikati(s):
    sez = []
    for e in s:
        if e not in sez:
            sez.append(e)
    return sez

# AVTOR -dela-
def avtor(tvit):
    at = tvit.split()[0]
    ime = ""
    for l in at:
        if l.isalpha():
            ime += l
    return ime

# VSI AVTORJI -dela-
def vsi_avtorji(tviti):
    sez = []
    for a in tviti:
        tr_avtor = avtor(a)
        if tr_avtor not in sez:
            sez.append(tr_avtor)
    return sez

# IZLOCI BESEDO -dela-
def izloci_besedo(beseda):
    while len(beseda) > 0 and not beseda[0].isalnum():
        beseda = beseda[1:]
    while len(beseda) > 0 and not beseda[-1].isalnum():
        beseda = beseda[:-1]
    return beseda

# SE ZACNE -dela-
def se_zacne_z(tvit, c):
    sez = []
    for e in tvit.split():
        if e.startswith(c):
            sez.append(izloci_besedo(e))
    return sez

# ZBERI SE ZACNE Z -dela-
def zberi_se_zacne_z(tviti, c):
    sez = []
    new_sez = []
    for e in tviti:
        new_sez.append(se_zacne_z(e, c))
    for e in new_sez:
        for i in e:
            if i != None and i not in sez:
                sez.append(i)
    return sez

# VSE AFNE -dela-
def vse_afne(tviti):
    c = "@"
    seznam = zberi_se_zacne_z(tviti, c)
    return seznam

# VSI HASHTAGI -dela-
def vsi_hashtagi(tviti):
    c = "#"
    seznam = zberi_se_zacne_z(tviti, c)
    return seznam


# VSE OSEBE -dela-
def vse_osebe(tviti):
    sez_oseb = []
    sez1 = vsi_avtorji(tviti)
    sez2 = zberi_se_zacne_z(tviti, "@")
    for e in sez1:
        if e not in sez_oseb:
            sez_oseb.append(e)
    for i in sez2:
        if i not in sez_oseb:
            sez_oseb.append(i)
    sez_oseb = sorted(sez_oseb)
    return sez_oseb

### --- program --- ###


# BESEDILO -dela-
def besedilo(tvit):
    sez = ""
    av = (tvit.split()[1:])
    for e in av:
        sez += e
        sez += " "
    sez = sez[:-1]
    return sez


# ZADNJI TVIT -dela-
def zadnji_tvit(tviti):
    sez = {}
    for e in tviti:
        ime = avtor(e)
        bes = besedilo(e)
        sez[ime] = bes
    return sez

# PRVI TVIT
def prvi_tvit(tviti):
    sez = {}
    for e in tviti:
        ime = avtor(e)
        bes = besedilo(e)
        if ime not in sez:
            sez[ime] = bes
    return sez

# PRESTEJ TVITE
def prestej_tvite(tviti):
    sez = {}
    for e in tviti:
        ime = avtor(e)
        if ime not in sez:
            sez[ime] = 0
        sez[ime] += 1
    return sez

# OMEMBE
def omembe(tviti):
    slov = {}
    c = "@"
    for e in tviti:
        ime = avtor(e)
        txt = se_zacne_z(e, c)
        if ime not in slov:
            slov[ime] = txt
        else:
            for i in txt:
                slov[ime].append(i)
    return slov

# NEOMEMBE
def neomembe(ime, omembe):
    vsa_imena = omembe.values()
    nova_imena = []
    for e in vsa_imena:
        for i in e:
            if i not in nova_imena and i in vsi_avtorji(omembe):
                nova_imena.append(i)
    omenjeni = omembe[ime]
    neomenjeni = []
    for e in nova_imena:
        if e != ime and e not in omenjeni:
            neomenjeni.append(e)
    return neomenjeni



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


