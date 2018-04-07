import unittest
import re
def unikati(s):
    seznam = []
    for x in s:
        if x not in seznam:
          seznam.append(x)
    return seznam

def avtor(tvit):
    splitted = tvit.split(":")
    return splitted[0]

def vsi_avtorji(tviti):
    nov_seznam = []
    for i in tviti:
        authors = avtor(i)
        if authors not in nov_seznam:
            nov_seznam.append(authors)
    return nov_seznam

def izloci_besedo(beseda):
    a=0
    a2=len(beseda)-1
    for x in range(0, len(beseda)-1):
        if beseda[x].isalnum():
            if beseda[x].isalnum() and x == 0:
                a = a - 1
            break
        else:
            a=x

    for y in range(len(beseda)-1, 0, -1):
        if beseda[y].isalnum():
            if y == len(beseda) -1 and beseda[y].isalnum():
                a2 = a2 +1
            break
        else:
            a2=y

    return (beseda[a+1:a2])

def se_zacne_z(tvit, c):
    seznamcek = []
    tvit = tvit.replace(",", " ").replace("?", " ").replace("!"," ").split(" ")
    for y in tvit:
        if c in y:
            seznamcek.append(y[1:])
    return unikati(seznamcek)

def zberi_se_zacne_z(tviti, c):
    seznamcek = []
    for x in tviti:
        x = x.replace(",", " ").replace("?", " ")
        spltd = x.split(" ")
        for y in spltd:
            if c in y:
                seznamcek.append(y[1:])
    return unikati(seznamcek)

def vse_afne(tviti):
    seznamcek = []
    for x in tviti:
        x = x.replace(",", " ").replace("?", " ")
        spltd = x.split(" ")
        for y in spltd:
            if "@" in y:
                seznamcek.append(y[1:])
    return unikati(seznamcek)

def vsi_hashtagi(tviti):
    seznamcek = []
    for x in tviti:
        x = x.replace(",", " ").replace("?", " ")
        spltd = x.split(" ")
        for y in spltd:
            if "#" in y:
                seznamcek.append(y[1:])
    return unikati(seznamcek)

def vse_osebe(tviti):
    prazen = []
    x = vsi_avtorji(tviti)
    y = vse_afne(tviti)
    z = list(set(x) | set(y))
    z.sort()
    return z

def custva(tviti, hashtagi):
    sezn = []
    for x in tviti:
        for y in hashtagi:
            if y in x:
                z=avtor(x)
                if z not in sezn:
                    sezn.append(z)
                    sezn.sort()
    return sezn

def se_poznata(tviti, oseba1, oseba2):
    for x in tviti:
        if oseba1 in x and oseba2 in x:
            nov_x = x
            if "@"+oseba2 in nov_x:
                return True
            return False


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

