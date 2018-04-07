def unikati(s):
    novi_unikati = []
    for unikatni_unikati in s:
        if unikatni_unikati not in novi_unikati:
            novi_unikati.append(unikatni_unikati)
    return novi_unikati


def avtor(tvit):
    ime_avtorja = ''
    for crka1 in tvit:
        if crka1 != ':':
            ime_avtorja = ime_avtorja + crka1
        else:
            break
    return ime_avtorja


def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        if avtor(tvit) not in seznam_avtorjev:
            seznam_avtorjev.append(avtor(tvit))
    return seznam_avtorjev



def izloci_besedo(beseda):
    seznam_besed = ''
    for crka in beseda:
        if True == crka.isalnum() or crka == '-':
            seznam_besed = seznam_besed + crka
    return seznam_besed


def se_zacne_z(tvit, c):
    vrnjene_besede = []
    beseda = ''
    pisemo = 0
    for i in range(len(tvit)):
        if tvit[i].isalnum() == False:
            pisemo = 0
            if beseda != '':
                vrnjene_besede.append(beseda)
            beseda = ''
        if pisemo == 1:
            beseda = beseda + tvit[i]
        if tvit[i] == c:
            pisemo = 1
        if i == len(tvit) - 1 and pisemo == 1:
            pisemo = 0
            if beseda != '':
                vrnjene_besede.append(beseda)
            beseda = ''
    return vrnjene_besede


def zberi_se_zacne_z(tviti, c):
    vrnjeni_tviti = []
    for vsi_tviti in tviti:
        besede_v_enem_tvitu = se_zacne_z(vsi_tviti, c)
        for ena_beseda in besede_v_enem_tvitu:
            if ena_beseda not in vrnjeni_tviti:
                vrnjeni_tviti.append(ena_beseda)
    return vrnjeni_tviti


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')


def vse_osebe(tviti):
    alfa_seznam = []
    a = vsi_avtorji(tviti)
    b = zberi_se_zacne_z(tviti, '@')
    for avtorji in a:
        if avtorji not in alfa_seznam:
            alfa_seznam.append(avtorji)
    for avtorji in b:
        if avtorji not in alfa_seznam:
            alfa_seznam.append(avtorji)
    alfa_seznam.sort()

    return alfa_seznam


def besedilo(tvit):
    string = ''
    pisemo = 0
    presledek = [' ']
    for crka in tvit:
        if pisemo == 1:
            string = string + crka
        if crka == ':':
            pisemo = 1
    if string[0] == ' ':
        string2 = ''
        for i in range(1, len(string)):
            string2 = string2 + string[i]
        return string2
    return string




def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        slovar[avtor(tvit)] = besedilo(tvit)
    return slovar



def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = besedilo(tvit)
    return slovar


def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = 1
        else:
            slovar[avtor(tvit)] = slovar[avtor(tvit)] + 1
    return slovar


def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        osebe = se_zacne_z(tvit, '@')
        if avtor(tvit) not in slovar:
            slovar[avtor(tvit)] = osebe
        else:
            for oseba in osebe:
                if oseba not in slovar[avtor(tvit)]:
                    slovar[avtor(tvit)].append(oseba)
    return slovar
        

def neomembe(ime, omembe):
    seznam = []
    for avtor in omembe:
        if avtor not in omembe[ime] and avtor != ime:
            seznam.append(avtor)
    return seznam






















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


