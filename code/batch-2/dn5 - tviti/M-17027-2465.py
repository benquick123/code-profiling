def unikati(s):
    t=[]
    for a in s:
        if a not in t:
            t.append(a)
    #print(t)
    return t

def avtor(tvit):
    a = tvit.split(":")
    b = a[0]
    return b

def vsi_avtorji(tviti):
    a=[]
    for n in tviti:
        a.append(avtor(n))
    a = unikati(a)
    return(a)

def izloci_besedo(beseda):
    t = beseda
    t = klic(t)
    t = t[::-1]
    t = klic(t)
    t = t[::-1]
    return t

def klic(t):
    for a in t:
        if a.isalnum() == False:
            t = t.replace(a, "")
        else:
            break
    return t

def se_zacne_z(tvit, c):
    k = tvit.split(" ")
    b=[]
    for a in k:
        #print(a)
        if c in a:
            b.append(izloci_besedo(a))
           # print(b)
    return b

def zberi_se_zacne_z(tviti, c):
    b = []
    for a in tviti:
        #print(a)
        if c in a:
            #print(a)
            b.extend(se_zacne_z(a, c))
           # print(b)
    b = unikati(b)
    #print(b)
    return b

def vse_afne(tviti):
    b = []
    for a in tviti:
        b.extend(se_zacne_z(a, "@"))
    b = unikati(b)
    return b

def vsi_hashtagi(tviti):
    b = []
    for a in tviti:
        b.extend(se_zacne_z(a, "#"))
    b = unikati(b)
    #print(b)
    return b

def vse_osebe(tviti):
     a = vsi_avtorji(tviti)
     a.extend(vse_afne(tviti))
     a = unikati(a)
     a.sort()
     return a

def custva(tviti, hashtagi):
    k  =[]
    for a in hashtagi:
        for b in tviti:
            if a in b:
                k.append(avtor(b))
    k = unikati(k)
    k.sort()
    return k

def se_poznata(tviti, oseba1, oseba2):
    for a in tviti:
        if avtor(a) == oseba1:
            if oseba2 in a and oseba2 in vse_osebe(tviti):
                k = avtor(a)
                print(oseba2, oseba1)
                return True
            else:
                return False











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

