import unittest

#naloga1
def unikati(s):
    a = []
    for x in s:
        if x not in a:
            a.append(x)

    return a

#naloga2
def avtor(tvit):
    ime = ""
    for crka in tvit:
        if crka == ":":
            break
        else:
            ime = ime + crka

    return ime

#naloga3
def vsi_avtorji(tviti):
    ime = ""
    seznamImen = []
    for tvit in tviti:
        for crka in tvit:
            if crka == ":":
                break
            else:
                ime = ime + crka

        if ime not in seznamImen:
            seznamImen.append(ime)

        ime = ""

    return seznamImen

#naloga4
def izloci_besedo(beseda):
    bes = beseda

    for crka in beseda:
        if not crka.isalnum():
            bes = bes[1:]
        else:
            break

    beseda = bes
    dolzina = len(beseda)

    for i in range(-1, -(dolzina + 1), -1):
        if not beseda[i].isalnum():
            bes = bes[:-1]
        else:
            break

    return bes

#naloga5
def se_zacne_z(tvit, c):
    bes = ""
    besede = []
    prepisuj = False
    dolzina = len(tvit)

    for i in range(0, dolzina):
        if tvit[i] == c:
            prepisuj = True

        if prepisuj == True and tvit[i].isspace():
            besede.append(bes)
            bes = ""
            prepisuj = False
        elif prepisuj == True and i == dolzina - 1:
            bes = bes + tvit[i]
            besede.append(bes)
            bes = ""
            prepisuj = False
        elif prepisuj == True:
            bes = bes + tvit[i]

    besedeFinal = []
    for beseda in besede:
        bes = izloci_besedo(beseda)
        besedeFinal.append(bes)

    return besedeFinal

#naloga6
def zberi_se_zacne_z(tviti, c):
    imena = []
    for tvit in tviti:
        imeDobljeno = se_zacne_z(tvit, c)
        if imeDobljeno:
            imena.append(imeDobljeno)

    i = []
    for var in imena:
        for ime in var:
            i.append(ime)

    return unikati(i)

#naloga7
def vse_afne(tviti):
    afne = []
    for tvit in tviti:
        afne.append(se_zacne_z(tvit, "@"))

    i = []
    for var in afne:
        for beseda in var:
            i.append(beseda)

    return unikati(i)

#naloga8
def vsi_hashtagi(tviti):
    has = []
    for tvit in tviti:
        has.append(se_zacne_z(tvit, "#"))

    i = []
    for var in has:
        for beseda in var:
            i.append(beseda)

    return unikati(i)

#naloga9
def vse_osebe(tviti):
    seznamImen1 = []
    seznamImen2 = []

    seznamImen1 = vsi_avtorji(tviti)
    seznamImen2 = zberi_se_zacne_z(tviti, "@")

    skupniSeznam = seznamImen1 + seznamImen2

    urejenSeznam = unikati(skupniSeznam)
    urejenSeznam.sort()

    return urejenSeznam

#dodatna naloga 1
def custva(tviti, hashtagi):
    seznamImen = []

    for tvit in tviti:
        ime = avtor(tvit)
        seznam = se_zacne_z(tvit, "#")

        if(len(seznam) != 0):
            for beseda in seznam:
                for has in hashtagi:
                    if (has == beseda):
                        seznamImen.append(ime)

    urejenSeznamImen = unikati(seznamImen)
    urejenSeznamImen.sort()

    return urejenSeznamImen

#dodatna naloga 2
def se_poznata(tviti, oseba1, oseba2):

    for tvit in tviti:
        ime = avtor(tvit)

        if ime == oseba1:
            seznamBesed = se_zacne_z(tvit, "@")

            if len(seznamBesed) != 0:
                for beseda in seznamBesed:
                    if beseda == oseba2:
                        return True

        elif ime == oseba2:
            seznamBesed = se_zacne_z(tvit, "@")

            if len(seznamBesed) != 0:
                for beseda in seznamBesed:
                    if(beseda == oseba1):
                        return True

    return False

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

