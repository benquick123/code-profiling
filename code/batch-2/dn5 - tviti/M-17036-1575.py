import unittest
def unikati(s):
    nov_seznam = []
     
    for i in range(len(s)):
        if s[i] in nov_seznam :
            pass
        else:
            nov_seznam.append(s[i])
    return nov_seznam

def avtor(tvit):
    tvit1 = tvit.split(":")
    ime = tvit1[0]
    return ime

def vsi_avtorji(tviti):
    imena = []
    for i in range(len(tviti)):
        if ":" in tviti[i]:
            tre_ime = tviti[i]
            ime = ""
            for a in range(len(tre_ime)):
                if tre_ime[a] == ':':
                    break
                else:
                    ime += tre_ime[a]
            if ime in imena:
                pass
            else:
                imena.append(ime)
    return imena

def izloci_besedo(beseda):
    ne_alfanumericna_beseda = ""
    for i in range(len(beseda)):
        if beseda[i].isalnum() or beseda[i] == "-":
            ne_alfanumericna_beseda += beseda[i]
        else:
            pass
    return ne_alfanumericna_beseda

def se_zacne_z(tvit, znak):
    hestag = []
    text = tvit.split()
    for i in range(len(text)):
        if znak in text[i]:
            od_znak = text[i]
            beseda = ""
            for a in range(len(od_znak)):
                if od_znak[a].isalnum():
                    beseda += (od_znak[a])
                else:
                    pass
            hestag.append(beseda)
    return hestag

def zberi_se_zacne_z(tviti, c):
    afna = []
    for i in range(len(tviti)):
        ime = ""
        s = tviti[i].split()
        for x in range(len(s)):
            od_c = s[x]
            if c in od_c:
                ime = ""
                for a in range(len(od_c)):
                    if od_c[a].isalnum():
                        ime += (od_c[a])
                    else:
                        pass
            if ime in afna or ime == "":
                pass
            else:       
                afna.append(ime)
    return afna

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    list_vse_afne = vse_afne(tviti)
    list_vsi_avtorji = vsi_avtorji(tviti)
    list_skupaj = list_vse_afne + [x for x in list_vsi_avtorji if x not in list_vse_afne]
    return sorted(list_skupaj)

def custva(tviti, hashtagi):
    osebe = []
    for i in range(len(tviti)):
        tvit = tviti[i]
        for a in range(len(hashtagi)):
            heshtag = hashtagi[a]
            if heshtag in tvit:
                if avtor(tvit) in osebe:
                    pass
                else:
                    osebe.append(avtor(tvit))
            else:
                pass
    return sorted(osebe)

def se_poznata(tviti, oseba1, oseba2):
    se_poznata = False
    for i in range(len(tviti)):
        tvit = tviti[i]
        oseba1_1 = avtor(tvit)
        if "@" + oseba2 in tvit and oseba1_1 == oseba1:
            se_poznata = True
    if se_poznata:
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

