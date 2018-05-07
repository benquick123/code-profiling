#DN5

#Obvezna naloga(1): unikati
def unikati(s):
    seznam = []
    for unikat in s:
        if unikat not in seznam:
            seznam.append(unikat)
    return seznam

#Obvezna naloga(2): avtor

def avtor(tvit):
    a = tvit.split (":")
    return (a[0])

#Obvezna naloga(3): vsi avtorji

def vsi_avtorji(tviti):
    seznam = []
    for e in tviti:
        a = e.split (":")
        if a[0] not in seznam:
            seznam.append (a[0])
    return seznam

#Obvezna naloga(4): izloci besedo

def izloci_besedo(beseda):
    for e in beseda:
        if e[0].isalnum () == False:
            beseda = beseda[1:]
        else:
            break
    for e in beseda:
        if beseda[-1].isalnum ():
            break
        else:
            beseda = beseda[:-1]
    return beseda


###nacin:2
###imoprt re
###def izloci_besedo(beseda):
###   if beseda.isalnum () == True:
###       return beseda
###   else:
###       iskano = re.compile ('^\W+|\W+$')
###       for znak in beseda:
###           izloceno = iskano.sub ("", beseda)
###       return izloceno
###
###
###nacin: 3
###def izloci_besedo(beseda):
###   if beseda.isalnum () == True:
###       return beseda
###   else:
###       for spredaj in enumerate (beseda):
###           zacetek, iskana_beseda = spredaj
###           if iskana_beseda.isalnum ():
###               break
###           for zadaj in enumerate (beseda[::-1]):
###               konec, iskana_beseda = zadaj
###               if iskana_beseda.isalnum ():
###                   break
###       return beseda[zacetek:len (beseda) - konec]
###
###nacin:4
###import re
###def izloci_besedo(beseda):
###   return re.sub("^\W+|\W+$", "", beseda)

#Obvezna naloga(5): se zacne z

def se_zacne_z(tvit, c):
    spredaj_urejen = []
    urejen = []
    besede = tvit.split (" ")
    for e in besede:
        if e[0] == c:
            spredaj_urejen.append (e[1:])
    for e in spredaj_urejen:
        if e[-1].isalnum () == False:
            e = e[:-1]
            urejen.append (e)
        else:
            urejen.append (e)
    return urejen

#Obvezna naloga(6): zberi se zacne z

def zberi_se_zacne_z(tviti, c):
    spredaj_urejen = []
    urejen = []
    sortiran = []
    for e in tviti:
        beseda = e.split (" ")
        for znak in beseda:
            if znak not in spredaj_urejen:
                if znak[0] == c:
                    spredaj_urejen.append (znak[1:])
        for znak in spredaj_urejen:
            if znak[-1].isalnum () == False:
                znak = znak[:-1]
                urejen.append (znak)
            else:
                urejen.append (znak)
    for d in urejen:
        if d not in sortiran:
            sortiran.append (d)
    return sortiran

#Obvezna naloga(7): vse afne

def vse_afne(tviti):
    spredaj_urejen = []
    urejen = []
    sortiran = []
    for e in tviti:
        a = e.split (" ")
        for g in a:
            if g not in spredaj_urejen:
                if g[0] == "@":
                    spredaj_urejen.append (g[1:])
        for g in spredaj_urejen:
            if g[-1].isalnum () == False:
                g = g[:-1]
                urejen.append (g)
            else:
                urejen.append (g)
    for d in urejen:
        if d not in sortiran:
            sortiran.append (d)
    return sortiran

#Obvezna naloga(8): vsi hashtagi

def vsi_hashtagi(tviti):
    spredaj_urejen = []
    urejen = []
    sortiran = []
    for e in tviti:
        a = e.split (" ")
        for g in a:
            if g not in spredaj_urejen:
                if g[0] == "#":
                    spredaj_urejen.append (g[1:])
        for g in spredaj_urejen:
            if g[-1].isalnum () == False:
                g = g[:-1]
                urejen.append (g)
            else:
                urejen.append (g)
    for d in urejen:
        if d not in sortiran:
            sortiran.append (d)
    return sortiran

#Obvezna naloga(9): vse osebe

def vse_osebe(tviti):
    spredaj_urejen = []
    urejen = []
    sortiran = []
    for e in tviti:
        a = e.split (" ")
        for g in a:
            if g not in spredaj_urejen:
                if g[0] == "@":
                    spredaj_urejen.append (g[1:])
        for g in spredaj_urejen:
            if g[-1].isalnum () == False:
                g = g[:-1]
                urejen.append (g)
            else:
                urejen.append (g)
    for d in urejen:
        if d not in sortiran:
            sortiran.append (d)
    for avtor in tviti:
        av = avtor.split (":")
        if av[0] not in sortiran:
            sortiran.append (av[0])
    return sorted(sortiran)
















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

