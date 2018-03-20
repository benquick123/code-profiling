# -*- coding: utf-8 -*-

def unikati(li):
    unikati = []
    for item in li:
        if (item not in unikati):
            unikati.append(item)
    return unikati

def vsi_avtorji(tviti):
    vsi = []
    for tvit in tviti:
        vsi.append(avtor(tvit))
    
    vsi_uni = unikati(vsi)
    return vsi_uni

def avtor(tvit):
    splitted = tvit.split(":")
    avtor = splitted[0]
    return avtor

def se_zacne_z(tvit, x):
    res = []
    rez = []
    splitted = tvit.split(" ")
    for beseda in splitted:
        bes = list(beseda)
        for letter in bes:
            if (letter == x):
                res.append("".join(beseda))
    res_uni = unikati(res)
    for word in res_uni:
        rez.append(izloci_besedo(word))
    return rez



def izloci_besedo(beseda):
    bes = list(beseda)
    #od spredi
    for letter in bes:
        if (letter.isalnum()):
            break
        else:
            bes = list(filter(lambda a: a != letter, bes))
    
    #od zadi
    for letter in bes[::-1]:
        if (letter.isalnum()):
            break
        else:
            bes = list(filter(lambda a: a != letter, bes))
    out = "".join(bes) 
    return out
def zberi_se_zacne_z(tviti, x):
    vsi = []
    for tvit in tviti:
        vsi = vsi + se_zacne_z(tvit, x)
    
    vsi = unikati(vsi)
    return vsi

def vsi_hash(tviti):
    denom = "#"
    return (zberi_se_zacne_z(tviti, denom))

def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        avtort = avtor(tvit)
        tags = se_zacne_z(tvit, "#")
        for tag in hashtagi:
            if (tag in tags):
                avtorji.append(avtort)
    
    avtorji = unikati(avtorji)
    avtorji = sorted(avtorji)
    return avtorji




def besedilo(tvit):
    splitted = tvit.split(":")
    rez = list(filter(lambda a: a != splitted[0], splitted))
    
    rez = ":".join(rez)
    rez = list(rez)
    if(rez[0] == " "):
        rez.pop(0)
    rez = "".join(rez)
    return (rez)


def zadnji_tvit(tviti):
    a = {}
    for tvit in tviti:
        avtort = avtor(tvit)
        besedilot = besedilo(tvit)
        a[avtort] = besedilot
    return a
        
def prvi_tvit(tviti):
    b = {}
    for tvit in tviti:
        avt = avtor(tvit)
        if (b.has_key(avt)):
            #b[avt] = besedilo(tvit)
            continue
        else:
            b[avt] = besedilo(tvit)
    return b

def prestej_tvite(tviti):
    c = {}
    avtorji = vsi_avtorji(tviti)
    for avtorr in avtorji:
        c[avtorr] = 0
        
    
    for tvit in tviti:
        at = avtor(tvit)
        c[at] = c[at] + 1
    return c

def omembe(tviti):
    o = {}
    for tvit in tviti:
        avt = avtor(tvit)
        o[avt] = []
        
    for tvit in tviti:
        av = avtor(tvit)
        #o[av] = []
        omembe = se_zacne_z(tvit, "@")  #poberi vse oznacene osebe iz tvitov
        for omemba in omembe:
            o[av].append(omemba)
    return o
    
def neomembe(ime, omembe):
    vsi_av = []
    not_av = []
    for kime, vrednost in omembe.iteritems():
        vsi_av.append(kime)
        if (kime == ime):
            omembe_os = vrednost
    
    
    for avtor_neomenjen in vsi_av:
        if(avtor_neomenjen in omembe_os):
            continue
        elif(avtor_neomenjen == ime):
            continue
        else:
            not_av.append(avtor_neomenjen)
        
    return not_av
        
    
def se_poznata(ime1, ime2, omembe):
    for key, value in omembe.iteritems():
        if (key == ime1):
            if(ime2 in value):
                return True
        elif (key == ime2):
            if(ime1 in value):
                return True
    
    return False
    
    
def hashtagi(tviti):
    vsi_h = vsi_hash(tviti)
    sl = {}
    for hashtag in vsi_h:
        sl[hashtag] = custva(tviti, [hashtag])
        
    return sl
        

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


