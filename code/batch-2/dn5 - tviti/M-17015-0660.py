
#1
def unikati(s):
    nov_seznam = []
    for x in s:
        if x not in nov_seznam:
            nov_seznam.append(x)
    return nov_seznam



#2
def avtor(tviti):
    tviti = tviti.split(' ')
    return tviti[0][:-1]



#3
def vsi_avtorji(tviti):
    imena = []
    for x in tviti:
        if (avtor(x) not in imena):
            imena.append(avtor(x))
    return imena


#4
def izloci_besedo(beseda):
    x = 0
    y = 0
    while (x == 0) & (y == 0):
        leng = len(beseda)
        if(beseda[0].isalnum() == False):
            beseda = beseda.strip(beseda[0])
            leng = len(beseda)
        else:
            x = 1
        if (beseda[leng-1].isalnum() == False):
            beseda = beseda.strip(beseda[leng-1])
            leng = len(beseda)
        else:
            y = 1
    return beseda


#5
def se_zacne_z(tvit, c):
    i = 0
    s = []
    tvit = tvit.split(' ')
    for x in tvit:
        bes = x
        if bes[0] == c:
            s.append(izloci_besedo(bes))
    return s


#6
def zberi_se_zacne_z(tviti, c):
    s = []
    for x in tviti:
        for y in se_zacne_z(x, c):
            if y not in s:
                s.append(y)
    return s


#7
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


#8
def vsi_hashtagi(tviti):
    return  zberi_se_zacne_z(tviti, "#")


#9
def vse_osebe(tviti):
    a = []
    for x in tviti:
        if avtor(x) not in a:
            a.append(avtor(x))
    for afne in vse_afne(tviti):
        if afne not in a:
            a.append(afne)
    return sorted(a)

print(vse_osebe(["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]))

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

if __name__ == "__main__":
    unittest.main()

