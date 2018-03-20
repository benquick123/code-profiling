
import unittest

def unikati(s):
    vrni = []
    for x in s:
        for y in vrni:
            if x==y:
                break
        else:
            vrni.append(x)
    return vrni

def avtor(tvit):
    ime = ""
    for crka in tvit:
        if crka == ':':
            break
        else:
            ime = ime + crka
    return ime

def vsi_avtorji(tviti):
    seznam_imen = []
    for tvit in tviti:
        seznam_imen.append(avtor(tvit))
    return unikati(seznam_imen)

def izloci_besedo(beseda):
    brisi = ""
    for znak in beseda:
        if znak.isalnum() == False:
            brisi = brisi + znak
        else:
            break

    beseda = beseda.replace(brisi, '')
    beseda = beseda[::-1]

    brisi = ""
    for znak in beseda:
        if znak.isalnum() == False:
            brisi = brisi + znak
        else:
            break

    beseda = beseda.replace(brisi, '')
    return beseda[::-1]

def se_zacne_z(tvit, c):
    zacni = False
    x = []
    beseda = ""
    for znak in tvit:
        if znak == c:
            zacni = True

        if znak == " " and zacni == True:
            zacni = False
            x.append(izloci_besedo(beseda))
            beseda = ""

        if zacni == True:
            beseda = beseda + znak

    if beseda != "":
        x.append(beseda)
    return x

def zberi_se_zacne_z(tviti, c):
    seznam_besed = []
    for posamezni_tvit in tviti:
        y = se_zacne_z(posamezni_tvit,c)
        for besede in y:
            seznam_besed.append(izloci_besedo(besede))
    return unikati(seznam_besed)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,'@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,'#')

def vse_osebe(tviti):
    osebe_zacetek = vsi_avtorji(tviti)
    osebe = vse_afne(tviti)
    for imena in osebe_zacetek:
        osebe.append(imena)
    return sorted(unikati(osebe))

def custva(tviti, hashtagi):
    uporabniki = []
    for posamezni_tvit in tviti:
        ime = avtor(posamezni_tvit)
        for h in hashtagi:
            if h in posamezni_tvit:
                uporabniki.append(ime)
    return sorted(unikati(uporabniki))


def prestej_tvite(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_tvita = tvit.split(":", 1)[0]
        if avtor_tvita not in slovar:
            slovar[avtor_tvita] = 1
        else:
            slovar[avtor_tvita] += 1
    return slovar

def prvi_tvit(tviti):
    slovar = {}
    for tvit in tviti:
        avtor_tvita = tvit.split(":", 1)[0]
        if avtor_tvita not in slovar:
            besedilo_tvita = besedilo(tvit)
            slovar[avtor_tvita] = besedilo_tvita
    return slovar


def zadnji_tvit(tviti):
    slovar ={}
    for tvit in tviti:
        avtor_tvita = tvit.split(":",1)[0]
        besedilo_tvita = besedilo(tvit)
        slovar[avtor_tvita] = besedilo_tvita
    return slovar

def besedilo(tvit):
   return  tvit.split(": ",1)[1:][0]

def omembe(tviti):
    slovar = {}
    seznam_imen  = []
    for tvit in tviti:
        avtor_tvita = tvit.split(":", 1)[0]
        seznam_imen = se_zacne_z(tvit,"@")
        if avtor_tvita not in slovar:
            slovar[avtor_tvita] = seznam_imen
        else:
            for tvit_omenjen in seznam_imen:
                slovar[avtor_tvita].append(tvit_omenjen)
            slovar[avtor_tvita] = unikati(slovar[avtor_tvita])
    return slovar

def neomembe(ime, slovar_omemb):
    vrni = []
    for imena in slovar_omemb:
        if imena not in slovar_omemb[ime] and imena != ime:
            vrni.append(imena)
    return vrni

def se_poznata(ime1,ime2,slovar_omemb):
    if ime1 not in slovar_omemb or ime2 not in slovar_omemb:
        return False
    if ime2 in slovar_omemb[ime1] or ime1 in slovar_omemb[ime2]:
        return True
    else:
        return False

def hashtagi(tviti):
    slovar = {}
    seznam = []
    seznam = zberi_se_zacne_z(tviti,"#")
    for hashi in seznam:
        slovar[hashi] = []
    seznam = []
    seznam = vsi_avtorji(tviti)
    for tvit in tviti:
        for hashi in slovar:
            if hashi in tvit:
                sorted(slovar[hashi].append(avtor(tvit)))
    return slovar


def hashtagi(tviti):
    slovar = {}
    seznam = []
    seznam = zberi_se_zacne_z(tviti,"#")
    for hashi in seznam:
        slovar[hashi] = []
    seznam = []
    seznam = vsi_avtorji(tviti)
    for tvit in tviti:
        for hashi in slovar:
            if hashi in tvit:
                slovar[hashi].append(avtor(tvit))
                slovar[hashi]= sorted(slovar[hashi])
    return slovar











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


