import collections
import unittest
import string

"""##################################################################################
   #########################@FUNKCIJE NALOGE Tviti@#########################
   ##################################################################################"""
def unikati(s): #vrne seznam v katerem se pojavijo elemnti,
    uni = []    #seznama "s", samo enkrat, v istem zaporedju
    repeated = set()
    for i in s:
        if i not in repeated:
            uni.append(i)
            repeated.add(i)
    return uni

def avtor(tvit):
    for beseda in tvit.split(): #in tvit.split() = izognemo dodatni vrstici za split
        if beseda.endswith(':'): #endswith = če se string konča z .....
            beseda = beseda[:-1] #odvzamemo zadnji znak besedi (:)
            return beseda

def vsi_avtorji(tviti): #vrne vse avtorje v "tviti"
    t = []
    for tvit in tviti:
        avt = avtor(tvit)
        t.append(avt)
    return t #t namesto unikati(t) [prestej_tvite]

def izloci_besedo(beseda): #vrne besedo brez ne-alfanumeričnih znakov
    return ''.join(ch for ch in beseda if ch in string.digits + string.ascii_letters + '_-' )

def se_zacne_z(tvit, c): #vrne vse besede v "tvit", ki se začnejo z "c"
    t = []
    for beseda in tvit.split():
        if beseda.startswith(c):
            nova = izloci_besedo(beseda)
            t.append(nova)
    return t

def zberi_se_zacne_z(tviti, c): #vrne vse besed v "tviti", ki se začnejo z "c"
    z = []
    for tvit in tviti:
        a = se_zacne_z(tvit, c)
        z.extend(a)
    return unikati(z)

def vse_afne(tviti): #vrne vse besede v "tviti", ki se začnejo z "@"
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti): #vrne vse besede v "tviti", ki se začnejo z "#"
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti): #vrne vse osebe, ki se omenjene v "tviti" po abecedi
    s_oseb = []
    afna_o = zberi_se_zacne_z(tviti, '@')
    s_oseb.extend(afna_o)
    avto = vsi_avtorji(tviti)
    s_oseb.extend(avto)
    return sorted(unikati(s_oseb))

def custva(tviti, hashtagi): #vrne osebe, ki so uporabile hashtagi
    t = []
    for tvit in tviti:
        for has in hashtagi:
            if has in tvit:
                avt = avtor(tvit)
                t.append(avt)
    return sorted(unikati(t))

def se_poznata(tviti, oseba1, oseba2): #vrne True, če je oseba1 kdaj omenila osebo2
    for tvit in tviti:
        if oseba1 in tvit:
            if oseba2 in tvit:
                return True
            return False

"""##################################################################################
   #########################@FUNKCIJE NALOGE Tviti_slovarji@#########################
   ##################################################################################"""

def besedilo(tvit):
    return tvit.split(': ', 1)[1] #[1] je za vrnitev 2. elementa
    #ekvivalent:
    #in_#1, in_#2 = tvit.split(': ', 1)
    #return in_#2

def zadnji_tvit(tviti):
    slovar = {} #prazen slovar
    for tvit in tviti:  #sprehod skozi tvite
        key, val = tvit.split(": ", 1) #split po dvopičju
        slovar.update({key: val}) #doda nove vrednosti v slovar
    return slovar   #vrne slovar

def prvi_tvit(tviti):
    t = [] #uporaba obrnjega seznama, s tem omogočimo uporabo vrednosti od začetka
    for i in list(reversed(tviti)): #funkcija reversed nam obrne seznam vendar moramo dodati list()
        t.append(i) #vrednosti dodajamo v nov seznam 't'
    return zadnji_tvit(t)   #vrnemo "zadnji" ozr. prvi tvit v slovar

def prestej_tvite(tviti):
    return collections.Counter(vsi_avtorji(tviti)) #prešteje kolikokrat je kateri avtor kaj napisal

def omembe(tviti):
    omemba = collections.defaultdict(list)
    for tvit in tviti:
        oseba = se_zacne_z(tvit, '@')
        omemba[avtor(tvit)].extend(oseba)
    return omemba

def neomembe(ime, omembe):
    key = []
    for avtor in omembe.keys():
        if avtor not in omembe[ime]:
            key.append(avtor)
    key.remove(ime)
    return key
def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe:
        if ime2 in omembe:
            if ime2 in omembe[ime1] or ime1 in omembe[ime2]:
                return True
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


