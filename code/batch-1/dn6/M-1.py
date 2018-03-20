import unittest

def unikati(s):

    seznam = []

    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam




def avtor(tvit):

    rez_tweet = ""

    avt = 0
    stevc = 0

    for x in tvit:
        stevc = tvit.find(":")
        while avt != stevc:
            rez_tweet+=tvit[avt]
            avt+=1
    return rez_tweet




def vsi_avtorji(tviti):

    a = ""

    prvi_seznam = []
    drugi_seznam = []

    for x in tviti:
        prvi_seznam.append(x)
        y = x.split(":")
        drugi_seznam.append(y[0])

    return unikati(drugi_seznam)




def izloci_besedo(beseda):

    xxx = ""
    koncno = ""

    for x in beseda:
        if x.isalnum() != True:
            beseda = beseda.replace(x, "")
        else:
            xxx = beseda[::-1]
            break

    for y in xxx:
        if y.isalnum() != True:
            xxx = xxx.replace(y, "")
        else:
            koncno = xxx[::-1]
            break

    return koncno





def se_zacne_z(tvit, c):

    seznam = []
    drugi_seznam = []

    seznam.append(tvit.split())

    for x in seznam:
        for y in x:
            if c in y:
                drugi_seznam.append(izloci_besedo(y))
    return drugi_seznam




def zberi_se_zacne_z(tviti, c):

    x = 0

    seznam = []
    koncni_seznam = []

    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for x in y:
                if c in x:
                    koncni_seznam.append(izloci_besedo(x))
    return unikati(koncni_seznam)





def vse_afne(tviti):

    ax = 0

    seznam = []
    drugi_seznam = []

    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for x in y:
                if "@" in x:
                    drugi_seznam.append(izloci_besedo(x))
    drugi = unikati(drugi_seznam)
    return drugi






def vsi_hashtagi(tviti):

    xx = 0

    seznam = []
    koncni_seznam = []

    for x in tviti:
        seznam.append(x.split())
    for y in seznam:
            for xx in y:
                if "#" in xx:
                    koncni_seznam.append(izloci_besedo(xx))
    return unikati(koncni_seznam)





def vse_osebe(tviti):

    seznam = []
    drugi_seznam = []
    tretji_seznam = []
    cetrti_seznam = []

    seznam.append(vse_afne(tviti))
    seznam.append(vsi_avtorji(tviti))

    for a in seznam:
        for b in a:
            drugi_seznam.append(b)
    tretji_seznam = sorted(drugi_seznam)
    cetrti_seznam = (unikati(tretji_seznam))
    return cetrti_seznam



'''...domaca naloga...'''


tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]



def besedilo(tvit):
    return tvit.split(" ", 1)[1]


def besedilo_avtor(tvit):
    return tvit.split(":", 1)[0]



def zadnji_tvit(tviti):

    x = {}

    for i in tviti:
        a = avtor(i)
        b = besedilo(i)
        #if a not in d:
        x[a] = b
    return x




def prvi_tvit(tviti):

    x = {}

    for i in tviti:
        a = avtor(i)
        b = besedilo(i)
        if a not in x:
            x[a] = b
    return x




def prestej_tvite(tviti):

    seznam = []
    xxx = {}
    slovar = {}

    for x in tviti:
        seznam.append(besedilo_avtor(x))
        slovar[besedilo_avtor(x)] = 0
    for y in seznam:
        xxx[y] = seznam.count(y)
    return xxx




def omembe(tviti):

    x = {}

    for y in tviti:
        a = avtor(y)
        osebe = se_zacne_z(y, "@")
        if a in x:
            for o in osebe:
                x[a].append(o)
        else:
            x[a] = osebe
    return x




def neomembe(ime, omembe):

    seznam = []

    for y in omembe:
        if y not in omembe[ime] and y != ime:
            seznam.append(y)
    return seznam





def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe and ime2 in omembe[ime1]:
        return True
    if ime2 in omembe and ime1 in omembe[ime2]:
        return True
    return False






def hashtagi(tviti):

    x = {}

    for y in tviti:
        xxx = se_zacne_z(y, "#")
        a = avtor(y)
        for t in xxx:
            if t not in x:
                x[t] = [a]
            elif t in x:
                x[t].append(a)
    for y in x:
        x[y].sort()
    return x




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


