def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    seznam = []
    for i in tviti:
        if avtor(i) not in seznam:
            seznam.append(avtor(i))
    return seznam

def izloci_besedo(beseda):
    beseda = list(beseda)
    while True:
        if beseda[0].isalnum() == False:
            beseda.pop(0)
        else:
            break
    i = len(beseda) - 1
    while True:
        if beseda[i].isalnum() == False:
            beseda.pop(i)
        else:
            break
        i -= 1

    return ''.join(beseda)

def se_zacne_z(tvit, c):
    seznam = tvit.split()
    seznamvrn = []
    for i in seznam:
        if i[0] == c:
            seznamvrn.append(izloci_besedo(i))
    return seznamvrn

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for i in tviti:
        for ii in se_zacne_z(i,c):
            if ii not in seznam:
                seznam.append(ii)
    return seznam

def vse_afne(tviti):
    seznam = []
    for i in tviti:
        for ii in se_zacne_z(i, "@"):
            if ii not in seznam:
                seznam.append(ii)
    return seznam

def vsi_hashtagi(tviti):
    seznam = []
    for i in tviti:
        for ii in se_zacne_z(i, "#"):
            if ii not in seznam:
                seznam.append(ii)
    return seznam

def vse_osebe(tviti):
    seznam = []
    seznam.extend(vsi_avtorji(tviti))
    seznam.extend(vse_afne(tviti))
    seznam = unikati(seznam)
    seznam = sorted(seznam)
    return seznam


def custva(tviti, hashtagi):
    seznam = []
    hashtagi_tvita = []

    for i in tviti:
        for ii in se_zacne_z(i, "#"):
            if ii not in hashtagi_tvita:
                hashtagi_tvita.append(ii)
        for iii in hashtagi_tvita:
            for iv in hashtagi:
                if iii == iv:
                    seznam.append(avtor(i))
        del hashtagi_tvita[:]

    seznam = unikati(seznam)
    seznam = sorted(seznam)
    return seznam


def se_poznata(tviti, oseba1, oseba2):
    a = 0
    osebe_tvita = []
    seznam = []
    for i in tviti:
        osebe_tvita.append(i)
        if avtor(i) == oseba1 or avtor(i) == oseba2:
            seznam.extend(vse_afne(osebe_tvita))
            for ii in seznam:
                if oseba1 == ii or oseba2 == ii:
                    return True
        del osebe_tvita[:]
        del seznam[:]
    return False

def besedilo(tvit):
    a = tvit.split(" ")
    a.pop(0)
    return  " ".join(a)

def zadnji_tvit(tviti):
    slov = {}
    for i in tviti:
        slov[avtor(i)] = besedilo(i)
    return slov

def prvi_tvit(tviti):
    slov = {}
    for i in tviti:
        if avtor(i) not in slov:
            slov[avtor(i)] = besedilo(i)
    return slov

def prestej_tvite(tviti):
    slov = {}
    for i in tviti:
        slov[avtor(i)] = 0
    for i in tviti:
        slov[avtor(i)] = slov[avtor(i)] + 1
    return slov

def omembe(tviti):
    slov = {}
    for i in tviti:
        if avtor(i) not in slov:
            slov[avtor(i)] = se_zacne_z(i, "@")
        else:
            slov[avtor(i)].extend(se_zacne_z(i,"@"))
    return slov

def neomembe(ime, omembe):
    polje = []
    for i in omembe:
        polje.append(avtor(i))
    i = 0
    while i < len(polje):
        if polje[i] in omembe[ime]:
            polje.pop(i)
        elif polje[i] == ime:
            polje.pop(i)
        else:
            i += 1
    return polje

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe.keys() and ime2 in omembe.keys():
        if ime1 not in neomembe(ime2, omembe) or ime2 not in neomembe(ime1, omembe):
            return True
    return False

def hashtagi(tviti):
    slov = {}
    for i in tviti:
        a = se_zacne_z(i, "#")
        for ii in a:
            if ii in slov:
                slov[ii].append(avtor(i))
                slov[ii] = sorted(slov[ii])
            else:
                slov[ii] = []
                slov[ii].append(avtor(i))
    return slov




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


