def unikati(s):
    t = []
    for i in s:
        if i not in t:
            t.append(i)
    return t

def avtor(tvit):
    a = tvit.split(": ")
    return a[0]

def vsi_avtorji(tviti):
    t = []
    a = [i.split(': ')[0] for i in tviti]
    for name in a:
        if name not in t:
            t.append(name)
    return t

def izloci_besedo(beseda):
    s = 0
    z = 1
    y = ""
    x = ""
    g = ""
    for b in beseda:
        if b.isalnum() == False:
            s += 1
        elif b.isalnum() == True:
            break
    y += beseda[s:]
    for d in y[::-1]:
        if d.isalnum() == False:
            z += 1
        elif d.isalnum() == True:
            break
    x += beseda[:-z]
    for i in y:
        if i in x:
            g += i
    return g

def se_zacne_z(tvit, c):
    n = []
    a = tvit.split(" ")
    while (True):
        for i in a:
            if i.isalnum() == False and i[0][:1] == c:
                n.append(i[1:])
        for d in n:
            if d.isalnum() == False:
                n.append(d[:-1])
                n.remove(d)
                n.sort()
        return n

def zberi_se_zacne_z(tviti, c):
    n = []
    s = []
    a = [i.split(' ') for i in tviti]
    for e in a:
        for d in e:
            if d[0] == c:
                n.append(d[1:])
            for k in n:
                if k.isalnum() == False:
                    n.append(k[:-1])
                    n.remove(k)
    for i in n:
        if i not in s:
            s.append(i)
    return s

def vse_afne(tviti):
    n = []
    s = []
    a = [i.split(" ") for i in tviti]
    while (True):
        for tvit in a:
            for e in tvit:
                if e[0] == "@":
                    n.append(e[1:])
                for d in n:
                    if d.isalnum() == False:
                        n.append(d[:-1])
                        n.remove(d)
        for i in n:
            if i not in s:
                s.append(i)

        break
    return s

def vsi_hashtagi(tviti):
    a = [i.split(" ") for i in tviti]
    n = []
    s = []
    while (True):
        for tvit in a:
            for e in tvit:
                if e[0] == "#":
                    n.append(e[1:])
            for d in n:
                if d.isalnum() == False:
                    n.append(d[:-1])
                    n.remove(d)
        for i in n:
            if i not in s:
                s.append(i)
        break
    return s

def vse_osebe(tviti):
    a = vse_afne(tviti)
    b = vsi_avtorji(tviti)
    return sorted(unikati(a+b))

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
        self.assertEqual(izloci_besedo("ana?"), "ana")
        self.assertEqual(izloci_besedo("!#$%\"=%/%()/Ben-jamin'"), "Ben-jamin")
        self.assertEqual(izloci_besedo("@ana"), "ana")

        self.assertEqual(izloci_besedo("@@ana!!!"), "ana")



    def test_vse_na_crko(self):
        self.assertEqual(se_zacne_z("ana: kdo so te @berta, @cilka, @dani? #krneki", "@"), ["berta", "cilka", "dani"])
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! Visoko!", "$"), ["je", "skocil"])
        self.assertEqual(se_zacne_z("Benjamin $je $skocil! #Visoko!", "$"), ["je", "skocil"])


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

