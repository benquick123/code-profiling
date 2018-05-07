import unittest
def unikati(s): #deklariramo funkcijo
    seznam=[] #prazen seznam za izpis
    for element in s: #zanka za pomik po seznamu
        if element not in seznam: #preverimo če smo že vrnili element
            seznam.append(element) #pripnemo element v seznam
    return seznam #funkcija vrne nov seznam

def avtor(tvit): #deklariramo funkcijo
    dvopicje=tvit.find(":") #najdemo dvopicje, saj je avtor podan pred dvopicjem
    return tvit[:dvopicje] #izpisemo kar je pred dvopicjem

def vsi_avtorji(tviti): #deklariramo funkcijo
    seznam=[] #prazen seznam za izpis imen
    for imeavtorja in tviti: #zanka za premik po seznamu tviti
        seznam.append(avtor(imeavtorja)) #pripnemo element v seznam
        unikatniseznam = unikati(seznam)#pokličemo še prvo funkcijo da dobimmo unikatna imena
    return unikatniseznam #izpišemo imena avtorjev

def izloci_besedo(beseda): #deklaracija funkcije
    for x in beseda: #premikanje po seznamu
        if x.isalnum(): #uporaba funkcije isalnum()
            a=beseda.find(x) #shrani se v a
            break #izhod iz if stavka
    beseda=beseda[::-1] #beseda je zadnji znak
    for x in beseda: #zanka za pomik po seznamu
        if x.isalnum(): #ponovna uporaba isalnum
            b=beseda.find(x)
            break #izhod iz if stavka
    beseda=beseda[::-1] #deklaracija zadnjega elementa
    konec= beseda[a:(len(beseda)-b)]
    return konec

def se_zacne_z(tvit, c): #deklaracija funkcije
    a=tvit.split() #razdelitev elementa
    seznam=[] #prazen seznam
    for x in a: #zanka za premik po terki
        if x[0]==c:#preveri če je element enak c
            seznam.append(izloci_besedo(x)) #pripnitev elementa v seznam (pripne elemnt katerega vrne funkcija izloči besedo)
    return seznam #izpis

def zberi_se_zacne_z(tviti, c): #deklaracija funkcije
    seznam=[]#prazen seznam
    for x in tviti:
        seznam+=se_zacne_z(x,c) #klic prejsnje funkcije v spremenljivko, ki se poveca za vrednost funkcije
    izpis=unikati(seznam) #klic prejsnje formule
    return izpis #izpis

def vse_afne(tviti): #deklaracija funkcija
    afne=zberi_se_zacne_z(tviti,"@") #klic prejšnje funkcije
    return afne # izpis

def vsi_hashtagi(tviti): #deklaracija funkcije
    hastagi=zberi_se_zacne_z(tviti, "#") #klic funkcije
    return hastagi  #izpis

def vse_osebe(tviti):
    osebe= sorted(unikati(vsi_avtorji(tviti)+zberi_se_zacne_z(tviti,"@"))) #sorted je funkcija za urejanje
    #hkrati združenje v osebe == funkcija vsi_avtorji, + funkcija zberi_se_zacne
    return osebe #izpis

class TestTviti(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]

    def test_unikat(self):
        self.assertEqual(unikati([1, 2, 1, 1, 3, 2]), [1, 2, 3])
        self.assertEqual(unikati([1, 3, 2, 1, 1, 3, 2]), [1, 3, 2])
        self.assertEqual(unikati([1, 5, 4, 3, 2]), [1, 5, 4, 3, 2])
        self.assertEqual(unikati([1, 1, 1, 1, 1]), [1])
        self.assertEqual(unikati([1]), [1])
        self.assertEqual(unikati([]), [])
        self.assertEqual(unikati(["Ana", "Berta", "Cilka", "Berta"]), ["Ana", "Berta", "Cilka"])

    def test_avtor(self):
        self.assertEqual(avtor("janez: pred dvopičjem avtor, potem besedilo"), "janez")
        self.assertEqual(avtor("ana: malo krajse ime"), "ana")
        self.assertEqual(avtor("benjamin: pomembne so tri stvari: prva, druga in tretja"), "benjamin")

    def test_vsi_avtorji(self):
        self.assertEqual(vsi_avtorji(self.tviti), ["sandra", "berta", "ana", "cilka", "benjamin", "ema"])
        self.assertEqual(vsi_avtorji(self.tviti[:3]), ["sandra", "berta"])

    def test_izloci_besedo(self):
        self.assertEqual(izloci_besedo("@ana"), "ana")
        self.assertEqual(izloci_besedo("@@ana!!!"), "ana")
        self.assertEqual(izloci_besedo("ana"), "ana")
        self.assertEqual(izloci_besedo("!#$%\"=%/%()/Ben-jamin'"), "Ben-jamin")

    def test_vse_na_crko(self):
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! #Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("ana: kdo so te @berta, @cilka, @dani? #krneki", "@"), ["berta", "cilka", "dani"])

    def test_zberi_na_crko(self):
        self.assertEqual(zberi_se_zacne_z(self.tviti, "@"), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])
        self.assertEqual(zberi_se_zacne_z(self.tviti, "#"), ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_vse_afne(self):
        self.assertEqual(vse_afne(self.tviti), ['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana'])

    def test_vsi_hashtagi(self):
        self.assertEqual(vsi_hashtagi(self.tviti), ['dougcajt', 'programiranje1', 'krneki', 'luft', 'zalosten', 'split'])

    def test_vse_osebe(self):
        self.assertEqual(vse_osebe(self.tviti), ['ana', 'benjamin', 'berta', 'cilka', 'dani', 'ema', 'sandra'])


class TestDodatna(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]

    def test_custva(self):
        self.assertEqual(custva(self.tviti, ["dougcajt", "krneki"]), ["ana", "sandra"])
        self.assertEqual(custva(self.tviti, ["luft"]), ["cilka"])
        self.assertEqual(custva(self.tviti, ["meh"]), [])

    def test_se_poznata(self):
        self.assertTrue(se_poznata(self.tviti, "ana", "berta"))
        self.assertTrue(se_poznata(self.tviti, "ema", "ana"))
        self.assertFalse(se_poznata(self.tviti, "sandra", "ana"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "luft"))
        self.assertFalse(se_poznata(self.tviti, "cilka", "balon"))


if __name__ == "__main__":
    unittest.main()

