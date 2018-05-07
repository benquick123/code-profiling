def unikati(s):
    tab = []
    i = 0
    j = 0
    while i < len(s):
        j = 0
        vsebuje = False
        while j < len(tab):
            if s[i] == tab[j]:
                vsebuje = True
            j = j + 1
        if vsebuje == False:
            tab.append(s[i])
        i = i + 1

    return tab

def avtor(tvit):
    znaki = list(tvit)
    i = 0
    while i < len(znaki):
        if znaki[i] == ":":
            break
        i = i + 1

    tab = []
    j = 0
    while j < i:
        tab.append(znaki[j])
        j = j + 1

    avtor = "".join(tab)

    return avtor

def vsi_avtorji(tviti):
    avtorji = []
    i = 0
    while i < len(tviti):
        x = avtor(tviti[i])
        avtorji.append(x)
        i = i + 1

    avtorji = unikati(avtorji)

    return avtorji


def izloci_besedo(beseda):
    tab = list(beseda)
    i = 0
    while i < len(beseda):
        if tab[i].isalnum() == 1:
            break
        i = i + 1

    j = len(beseda) - 1
    while j > 0:
        if tab[j].isalnum() == 1:
            break
        j = j - 1

    tab2 = []

    while i <= j:
        tab2.append(tab[i])
        i = i + 1

    return "".join(tab2)

def se_zacne_z(tvit, c):
    tab1 = tvit.split()
    tab2 = []
    i = 0
    while i < len(tab1):
        beseda = list(tab1[i])
        if beseda[0] == c:
            tab2.append(tab1[i])
        i = i + 1


    besede = []
    j = 0
    while j < len(tab2):
        besede.append(izloci_besedo(tab2[j]))
        j = j + 1

    return besede

def zberi_se_zacne_z(tviti, c):
    i = 0
    besede = []
    while i < len(tviti):
        besede = list(besede) + list(se_zacne_z(tviti[i], c))
        i = i +1

    return unikati(besede)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    tab = list(vsi_avtorji(tviti))+list(vse_afne(tviti))
    return sorted(unikati(tab), key=str.lower)


#----------------------------------------------------------------------------

def besedilo(tvit):
    znaki = list(tvit)
    tab = []
    stevec = 0

    while stevec < len(znaki):
        if znaki[stevec] == ":":
            break
        stevec = stevec + 1

    stevec = stevec + 2

    while stevec < len(znaki):
        tab.append(znaki[stevec])
        stevec = stevec + 1

    return "".join(tab)

def zadnji_tvit(tviti):
    slovar = {}
    stevec = 0
    while stevec < len(tviti):
        slovar[avtor(tviti[stevec])] = besedilo(tviti[stevec])
        stevec = stevec + 1
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    stevec = 0
    while stevec < len(tviti):
        if avtor(tviti[stevec]) not in slovar:
            slovar[avtor(tviti[stevec])] = besedilo(tviti[stevec])
        stevec = stevec + 1
    return slovar

def prestej_tvite(tviti):
    slovar = {}
    stevec = 0
    while stevec < len(tviti):
        if avtor(tviti[stevec]) in slovar:
            slovar[avtor(tviti[stevec])] = slovar[avtor(tviti[stevec])]+1
        else:
            slovar[avtor(tviti[stevec])] = 1
        stevec = stevec + 1
    return slovar

def vse_omembe_od_osebe(tviti, oseba):
    tab = []
    a = 0
    while a < len(tviti):
        if avtor(tviti[a]) == oseba:
            tab.append(besedilo(tviti[a]))
        a = a + 1
    return vse_afne(tab)

def omembe(tviti):
    slovar = {}
    a = 0
    while a < len(tviti):
        if avtor(tviti[a]) not in slovar:
            slovar[avtor(tviti[a])] = vse_omembe_od_osebe(tviti, avtor(tviti[a]))
        a = a + 1
    return slovar

def avtorji_omemb(slovar):
    return list(slovar.keys())

def neomembe(ime, omembe):
    tab1 = omembe[ime]
    tab1.append(ime)
    tab2 = avtorji_omemb(omembe)
    tab3 = []
    for x in tab2:
        if x not in tab1:
            tab3.append(x)
    return tab3




































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


