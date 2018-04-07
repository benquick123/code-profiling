import unittest

def unikati(s):
    seznam = []
    for i in s:
        if i not in seznam:
            seznam.append(i)
    return seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    seznam = []
    for i in tviti:
        if avtor(i) not in seznam:
            seznam.append(avtor(i))
    return seznam

def izloci_besedo(beseda):
    beseda = list(beseda)
    while True:
        if beseda[0].isalnum() == False:
            beseda.pop(0)
        else:
            break
    i = len(beseda) - 1
    while True:
        if beseda[i].isalnum() == False:
            beseda.pop(i)
        else:
            break
        i -= 1

    return ''.join(beseda)

def se_zacne_z(tvit, c):
    seznam = tvit.split()
    seznamvrn = []
    for i in seznam:
        if i[0] == c:
            seznamvrn.append(izloci_besedo(i))
    return seznamvrn

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for i in tviti:
        for ii in se_zacne_z(i,c):
            if ii not in seznam:
                seznam.append(ii)
    return seznam

def vse_afne(tviti):
    seznam = []
    for i in tviti:
        for ii in se_zacne_z(i, "@"):
            if ii not in seznam:
                seznam.append(ii)
    return seznam

def vsi_hashtagi(tviti):
    seznam = []
    for i in tviti:
        for ii in se_zacne_z(i, "#"):
            if ii not in seznam:
                seznam.append(ii)
    return seznam

def vse_osebe(tviti):
    seznam = []
    seznam.extend(vsi_avtorji(tviti))
    seznam.extend(vse_afne(tviti))
    seznam = unikati(seznam)
    seznam = sorted(seznam)
    return seznam


def custva(tviti, hashtagi):
    seznam = []
    hashtagi_tvita = []

    for i in tviti:
        for ii in se_zacne_z(i, "#"):
            if ii not in hashtagi_tvita:
                hashtagi_tvita.append(ii)
        for iii in hashtagi_tvita:
            for iv in hashtagi:
                if iii == iv:
                    seznam.append(avtor(i))
        del hashtagi_tvita[:]

    seznam = unikati(seznam)
    seznam = sorted(seznam)
    return seznam


def se_poznata(tviti, oseba1, oseba2):
    a = 0
    osebe_tvita = []
    seznam = []
    for i in tviti:
        osebe_tvita.append(i)
        if avtor(i) == oseba1 or avtor(i) == oseba2:
            seznam.extend(vse_afne(osebe_tvita))
            for ii in seznam:
                if oseba1 == ii or oseba2 == ii:
                    return True
        del osebe_tvita[:]
        del seznam[:]
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

