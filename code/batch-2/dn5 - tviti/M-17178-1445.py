#FUNKCIJE

def unikati(s):
    nov_seznam = []
    for i in s:
        if i not in nov_seznam:
            nov_seznam.append(i)
    return nov_seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    nov_seznam = []
    for i in tviti:
        ime = i.split(":")[0]
        if ime not in nov_seznam:
            nov_seznam.append(ime)
    return nov_seznam

def izloci_besedo(beseda):
    crke = []
    prejsnja = beseda[0]
    dodajPrejsnjo = False
    for c in beseda:
        if not c.isalnum():
            if prejsnja.isalnum() and c == '-':
                dodajPrejsnjo = True
        else:
            if dodajPrejsnjo:
                crke.append(prejsnja)
                dodajPrejsnjo = False
            crke.append(c)
        prejsnja = c
    return ''.join(crke)

def se_zacne_z(tvit, c):
    split_seznam = tvit.split(" ")
    seznam = []
    for i in split_seznam:
        for element in i:
            if element[0] == c:
                seznam.append(izloci_besedo(i))
    return seznam

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for i in tviti:
        split_seznam = i.split(" ")
        for element in split_seznam:
                if element[0] == c:
                    izlocen_del = izloci_besedo(element)
                    if izlocen_del not in seznam:
                        seznam.append(izlocen_del)
    return seznam

def vse_afne(tviti):
    seznam = []
    for i in tviti:
        split_seznam = i.split(" ")
        for element in split_seznam:
                if element[0] == "@":
                    izlocen_del = izloci_besedo(element)
                    if izlocen_del not in seznam:
                        seznam.append(izlocen_del)
    return seznam

def vsi_hashtagi(tviti):
    seznam = []
    for i in tviti:
        split_seznam = i.split(" ")
        for element in split_seznam:
                if element[0] == "#":
                    izlocen_del = izloci_besedo(element)
                    if izlocen_del not in seznam:
                        seznam.append(izlocen_del)
    return seznam

def vse_osebe(tviti):
    seznam = []
    avtorji = vsi_avtorji(tviti)
    afne = vse_afne(tviti)
    for i in avtorji:
        if i not in seznam:
            seznam.append(i)
        for j in afne:
            if j not in seznam:
                seznam.append(j)
            else:
                continue
    return sorted(seznam)

#IZPISI

tviti = ["sandra: Spet ta dež. #dougcajt",
 "berta: @sandra Delaj domačo za #programiranje1",
 "sandra: @berta Ne maram #programiranje1 #krneki",
 "ana: kdo so te @berta, @cilka, @dani? #krneki",
 "cilka: jst sm pa #luft",
 "benjamin: pogrešam ano #zalosten",
 "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


s = [1, 2, 1, 1, 3, 2]
print(unikati(s))

tvit = "ana: kdo so te @berta, @cilka, @dani? #krneki"
print(avtor(tvit))

print(vsi_avtorji(tviti))

beseda = "@janez-novak!!!"
print(izloci_besedo(beseda))

tvit = "Benjamin $je $skocil! Visoko!"
c = "$"
print(se_zacne_z(tvit, c))

c = "@"
print(zberi_se_zacne_z(tviti, c))

print(vse_afne(tviti))

print(vsi_hashtagi(tviti))

print(vse_osebe(tviti))


#TESTI

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

