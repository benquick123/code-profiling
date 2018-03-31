def unikati(s):
    a = []
    for element in s:
        if not element in a:
            a.append(element)
    return a

def avtor(tvit):
    tvit = tvit.split(":")
    return tvit[0]

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        tvit = tvit.split(":")
        avtorji.append(tvit[0])
    avtorji = unikati(avtorji)
    return avtorji

def izloci_besedo(beseda):
    beseda = list(beseda)
    i = 0
    while True:
        if beseda[i].isalnum():
            break
        else:
            beseda.pop(i)
    while True:
        i = len(beseda) - 1
        if beseda[i].isalnum():
            break
        else:
            beseda.pop(i)
    return ''.join(beseda)

def se_zacne_z(tvit,c):
    a = []
    besede = tvit.split()
    for beseda in besede:
        if beseda.startswith(c):
            beseda = izloci_besedo(beseda)
            a.append(beseda)
    a = unikati(a)
    return a

def zberi_se_zacne_z(tviti,c):
    seznam = []
    for tvit in tviti:
        a = se_zacne_z(tvit,c)
        for k in a:
            if k != "":
                seznam.append(k)
    seznam = unikati(seznam)
    return seznam

def vse_afne(tviti):
    return(zberi_se_zacne_z(tviti,"@"))

def vsi_hashtagi(tviti):
    return(zberi_se_zacne_z(tviti,"#"))

def vse_osebe(tviti):
    a = []
    a.extend(vsi_avtorji(tviti))
    a.extend(vse_afne(tviti))
    a = unikati(a)
    a = sorted(a)
    return a

def custva(tviti,hashtagi):
    ljudje = []
    for tvit in tviti:
        a = se_zacne_z(tvit,"#")
        for hashtag in hashtagi:
            if hashtag in a:
                ljudje.append(avtor(tvit))
    ljudje = unikati(ljudje)
    ljudje = sorted(ljudje)
    return ljudje

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        a = se_zacne_z(tvit, "@")
        if avtor(tvit) == oseba1:
            for tag in a:
                if tag == oseba2:
                    return True
        elif avtor(tvit) == oseba2:
            for tag in a:
                if tag == oseba1:
                    return True
    return False

def vse_osebe(tviti):
    a = []
    a.extend(vsi_avtorji(tviti))
    a.extend(vse_afne(tviti))
    a = unikati(a)
    a = sorted(a)
    return a

def custva(tviti,hashtagi):
    ljudje = []
    for tvit in tviti:
        a = se_zacne_z(tvit,"#")
        for hashtag in hashtagi:
            if hashtag in a:
                ljudje.append(avtor(tvit))
    ljudje = unikati(ljudje)
    ljudje = sorted(ljudje)
    return ljudje

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        a = se_zacne_z(tvit, "@")
        if avtor(tvit) == oseba1:
            for tag in a:
                if tag == oseba2:
                    return True
        elif avtor(tvit) == oseba2:
            for tag in a:
                if tag == oseba1:
                    return True
    return False

def besedilo(tvit):
    tvit1 = tvit.split(' ')
    tvit1.pop(0)
    tvit1 = ' '.join(tvit1)
    return tvit1

def zadnji_tvit(tviti):
    dict = {}
    for tvit in tviti:
        dict[avtor(tvit)] = besedilo(tvit)
    return dict

def prvi_tvit(tviti):
    dict = {}
    for tvit in tviti:
        if not avtor(tvit) in dict:
            dict[avtor(tvit)] = besedilo(tvit)
    return dict

def prestej_tvite(tviti):
    dict = {}
    for tvit in tviti:
        if avtor(tvit) in dict:
            stevilopojav = dict[avtor(tvit)] + 1
            dict[avtor(tvit)] = stevilopojav
        else:
            dict[avtor(tvit)] = 1
    return dict

def omembe(tviti):
    dict = {}
    for tvit in tviti:
        if avtor(tvit) in dict:
            dodaj = dict[avtor(tvit)]
            dodaj.extend(se_zacne_z(tvit,"@"))
            dict[avtor(tvit)] = dodaj
        else:
            dict[avtor(tvit)] = se_zacne_z(tvit,"@")
    return dict

def neomembe(ime,omembe):
    vseosebe = []
    for i in omembe:
        vseosebe.append(i)
    vseosebe = unikati(vseosebe)
    i = 0
    while i < len(vseosebe):
        if ime == vseosebe[i]:
            vseosebe.pop(i)
        elif vseosebe[i] in omembe[ime]:
            vseosebe.pop(i)
        else:
            i = i + 1
    return vseosebe

def se_poznata(ime1, ime2, omembe):
    a = False
    if ime1 in omembe.keys() and ime2 in omembe.keys():
        if ime1 in omembe[ime2]:
            a = True
        if ime2 in omembe[ime1]:
            a = True
    return a

def hashtagi(tviti):
    dic = {}
    for tvit in tviti:
        a = se_zacne_z(tvit, "#")
        for hasht in a:
            if hasht in dic:
                dic[hasht].append(avtor(tvit))
                dic[hasht] = sorted(dic[hasht])
            else:
                dic[hasht] = []
                dic[hasht].append(avtor(tvit))
    return dic

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


