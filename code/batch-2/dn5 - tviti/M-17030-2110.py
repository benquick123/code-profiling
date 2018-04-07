import unittest
def unikati(s):
    seznam= []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam
def avtor(tvit):
    tvit = tvit.split()
    ime = tvit[0]
    ime = ime.split()
    ime = list(map(lambda x: x[:-1], ime))
    ime = ime.pop()
    return(ime)
def vsi_avtorji(tviti):
    imena = []
    for i in tviti:
        i = i.split()
        ime = i[0]
        ime = ime.split()
        ime = list(map(lambda x: x[:-1], ime))
        ime = ime.pop()
        if ime not in imena:
            imena.append(ime)
    return(imena)
def izloci_besedo(beseda):
    import re
    beseda = re.sub('[^0-9a-zA-Z--]+', '', beseda)

    return beseda
def se_zacne_z(tvit, c):
    import re
    seznam=[]
    tvit = tvit.split()
    for beseda in tvit:
        if beseda[0] == c:
            beseda = re.sub('[^0-9a-zA-Z--]+', '', beseda)
            seznam.append(beseda)
    return (seznam)
def zberi_se_zacne_z(tviti, c):
    imena = []
    for tvit in tviti:
        import re
        tvit = tvit.split()
        for beseda in tvit:
            if beseda[0] == c:
                beseda = re.sub('[^0-9a-zA-Z--]+', '', beseda)
                if beseda not in imena:
                    imena.append(beseda)
    return (imena)
def vse_afne(tviti):
    seznam=zberi_se_zacne_z(tviti,c="@")
    return seznam
def vsi_hashtagi(tviti):
    seznam=zberi_se_zacne_z(tviti,c="#")
    return seznam
def vse_osebe(tviti):
    vse_osebe=[]
    seznam=vsi_avtorji(tviti)
    drugi_seznam=vse_afne(tviti)
    for ime in seznam:
        if ime not in drugi_seznam:
            drugi_seznam.append(ime)
    drugi_seznam.sort()
    return drugi_seznam
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


if __name__ == "__main__":
    unittest.main()

