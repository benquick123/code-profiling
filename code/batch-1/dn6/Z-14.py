def unikati(s):
    nov = []
    for x in s:
        if x not in nov:
            nov.append(x)
    return nov

def avtor(tvit):
    for beseda in tvit.split():
        if ":" in beseda:
            return beseda[:-1]

def vsi_avtorji(tviti):
    sez = []
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in sez:
            sez.append(ime)
    return sez

def izloci_besedo(beseda):
    spredaj = False
    zadaj = False
    while spredaj == False:
        if not beseda[0].isalnum():
            beseda = beseda[1:]
        else:
            spredaj = True
            break
    while zadaj == False:
        if not beseda[-1].isalnum():
            beseda = beseda[:-1]
        else:
            zadaj = True
            break
    return beseda

def se_zacne_z(tvit, c):
    sez = []
    for beseda in tvit.split():
        if beseda.startswith(c):
            beseda = izloci_besedo(beseda)
            sez.append(beseda)
    return sez

def zberi_se_zacne_z(tviti, c):
    sez = []
    vse = " ".join(tviti)
    sez += se_zacne_z(vse,c)
    return unikati(sez)

def vse_afne(tviti):
    afne = zberi_se_zacne_z(tviti, "@")
    return afne

def vsi_hashtagi(tviti):
    hash = zberi_se_zacne_z(tviti, "#")
    return hash

def vse_osebe(tviti):
    sez = []
    sez += vsi_avtorji(tviti)
    sez += vse_afne(tviti)
    sez = unikati(sez)
    return sorted(sez)

def custva(tviti, hashtagi):
    sez = []
    for tvit in tviti:
        for hash in hashtagi:
            if hash in tvit:
                sez.append(avtor(tvit))
    return sorted(unikati(sez))

def se_poznata(tviti, oseba1, oseba2):
    poznanstvo = False
    tviti1 = []
    tviti2 = []
    for x in tviti:
        if oseba1 == avtor(x):
            tviti1.append(x)
            if oseba2  in vse_afne(tviti1):
                poznanstvo = True
    for y in tviti:
        if oseba2 == avtor(y):
            tviti2.append(y)
            if oseba1 in vse_afne(tviti2):
                poznanstvo = True
    return poznanstvo


def besedilo(tvit):
    sez = []
    for beseda in tvit.split():
        sez.append(beseda)
    t = " ".join(sez[1:])
    return t

def zadnji_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        oseba = avtor(tvit)
        slovar[oseba] = besedilo(tvit)
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        oseba = avtor(tvit)
        if oseba not in slovar:
            slovar[oseba] = besedilo(tvit)
    return slovar

def prestej_tvite(tviti):
    stej = {}
    for tvit in tviti:
        oseba = avtor(tvit)
        if oseba not in stej:
            stej[oseba] = 0
        stej[oseba] += 1
    return stej

def omembe(tviti):
    slovar = {}
    for tvit in tviti:
        oseba = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if oseba not in slovar:
            slovar[oseba] = []
        slovar[oseba] += omenjeni
    return slovar


def neomembe(ime, omembe):
    s = set()
    for oseba in omembe:
        if oseba not in s and oseba != ime:
            s.add(oseba)
    for oseba, seznam in omembe.items():
        if ime == oseba:
            t = set(seznam)
            neomenjeni = s.difference(t)
    return list(neomenjeni)


def se_poznata(ime1, ime2, omembe):
    poznanstvo = False
    for ime, seznam in omembe.items():
        if ime1 == ime:
            omenjeni = seznam
            if ime2 in omenjeni:
                poznanstvo = True
    for ime, seznam in omembe.items():
        if ime2 == ime:
            omenjeni2 = seznam
            if ime1 in omenjeni2:
                poznanstvo = True
    return poznanstvo

#ki prejme seznam tvitov in vrne slovar, katerega ključi so hashtagi (brez znaka #),
# pripadajoče vrednosti pa seznami avtorjev, ki so uporabili ta hashtagi. Avtorji naj bodo urejeni po abecedi.
import collections
def hashtagi(tviti):
    slovar = collections.defaultdict(list)
    for tvit in tviti:
        oseba = avtor(tvit)
        for beseda in tvit.split():
            if beseda.startswith("#"):
                hash = beseda[1:]
                if hash.endswith("?"):
                    hash = hash[:-1]
                    if hash not in slovar:
                        slovar[hash] = oseba
                    else:
                        slovar[hash].add(oseba)
    for kljuc, vrednost in slovar.items():
        key = kljuc.strip()
        sez = list(sorted(vrednost))
        slovar[key] = sez
    return slovar








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


