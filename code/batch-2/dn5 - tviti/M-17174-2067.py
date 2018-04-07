def unikati(s):
    c=[]
    for x in s:
        x=str(x)
        x=x.split()
        x=x[0]
        if len(x)<2:
            x = int(x)
        if x not in c:
            c.append(x)
    return c

def avtor(tvit):
    x = tvit.split()
    x = x[0]
    return x[:-1]

def vsi_avtorji(tviti):
    c = []
    for x in tviti:
        x = x.split()
        x = x[0]
        x = x[:-1]
        if x not in c:
            c.append(x)
    return c

def izloci_besedo(beseda):
    for x in beseda:
        if ord(x) >= 48 and ord(x) <= 57 or \
            ord(x) >= 65 and ord(x) <= 90 or \
            ord(x) >= 97 and ord(x) <= 122:
            break
        else:
            beseda = beseda[1:]

    for x in range(len(beseda)-1,0, -1):
        if ord(beseda[x]) >= 48 and ord(beseda[x]) <= 57 or \
                                ord(beseda[x]) >= 65 and ord(beseda[x]) <= 90 or \
                                ord(beseda[x]) >= 97 and ord(beseda[x]) <= 122:
            break
        else:
            beseda = beseda[:-1]

    return beseda

def se_zacne_z(tvit, c):
    t=[]
    tvit=tvit.split()
    for x in tvit:
        if x[0]==c:
            t+=(izloci_besedo(x),)
    return t

def zberi_se_zacne_z(tviti, c):
    t=[]
    for x in tviti:
        f=se_zacne_z(x,c)
        for s in f:
            if s not in t:
                t+=(s,)
    return t

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return (zberi_se_zacne_z(tviti, "#"))

def vse_osebe(tviti):
    o=[]
    for x in tviti:
        for y in range(0,len(x)):
            if x[y]==":":
                if x[:y] not in o:
                    o.append(x[:y])
    x=vse_afne(tviti)
    for z in x:
        if z not in o:
           o.append(z)

    o=sorted(o)
    return o

def custva(tviti, hashtagi):
    o=[]
    for x in tviti:
        for z in hashtagi:
            if "#"+z in x:
                for y in range(0, len(x)):
                    if x[y] == ":":
                        if x[:y] not in o:
                            o.append(x[:y])
    o = sorted(o)
    return o

def se_poznata(tviti, oseba1, oseba2):
    for x in tviti:
        if "#"+oseba1 not in x and "#"+oseba2 not in x:
            if oseba1 in x and oseba2 in x:
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

