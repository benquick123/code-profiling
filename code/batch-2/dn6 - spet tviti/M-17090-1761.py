#FUNKCIJE IZ PREJŠNJE NALOGE

#Unikati
def unikati(s):
    s_unikati = []
    for i in s:
        if i not in s_unikati: #preveri, če se element še ni pojavil
            s_unikati.append(i) #doda nov element
    return s_unikati

#Avtor
def avtor(tvit):
    s = tvit.split() #spremeni 'tvit' v seznam
    avtor = s[0] #vzame prvo besedo (avtorja)
    return avtor[:-1] #vrne brez ':'

#Vsi avtorji
def vsi_avtorji(tviti):
    avtorji = []
    for i in tviti: #iz vseh tvitov
        avtorji.append(avtor(i)) #zabeleži avtorje
    return unikati(avtorji) #in vrne vse unikatne

#Izloči besedo (brez 'čudnih' znakov)
def izloci_besedo(beseda):
    samo_beseda = ""
    for char in beseda:
        if char.isalnum() or char == '-': #preveri, če je simbol črka ali '-'
            samo_beseda += char #doda novi besedi
    return samo_beseda

#Se začne z ...
def se_zacne_z(tvit, c):
    besede = tvit.split() #razdeli besede v seznam
    iskane_besede = []
    for i in besede:
        if i.startswith(c): #če se beseda začne z iskanim znakom
            iskane_besede.append(izloci_besedo(i)) #doda besedo brez 'čudnih' znakov
    return iskane_besede

#Zberi 'Se začne z ...' (iz vseh tvitov)
def zberi_se_zacne_z(tviti, c):
    besede = []
    iskane_besede = []
    for tvit in tviti: #vsak tvit posebej
        besede.append(se_zacne_z(tvit,c)) #zbere vse besede (v podsezname za posamezen tvit)
    for i in besede:
        for j in i:
            if j not in iskane_besede: #ker so besede prej v podseznamih
                iskane_besede.append(j) #unikate prepišemo v nov seznam
    return iskane_besede #lahko tudi z return unikati(iskane_besede), namesto zadnjega if-stavka

#Vse afne
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@') #zbere vse besede iz vseh tvitov, ki se začnejo z '@'

#Vsi hashtagi
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#') #zbere vse besede iz vseh tvitov, ki se začnejo z '#'

#Vse osebe
def vse_osebe(tviti):
    avtorji = vsi_avtorji(tviti) #poiščemo vse avtorje
    omenjeni = vse_afne(tviti) #poiščemo vse omenjene osebe
    osebe = []
    for i in avtorji:
        if i not in osebe:
            osebe.append(i) #vse poiskane dodamo v seznam, brez ponavljanj
    for i in omenjeni:
        if i not in osebe:
            osebe.append(i)
    return sorted(osebe) #seznam uredimo po abecedi



#OBVEZNI DEL

'''def ime_avtor(tvit): #vrne ime avtorja tvita
    s = tvit.split() #razdeli tvit na besede
    avtor = s[0] #vzame prvo (avtorja)
    return avtor[:-1] #in vrne brez ':'

def slovar_avtorjev(tviti): #vrne slovar z avtorji tvitov
    slovar = {}
    for tvit in tviti:
        avtor = ime_avtor(tvit) #vzame avtorja tvita
        if avtor not in slovar: #če ga ni v slovarju
            slovar[avtor] = set() #ga doda
    return slovar'''

def besedilo(tvit): #vrne besedilo tvita brez avtorja
    s = tvit.split()
    return ' '.join(s[1:])

def zadnji_tvit(tviti): #vrne slovar avtorjev in njihovih zadnjih tvitov
    slovar = {}
    for tvit in tviti:
        s = tvit.split()
        avtor = s[0] #posebej vzamemo avtorja, da se lahko znebimo ':'
        if avtor[:1] not in slovar: #če se avtor pojavi prvič
            slovar[avtor[:-1]] = set() #ga doda v slovar
        slovar[avtor[:-1]] = ' '.join(s[1:]) #in zabeleži njegov zadnji tvit
    return slovar

def prvi_tvit(tviti): #vrne slovar avtorjev in njihovih prvih tvitov
    slovar = {}
    for tvit in tviti:
        s = tvit.split()
        avtor = s[0] #posebej vzamemo avtorja, da se lahko znebimo ':'
        if avtor[:-1] not in slovar: #če se avtor še ni pojavil
            slovar[avtor[:-1]] = ' '.join(s[1:]) #si zabeleži njegov prvi tvit
    return slovar

def prestej_tvite(tviti): #vrne slovar avtorjev in število njihovih tvitov
    slovar = {}
    for tvit in tviti:
        s = tvit.split()
        avtor = s[0]
        if avtor[:-1] not in slovar:
            slovar[avtor[:-1]] = 0 #avtorja doda v slovar
        slovar[avtor[:-1]] += 1 #in njegovemu številu tvitov prišteje 1
    return slovar

def omembe(tviti): #vrne slovar avtorjev in ljudi, ki jih omenijo
    slovar = {}
    for tvit in tviti:
        s = tvit.split()
        avtor = s[0]
        if avtor[:-1] not in slovar: #napolne slovar z avtorji
            slovar[avtor[:-1]] = []
        for beseda in s: #gre čez vse besede v tvitu
            if beseda.startswith('@'): #če se beseda začne z '@'
                slovar[avtor[:-1]].append(izloci_besedo(beseda)) #jo doda brez '@'
    return slovar

def neomembe(ime, omembe): #vrne seznam oseb, ki jih 'ime' ni omenil, a so med avtorji
    neomenjeni = []
    omenjeni = omembe[ime] #seznam ljudi, ki jih je omenil 'ime'
    for avtor in omembe: #gre čez vse avtorje
        if avtor not in omenjeni and avtor != ime: #tiste, ki niso omenjeni
            #if avtor != ime: #brez samega sebe
                neomenjeni.append(avtor) #doda seznamu
    return neomenjeni



#DODATNI DEL

def se_poznata(ime1, ime2, omembe): #vrne True, če sta se 'ime1' in 'ime2' kdaj omenila
    for avtor in omembe: #v slovarju pogleda
        if avtor == ime1 and ime2 in omembe[ime1]: #če avtor 'ime1' med omembami vsebuje 'ime2'
            return True
        if avtor == ime2 and ime1 in omembe[ime2]: #ali če 'ime2' vsebuje 'ime1'
            return True
    return False #drugače vrne False

def hashtagi(tviti): #vrne slovar hastagov in imen avtorjev, ki so jih uporabili
    slovar = {}
    for i in tviti: #vsak tvit posebej
        tvit = i.split() #razdeli tvit na besede
        for beseda in tvit:
            if beseda.startswith("#"): #če je avtor uporabil '#'
                hash = izloci_besedo(beseda) #odstrani ne-črke (dobi ključ slovarja)
                if hash not in slovar: #če ključa še ni
                    slovar[hash] = [] #ga doda
                slovar[hash].append(tvit[0][:-1]) #ključu doda avtorja
                slovar[hash].sort() #in avtorje uredi po abecedi
    return slovar


#TESTI (ne spreminjaj)
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


