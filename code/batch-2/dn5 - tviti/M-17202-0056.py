

def unikati(s):
    seznam=[]
    seznam.clear()
    for x in s:
        if x not in seznam:
            seznam.append(x)

    return seznam

def avtor(tvit):
    return tvit.split(": ",1)[0]

def vsi_avtorji(tviti):
    seznam_avtorji=[]
    seznam_avtorji.clear()
    for i in tviti:
        seznam_avtorji.append(avtor(i))

    return unikati(seznam_avtorji)

def izloci_besedo(beseda):
    wrd=list(beseda)
    while True:
        if not (wrd[0].isalnum()):
            del wrd[0]
        else:break

    while True:
        if not (wrd[len(wrd)-1].isalnum()):
            del wrd[len(wrd)-1]
        else:break

    wrd="".join(wrd)
    return wrd

def se_zacne_z(tvit, c):
    z=tvit.split(" ")
    l=[]
    for i in z:
        if i.startswith(c):
            l.append(izloci_besedo(i))
    if l==[]:
        return
    else:
        return l

def zberi_se_zacne_z(tviti, c):
    lt=[]
    for i in tviti:
        l=se_zacne_z(i,c)
        if l!=None:
            for j in l:
                    lt.append(j)

    return unikati(lt)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def unija(s1, s2):
    return list(set(s1) | set(s2))


def vse_osebe(tviti):
    osebe=unija(vsi_avtorji(tviti),vse_afne(tviti))
    osebe.sort()
    return osebe

def custva(tviti, hashtagi):
    osebe=[]
    for i in tviti:
        for j in hashtagi:
            if j in i:
                osebe.append(avtor(i))
    osebe=unikati(osebe)
    osebe.sort()
    return osebe

def se_poznata(tviti, oseba1, oseba2):
    if oseba1 in vse_osebe(tviti) and oseba2 in vse_osebe(tviti) and (oseba1 in vsi_avtorji(tviti) or oseba2 in vsi_avtorji(tviti)):
        for i in tviti:
            if oseba1==avtor(i):
                if i.find(oseba2)>0:
                    return True
            elif oseba2 ==avtor(i):
                if i.find(oseba1)>0:
                    return True

        return False
    else:return False




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

