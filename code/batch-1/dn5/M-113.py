import unittest
from collections import OrderedDict
#1
def unikati(s):
    return(list(OrderedDict.fromkeys(s)))
#2
def avtor(tvit):
    a = tvit.split(":")
    return(a[0])
#3
def vsi_avtorji(tviti):
    s =[]
    for a in tviti:
        s.append(avtor(a))
    return(unikati(s))
#4
def izloci_besedo(beseda):
    od = 0
    do = 0
    p=0
    k = []
    for i in range(0,len(beseda),1):
        if beseda[i].isalnum() == True and p == 0:
            p+=1
            od = i
        elif beseda[i].isalnum() == True:
            do = i
    do+=1
    for c in range(od,do,1):
        k.append(beseda[c])
    return("".join(k))
#5
def se_zacne_z(tvit, c):
    a = tvit.split()
    sez = []
    for i in a:
        if i[0] == c:
            sez.append(izloci_besedo(i))
    return(sez)
#6
def zberi_se_zacne_z(tviti, c):
    sez = []
    for j in tviti:
        k = j.split()
        for i in k:
            if i[0] == c:
                sez.append(izloci_besedo(i))

    return(unikati(sez))
#7
def vse_afne(tviti):
    return(zberi_se_zacne_z(tviti, "@"))
#8
def vsi_hashtagi(tviti):
    return (zberi_se_zacne_z(tviti, "#"))
#9
def vse_osebe(tviti):
    avtorji = vsi_avtorji(tviti)
    afne = vse_afne(tviti)
    avtorji.extend(afne)
    a = unikati(avtorji)
    return(sorted(a))
#Dodatne
def custva(tviti, hashtagi):
    sez = []
    for i in tviti:
        a = se_zacne_z(i, "#")
        for k in hashtagi:
            for j in a:
                if j == k:
                    sez.append(avtor(i))
    return(sorted(unikati(sez)))
def se_poznata(tviti, oseba1, oseba2):
    for i in tviti:
        if avtor(i) == oseba1:
            afna = se_zacne_z(i,"@")
            for j in afna:
                if j == oseba2:
                    return(True)
                    break
        if avtor(i) == oseba2:
            afna = se_zacne_z(i,"@")
            for j in afna:
                if j == oseba1:
                    return(True)
                    break

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

