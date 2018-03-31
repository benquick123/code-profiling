import unittest
import collections



def unikati(s):
    x = []
    for i in s:
        if i not in x:
            x.append(i)
    return x


def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    avtorji=[]
    for i in tviti:
        avtorji.append(avtor(i))
    return unikati(avtorji)


def izloci_besedo(beseda):
    pripona = ""
    predpona = ""
    for i in beseda:
        if not i.isalnum():
            predpona += i
        else:
            break
    for x in beseda[::-1]:
        if not x.isalnum():
            pripona += x
        else:
            break
    return beseda.replace(pripona, "").replace(predpona, "")


def se_zacne_z(tvit,c):
    besede = tvit.split()
    seznam_besed_c = []
    for b in besede:
        if b[0]==c:
            seznam_besed_c.append(izloci_besedo(b))
    return seznam_besed_c


def zberi_se_zacne_z(tviti, c):
    s=[]
    for t in tviti:
     s = s + se_zacne_z(t, c)
    return unikati(s)


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    seznam_oseb = vsi_avtorji(tviti) + vse_afne(tviti)
    return sorted(unikati(seznam_oseb))


def custva(tviti, hashtagi):
    avtorji = []
    for i in tviti:
        if bool(set(se_zacne_z(i, "#")) & set(hashtagi)):
            avtorji.append(avtor(i))
    return sorted(unikati(avtorji))


# def se_poznata(tviti, o1, o2):
#     for i in tviti:
#         avtor_t = avtor(i)
#         omenjeni = se_zacne_z(i, "@")
#         if omenjeni != []:
#             osebe = []
#             osebe = osebe + omenjeni
#             osebe.append(avtor_t)
#             if o1 in unikati(osebe) and o2 in unikati(osebe):
#                 return True
#         else:
#             continue
#     else:
#         return False

#Nove funkcije

def besedilo(tvit):
    return ''.join(map(str, (tvit.split(": ", 1)[1:])))


def zadnji_tvit(tviti):
    slovar_tviti = {}
    for i in tviti:
        slovar_tviti[avtor(i)] = besedilo(i)
    return slovar_tviti


def prvi_tvit(tviti):
    slovar_tviti = {}
    for i in tviti:
        if avtor(i) not in slovar_tviti:
            slovar_tviti[avtor(i)] = besedilo(i)
    return slovar_tviti


def prestej_tvite(tviti):
    avtorji = []
    for i in tviti:
        avtorji.append(avtor(i))
    return collections.Counter(avtorji)


def omembe(tviti):
    slovar_tvitov = {}
    for i in tviti:
        slovar_tvitov.setdefault(avtor(i), [])
        slovar_tvitov[avtor(i)] = slovar_tvitov.get(avtor(i)) + se_zacne_z(i, "@")
    return slovar_tvitov


def neomembe(ime, omembe):
    omembeosebe = omembe[ime]
    neomenjeni = []
    for i in omembe.keys():
       if i not in omembeosebe and i != ime:
           neomenjeni.append(i)
    return neomenjeni


def se_poznata(ime1, ime2, omembe):
    omenjeni_obeh = []
    if omembe.get(ime1):
        omenjeni_obeh = omenjeni_obeh + omembe[ime1]
    if omembe.get(ime2):
        omenjeni_obeh = omenjeni_obeh + omembe[ime2]
    if ime1 in omenjeni_obeh + [ime2]:
        return True
    elif ime2 in omenjeni_obeh + [ime1]:
        return True
    else:
        return False


def hashtagi(tviti):
    slovar_hashtagov = {}
    vse_lojtre = vsi_hashtagi(tviti)
    for i in vse_lojtre:
        slovar_hashtagov.setdefault(i, [])
    for i in tviti:
        for x in i.split(" "):
            if x[0] == "#":
                key = izloci_besedo(x)
                slovar_hashtagov[key] = sorted(slovar_hashtagov[key] + [avtor(i)])

    return slovar_hashtagov


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


