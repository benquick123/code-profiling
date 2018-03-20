import unittest
import re

def unikati(s):
    nov_seznam = []
    for seznam in s:
        if seznam in nov_seznam:
            continue
        else:
            nov_seznam.append(seznam)
    return(nov_seznam)

def avtor(tviti):
    besedilo = tviti.split()
    regex = re.compile('[^a-zA-Z]')
    return(regex.sub("", besedilo[0]))

def vsi_avtorji(tviti):
    sez_avtorjev = []
    regex = re.compile('[^a-zA-Z]')
    for tvit in tviti:
        besedilo = tvit.split()
        avtor = regex.sub("",besedilo[0])
        if avtor in sez_avtorjev:
            continue
        else:
            sez_avtorjev.append(avtor)
    return(sez_avtorjev)

def izloci_besedo(beseda):
    regex = re.compile('[^a-zA-Z--]')
    return(regex.sub("", beseda))

def se_zacne_z(tvit,c):
    seznam = []
    besedilo = tvit.split()
    for besede in besedilo:
        beseda = besede
        if(beseda[0] == c):
            rege = re.compile('[^a-zA-Z]')
            beseda = rege.sub("",beseda)
            seznam.append(beseda)
    return(seznam)

def vse_afne(tviti):
    seznam_besed = []
    regex = re.compile('[^a-zA-Z-1-9]')
    for tvit in tviti:  # gre čez vse tvite
        besedilo = tvit.split()
        for besede in besedilo:  # gre čez trenuten tvit
            beseda = besede
            if (beseda[0] == "@"):  # preveri če se beseda začne na c
                beseda = regex.sub("", beseda)  # zamenja znake v besedi
                if (beseda not in seznam_besed):  # preveri če je beseda že v seznamu
                    seznam_besed.append(beseda)
    return (seznam_besed)

def vsi_hashtagi(tviti):
    seznam_besed = []
    regex = re.compile('[^a-zA-Z-1-9]')
    for tvit in tviti:  # gre čez vse tvite
        besedilo = tvit.split()
        for besede in besedilo:  # gre čez trenuten tvit
            beseda = besede
            if (beseda[0] == "#"):  # preveri če se beseda začne na c
                beseda = regex.sub("", beseda)  # zamenja znake v besedi
                if (beseda not in seznam_besed):  # preveri če je beseda že v seznamu
                    seznam_besed.append(beseda)
    return (seznam_besed)

def zberi_se_zacne_z(tviti,c):
    seznam_besed = []
    regex = re.compile('[^a-zA-Z-1-9]')
    for tvit in tviti: # gre čez vse tvite
        besedilo = tvit.split()
        for besede in besedilo: # gre čez trenuten tvit
            beseda = besede
            if(beseda[0] == c): # preveri če se beseda začne na c
                beseda = regex.sub("", beseda)  # zamenja znake v besedi
                if(beseda not in seznam_besed): # preveri če je beseda že v seznamu
                    seznam_besed.append(beseda)
    return(seznam_besed)

def vse_osebe(tviti):
    seznam_besed = []
    regex = re.compile('[^a-zA-Z-1-9]')
    for tvit in tviti:  # gre čez vse tvite
        besedilo = tvit.split()
        avtor = regex.sub("", besedilo[0])
        if avtor in seznam_besed:
            continue
        else:
            seznam_besed.append(avtor)
        for besede in besedilo:  # gre čez trenuten tvit
            beseda = besede
            if (beseda[0] == "@"):  # preveri če se beseda začne na c
                beseda = regex.sub("", beseda)  # zamenja znake v besedi
                if (beseda not in seznam_besed):  # preveri če je beseda že v seznamu
                    seznam_besed.append(beseda)
    return (sorted(seznam_besed))




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

