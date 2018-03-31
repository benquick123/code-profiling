import unittest

def unikati(s):
    seznam = []
    for x in s:
        if x not in seznam:
            seznam.append(x)
    return seznam

def avtor(tviti):
    tvit= tviti.split(':')
    return tvit[0]

def vsi_avtorji(tviti):
    avtorji = []
    for x in tviti:
        ime, tvit = x.split(':')
        if ime not in avtorji:
            avtorji.append(ime)
    return avtorji

def izloci_besedo(beseda):
    sez = list(beseda)
    for x in list(beseda):
        if not x.isalpha():
            del sez[0]
        elif x.isalpha():
            break
    for x in reversed(list(beseda)):
        if not x.isalpha():
            del sez[-1]
        elif x.isalpha():
            break
    sez = ''.join(sez)
    return sez

def se_zacne_z(tvit, c):
    besede = tvit.split()
    sez = []
    for x in besede:
        if x.startswith(c):
            sez.append(x)
    print(sez)
    sez1 = sez
    st = 0
    for x in sez1:
        sez[st] = x.lstrip(c)
        st += 1
    st = 0
    sez1 = sez
    print(sez)
    for x in sez1:
        if not x.isalpha():
            el = sez[st]
            sez[st] = el[:-1]
        st += 1

    return sez

def zberi_se_zacne_z(tviti, c):
    sez = []
    for tvit in tviti:
        besede = tvit.split()
        for x in besede:
            if x.startswith(c):
                sez.append(x)

    sez1 = sez
    st = 0
    for x in sez1:
        sez[st] = x.lstrip(c)
        st += 1
    st = 0

    for x in sez:
        if x[-1].isdigit():
            break
        else:
            if not x.isalpha():
                el = sez[st]
                sez[st] = el[:-1]
            st += 1

    imena = []
    for x in sez:
        if not x in imena:
            imena.append(x)
    return imena

def vse_afne(tviti):
    c = '@'
    sez = []
    for tvit in tviti:
        besede = tvit.split()
        for x in besede:
            if x.startswith(c):
                sez.append(x)

    sez1 = sez
    st = 0
    for x in sez1:
        sez[st] = x.lstrip(c)
        st += 1
    st = 0

    for x in sez:
        if x[-1].isdigit():
            break
        else:
            if not x.isalpha():
                el = sez[st]
                sez[st] = el[:-1]
            st += 1

    imena = []
    for x in sez:
        if not x in imena:
            imena.append(x)
    return imena

def vsi_hashtagi(tviti):
    c = '#'
    sez = []
    for tvit in tviti:
        besede = tvit.split()
        for x in besede:
            if x.startswith(c):
                sez.append(x)

    sez1 = sez
    st = 0
    for x in sez1:
        sez[st] = x.lstrip(c)
        st += 1
    st = 0

    for x in sez:
        if x[-1].isdigit():
            break
        else:
            if not x.isalpha():
                el = sez[st]
                sez[st] = el[:-1]
            st += 1

    imena = []
    for x in sez:
        if not x in imena:
            imena.append(x)
    return imena

def vse_osebe(tviti):
    c = '@'
    sez = []
    for tvit in tviti:
        st = 0
        imena = []
        besede = tvit.split()
        for x in besede:
            if st == 0:
                imena.append(x)
            if x.startswith(c):
                sez.append(x)
            st += 1

    sez1 = sez
    st = 0
    for x in sez1:
        sez[st] = x.lstrip(c)
        st += 1
    st = 0

    for x in sez:
        if x[-1].isdigit():
            break
        else:
            if not x.isalpha():
                el = sez[st]
                sez[st] = el[:-1]
            st += 1


    for x in sez:
        if not x in imena:
            imena.append(x)
    st = 0
    for x in imena:
        if x[-1].isdigit():
            break
        else:
            if not x.isalpha():
                el = imena[st]
                imena[st] = el[:-1]
            st += 1

    imena.sort()
    return imena



class TestTviti(unittest.TestCase):
    tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split ? po dvopičju, za začetek?",
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

