import unittest

# funkcije

def unikati(s):
    vrni = []
    for x in s:
        for y in vrni:
            if x==y:
                break
        else:
            vrni.append(x)
    return vrni

def avtor(tvit):
    ime = ""
    for crka in tvit:
        if crka == ':':
            break
        else:
            ime = ime + crka
    return ime

def vsi_avtorji(tviti):
    seznam_imen = []
    for tvit in tviti:
        seznam_imen.append(avtor(tvit))
    return unikati(seznam_imen)

def izloci_besedo(beseda):
    brisi = ""
    for znak in beseda:
        if znak.isalnum() == False:
            brisi = brisi + znak
        else:
            break

    beseda = beseda.replace(brisi, '')
    beseda = beseda[::-1]

    brisi = ""
    for znak in beseda:
        if znak.isalnum() == False:
            brisi = brisi + znak
        else:
            break

    beseda = beseda.replace(brisi, '')
    return beseda[::-1]

def se_zacne_z(tvit, c):
    zacni = False
    x = []
    beseda = ""
    for znak in tvit:
        if znak == c:
            zacni = True

        if znak == " " and zacni == True:
            zacni = False
            x.append(izloci_besedo(beseda))
            beseda = ""

        if zacni == True:
            beseda = beseda + znak

    if beseda != "":
        x.append(beseda)
    return x

def zberi_se_zacne_z(tviti, c):
    seznam_besed = []
    for posamezni_tvit in tviti:
        y = se_zacne_z(posamezni_tvit,c)
        for besede in y:
            seznam_besed.append(izloci_besedo(besede))
    return unikati(seznam_besed)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,'@')

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,'#')

def vse_osebe(tviti):
    osebe_zacetek = vsi_avtorji(tviti)
    osebe = vse_afne(tviti)
    for imena in osebe_zacetek:
        osebe.append(imena)
    return sorted(unikati(osebe))

def custva(tviti, hashtagi):
    uporabniki = []
    for posamezni_tvit in tviti:
        ime = avtor(posamezni_tvit)
        for h in hashtagi:
            if h in posamezni_tvit:
                uporabniki.append(ime)
    return sorted(unikati(uporabniki))

def se_poznata(tviti, oseba1, oseba2):
   for posamezni_tvit in tviti:
       avtor_tvita = avtor(posamezni_tvit)
       vsi_oznaceni = se_zacne_z(posamezni_tvit,'@')
       for osebe_omenjene in vsi_oznaceni:
           if (oseba1 == avtor_tvita or oseba2 == avtor_tvita) and (oseba1 in osebe_omenjene or oseba2 in osebe_omenjene):
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

