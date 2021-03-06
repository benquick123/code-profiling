def unikati(s):
    seznam = []
    for _ in s:
        if _ not in seznam:
            seznam.append(_)
    return seznam

def avtor(tvit):
    return tvit.split(':')[0]

def vsi_avtorji(tviti):
    return unikati(split[0] for split in (x.split(':') for x in tviti))

def izloci_besedo(beseda):
    '''
    for i, crka in enumerate(beseda):
        if crka.isalpha():
            index1 = i
            break
    for i, crka in enumerate(reversed(beseda)):
        if crka.isalpha():
            index2 = len(beseda) - i
            break
    return(beseda[int(index1):int(index2)])
    '''
    return ','.join(vrnjena for vrnjena in beseda if vrnjena.isalnum() != False or vrnjena == '-').replace(',', '')

def se_zacne_z(tvit, c):
    s = []
    seznam = list(word.strip(c) for word in tvit.split() if word.startswith(c))
    for _ in seznam:
        if _.isalnum() == False:
            s.append(izloci_besedo(_))
        else:
            s.append(_)
    return s  

def zberi_se_zacne_z(tviti, c):
    seznam = []
    for beseda in tviti:
        temp = beseda.split()
        for _ in temp:
            if _.startswith(c):
                if _.isalnum() == False:
                    seznam.append(izloci_besedo(_))
                else:
                    seznam.append(_)
    return unikati(seznam)

def vse_afne(tviti):
    seznam = []
    for beseda in tviti:
        s = beseda.split()
        for _ in s:
            if _.startswith('@'):
                if _.isalnum() == False:
                    seznam.append(izloci_besedo(_))
                else:
                    seznam.append(_)
    return unikati(seznam)

def vsi_hashtagi(tviti):
    seznam = []
    for beseda in tviti:
        s = beseda.split()
        for _ in s:
            if _.startswith('#'):
                if _.isalnum() == False:
                    seznam.append(izloci_besedo(_))
                else:
                    seznam.append(_)
    return unikati(seznam)

def vse_osebe(tviti):
    seznam = vse_afne(tviti)
    s = vsi_avtorji(tviti)
    for ime in s:
        if ime not in seznam:
            seznam.append(ime)
    return sorted(seznam)    

def custva(tviti, hashtagi):
    s = []
    for hashtag in hashtagi:
        tempHashtag = hashtag
        for beseda in tviti:
            if tempHashtag in beseda:
                s.append(avtor(beseda))
    return unikati(sorted(s))

def se_poznata(tviti, oseba1, oseba2):
    s = vse_osebe(tviti)
    if oseba1 in s and oseba2 in s:
        for beseda in tviti:
            if oseba1 in beseda and oseba2 in beseda:
                return True
    else:
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

