import unittest

def tegi(tvit):
    omenjene_osebe = []
    locen_tvit = tvit.split(" ")
    for beseda in locen_tvit:
        if '@' in beseda:
            ociscena_beseda = izloci_besedo(beseda)
            omenjene_osebe.append(ociscena_beseda)
    return omenjene_osebe


def unikati(s):
    vsi_unikati= []
    for x in s:
        if x not in vsi_unikati:
            vsi_unikati.append(x)
    return vsi_unikati

def avtor(tvit):
    name = tvit.split(":")
    ime = name[0]
    return ime

def vsi_avtorji(tviti):
    avtorji = []
    for tvit in tviti:
        name = tvit.split(":")
        ime = name[0]
        if ime not in avtorji:
            avtorji.append(ime)
    return avtorji

def izloci_besedo(beseda):
   cnt1 = 0
   cnt2 = 0
   dolzina = len(beseda)
   for i in range (0, dolzina):
               if beseda[i].isalnum() == True:
                   break
               if beseda[i].isalnum() == False:
                   cnt1 += 1
   obrnejana_beseda = beseda[::-1]
   for j in range (0, dolzina):
        if obrnejana_beseda[j].isalnum() == True:
            break
        if obrnejana_beseda[j].isalnum() == False:
            cnt2 += 1
   x = dolzina - cnt2
   return beseda[cnt1:x]



def se_zacne_z(tvit,c):
    yx = []
    tvit1 = tvit.split(" ")
    for beseda in tvit1:
        if c in beseda:
            tegi = beseda.replace(c, "")
            tegi2 = izloci_besedo(tegi)
            yx.append(tegi2)
    return yx

def zberi_se_zacne_z(tviti,c):
    izlocene_besede = []
    for tvit in tviti:
        besede = se_zacne_z(tvit,c)
        izlocene_besede += besede
    vse_besede_enkrat = unikati(izlocene_besede)
    return vse_besede_enkrat

def vse_afne(tviti):
    imena = []
    for tvit in tviti:
        besede = tvit.split(" ")
        for beseda in besede:
            if '@' in beseda:
                ociscena_beseda = izloci_besedo(beseda)
                imena.append(ociscena_beseda)
    izbrana_imena = unikati(imena)


    return izbrana_imena


def vsi_hashtagi(tviti):
    hastag = zberi_se_zacne_z(tviti, "#")
    return hastag

def vse_osebe(tviti):
        avtorji = vsi_avtorji(tviti)
        omenjeni = vse_afne(tviti)
        osebe = avtorji + omenjeni
        izlocena_imena = unikati(osebe)
        razrvsena = sorted(izlocena_imena)
        return razrvsena



def custva(tviti, hastagi):
    osebe=[]
    for hastag in hastagi:
        for tvit in tviti:
            for beseda in tvit.split(" "):
                if hastag in beseda:
                    avtor2 = avtor(tvit)
                    osebe.append(avtor2)
    urejeni = unikati(osebe)

    return sorted(urejeni)



def se_poznata (tviti,oseba1,oseba2):
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        if avtor_tvita == oseba1:
            omenjeni = tegi(tvit)
            if oseba2 in omenjeni:
                return True
        if avtor_tvita == oseba2:
            omenjeni2 = tegi(tvit)
            if oseba1 in omenjeni2:
                return True
    return False









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

