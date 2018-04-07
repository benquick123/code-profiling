
import unittest

def unikati(s):
    seznam = []
    for stvar in s:
        if stvar not in seznam:
            seznam.append(stvar)
    return seznam
def avtor(tvit):
    tvit = tvit.split()
    avtor = tvit[0].replace(":", " ").strip()
    return avtor
def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        oseba = avtor(tvit)
        if oseba not in avtorji:
            avtorji.append(oseba.replace(":", " ").strip())
    return avtorji
def izloci_besedo(beseda):
    cista_beseda = beseda
    for i in beseda:
        if not i.isalnum():
            cista_beseda = cista_beseda.strip(i)
    return cista_beseda
def se_zacne_z(tvit, c):
    prave_besede = []
    for beseda in tvit.split():
        if beseda.startswith(c):
            prave_besede.append(izloci_besedo(beseda))
    return prave_besede
def zberi_se_zacne_z(tviti, c):
    seznam = []
    for tvit in tviti:
        besede = se_zacne_z(tvit, c)
        for beseda in besede:
            if beseda not in seznam:
                seznam.append(beseda)
    return seznam
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")
def vse_osebe(tviti):
    seznam = []
    for ime in zberi_se_zacne_z(tviti, "@"):
        seznam.append(ime)
    for ime in vsi_avtorji(tviti):
        if ime not in seznam:
            seznam.append(ime)
    return sorted(seznam)
def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        for beseda in tvit.split():
            if izloci_besedo(beseda) in hashtagi and avtor(tvit) not in avtorji:
                avtorji.append(avtor(tvit))
    return sorted(avtorji)
def se_poznata1(tviti, oseba1, oseba2):
    for tvit in tviti:
        oseba = avtor(tvit)
        poznane = se_zacne_z(tvit, "@")
        if oseba == oseba1 and oseba2 in poznane or oseba == oseba2 and oseba1 in poznane:
            return True
    return False


def besedilo(tvit):
    vse = {}
    besedilo = []
    t_avtor = avtor(tvit)
    for besede in tvit.split():
        if besede.strip(":") != t_avtor:
            besedilo.append(besede)
    t_besedilo = " ".join(besedilo)
    vse[avtor] = t_besedilo
    return vse[avtor]
def zadnji_tvit(tviti):
    vsi = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        besedilo1 = besedilo(tvit)
        vsi[avtor1] = besedilo1
    return vsi
def prvi_tvit(tviti):
    vsi = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        besedilo1 = besedilo(tvit)
        if avtor1 not in vsi:
            vsi[avtor1] = besedilo1
    return vsi
def prestej_tvite(tviti):
    kolikokrat = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        if avtor1 not in kolikokrat:
            kolikokrat[avtor1] = 1
        else:
            kolikokrat[avtor1] += 1
    return kolikokrat
import collections
def omembe(tviti):
    omenjeni = collections.defaultdict(list)
    for tvit in tviti:
        avtor1 = avtor(tvit)
        omembe = se_zacne_z(tvit, "@")
        omenjeni[avtor1]
        for imena in omembe:
            omenjeni[avtor1].append(imena)
    return omenjeni
def neomembe(ime, omembe):
    neomenjeni = []
    for avtor in omembe:
        if avtor not in omembe[ime] and avtor != ime:
            neomenjeni.append(avtor)
    return neomenjeni

def se_poznata(ime1, ime2, omembe):
    for ime in omembe:
        if ime== ime1 and ime2 in omembe[ime]:
            return True
        elif ime == ime2 and ime1 in omembe[ime]:
            return True
    return False
def hashtagi(tviti):
    hashi = collections.defaultdict(list)
    for tvit in tviti:
        avtor1 = avtor(tvit)
        beseda = se_zacne_z(tvit, "#")
        for tag in beseda:
            if avtor1 not in tag:
                hashi[tag].append(avtor1)
    for tvit, seznam in hashi.items():
        seznam = sorted(seznam)
        hashi[tvit] = seznam
    return hashi



























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


