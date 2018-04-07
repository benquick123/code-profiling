def unikati(s):

    a = []
    for i in s:
        if i in a:
            pass
        else:
            a.append (i)
    return a

def avtor(tvit):

    b = tvit.split()
    for i in b:
        if i.find(":") > 0:
            i = i.replace(":","")
            return i

def vsi_avtorji(tviti):
    a = []
    for i in tviti:
        b = avtor(i)
        a.append(b)
    c = unikati(a)
    return c

def izloci_besedo(beseda):
    #beseda = "!#$%\"=%/%()/Ben-jamin'"
    b = 0
    while beseda[b].isalnum() == False:
        a = beseda.replace(beseda[b],"")
        beseda = a

    besedilo = beseda[::-1]
    while besedilo[b].isalnum() == False:
        besedilo = besedilo.replace(besedilo[b],"")

    c = besedilo[::-1]
    return c

def se_zacne_z(tvit, c):
    a = []
    tvit = tvit.split()
    for i in tvit:
        for x in i:
            if x == c:
                i = i.replace(c, "")
                i = izloci_besedo(i)
                a.append(i)
    return a

def zberi_se_zacne_z(tviti, c):
    a = []

    for i in tviti:
        i = i.split()
        for x in i:
            if c in x:
                d = x.replace(c, "")
                d = izloci_besedo(d)
                if d in a:
                    pass
                else:
                    a.append(d)
    return a

def vse_afne(tviti):
    b = zberi_se_zacne_z(tviti,"@")
    return b

def vsi_hashtagi(tviti):
     a = zberi_se_zacne_z(tviti,"@" and "#")
     return a

def vse_osebe(tviti):
    a = []

    b = vsi_avtorji(tviti)
    if b not in a:
        a.extend(b)

    c = vse_afne(tviti)
    for i in c:
        if i in a:
            pass
        else:
            a.append(i)

    a.sort()
    print(a)
    return a

def custva(tviti, hashtagi):
    a = []
    for i in tviti:
        for e in hashtagi:
            if e in i:
                if i.find(e) > 0:
                    h = i.replace(":", "")
                    c = h.split()
                    if c[0] not in a:
                        a.append(c[0])
    a.sort()
    return a

def se_poznata(tviti, oseba1, oseba2):
    b = []
    f = "@"
    for i in tviti:
        i  = i.split()
        for a in i:

            if a.find(":") > 0:
                a = a.replace(":", "")
                b.append(a)

            if "@" in a:
                a = a.replace(f, "")
                b.append(a)
            if "," in a:
                a = a.replace(",", "")
                b.append(a)
            if oseba1 in b:
                print(b, "true")
                if oseba2 in b:
                    print (b, "lul")
                    return True

        del b[:]
    return False


#-------------------------------------------------------------

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

