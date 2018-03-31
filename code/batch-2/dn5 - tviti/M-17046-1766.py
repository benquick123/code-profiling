def unikati(s):
	novi_seznam = []
	for element in s:
		if element not in novi_seznam:
			novi_seznam.append(element)
	return novi_seznam

def avtor(tvit):
	return tvit.split(':')[0]

def vsi_avtorji(tviti):
	avtorji = []
	for tvit in tviti:
		avtorji.append(avtor(tvit))
	return unikati(avtorji)

def izloci_besedo(beseda):
	while not beseda[0].isalnum():
		beseda = beseda[1:]
	while not beseda[-1].isalnum():
		beseda = beseda[0:-1]
	return beseda

def se_zacne_z(tvit,c):
	novi_seznam = []
	for beseda in tvit.split():
		if(beseda[0] == c):
			novi_seznam.append(izloci_besedo(beseda))
	return novi_seznam

def zberi_se_zacne_z(tviti, c):
	novi_seznam = []
	for tvit in tviti:
		izlocene_besede = se_zacne_z(tvit,c)
		for beseda in izlocene_besede:
			novi_seznam.append(beseda)
	return unikati(novi_seznam)


def vse_afne(tviti):
	return zberi_se_zacne_z(tviti,'@')

def vsi_hashtagi(tviti):
	return zberi_se_zacne_z(tviti,'#')

def vse_osebe(tviti):
	osebe = []
	for avtor in vsi_avtorji(tviti):
		osebe.append(avtor)
	for afna in vse_afne(tviti):
		osebe.append(afna)
	osebe.sort()
	return unikati(osebe)


def custva(tviti, hashtagi):
	osebe = []
	for tvit in tviti:
		if len([ element for element in se_zacne_z(tvit,'#') if element in hashtagi ]) > 0:
			#se_zacne_z(tvit,'#') in hashtagi:
			osebe.append(avtor(tvit))
	osebe.sort()
	return unikati(osebe)

def se_poznata(tviti, oseba1, oseba2):
	for tvit in tviti:
		if avtor(tvit) == oseba1 and len([ element for element in se_zacne_z(tvit,'@') if element == oseba2 ]) > 0:
			return True
		elif avtor(tvit) == oseba2 and len([ element for element in se_zacne_z(tvit,'@') if element == oseba1 ]) > 0:
			return True
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

