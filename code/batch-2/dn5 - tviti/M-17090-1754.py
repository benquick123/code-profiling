#OBVEZNI DEL

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


#DODATNI DEL

#Čustva (osebe, ki so uporabile določen '#')
def custva(tviti, hashtagi):
    osebe = []
    for tvit in tviti:
        for i in se_zacne_z(tvit, '#'): #poišče vse besede, ki se začnejo z '#'
            if i in hashtagi: #če so to iskane besede
                osebe.append(avtor(tvit)) #si zapomni avtorja
    return sorted(unikati(osebe)) #seznam uredi in izloči duplikate

#Se poznata
def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if oseba1 == avtor(tvit) or oseba2 == avtor(tvit): #če je ena od oseb avtor
            if oseba2 in se_zacne_z(tvit, '@') or oseba1 in se_zacne_z(tvit, '@'): #in omeni drugo osebo
                return True #potem se poznata
    return False


#TESTI (ne spreminjaj)

import unittest


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

