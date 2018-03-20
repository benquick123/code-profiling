import unittest

def unikati(s):
    nov_seznam = []
    for i in range(len(s)):
        if s[i] not in nov_seznam:
            nov_seznam.append(s[i])
    return nov_seznam

def avtor(tvit):
    return tvit.split(":")[0]

def vsi_avtorji(tviti):
    imena = []
    for tvit in tviti:
        imena.append(avtor(tvit))
    return unikati(imena)

def izloci_besedo(beseda):
    nova_beseda = ''
    for i in range(len(beseda)):
        if i == 0 or i == len(beseda)-1:
            if beseda[i].isalnum():
                nova_beseda += beseda[i]
        else:
            if beseda[i].isalnum() or (beseda[i-1].isalnum() and beseda[i+1].isalnum()):
                nova_beseda += beseda[i]

    return nova_beseda

def se_zacne_z(tvit, c):
    beseda       = ''
    seznam_besed = []
    zapisuj      = False

    for i in range(len(tvit)):
        if tvit[i] == c:
            zapisuj = True
        if (tvit[i].isspace() or i == len(tvit)-1) and zapisuj:
            beseda += tvit[i]
            seznam_besed.append(beseda)
            beseda  = ''
            zapisuj = False
        if zapisuj:
            beseda += tvit[i]

    for i in range(len(seznam_besed)):
        seznam_besed[i] = izloci_besedo(seznam_besed[i])

    return seznam_besed

def zberi_se_zacne_z(tviti, c):
    seznam_besed = []

    for tvit in tviti:
        besede_v_tvitu = se_zacne_z(tvit, c)
        for beseda in besede_v_tvitu:
            if beseda not in seznam_besed:
                seznam_besed.append(beseda)

    return seznam_besed

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, '@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, '#')

def vse_osebe(tviti):
    omenjene_osebe = vse_afne(tviti)
    avtorji        = []
    seznam_oseb    = []

    for tvit in tviti:
        avtorji.append(avtor(tvit))

    for avtorr in avtorji:
        if avtorr not in seznam_oseb:
            seznam_oseb.append(avtorr)

    for oseba in omenjene_osebe:
        if oseba not in seznam_oseb:
            seznam_oseb.append(oseba)

    return sorted(seznam_oseb)

def custva(tviti, hashtagi):
    seznam_avtorjev = []

    for tvit in tviti:
        avtorr  = avtor(tvit)
        custvaa = se_zacne_z(tvit, '#')
        for custvo in custvaa:
            if custvo in hashtagi and avtorr not in seznam_avtorjev:
                seznam_avtorjev.append(avtorr)
                break

    return sorted(seznam_avtorjev)

def se_poznata(tviti, oseba1, oseba2):
    poznanstvo = relacija(tviti, oseba1, oseba2)

    if not poznanstvo:
        return relacija(tviti, oseba2, oseba1)

    return poznanstvo

def relacija(tviti, oseba1, oseba2):
    for tvit in tviti:
        avtorr = avtor(tvit)
        if avtorr == oseba1:
            osebe = se_zacne_z(tvit, '@')
            if oseba2 in osebe:
                return True
            else:
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

