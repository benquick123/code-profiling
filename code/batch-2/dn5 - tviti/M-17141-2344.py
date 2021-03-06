# tweets



# tweets
tweets = ["sandra: Spet ta dež. #dougcajt",
          "berta: @sandra Delaj domačo za #programiranje1",
          "sandra: @berta Ne maram #programiranje1 #krneki",
          "ana: kdo so te @berta, @cilka, @dani? #krneki",
          "cilka: jst sm pa #luft",
          "benjamin: pogrešam ano #zalosten",
          "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


def unikati(s):
    novi = []
    for e in s:
        if e not in novi:
            novi.append(e)
    return novi


# print(unikati(['d','c','b','c']))

def avtor(tvit):
    for e in tvit.split():
        e = e.replace(":", "")
        return e


# print(avtor("ana: kdo so te??"))

def vsi_avtorji(tviti):
    vsi = []
    for tvit in tviti:
        vsi.append(avtor(tvit))
    return unikati(vsi)


# print(vsi_avtorji(["ana: kdo so te??","janc: kdo so te??","junc: kdo so te??","ana: kdo so te??","rin: kdo so te??"]))

def izloci_besedo(beseda):
    if beseda.isalnum():
        return (beseda)
    else:
        for i in beseda.strip():
            if i.isalnum() is True:
                pass
            else:
                if i == "-":
                    pass
                else:
                    beseda = beseda.replace(i, "")
        return beseda


# print(izloci_besedo("@janez-novak!!!!"))

def se_zacne_z(tvit, c):
    rez = []
    for beseda in tvit.split():
        if beseda[0] == c:
            beseda = izloci_besedo(beseda)
            rez.append(beseda)
    return rez


def se_zacne_z_nejceva(tviti, c):
    rez = []
    for tvit in tviti:
        for beseda in tvit.split():
            if beseda[0] == c:
                beseda = izloci_besedo(beseda)
                rez.append(beseda)
    return rez


def zberi_se_zacne_z(tviti, c):
    return unikati(se_zacne_z_nejceva(tviti, c))


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")


def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")


def vse_osebe(tviti):
    return sorted(unikati(vse_afne(tviti) + vsi_avtorji(tviti)))


def custva(tviti, hashtagi):
    avtorji = []
    for i in hashtagi:
        for tvit in tviti:
            if i in tvit:
                avtorji.append(avtor(tvit))
    return sorted(unikati(avtorji))


# print(custva(tweets, ["krneki", "dougcajt"]))

def se_poznata(tviti, oseba1, oseba2):

  if (oseba1 not in vse_osebe(tviti)) | (oseba2 not in vse_osebe(tviti)):
    return False

  for tvit in tviti:
    if avtor(tvit) == oseba1:
      for beseda in tvit.split():
        if oseba2 == izloci_besedo(beseda):
          return True
    elif avtor(tvit) == oseba2:
      for beseda in tvit.split():
        if oseba1 == izloci_besedo(beseda):
          return True


#print(se_poznata(tweets, "ana", "benjamin"))


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










