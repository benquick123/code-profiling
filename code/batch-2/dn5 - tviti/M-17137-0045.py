def unikati(s):
    seznam = []
    for i in s:
        if i in seznam:
            continue
        else:
            seznam.append(i)
    return seznam

def avtor(tvit):
    a = tvit.split()
    b = a[0]
    c = b[:-1]
    return c

def vsi_avtorji(tviti):
    s = []
    for i in tviti:
        a = avtor(i)
        if a not in s:
            s.append(a)
    return s

def izloci_besedo(beseda):
    for i in range(len(beseda) - 1):
        if beseda[i].isalnum():
            break

    for j in range(len(beseda)-1,0,-1):
        if beseda[j].isalnum():
            break
    beseda = beseda[i:j + 1]
    return beseda

def se_zacne_z(tvit, c):
    s = []
    a = tvit.split()
    beseda = ""
    for bes in a:
        if c in bes:
            for crka in bes:
                if crka.isalnum() == False:
                    continue
                else:
                    beseda = beseda + crka
            s.append(beseda)
            beseda = ""
        else:
            continue
    return s

def zberi_se_zacne_z(tviti, c):
    s = []
    for tvit in tviti:
        for beseda in tvit:
            a = se_zacne_z(tvit, c)
            for b in a:
                if b not in s and b!=[]:
                    s.append(b)

    return s

def vse_afne(tviti):
    s = []
    a = zberi_se_zacne_z(tviti, "@")
    b = vsi_avtorji(tviti)
    for i in a:
        for j in b:
            if j not in a:
                s.append(j)

    return a

def vsi_hashtagi(tviti):
    a = zberi_se_zacne_z(tviti, "#")
    return a

def vse_osebe(tviti):
    a = zberi_se_zacne_z(tviti, "@")
    b = vsi_avtorji(tviti)

    for i in a:
        for j in b:
            if j not in a:
                a.append(j)
    a = sorted(a)
    return a

#dodatna
def custva(tviti, hashtagi):
    s = []
    for b in hashtagi:
        for tvit in tviti:
            a = tvit.split()
            for c in a:
                if b == c[1:]:
                    if avtor(tvit) not in s:
                        s.append(avtor(tvit))
    return sorted(s)

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        a = tvit.split()
        g = a[1:]
        for b in g:
            if avtor(tvit) == oseba1:
                if oseba2 == izloci_besedo(b) and izloci_besedo(b) in vse_osebe(tviti):
                    return True
            elif avtor(tvit) == oseba2 and izloci_besedo(b) in vse_osebe(tviti):
                if oseba1 == izloci_besedo(b):
                    return True
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

