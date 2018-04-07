import unittest

def unikati(s):                     #prejme seznam nekih stvari in kot rezultat vrne nov seznam, v katerem se vsak element pojavi le enkrat.
    s1 = []
    for i in s:
        if i not in s1:
            s1.append(i)
    return s1

def avtor(tvit):                    #vrne ime avtorja podanega tvita
    for a in tvit.split(":"):
        return a

def vsi_avtorji(tviti):             #prejme seznam tvitov in vrne seznam vseh njihovih avtorjev
    s = []
    for a in (tviti):
        s.append(avtor(a))
    return unikati(s)

def izloci_besedo(beseda):          #vrne besedo brez vseh ne-alfanumeričnih znakov
    i = 0
    b = 0
    s = beseda[::-1]
    for a in list(s):
        if not a.isalpha():
            i = i + 1
        else:
            break

    for a in list(beseda):
        if not a.isalpha():
            b = b + 1
        else:
            break

    while i > 0:
        beseda = beseda[:-1]
        i = i - 1

    while b > 0:
        beseda = beseda[1:]
        b = b - 1

    n=""
    for a in beseda:
        if a == "-":
            n = n + a
        if a.isalnum():
             n = n + a
    return n

def se_zacne_z(tvit, c):            #prejme nek tvit in nek znak. Vrnevse tiste besede iz tvita, ki se začnejo s podanim znakom# . Pri tem mora od besed odluščiti vse nealfanumerične znake na začetku in na koncu.
    s = ""
    l = []
    for a in tvit.split():
        if a[0] == c:
            for b in a:
                if b.isalnum():
                    s = s + b
            if s:
                l.append(s)
                s = ""
    return l

def zberi_se_zacne_z(tviti, c):     #podobna prejšnji, vendar prejme seznam tvitov in vrne vse besede, ki se pojavijo v njih in se začnejo s podano črko. Poleg tega naj se vsaka beseda pojavi le enkrat.
    s = ""
    l = []
    for b in tviti:
        for a in b.split():
            if a[0] == c:
                for b in a:
                    if b.isalnum():
                        s = s + b
                if s:
                    l.append(s)
                    s = ""
    return unikati(l)

def vse_afne(tviti):
    s = ""
    l = []
    for b in tviti:
        for a in b.split():
            if a[0] == "@":
                for b in a:
                    if b.isalnum():
                        s = s + b
                if s:
                    l.append(s)
                    s = ""
    return unikati(l)

def vsi_hashtagi(tviti):
    s = ""
    l = []
    for b in tviti:
        for a in b.split():
            if a[0] == "#":
                for b in a:
                    if b.isalnum():
                        s = s + b
                if s:
                    l.append(s)
                    s = ""
    return unikati(l)

def vse_osebe(tviti):
    a1 = []
    for a in tviti:
        a1.append(avtor(a))
    a2 = unikati(a1)

    a3 = vse_afne(tviti)
    a2 = a2 + unikati(a3)
    return sorted(unikati(a2))

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

