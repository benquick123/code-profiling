import collections
import unittest


def hastegi_v_tvitu(tvit):
    vsi_tegi = []
    locen_tvit = tvit.split(" ")
    for beseda in locen_tvit:
        if "#" in beseda:
            izlocen_teg = izloci_besedo(beseda)
            vsi_tegi.append(izlocen_teg)
    return vsi_tegi



def izloci_besedo(beseda):
   cnt1 = 0
   cnt2 = 0
   dolzina = len(beseda)
   for i in range (0, dolzina):
        if beseda[i].isalnum() == True:
            break
        if beseda[i].isalnum() == False:
            cnt1 += 1
   obrnejana_beseda = beseda[::-1]
   for j in range (0, dolzina):
        if obrnejana_beseda[j].isalnum() == True:
            break
        if obrnejana_beseda[j].isalnum() == False:
            cnt2 += 1
   x = dolzina - cnt2
   return beseda[cnt1:x]



def vse_afne(tvit):
    imena = []
    besede = tvit.split(" ")
    for i in range (0, len(besede)):
        if '@' in besede[i]:
            ociscena_beseda = izloci_besedo(besede[i])
            imena.append(ociscena_beseda)
    return imena





def avtor(tvit):
    name = tvit.split(":")
    ime = name[0]
    return ime




def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        name = tvit.split(":")
        ime = name[0]
        if ime not in avtorji:
            avtorji.append(ime)
    return avtorji



def besedilo(tvit):
    cnt = 1
    for i in range (0, len(tvit)):
        if tvit[i].isalnum()== True:
            cnt += 1
        if tvit[i].isalnum() == False:
            if tvit[i +1].isalnum()== True:
                cnt += 1
                if tvit[i + 2].isalnum() == True:
                    break
    return tvit[cnt:]



def zadnji_tvit(tviti):
    tviti_slovar = collections.defaultdict(str)
    for tvit in tviti[::-1]:
        avtor_tvita = avtor(tvit)
        locen_tvit = besedilo(tvit)
        if avtor_tvita not in tviti_slovar:
            tviti_slovar[avtor_tvita]= locen_tvit


    return tviti_slovar



def prvi_tvit(tviti):
    tviti_slovar = collections.defaultdict(str)
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        locen_tvit = besedilo(tvit)
        if avtor_tvita not in tviti_slovar:
            tviti_slovar[avtor_tvita]= locen_tvit
    return tviti_slovar


def prestej_tvite(tviti):
    presteti_tviti = collections.defaultdict(int)
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        if avtor_tvita not in presteti_tviti:
            presteti_tviti[avtor_tvita] = 1
        else:
            presteti_tviti[avtor_tvita] += 1
    return presteti_tviti



def omembe(tviti):
    slovar_teganih = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        slovar_teganih[avtor_tvita]= []
    for tvit in tviti:
        avtor_tvita2= avtor(tvit)
        omenjeni = vse_afne(tvit)
        for oseba in omenjeni:
            if oseba:
               slovar_teganih[avtor_tvita2].append(oseba)
    return slovar_teganih



def neomembe(ime,omembe):
    neomenjeni = []
    a = omembe
    avtorji = []
    for k in a:
        omenjeni = a[ime]
        if k != ime:
            avtorji.append(k)
        for y in avtorji:
            if y not in omenjeni and y not in neomenjeni:
                neomenjeni.append(y)
    return neomenjeni

def se_poznata(ime1, ime2, omembe):
    if ime1 not in omembe:
        omembe[ime1] = ""
    if ime2 not in omembe:
        omembe[ime2] = ""
    for oseba in omembe[ime1]:
        if oseba == ime2:
            return True
    for oseba2 in omembe[ime2]:
            if oseba2 == ime1:
                return True
    return False


def hashtagi(tviti):
    slovar_tegov = {}
    urejeni_tegi = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        tegi = hastegi_v_tvitu(tvit)
        for teg in tegi:
            if teg not in slovar_tegov and teg:
                slovar_tegov[teg] = [avtor_tvita]
            else:
                slovar_tegov[teg].append(avtor_tvita)

    for kluc in slovar_tegov:
        a = slovar_tegov[kluc]
        b = sorted(a)
        urejeni_tegi[kluc] = b
    return urejeni_tegi








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


