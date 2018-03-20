import unittest

def unikati(a):
    b =[]
    for i in a:
        if i not in b:
            b.append(i)
    return b

def avtor(tvit):
    ime = ""
    i=0
    while tvit[i] != ":":
        ime += tvit[i]
        i+=1
    return ime

def vsi_avtorji(tviti):
    avtorji = []
    cistovsiavtorji =[]
    for tvit in tviti:
        a = avtor(tvit)
        cistovsiavtorji.append(a)
        for a in cistovsiavtorji:
            if avtorji.count(a)<1:
                avtorji.append(a)
    return avtorji

def izloci_besedo(beseda):
    for beseda_n in beseda:
        if beseda_n.isalnum():
            break
        else:
            beseda = beseda.lstrip(beseda_n[0])
    for beseda_n in beseda[::-1]:
        if beseda_n.isalnum():
            break
        else:
            beseda = beseda.rstrip(beseda_n[-1])
    return beseda

def se_zacne_z(tvit, c):
    besede_a =[]
    tvit = tvit.split()
    for a in tvit:
        for b in a:
            if b ==c:
                beseda =izloci_besedo(a)
                besede_a.append(beseda)
    return  besede_a

def zberi_se_zacne_z(tviti,c):
    besede_b =[]
    besede_c = []
    for tvit in tviti:
        tvit = tvit.split()
        for beseda in tvit:
            for b in beseda:
                if b == c:
                  beseda =izloci_besedo(beseda)
                  besede_b.append(beseda)
                  besede_c = unikati(besede_b)
    return besede_c


def vse_afne(tviti):
    a = []
    for e in tviti:
        beseda = se_zacne_z(e, "@")
        for e in beseda:
            a.append(e)
            a = unikati(a)
    return a


def vsi_hashtagi(tviti):
    h = []
    for e in tviti:
        beseda = se_zacne_z(e, "#")
        for e in beseda:
            h.append(e)
            h = unikati(h)
    return h

def vse_osebe(tviti):
    a = vse_afne(tviti)
    b = vsi_avtorji(tviti)
    c = a + b
    d = []
    for tvit in tviti:
        tvit = tvit.split()
        for e in c:
            if e not in d:
                d.append(e)
    return sorted(d)


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

