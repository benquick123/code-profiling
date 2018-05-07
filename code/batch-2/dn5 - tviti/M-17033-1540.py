import unittest

def unikati(s):
    vrnjen_seznam = []
    for a in s:
        if (a in vrnjen_seznam):
            pass
        else:
            vrnjen_seznam.append(a)
    return vrnjen_seznam

def avtor(tvit):
    seznam_besed = tvit.split()
    ime = seznam_besed[0]
    ime = ime[:-1]
    return ime

def vsi_avtorji(tvit):
    vsi_seznam = []
    for a in tvit:
        seznam_besed =  a.split()
        ime_avtorja = seznam_besed[0][:-1]
        if ime_avtorja in vsi_seznam:
            pass
        else:
            vsi_seznam.append(ime_avtorja)
    return vsi_seznam

def izloci_besedo(beseda):
    novabeseda=""
    for a in beseda:
        if a == "-":
            novabeseda+=a
        if a.isalnum():
                novabeseda+=a
    return novabeseda

def se_zacne_z(tvit, c):
    vsebesede = tvit.split()
    sez = []
    beseda_nova = ""
    for beseda in vsebesede:
        if beseda[0] is c:
            for crka in beseda:
                if crka.isalnum():
                    beseda_nova += crka
            if crka:
                sez.append(beseda_nova)
                beseda_nova = ""
    return sez

def zberi_se_zacne_z(tvit, c):
    vrnjen_seznam = []
    nova_beseda=""
    for posamezen_tvit in tvit:
        seznam_besed = posamezen_tvit.split()
        for posamezna_beseda in seznam_besed:
            if posamezna_beseda[0] is c:
                for posamezna_crka in posamezna_beseda:
                    if posamezna_crka.isalnum():
                        nova_beseda+=posamezna_crka
                if nova_beseda in vrnjen_seznam:
                    pass
                else:
                    vrnjen_seznam.append(nova_beseda)
                if posamezna_crka:
                    nova_beseda = ""
    return vrnjen_seznam

def vse_afne(tvit):
    c = "@"
    vrnjen_seznam = []
    nova_beseda=""
    for posamezen_tvit in tvit:
        seznam_besed = posamezen_tvit.split()
        for posamezna_beseda in seznam_besed:
            if posamezna_beseda[0] is c:
                for posamezna_crka in posamezna_beseda:
                    if posamezna_crka.isalnum():
                        nova_beseda+=posamezna_crka
                if nova_beseda in vrnjen_seznam:
                    pass
                else:
                    vrnjen_seznam.append(nova_beseda)
                if posamezna_crka:
                    nova_beseda = ""
    return vrnjen_seznam

def vsi_hashtagi(tvit):
    c = "#"
    vrnjen_seznam = []
    nova_beseda=""
    for posamezen_tvit in tvit:
        seznam_besed = posamezen_tvit.split()
        for posamezna_beseda in seznam_besed:
            if posamezna_beseda[0] is c:
                for posamezna_crka in posamezna_beseda:
                    if posamezna_crka.isalnum():
                        nova_beseda+=posamezna_crka
                if nova_beseda in vrnjen_seznam:
                    pass
                else:
                    vrnjen_seznam.append(nova_beseda)
                if posamezna_crka:
                    nova_beseda = ""
    return vrnjen_seznam

def vse_osebe(tviti):
    seznam_avtorji = vsi_avtorji(tviti)
    seznam_vse_afne = vse_afne(tviti)
    avtorji = []
    for oseba in seznam_vse_afne:
        avtorji.append(oseba)
    for avtor in seznam_avtorji:
        if not(avtor in avtorji):
            avtorji.append(avtor)
    avtorji = sorted(avtorji)
    return avtorji


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

