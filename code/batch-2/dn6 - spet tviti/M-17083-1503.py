def unikati(s):
    output = []
    for item in s:
        if item not in output:
            output.append(item)
    return output

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)

def izloci_besedo(beseda):
    l = len(beseda)
    j = -1
    k = -1
    if l == 0:
        return ""
    for i in range(0, l - 1):
        crka = beseda[i]
        if crka.isalnum():
            j = i
            break
    for i in range(l - 1, 0, -1):
        crka = beseda[i]
        if crka.isalnum():
            k = i + 1
            break
    return beseda[j:k]

def se_zacne_z(tvit, c):
    output = []
    first = True
    array1 = tvit.split(c)
    for chunk in array1:
        if not first:
            array2 = chunk.split(" ")
            output.append(izloci_besedo(array2[0]))
        else:
            first = False
    return output

def zberi_se_zacne_z(tviti, c):
    output = []
    for tvit in tviti:
        for vnos in se_zacne_z(tvit, c):
            output.append(vnos)
    return unikati(output)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    seznam1 = vsi_avtorji(tviti)
    seznam2 = vse_afne(tviti)
    for oseba in seznam2:
        seznam1.append(oseba)
    output = unikati(seznam1)
    output.sort()
    return output

def custva(tviti, hashtagi):
    output = []
    for hashtag in hashtagi:
        for tvit in tviti:
            najdeni = se_zacne_z(tvit, "#")
            if hashtag in najdeni:
                output.append(avtor(tvit))
    output = unikati(output)
    output.sort()
    return output

def se_poznata1(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            besede = se_zacne_z(tvit, "@")
            if oseba2 in besede:
                return True
        elif avtor(tvit) == oseba2:
            besede = se_zacne_z(tvit, "@")
            if oseba1 in besede:
                return True
    return False

# ^ Funkcije iz prejšnje naloge ^


def besedilo(tvit):
    return tvit[len(tvit.split(":")[0]) + 2:len(tvit)]

def zadnji_tvit(tviti):
    s = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        besedilo1 = besedilo(tvit)
        s[avtor1] = besedilo1
    return s

def prvi_tvit(tviti):
    s = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        if avtor1 not in s:
            s[avtor1] = besedilo(tvit)
    return s

def prestej_tvite(tviti):
    s = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        if avtor1 not in s:
            s[avtor1] = 1
        else:
            s[avtor1] += 1
    return s

def omembe(tviti):
    s = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        if avtor1 not in s:
            s[avtor1] = se_zacne_z(tvit, "@")
        else:
            s[avtor1].extend(se_zacne_z(tvit, "@"))
    return s

def neomembe(ime, omembe):
    s = []
    for omemba1 in omembe:
        if omemba1 != ime:
            s.append(omemba1)
    omembe2 = omembe[ime]
    for omemba in omembe2:
        if omemba in s:
            s.remove(omemba)
    return s

def se_poznata(ime1, ime2, omembe):
    for omemba in omembe:
        if ime1 == omemba:
            for znanec in omembe[ime1]:
                if ime2 == znanec:
                    return True
        if ime2 == omemba:
            for znanec in omembe[ime2]:
                if ime1 == znanec:
                    return True
    return False

def hashtagi(tviti):
    s = {}
    for tvit in tviti:
        avtor1 = avtor(tvit)
        hashtagi1 = se_zacne_z(besedilo(tvit), "#")
        for hashtag1 in hashtagi1:
            if hashtag1 not in s:
                s[hashtag1] = [avtor1]
            else:
                stari = s[hashtag1]
                stari.append(avtor1)
                s[hashtag1] = stari
    for hashtag2 in s:
        s[hashtag2].sort()
    return s

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


