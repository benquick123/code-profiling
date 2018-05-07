import unittest
from collections import defaultdict
#iz prejšnje naloge
def unikati(s):
    s1 = []
    for i in s:
        if i not in s1:
            s1.append(i)
    return s1

def avtor(tvit):
    avtor = tvit.split(":")
    return avtor[0]

def vsi_avtorji(tviti):
    s = []
    for i in tviti:
        avtor = i.split(":")
        if avtor[0] not in s:
            s.append(avtor[0])
    return s

def izloci_besedo(beseda):
    izloceno = []
    for i in beseda:
        if i.isalnum() or i == "-":
            izloceno.append(i)
    izloceno = "".join(str(x) for x in izloceno)
    return izloceno

def se_zacne_z(tvit, c):
    s = []
    razdeljeno = tvit.split(" ")
    for i in razdeljeno:
        if i[0] == c:
            a = izloci_besedo(i)
            s.append(a)
    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for i in tviti:
        zacasni = i.split(" ")
        for j in zacasni:
            if j[0] == c:
                a = izloci_besedo(j)
                if a not in s:
                    s.append(a)
    return s

def zberi_se_zacne_z2(tviti, c):
    s = []
    zacasni = tviti.split(" ")
    for j in zacasni:
        if j[0] == c:
            a = izloci_besedo(j)
            if a not in s:
                s.append(a)
    return s

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_afne2(tviti):
    return zberi_se_zacne_z2(tviti, "@")

def vsi_hashtagi2(tviti):
    return zberi_se_zacne_z2(tviti, "#")

def vse_osebe(tviti):
    s = vsi_avtorji(tviti)
    for i in tviti:
        k = se_zacne_z(i,"@")
        for j in k:
            if j not in s:
                s.append(j)
    s.sort()
    return s
#-----------------------------------------------------------------------------------------------
#obvezni del
def besedilo(tvit):
    a = tvit.replace(avtor(tvit),' ')
    a = a.replace(':',' ',1)
    a = a.strip()
    return a

def zadnji_tvit(tviti):
    d = {}
    for tvit in tviti:
        if avtor(tvit) not in d:
            d[avtor(tvit)] = besedilo(tvit)
        else:
            d.update({avtor(tvit):besedilo(tvit)})
    return d

def prvi_tvit(tviti):
    d = {}
    for tvit in tviti:
        if avtor(tvit) not in d:
            d[avtor(tvit)] = besedilo(tvit)
    return d

def prestej_tvite(tviti):
    a = {}
    s = []
    for i in tviti:
        avtor = i.split(":")
        s.append(avtor[0])
    for av in s:
        a[av] = s.count(av)
    return a

def omembe(tviti):
    d = {}
    for i in tviti:
        if avtor(i) not in d:
            d[avtor(i)] = vse_afne2(i)
        else:
            s = vse_afne2(i)
            for k in s:
                d[avtor(i)].append(k)
            
    return d

def neomembe(ime, omembe):
    s = []
    for k in omembe:
        if k not in omembe[ime] and k != ime:
            s.append(k)
    return s
#-------------------------------------------------------------------------------------------------------------
#dodatni del
def se_poznata(ime1, ime2, omembe):
    a = []
    for kljuc, vrednost in omembe.items():
        a.append(kljuc)
    if ime1 in a and ime2 in a:
        if ime2 in omembe[ime1] or ime1 in omembe[ime2]:
            return True
        else:
            return False

def hashtagi(tviti):
    s = {}
    hash = vsi_hashtagi(tviti)
    for a in hash:
        k = []
        for tvit in tviti:
            if a in tvit:
                k.append(avtor(tvit))
                k.sort()
            s[a] = k
    return s

#-------------------------------------------------------------------------------------------------------------

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