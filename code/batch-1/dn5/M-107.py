import unittest

def unikati(s):
    new_s=[]
    for i in s:
        if i not in new_s:
            new_s.append(i)
    return new_s

def avtor(tvit):
    new_tvit=[]
    for crka in tvit:
        if(crka==':'):
            return ''.join(new_tvit)
        new_tvit.append(crka)

def vsi_avtorji(tviti):
    avtorji=[]
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    avtorji=unikati(avtorji)
    return avtorji

def izloci_besedo(beseda):
    new_beseda=[]
    prejsna_crka=""
    for crka in beseda:
        if(crka.isalnum()):
            prejsna_crka=crka
            new_beseda.append(crka)
        else:
            if(prejsna_crka.isalnum() and crka=='-'):
                new_beseda.append(crka)
                prejsna_crka=""
    return "".join(new_beseda)

def se_zacne_z(tvit, c):
    tvit_array=tvit.split()
    besede_array=[]
    for beseda in tvit_array:
        if(beseda[:1]==c):
            beseda=izloci_besedo(beseda)
            besede_array.append(beseda)
    return besede_array

def zberi_se_zacne_z(tviti, c):
    besede=[]
    array_besede=[]
    for tvit in tviti:
        besede.append(se_zacne_z(tvit, c))
    for beseda in besede:
        if(isinstance(beseda, list)):
            for beseda2 in beseda:
                array_besede.append(beseda2)
        else:
            array_besede.append(beseda)
    array_besede=unikati(array_besede)
    return array_besede

def vse_afne(tviti):
    besede = zberi_se_zacne_z(tviti, '@')
    return besede

def vsi_hashtagi(tviti):
    besede = zberi_se_zacne_z(tviti, '#')
    return besede
def vse_osebe(tviti):
    osebe1=vse_afne(tviti) #vse v tvitih
    osebe2=vsi_avtorji(tviti) #vsi avtorji
    osebe=osebe1+osebe2 #skupaj
    osebe=unikati(osebe) #unikat (ne podvaja)
    osebe.sort() #sortira
    return osebe
#---------------------- DODATNA NALOGA ------------------------#

def custva(tviti, hashtagi):
    avtorji=[]
    for tvit in tviti:
        avtor_tvita=avtor(tvit)
        hastagi_avtorja=se_zacne_z(tvit, '#')
        for hastag in hashtagi:
            if(hastag in hastagi_avtorja):
                avtorji.append(avtor_tvita)
    avtorji = unikati(avtorji)
    avtorji.sort()
    return avtorji
def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        avtor_tvita=avtor(tvit)
        if(avtor_tvita==oseba1):
            osebe_tvita=se_zacne_z(tvit, '@')
            if(oseba2 in osebe_tvita):
                return True
        if(avtor_tvita==oseba2):
            osebe_tvita = se_zacne_z(tvit, '@')
            if (oseba1 in osebe_tvita):
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

