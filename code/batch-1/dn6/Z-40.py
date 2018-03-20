
#OBVEZNI DEL:

#1.Funkcija besedilo(tvit) prejme tvit in vrne besedilo - torej vse,
#  kar sledi prvemu dvopičju. Klic besedilo("ana: kdo so te: @berta, @cilka, @dani?")
# vrne "kdo so te: @berta, @cilka, @dani?.
import collections


def besedilo(tvit):
    loceno=tvit.split(": ")
    velikost_prvega_elementa=len(loceno[0])
    dolzina=velikost_prvega_elementa+2
    return tvit[dolzina:]
print(besedilo("ana: kdo so te: @berta, @cilka, @dani?"))
#2.Funkcija zadnji_tvit(tviti) prejme seznam tvitov in vrne slovar,
# katerega ključi so avtorji tvitov,
# vrednosti pa njihovi tviti.
# Če je en in isti avtor napisal več tvitov,
# naj bo v slovarju njegov zadnji tvit.
#  Rezultat je lahko, recimo
def avtor(tvit):
    avtor=tvit.split(":")
    return avtor[0]
def zadnji_tvit(tviti):
    novi_slovar={ }
    for tvit in tviti:
        ime_avtorja=avtor(tvit)
        besedilo_tvita=besedilo(tvit)
        #if ime_avtorja not in novi_slovar:
        novi_slovar[ime_avtorja]=besedilo_tvita #DOODAJANJE V SLOVAR, IME SLOVARJA[KLJUČ SLOVARJA]=VREDNOSTI SLOVARJA

    return novi_slovar

#3Funkcija prvi_tvit(tviti) je jako podobna,
#  le da v primeru, da je ista oseba napisala več tvitov,
#  obdrži njen prvi tvit.
def prvi_tvit(tviti):
    novi_slovar={ }
    for tvit in tviti:
        ime_avtorja=avtor(tvit)
        besedilo_tvita=besedilo(tvit)
        if ime_avtorja not in novi_slovar:
            novi_slovar[ime_avtorja]=besedilo_tvita
    return novi_slovar

#4Funkcija prestej_tvite(tviti) vrne slovar,
# katerega ključi so (spet) avtorji,
# pripadajoče vrednosti pa število tvitov,
# ki so jih napisali, na primer



def prestej_tvite(tviti): #v teh tviti, je seznam tvitov
    seznam_avtorjev=[]
    for tvit in tviti:
        ime_avtorja=avtor(tvit)
        seznam_avtorjev.append(ime_avtorja)
    število_avtorjev=collections.Counter(seznam_avtorjev)
    return število_avtorjev

#5Funkcija omembe(tviti) vrne slovar,
# katerega ključi so avtorji tvitov,
#  vrednosti pa seznami oseb,
# ki so jih ti avtorji omenjali v svojih tvitih.
# Vrstni red oseb mora biti enak vrstnemu redu omenjanj.
#  Funkcija lahko vrne, recimo

def unikati(s):
    novi_seznam=[]
    for podatki in s:
        if podatki not in novi_seznam:
            novi_seznam.append(podatki)
    return novi_seznam


def vsi_avtorji(tviti):
    novi_seznam_ko_samo_imena=[]
    for podatki in tviti: #za podatek dobim posamezni tvit
        ime_avtorja=avtor(podatki) #ker v podatkih shranjenj posamezni tvit
        #if ime_avtorja not in novi_seznam_ko_samo_imena:
        novi_seznam_ko_samo_imena.append(ime_avtorja)
    novi_seznam_ko_samo_imena=unikati(novi_seznam_ko_samo_imena)
    return novi_seznam_ko_samo_imena


def izloci_besedo(beseda):
    for i in range(0,len(beseda)):
        znak=beseda[i]
        if not znak.isalnum():
            beseda=beseda[:i]+ " "+ beseda[i+1:]
        else:
            break


    for i in range(len(beseda)-1, 0, -1): #prva -1, je da dobimo zadnji indeks, drugi -1 pa je negativni korak
        znak=beseda[i]
        if not znak.isalnum():
             beseda= beseda[:i]+ " "+ beseda[i+1:]
        else:
            break

    return beseda.strip()

def se_zacne_z(tvit, c):
    seznam_besed=tvit.split(" ") #dobimo seznam razdeljen po besedah
    seznam_besed_z_c=[]
    for beseda in seznam_besed:
        if beseda[0]==c:
            samo_alfanumerične=izloci_besedo(beseda)
            seznam_besed_z_c.append(samo_alfanumerične)

    return seznam_besed_z_c


def zberi_se_zacne_z(tviti, c):
    novi_seznam_besed_ki_jih_iscemo=[]
    for tvit in tviti:
        za_besede_ki_zacnejo_z_c=se_zacne_z(tvit,c)
        novi_seznam_besed_ki_jih_iscemo=novi_seznam_besed_ki_jih_iscemo+za_besede_ki_zacnejo_z_c

    nepodvojene_besede=unikati(novi_seznam_besed_ki_jih_iscemo)
    return nepodvojene_besede



def vse_afne(tviti):
    afne=zberi_se_zacne_z(tviti,"@")

    return afne

def omembe(tviti):
    novi_slovar={}
    for tvit in tviti:
        avtor_tvita=avtor(tvit)
        za_besede_ki_zacnejo_z_c = se_zacne_z(tvit, "@")
        if avtor_tvita not in novi_slovar:
            novi_slovar[avtor_tvita] = []
        novi_slovar[avtor_tvita]=novi_slovar[avtor_tvita]+za_besede_ki_zacnejo_z_c

    return novi_slovar

#6Funkcija neomembe(ime, omembe) prejme ime neke osebe in takšen slovar,
#  kakršnega vrne gornja funkcija.
# Vrniti mora seznam vseh ljudi, ki so avtorji kakega tvita,
# podana oseba (ime) pa jih ni omenjala.
# Če funkciji kot argument podamo ime "Ana" in gornji slovar,
#  mora vrniti ["sandra", "benjamin], saj Ana ni omenjala Sandre in Benjamina,
#  Cilko in Berto pa je. Iz seznama naj bo seveda izključena oseba
# sama (v tem primeru Ana). Vrstni red oseb v seznamu je lahko poljuben.
def neomembe(ime, omembe):
    seznam_avtorjev=[]
    for ime_avtorja in omembe:#OMEMBE JE SLOVAR IZ PREJŠNE FUNKCIJE OMEMBE
        seznam_avtorjev.append(ime_avtorja) #če je samo en za en za dodoat damo append
    omembe_ime_avtorja=omembe[ime]
    zdruzeno=omembe_ime_avtorja+[ime]
    množica_neomemb=set(seznam_avtorjev)-set(zdruzeno)
    return list(množica_neomemb)

def se_poznata(ime1, ime2, omembe):
    if ime1 in omembe and ime2 in omembe[ime1]:
        return True
    if ime2 in omembe and ime1 in omembe[ime2]:
        return True

    return False


def hashtagi(tviti):
    novi_slovar = {}
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        za_besede_ki_zacnejo_z_c = se_zacne_z(tvit, "#")
        for hash in za_besede_ki_zacnejo_z_c:
            if hash not in novi_slovar:
                novi_slovar[hash] = []
            novi_slovar[hash].append(avtor_tvita)
        novi_slovar[hash].sort()
    return novi_slovar


























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



