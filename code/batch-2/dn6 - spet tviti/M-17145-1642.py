
import unittest
#obvezna naloga:
def besedilo(tvit):
    nov_tvit=[]
    prvo_dvopicje=False
    prvi_presledek=False
    for crka in tvit:
        if(prvo_dvopicje==True):
            if(crka==' ' and prvi_presledek==False):
                prvi_presledek=True
            else:
                nov_tvit.append(crka)
        else:
            if(crka==':'):
                prvo_dvopicje=True
    return ''.join(nov_tvit)
#prejsna naloga
def avtor(tvit):
    new_tvit=[]
    for crka in tvit:
        if(crka==':'):
            return ''.join(new_tvit)
        new_tvit.append(crka)
#prejsna naloga
def zadnji_tvit(tviti):
    novi_tviti={}
    for tvit in tviti:
        avtor_tvita=avtor(tvit)
        besedilo_tvita=besedilo(tvit)
        novi_tviti.update({avtor_tvita:besedilo_tvita})
    return novi_tviti

def prvi_tvit(tviti):
    novi_tviti = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        besedilo_tvita = besedilo(tvit)
        if(avtor_tvita not in novi_tviti.keys()):
            novi_tviti.update({avtor_tvita: besedilo_tvita})
    return novi_tviti
def prestej_tvite(tviti):
    novi_tviti = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        if(avtor_tvita in novi_tviti.keys()):
            count=novi_tviti[avtor_tvita]+1
            novi_tviti.update({avtor_tvita: count})
        else:
            novi_tviti.update({avtor_tvita: 1})
    return novi_tviti

#prejsna naloga
def unikati(s):
    new_s=[]
    for i in s:
        if i not in new_s:
            new_s.append(i)
    return new_s
def izloci_besedo(beseda):
    new_beseda=[]
    prejsna_crka=""
    for crka in beseda:
        if(crka.isalnum()):
            prejsna_crka=crka
            new_beseda.append(crka)
        else:
            if(prejsna_crka.isalnum() and crka=='-'):
                new_beseda.append(crka)
                prejsna_crka=""
    return "".join(new_beseda)

def se_zacne_z(tvit, c):
    tvit_array=tvit.split()
    besede_array=[]
    for beseda in tvit_array:
        if(beseda[:1]==c):
            beseda=izloci_besedo(beseda)
            besede_array.append(beseda)
    return besede_array
#prejsna naloga
def omembe(tviti):
    novi_tviti = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        osebe=se_zacne_z(tvit, '@')
        if(avtor_tvita in novi_tviti.keys()):
            novi_tviti[avtor_tvita].extend(osebe)
        else:
            novi_tviti.update({avtor_tvita: osebe})
    return novi_tviti
def neomembe(ime, omembe):
    ni_omenjen=[]
    for avtor in omembe:
        if avtor not in omembe[ime] and avtor!=ime:
            ni_omenjen.append(avtor)
    return ni_omenjen

#----------------------- Dodatna naloga -----------------------#
def se_poznata(ime1, ime2, omembe):
    for avtor in omembe:
        if(avtor == ime1 and ime2 in omembe[avtor]):
            return True
        if(avtor == ime2 and ime1 in omembe[avtor]):
            return True
    return False

def hashtagi(tviti):
    novi_seznam={}
    hashtag=[]
    for tvit in tviti:
        hashtag.extend(se_zacne_z(tvit, '#'))
    hashtagi=unikati(hashtag)
    for hashtag in hashtagi:
        for tvit in tviti:
            if(hashtag in tvit):
                if(hashtag in novi_seznam.keys()):
                    novi_seznam[hashtag].append(avtor(tvit))
                else:
                    novi_seznam.update({hashtag:[avtor(tvit)]})
    for hashtag in hashtagi:
        novi_seznam[hashtag].sort()
    return novi_seznam

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


