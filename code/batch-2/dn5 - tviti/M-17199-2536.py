import unittest


def unikati (s):
    a = []
    for st in s:
        if st not in a:
            a.append(st)
    return a


def avtorji (tvit):
    a = []
    for i in tvit.split(":"):
        a.append(i)
    return a [0]


def vsi_avtorji (tviti):
    a = []
    for tvit in tviti:
        ime = avtor(tvit)
        if ime not in a:
            a.append(ime)
    return a


def izloci_besedo (beseda):
    a = ""
    for i in beseda:
        if (i.isalnum()) or (i=="-") :
            a += i
    return a


def se_zacne_z (tvit, c):
    a = []
    for i in tvit.split():
        if i[0] == c :
            a.append(izloci_besedo(i))
    return a


def zberi_se_zacne_z(tviti, c):
    a = []
    for i in tviti:
        for x in i.split():
            if (x[0] == c):
                beseda = izloci_besedo(x)
                if beseda not in a:
                 a.append(beseda)
    return a


def vse_afne(tviti):
    a = []
    for i in tviti:
        for x in i.split():
            if (x[0] == "@"):
                beseda = izloci_besedo(x)
                if beseda not in a:
                    a.append(beseda)
    return a


def vsi_hashtagi(tviti):
    a = []
    for i in tviti:
        for x in i.split():
            if x[0] == "#":
                a.append(izloci_besedo(x))
    return a


def vse_osebe(tviti):
    osebe = []
    osebe.extend(vsi_avtorji(tviti))
    osebe.extend(vse_afne(tviti))
    return sorted(unikati(osebe))

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



if __name__ == "__main__":
    unittest.main()

