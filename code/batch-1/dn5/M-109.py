def unikati(s):
    sez = []
    for x in s:
        if x not in sez:
            sez.append(x)
    return sez
def avtor(tvit):
    a = ""
    for x in range(len(tvit)):
        if tvit[x] == ":":
            break
        else:
            a += tvit[x]
    return a
def izloci_besedo(beseda):
    beseda_1 = ""
    for x in range(len(beseda)):
        if beseda[x].isalnum() == True:
            beseda_1 += beseda[x]
        elif beseda[x] == "-" and beseda[x-1].isalnum() == True and beseda[x+1].isalnum() == True:
            beseda_1 += beseda[x]
    return beseda_1
def vsi_avtorji(tviti):
    sez = []
    for x in tviti:
        avtor_ime = avtor(x)
        if avtor_ime not in sez:
            sez.append(avtor_ime)
    return sez

def se_zacne_z(tvit, c):
    sez = tvit.split()
    sez_besed = []
    for x in sez:
        if x[0] == c:
            if x[-1].isalnum() == True:
                sez_besed.append(x[1:])
            else:
                sez_besed.append(x[1:-1])
    return sez_besed

def vse_afne(tviti):
    sez_imen = []
    for x in tviti:
        besede = x.split()
        for x in besede:
            if x[0] == "@":
                if x[-1].isalnum() == True:
                    if x[1:] not in sez_imen:
                        sez_imen.append(x[1:])
                else:
                    if x[1:-1] not in sez_imen:
                        sez_imen.append(x[1:-1])
    return sez_imen
def vse_osebe(tviti):
    sez = vse_afne(tviti)
    sez_imen = vsi_avtorji(tviti)
    n = 0
    for x in range(len(sez)):
        if sez[n] not in sez_imen:
            sez_imen.append(sez[n])
        n += 1
    sez = sorted(sez_imen)
    return sez

def vsi_hashtagi(tviti):
    sez = []
    for x in tviti:
        besede = x.split()
        for x in besede:
            if x[0] == "#":
                if x[-1].isalnum() == True:
                    if x[1:] not in sez:
                        sez.append(x[1:])
                else:
                    if x[1:-1] not in sez:
                        sez.append(x[1:-1])
    return sez
def zberi_se_zacne_z(tviti, c):
    sez_besed = []
    for x in tviti:
        sez = x.split()
        for x in sez:
            if x[0] == c:
                if x[-1].isalnum() == True:
                    if x[1:] not in sez_besed:
                        sez_besed.append(x[1:])
                else:
                    if x[1:-1] not in sez_besed:
                        sez_besed.append(x[1:-1])
    return sez_besed
def custva(tviti, hashtagi):
    sez_imen = []
    for x in tviti:
        sez = x.split()
        avtor = sez[0][:-1]
        for x in sez:
            if x[0] == "#":
                if x[1:] in hashtagi and avtor not in sez_imen:
                    sez_imen.append(avtor)
    return sorted(sez_imen)

def se_poznata(tviti, oseba1, oseba2):
    zakljucek = False
    sez = [oseba1, oseba2]
    for x in sez:
        for y in tviti:
            besede = y.split()
            for s in besede:
                sez_besed = []
                if s[0] == "@":
                    if besede[0][:-1] == x:
                        if s[-1].isalnum() == True:
                            if s[1:] not in sez_besed:
                                sez_besed.append(s[1:])
                        else:
                            if s[1:-1] not in sez_besed:
                                sez_besed.append(s[1:-1])
                        for d in sez_besed:
                            if x == oseba1:
                                if oseba2 in sez_besed:
                                    zakljucek = True
                            else:
                                if oseba1 in sez_besed:
                                    zakljucek = True
    return zakljucek
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

