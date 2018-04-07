import unittest

# Naloga: Tviti (OK)

def unikati(s):
	s1 = []
	for x in s:
		if x not in s1:
			s1.append(x)
	return s1

def avtor(tvit):
	s = ""
	for x in tvit:
		if x != '"':
			if x != ':':
				s += x
			else:
				return s

def vsi_avtorji(tviti):
	s = []
	for tvit in tviti:
		a = avtor(tvit)
		s.append(a)
	return unikati(s)

def izloci_besedo(beseda):
	if beseda.isalnum():
		return beseda
	else:
		s = ""
		for x in beseda:
			if x.isalnum() or x == "-":
				s += x
		return s

def se_zacne_z(tvit, c):
	tvit2 = tvit.split()
	s = []
	for x in tvit2:
		if x[0] == c:
			s.append(izloci_besedo(x))
	return s

def zberi_se_zacne_z(tviti, c):
	s = []
	for tvit in tviti:
		a = se_zacne_z(tvit, c)
		for x in a:
			s.append(x)
	return unikati(s)

def vse_afne(tviti):
	return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
	return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
	vsi = vsi_avtorji(tviti) + vse_afne(tviti)
	vsi = sorted(unikati(vsi))
	return vsi

def custva(tviti, hashtagi):
	s = []
	for hash in hashtagi:
		hash = "#" + hash
		for tvit in tviti:
			tvit2 = tvit.split()
			if hash in tvit2:
				s.append(avtor(tvit))
	s = sorted(unikati(s))
	return s

def se_poznata(tviti, oseba1, oseba2):
	for tvit in tviti:
		if avtor(tvit) == oseba1 and oseba2 in se_zacne_z(tvit, "@") or avtor(tvit) == oseba2 and oseba1 in se_zacne_z(tvit, "@"):
			return True
	return False

# Konec naloge: Tviti

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

