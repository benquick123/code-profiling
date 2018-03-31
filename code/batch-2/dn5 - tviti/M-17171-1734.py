def unikati(s):
    novsez = []
    for element in s:
        if element not in novsez:
            novsez.append(element)
        else:
            continue
    return novsez

def avtor(tvit):
    a = tvit.split(":")
    return a[0]

def vsi_avtorji(tviti):
    sez = []
    for e in tviti:
        avt = avtor(e)
        if avt not in sez:
            sez.append(avt)

    return sez

def izloci_besedo(beseda):
    i = 0
    text = beseda
    nov = ""
    while i < len(text):
        crka = text[i]
        if text[i] == "-":
            nov += text[i]
        if text[i].isalnum() == True:
            nov += text[i]
        i += 1
    return nov


def se_zacne_z(tvit, c):
    sez = tvit.split()
    nov = []
    for beseda in sez:
        if beseda[0] == c:
            uredi = izloci_besedo(beseda)
            nov.append(uredi)
    return nov

def zberi_se_zacne_z(tviti, c):
    sez = []
    for tvit in tviti:
        urejen = tvit.split()
        for beseda in urejen:
            uredi = se_zacne_z(tvit,c)
            sez += uredi
    mno = unikati(sez)
    return mno

def vse_afne(tviti):
    poklici = zberi_se_zacne_z(tviti, "@")
    return poklici

def vsi_hashtagi(tviti):
    poklici = zberi_se_zacne_z(tviti, "#")
    return poklici

def vse_osebe(tviti):
    sez = vsi_avtorji(tviti)
    sez2 = vse_afne(tviti)
    sez3 = sorted((sez + sez2))
    sez4 = unikati(sez3)
    return sez4

def custva(tviti, hashtagi):
    sez = []
    for tvit in tviti:
        avt = avtor(tvit)
        razdeli = tvit.split()
        for element in razdeli:
            izloc = izloci_besedo(element)
            if izloc in hashtagi:
                sez.append(avt)
    novi = unikati(sez)
    urejen = sorted(novi)
    return urejen

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        kdo = avtor(tvit)
        afna = se_zacne_z(tvit,"@")
        if afna != []:
            for element in afna:
                if kdo == oseba1 and element == oseba2 or kdo == oseba2 and element == oseba1:
                    return True
    else:
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

