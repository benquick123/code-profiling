from math import *
import math

def unikati(seznam):
    novi_seznam = []
    for element_a in seznam:
        if(element_a in novi_seznam):
            continue
        else:
            novi_seznam.append(element_a)

    return novi_seznam

def avtor(tvit):
    seznam = tvit.split()
    prvi_element = seznam[0]
    odgovor = prvi_element[0:len(prvi_element)-1]

    return odgovor

def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        nov_uporabnik = avtor(tvit)
        seznam_avtorjev.append(nov_uporabnik)

    return(unikati(seznam_avtorjev))

def izloci_besedo(beseda):
    stevec_d = 0
    stevec_l = 0
    for i in range(0, len(beseda)):
        if (beseda[i].isalnum() == False):
            stevec_l = stevec_l + 1
        else:
            break

    for i in range(len(beseda) - 1, 0, -1):
        if (beseda[i].isalnum() == False):
            stevec_d = stevec_d + 1
        else:
            break

    return beseda[stevec_l:len(beseda) - stevec_d]

def se_zacne_z(tvit, c):
    seznam_besed = []
    seznam_tvit = tvit.split()
    for beseda in seznam_tvit:
        if(beseda[0] == c):
            if(len(beseda) > 1):
                skrajsana_beseda = izloci_besedo(beseda)
                seznam_besed.append(skrajsana_beseda)
            else:
                continue
        else:
            continue

    return unikati(seznam_besed)

def zberi_se_zacne_z(tviti, c):
    koncni_seznam = []
    for tvit in tviti:
        koncni_seznam.extend(se_zacne_z(tvit, c))

    return unikati(koncni_seznam)

def vse_afne(tviti):
    odgovor = zberi_se_zacne_z(tviti, "@")

    return  odgovor

def vsi_hashtagi(tviti):
    odgovor = zberi_se_zacne_z(tviti, "#")

    return odgovor

def vse_osebe(tviti):
    seznam1 = vsi_avtorji(tviti)
    seznam2 = vse_afne(tviti)

    return  sorted(unikati(seznam1+seznam2))

def custva(tviti, hashtagi):
    seznam = []
    for tvit in tviti:
        oseba = avtor(tvit)
        primerjava = se_zacne_z(tvit, "#")
        for prvi in primerjava:
            if(prvi in hashtagi):
                seznam.append(oseba)
            else:
                continue

    return sorted(unikati(seznam))

def se_poznata(tviti, oseba1, oseba2):
    tabela = []
    for tvit in tviti:
        pisec = avtor(tvit)
        poznavalec = se_zacne_z(tvit, "@")

        if(pisec == oseba1 and oseba2 in poznavalec) or (pisec == oseba2 and oseba1 in poznavalec):
            tabela.append(pisec)
            tabela.append(poznavalec)

    return tabela








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

