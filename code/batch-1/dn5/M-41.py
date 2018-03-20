def unikati(s):
    novi = []
    for del_seznama in s:
        if del_seznama in novi:
            None
        else:
            novi.append(del_seznama)
    return novi
def avtor(tvit):
    return tvit.split( )[0][:-1]
def vsi_avtorji(tviti):
    avtorji =[]
    for tvit in tviti:
        avtorji.append(avtor(tvit))
    return unikati(avtorji)
def izloci_besedo(beseda):
    i= 0
    while i < len(beseda):
        if not str.isalnum(beseda[i]):
            beseda = beseda[i + 1:]
        else:
            break
    for i in range(len(beseda)):
        if i < len(beseda):
            if not str.isalnum(beseda[-1 - i]):
                beseda = beseda[:-1-i]
            else:
                break
    return beseda
def se_zacne_z(tvit, c):
    se_zacnejo =[]
    tvit = tvit.split( )
    for beseda in tvit:
        if beseda[0] == c:
            se_zacnejo.append(izloci_besedo(beseda))
    return se_zacnejo
def zberi_se_zacne_z(tviti, c):
    a = []
    besede = []
    for tvit in tviti:
        if c in tvit:
            besede_v_tvitu = se_zacne_z(tvit,c)
            a = a + besede_v_tvitu
    return unikati(a)
def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")
def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti,"#")
def po_abecedi(imena):
    urejena = []
    while len(imena) != 0:
        najmanjse_ime = "zzzzzzzzz"
        for ime in imena:
            if ime < najmanjse_ime:
                najmanjse_ime=ime
        imena.remove(najmanjse_ime)
        urejena.append(najmanjse_ime)
    return urejena
def vse_osebe(tviti):
    vsi = unikati(vsi_avtorji(tviti) + vse_afne(tviti))
    return po_abecedi(vsi)
def custva(tviti, hashtagi):
    imena = []
    for tvit in tviti:
        for hashtag in hashtagi:
            if hashtag in tvit:
                imena.append(avtor(tvit))
    return po_abecedi(unikati(imena))
def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1 and oseba2 in vse_afne(tvit.split( )) or oseba2 == avtor(tvit) and oseba1 in vse_afne(tvit.split( )):
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

