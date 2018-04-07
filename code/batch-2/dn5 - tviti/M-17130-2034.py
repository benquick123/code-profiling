def unikati(s):
    unikati = []

    for unikat in s:

        if unikat in unikati:
            unikati = unikati

        else:
            unikati.append(unikat)

    return unikati

def avtor(tvit):
    i = 0
    avtor= []
    while i < len(tvit):
        if tvit[i] != ":":
            avtor.append(tvit[i])
        else:
            break
        i += 1
    avtor = "".join(avtor)
    return avtor

def vsi_avtorji(tviti):
    avtorji = []

    for tvit in tviti:

        avtorji.append(avtor(tvit))
    avtorji = unikati(avtorji)
    return avtorji

def izloci_besedo(beseda):
    i = 0

    while i < len(beseda):
        if beseda[i].isalnum():
            break
        else:
            beseda = beseda.replace(beseda[i],"")


    j = (len(beseda)-1)
    while beseda[j].isalnum() == False:
        beseda = beseda.replace(beseda[j], "")
        j = (len(beseda) - 1)
    return beseda

def se_zacne_z(tvit, c):
    i = 0
    j = 0
    besede = []
    beseda = []
    bes = ""
    while i < len(tvit)-1:
        if tvit[i] == c:
            j = i +1

            while tvit[j].isalnum():

                beseda.append(tvit[j])
                j += 1
                if j == len(tvit):
                    break

            bes = "".join(beseda)

            besede.append(bes)
            beseda = []
        i +=1
    return besede

def zberi_se_zacne_z(tviti, c):
    besede = []
    for tvit in tviti:
        besede += se_zacne_z(tvit, c)
    besede = unikati(besede)
    return besede

def vse_afne(tviti):
    afne = zberi_se_zacne_z(tviti, "@")
    return afne

def vsi_hashtagi(tviti):
    hashi = zberi_se_zacne_z(tviti, "#")
    return hashi

def vse_osebe(tviti):
    osebe= vsi_avtorji(tviti) + vse_afne(tviti)
    osebe = unikati(osebe)
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    imena = []


    for tvit in tviti:

        for hash in hashtagi:

            for hash_v_tvitu in se_zacne_z(tvit, "#"):
                if hash_v_tvitu == hash:
                    avtor1 = avtor(tvit)
                    imena.append(avtor1)

    imena = unikati(imena)
    imena.sort()
    return imena

def se_poznata(tviti, oseba1, oseba2):



    for tvit in tviti:
        avtor1 = avtor(tvit)
        if avtor1 == oseba1 and oseba2 in se_zacne_z(tvit, "@"):
            return True
        if avtor1 == oseba2 and oseba1 in se_zacne_z(tvit, "@") :
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

