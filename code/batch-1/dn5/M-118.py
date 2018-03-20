import unittest

def unikati(s):
    unik = []
    for i in s:
        if i in unik:
            continue
        unik.append(i)
    return unik

def avtor(tvit):
    avt = tvit.split(":")[0]
    return avt

def vsi_avtorji(tviti):
    va = []
    for tvit in tviti:
        avt = tvit.split(":")[0]
        if avt in va:
            continue
        va.append(avt)
    return va

def izloci_besedo(beseda):
    for i in beseda:
        if i.isalnum():
            break
        beseda = beseda.replace(i, "")
    for i in beseda[::-1]:
        if i.isalnum():
            break
        beseda = beseda.replace(i, "")
    return beseda

def se_zacne_z(tvit, c):
    szz = tvit.split()
    words_with_c = []
    for i in szz:
        if i.startswith(c):
            words_with_c.append(izloci_besedo(i))
    return words_with_c

def zberi_se_zacne_z(tviti, c):
    words_with_c = []
    for tvit in tviti:
        szz = tvit.split()
        for i in szz:
            if i.startswith(c) and izloci_besedo(i) not in words_with_c:
                words_with_c.append(izloci_besedo(i))
    return words_with_c

smartass = False
def vse_afne(tviti):
    if not smartass:
        handles = []
        for tvit in tviti:
            szz = tvit.split()
            for i in szz:
                if i.startswith("@") and izloci_besedo(i) not in handles:
                    handles.append(izloci_besedo(i))
        return handles
    else:
        return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    if not smartass:
        hashtags = []
        for tvit in tviti:
            szz = tvit.split()
            for i in szz:
                if i.startswith("#") and izloci_besedo(i) not in hashtags:
                    hashtags.append(izloci_besedo(i))
        return hashtags
    else:
        return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti)
    handles = vse_afne(tviti)
    for i in handles:
        if i not in osebe:
            osebe.append(i)
    return sorted(osebe)









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

