import unittest
tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]

def unikati(s):
    xs = []
    for x in s:
        if x not in xs:
            xs.append(x)
    return xs

def avtor(tvit):
    xs = tvit.split(':')
    return xs[0]


def vsi_avtorji(tviti):
    xs = []
    for x in tviti:
        if x.split(':')[0] not in xs:
            xs.append(x.split(':')[0])
    return xs

def izloci_besedo(beseda):
    i1 = 0
    i2 = 0
    i3 = -1
    i4 = 0
    for x in beseda:
        if beseda[i2].isalnum() == False:
            i1 = i1 + 1
        else:
            break
        i2 = i2 + 1
    for x in beseda:
        if beseda[i3].isalnum() == False:
            i4 = i4 + 1
        else:
            break
        i3 = i3 - 1
    return beseda[i1:len(beseda)-i4]

def se_zacne_z(tvit, c):
    xss = []
    xs = tvit.split()
    for x in xs:
        if x[0] == c:
            b = 1
            for i in x:

                if i.isalnum() == True:
                    b = b + 1
            xss.append(x[1:b])
    return xss

def zberi_se_zacne_z(tviti, c):
    xss = []
    xs = []

    for x in tviti:
        xs = x.split()

        for b in xs:
            if b[0] == c:
               if b[-1].isalnum() == False:
                   if b[1:-1] not in xss:
                       xss.append(b[1:-1])
               elif b[1:] not in xss:
                    xss.append(b[1:])
    return xss


def vse_afne(tviti):

        xss = []
        xs = []

        for x in tviti:
            xs = x.split()

            for b in xs:
                if b[0] == '@':
                    if b[-1].isalnum() == False:
                        if b[1:-1] not in xss:
                            xss.append(b[1:-1])
                    elif b[1:] not in xss:
                        xss.append(b[1:])
        return xss


def vsi_hashtagi(tviti):
    xss = []
    xs = []

    for x in tviti:
        xs = x.split()

        for b in xs:
            if b[0] == '#':
                if b[-1].isalnum() == False:
                    if b[1:-1] not in xss:
                        xss.append(b[1:-1])
                elif b[1:] not in xss:
                    xss.append(b[1:])
    return xss

def vse_osebe(tviti):
    xs =[]
    xss = []
    for x in tviti:
        if x.split(':')[0] not in xss:
            xss.append(x.split(':')[0])

    for x in tviti:
        xs = x.split()

        for b in xs:
            if b[0] == '@':
                if b[-1].isalnum() == False:
                    if b[1:-1] not in xss:
                        xss.append(b[1:-1])
                elif b[1:] not in xss:
                    xss.append(b[1:])
    return sorted(xss)




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

