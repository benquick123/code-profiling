import unittest

##########Obvezna naloga#########
def unikati(s):
    s_unikati=[]
    for e in s:
        if e not in s_unikati:
            s_unikati.append(e)
    return s_unikati

def avtor(tvit):
    ime=tvit[0:tvit.find(":")]
    return ime

def vsi_avtorji(tviti):
    imena=[]
    for tvit in tviti:
        if avtor(tvit) not in imena:
            imena.append(avtor(tvit))
    return imena

def izloci_besedo(beseda):
    for e in beseda:
        if e.isalnum()==False:
            beseda=beseda.lstrip(e[0])
    for i in beseda[::-1]:
        if i.isalnum()==False:
            beseda = beseda.rstrip(i[-1])
    return beseda

def se_zacne_z(tvit, c):
    vsi=[]
    for beseda in tvit.split():
        for e in beseda:
            if e==c:
                najdena_beseda=izloci_besedo(beseda)
                vsi.append(najdena_beseda)
    return vsi

def zberi_se_zacne_z(tviti, c):
    ponovitve=[]
    for tvit in tviti:
        for beseda in tvit.split():
            for e in beseda:
                if e == c:
                    najdena_beseda = izloci_besedo(beseda)
                    if najdena_beseda not in ponovitve:
                        ponovitve.append(najdena_beseda)
    return ponovitve

def vse_afne(tviti):
    afne=zberi_se_zacne_z(tviti,"@")
    return afne

def vsi_hashtagi(tviti):
    hashtagi=zberi_se_zacne_z(tviti,"#")
    return hashtagi

def vse_osebe(tviti):
    osebe=[]
    for avtor in vsi_avtorji(tviti):
        osebe.append(avtor)
    for ime in vse_afne(tviti):
        if ime not in osebe:
            osebe.append(ime)
    osebe.sort()
    return osebe

################Dodatna naloga###############

def custva(tviti, hashtagi):
    avtorji=[]
    for hash in hashtagi:
        for tvit in tviti:
            for beseda in tvit.split():
                if hash==izloci_besedo(beseda):
                    ime=avtor(tvit)
                    if ime not in avtorji:
                        avtorji.append(ime)

    avtorji.sort()
    return avtorji


def se_poznata(tviti, oseba1, oseba2):
    s = []
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            for beseda in tvit.split():
                if izloci_besedo(beseda) == oseba2 and (izloci_besedo(beseda) in vse_afne(tviti)):
                    s.append(beseda)
        if avtor(tvit) == oseba2:
            for beseda in tvit.split():
                if izloci_besedo(beseda) == oseba1 and (izloci_besedo(beseda) in vse_afne(tviti)):
                    s.append(beseda)
    return bool(s)


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

