
tviti = ["sandra: Spet ta dež. #dougcajt",
         "berta: @sandra Delaj domačo za #programiranje1",
         "sandra: @berta Ne maram #programiranje1 #krneki",
         "ana: kdo so te @berta, @cilka, @dani? #krneki",
         "cilka: jst sm pa #luft",
         "benjamin: pogrešam ano #zalosten",
         "ema: @benjamin @ana #split? po dvopičju, za začetek?"]


def unikati(s):
    c = int(input("vnesi število:  "))
    for x in c :
        if x in unikati(s):
            break
        else:
            unikati(s).append(c)

def avtor(tvit):
    ime = [("sandra" , "berta ", "ana", "cilka", "benjamin", "ema")]
    for k in (tviti):
        if k in tviti and k == ime:
            return k

def vsi_avtorji(tviti):
    avtor = []
    for ime in tviti:
        if ime in tviti and ime not in vsi_avtorji(tviti):
            avtor.append(tviti)


def izloci_besedo(beseda):
    for znake in beseda:
        if znake == str:
            return beseda

        else:
            beseda.replace(znake, "")


def se_zacne_z(tvit, c):
    tvit = ""
    c = ""
    for t in tvit.split():
        if t.startswith('c'):
            if t == str:
                return t
            else:
                t.replace(tviti, "")

def zberi_se_zacne_z(tviti, c):
    tvit = ""
    c = ""
    for t in tvit.split():
        if t.startswith('c'):
            if t == str:
                if t not in tvit:
                    return t
                else:
                    break

            else:
                t.replace(tviti, "")
                if t not in tvit:
                    return t
                else:
                    break

def vse_afne(tviti):
    for y in tviti:
        if y.startswith("@"):
            y.replace("@", "")
            return y

def vsi_hashtagi(tviti):
    for hash in tviti:
        if hash.startswith("#"):
           hash.replace("#", "")
           return hash

def vse_osebe(tviti):
    ime = [("sandra", "berta ", "ana", "cilka", "benjamin", "ema")]
    for vse in tviti:
        if vse in ime:
            return  ime




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


if __name__ == "__main__":
    unittest.main()














