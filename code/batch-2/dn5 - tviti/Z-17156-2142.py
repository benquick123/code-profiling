def unikati(s):
    s_nov = []
    for e in s:
        if e not in s_nov:
            s_nov.append(e)
    return s_nov

def avtor(tvit):
    return tvit[:tvit.index(":")]       #najdem najprej indeks od dvopicja, nato vse do tega indeksa je avtor tvita (ime)
                                        # return tvit.split(":")[0] še ena opcija

def vsi_avtorji(tviti):
    return unikati([avtor(tvit) for tvit in tviti])    #izvirna koda po korakih v bju


def pomožna_funkcija1(beseda):
    for e in beseda:
        if e.isalnum():
            indeks = beseda.index(e)
            break
    return beseda[indeks:]


def izloci_besedo(beseda):
    beseda = pomožna_funkcija1(beseda)          #tu imam iz prve strani pobrisan
    beseda = pomožna_funkcija1(beseda[::-1])    # brisanje druge strani
    return beseda[::-1]                         #ker je beseda obrnjena, jo rabim obrnat spet v pravo stran, torej vrnem prav obrnjeno besedo


def se_zacne_z(tvit, c):
    return [izloci_besedo(e) for e in tvit.split() if e[0] == c]  #v bju mam celo kodo, ki je bolj berljiva

def zberi_se_zacne_z(tviti, c):
    return unikati(se_zacne_z(" ".join(tviti), c))   #v bju mam celo kodo, ki je po korakih

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")

def vse_osebe(tviti):
    s = vsi_avtorji(tviti)
    s += vse_afne(tviti)
    return sorted(unikati(s))


def custva(tviti, hashtagi):
    s = []
    for tvit in tviti:
        avtor_tvita = avtor(tvit)
        seznam_besed_tvita = tvit.split()
        for beseda in seznam_besed_tvita:
            if beseda[1:] in hashtagi:        #skrb kaj če nastopi ista beseda v hastagih a je brez hastaga???
                s.append(avtor_tvita)         #USEEN COOL KER pol beseda[1:] bo pokvarjena in nebo enaka besedi hastaga!
                break                         #AKA NEBOTA ISTE
    return sorted(unikati(s))



def se_poznata(tviti, oseba1, oseba2):
    return any(True for tvit in tviti if (avtor(tvit) == oseba1 or avtor(tvit) == oseba2) and (oseba1 in se_zacne_z(tvit, "@") or oseba2 in se_zacne_z(tvit, "@")))

    #v bju mam po korakih spisan




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

