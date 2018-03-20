import collections


def avtor(tvit):
    besede = tvit.split()

    return besede[0][:-1]


def unikati(s):
    sez_unikatov = []

    for element in s:
        if element in sez_unikatov:
            continue

        else:
            sez_unikatov.append(element)

    return sez_unikatov


def izloci_besedo(beseda):
    indeks_zac = 0
    indeks_kon = len(beseda) - 1

    for i in range(0, len(beseda)):
        if beseda[i].isalnum():
            break

        else:
            indeks_zac += 1

    for j in range(len(beseda) - 1, -1, -1):
        if beseda[j].isalnum():
            break

        else:
            indeks_kon -= 1

    return beseda[indeks_zac:indeks_kon + 1]


def zberi_se_zacne_z(tvit, c):
    seznam_besed = []
    tvit_besede = tvit.split()
    for beseda in tvit_besede:
        if beseda[0] == c:
            seznam_besed.append(izloci_besedo(beseda))

        else:
            continue

    return unikati(seznam_besed)


def vse_afne(tvit):
    seznam_afn = zberi_se_zacne_z(tvit, "@")
    seznam_afn = unikati(seznam_afn)

    for i in range(0, len(seznam_afn)):
        seznam_afn[i] = izloci_besedo(seznam_afn[i])

    return seznam_afn


def vsi_hashtagi(tvit):
    seznam_hashov = zberi_se_zacne_z(tvit, "#")
    seznam_hashov = unikati(seznam_hashov)

    for i in range(0, len(seznam_hashov)):
        seznam_hashov[i] = izloci_besedo(seznam_hashov[i])

    return seznam_hashov


def besedilo(tvit):
    tvit_split = tvit.split()
    return " ".join(tvit_split[1:])


def zadnji_tvit(tviti):
    slovar_zadnji_tvit = collections.defaultdict()
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        besedilo_tvita = besedilo(tvit)
        slovar_zadnji_tvit[avtor_tvita] = besedilo_tvita

    return dict(slovar_zadnji_tvit)


def prvi_tvit(tviti):
    slovar_prvi_tvit = collections.defaultdict(str)
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        trenutni_tvit_avtorja = slovar_prvi_tvit[avtor_tvita]
        if trenutni_tvit_avtorja == "":
            besedilo_tvita = besedilo(tvit)
            slovar_prvi_tvit[avtor_tvita] = besedilo_tvita

        else:
            continue

    return dict(slovar_prvi_tvit)


def prestej_tvite(tviti):
    slovar_prestej_tvite = collections.defaultdict(int)
    for tvit in tviti:
        slovar_prestej_tvite[avtor(tvit)] += 1

    return dict(slovar_prestej_tvite)


def omembe(tviti):
    slovar_omemb = collections.defaultdict(list)
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        seznam_omemb_v_tvitu = vse_afne(tvit)
        trenutne_omembe = slovar_omemb[avtor_tvita]
        trenutne_omembe.extend(seznam_omemb_v_tvitu)
        trenutne_omembe = unikati(trenutne_omembe)
        slovar_omemb[avtor_tvita] = trenutne_omembe

    return dict(slovar_omemb)


def neomembe(ime, omembe):
    seznam_neomenjenih_ljudi = []
    seznam_omenjenih_ljudi = omembe[ime]
    for oseba in omembe:
        if oseba in seznam_omenjenih_ljudi or oseba == ime:
            continue

        else:
            seznam_neomenjenih_ljudi.append(oseba)

    return seznam_neomenjenih_ljudi


def se_poznata(ime1, ime2, omembe):
    omembe_prve = []
    omembe_druge = []

    for ime in omembe:
        if ime == ime1:
            omembe_prve = omembe[ime1]
            continue

        if ime == ime2:
            omembe_druge = omembe[ime2]
            continue

    if (ime1 in omembe_druge) or (ime2 in omembe_prve):
        return True

    else:
        return False


def hashtagi(tviti):
    slovar_hashtagov = collections.defaultdict(list)
    for tvit in tviti:
        avtor_tega_tvita = avtor(tvit)
        seznam_hashov_v_tvitu = vsi_hashtagi(tvit)
        for hashtag in seznam_hashov_v_tvitu:
            if avtor_tega_tvita in slovar_hashtagov[hashtag]:
                continue
            else:
                slovar_hashtagov[hashtag].append(avtor_tega_tvita)

    for hashtag in slovar_hashtagov:
        uredi = slovar_hashtagov[hashtag]
        uredi.sort()
        slovar_hashtagov[hashtag] = uredi

    return dict(slovar_hashtagov)


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
