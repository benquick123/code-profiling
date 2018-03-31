tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]
def unikati(s):
    seznamUnikati=[]
    for el1 in s:
        if el1 not in seznamUnikati:
            seznamUnikati.append(el1)
    return seznamUnikati

#print(unikati([1, 3, 2, 1, 1, 3, 2]))

def avtor(tvit):
  avtor= tvit.split(":")
  return avtor[0]

#print(avtor( "ana: kdo so te @berta, @cilka, @dani? #krneki"))

def vsi_avtorji(tviti):
    avtorji=[]
    for el in tviti:
        avtorji.append(avtor(el))
    return unikati(avtorji)

#print(vsi_avtorji(tviti))
def izloci_besedo(beseda):
    i=0
    b=False
    word=[]
    while i<len(beseda):
        if beseda[i].isalnum() or beseda[i]=="-":
            if beseda[i]!="-":
                word.append(beseda[i])
            elif i>0 and i+1<len(beseda) and beseda[i-1].isalnum() and beseda[i+1].isalnum():
                word.append(beseda[i])
        i=i+1
    return "".join(word)


#print(izloci_besedo("!%$ana---"))
#print(izloci_besedo("@janez-nov-ak!!----!"))

def se_zacne_z(tvit, c):
    ustreza=[]
    vrni=[]
    for beseda in tvit.split():
        if beseda[0]==c:
            ustreza.append(beseda)
    for beseda in ustreza:
        vrni.append(izloci_besedo(beseda))
    return vrni

#print(se_zacne_z("sandra: @berta Ne maram #programiranje1 #krneki", "#"))

def zberi_se_zacne_z (tviti,c):
    afne=[]
    for tvit in tviti:
        tvit=tvit.split()
        for beseda in tvit:
            if c in beseda:
                afna=beseda.split(c)
                afna=izloci_besedo(afna[1])
                afne.append(afna)
    return unikati(afne)
#print(zberi_se_zacne_z(tviti,"@"))
def vse_afne(tviti):
    return  zberi_se_zacne_z(tviti,"@")

#print(vse_afne(tviti))

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

#print(vsi_hashtagi(tviti))

def vse_osebe(tviti):
    skupaj=vsi_avtorji(tviti)+zberi_se_zacne_z(tviti,"@")
    urejeno=unikati(skupaj)
    urejeno.sort()
    return urejeno
#print(vse_osebe(tviti))

def custva(tviti, hashtagi):
    avtorji=[]
    for tvit in tviti:
        for tag in hashtagi:
            if tag in tvit:
                avtorji.append(avtor(tvit))
    avtorji=unikati(avtorji)
    avtorji.sort()
    return avtorji
#print(custva(tviti, ["dougcajt", "krneki"]))

def se_poznata1(tviti, oseba1, oseba2):
    vsebuje=[]
    for tvit in tviti:
        if oseba1 in tvit:
            vsebuje.append(tvit)
    for tvit in vsebuje:
        if oseba2 in tvit:
            return True
        else:
            return False


def besedilo(tvit):
    if ":" in tvit:
        i=tvit.index(":")
        tvit=tvit[i+1:]
        if tvit[0]==" ":
            return tvit[1:]
        else:
            return tvit
    else:
        return tvit
#print(besedilo("Spet ta dež. #dougcajt"))


def prestej_tvite(tviti):
    av_tvit={}
    avtorji=vsi_avtorji(tviti)
    counter=0
    for pisec in avtorji:
        for tvit in tviti:
            if pisec == avtor(tvit):
                counter=counter+1
        av_tvit[pisec]=counter
        counter=0
    return av_tvit

def zadnji_tvit(tviti):
    d={}
    avtorji=vsi_avtorji(tviti)
    for pisec in avtorji:
        for i in range(len(tviti),0,-1):
            if pisec == avtor(tviti[i-1]):
                if pisec not in d:
                    d[pisec]=besedilo(tviti[i-1])
    return d

def prvi_tvit(tviti):
    d={}
    avtorji=vsi_avtorji(tviti)
    for pisec in avtorji:
        for i in range(0,len(tviti),1):
            if pisec == avtor(tviti[i]):
                if pisec not in d:
                    d[pisec]=besedilo(tviti[i])
    return d

def omembe(tviti):
    d={}
    avtorji=vsi_avtorji(tviti)
    for pisec in avtorji:
        polje=[]
        for tvit in tviti:
            if pisec == avtor(tvit):
                tvit=tvit.split()
                for beseda in tvit:
                    if "@" in beseda:
                        omenjen=beseda.split("@")
                        omenjen=izloci_besedo(omenjen[1])
                        polje.append(omenjen)
                        d[pisec]=polje
                    if "@" not in beseda and pisec not in d:
                        d[pisec]=polje
    return d


def neomembe(ime, omembe):
    polje=[]
    polje=omembe[ime]
    avtorji=vsi_avtorji(tviti)
    neomenjeni=[]
    for pisec in avtorji:
        if pisec not in polje and pisec != ime:
            neomenjeni.append(pisec)
    return neomenjeni

def neomembe(ime, omembe):
    polje=[]
    omenjeni=omembe[ime]
    avtorji= omembe.keys()
    neomenjeni=[]
    for pisec in avtorji:
        if pisec not in omenjeni and pisec != ime:
            neomenjeni.append(pisec)
    return neomenjeni



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


