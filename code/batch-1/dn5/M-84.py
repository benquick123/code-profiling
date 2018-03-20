import unittest

def unikati(s):
    prazen_seznam = []

    for i in s:                         # for i in s pomeni, da se i premika po vrednostih seznama s, NE PO INDEKSIH!
        if i not in prazen_seznam:
            prazen_seznam.append(i)

    return prazen_seznam


def avtor(tvit):
    seznam_razclembe = []
    seznam_razclembe = tvit.split(":")  #razclemba imena od ostalega besedila naprej od " : "
    return seznam_razclembe[0]

def vsi_avtorji(tviti):
    prazen_seznam_imen = []
    for i in tviti:
        s = avtor(i)                    #funkcija "avtor()", kot argument prejme string in ne seznam
        prazen_seznam_imen.append(s)

    return unikati(prazen_seznam_imen)

def izloci_besedo(beseda):
    for i in beseda:
        if not beseda[0].isalnum():
            beseda = beseda[1:]
        else:
            break

    od_zadaj = len(beseda) - 1              #od_zadaj je stevec iz desne proti levi ki se premika po besedi, -1 ker se indeksiranje zacne z 0
                                            # in konca z eno manj kot je dejansko dolg niz
    while od_zadaj >= 0:
        if not beseda[od_zadaj].isalnum():
            beseda = beseda[:od_zadaj]
        else:
            break
        od_zadaj-=1

    return beseda

def se_zacne_z(tvit, c):
    prazen_seznam = []
    rezultat = []
    prazen_seznam = tvit.split(" ")
    for s in prazen_seznam:
        if s[0] == c:
            rezultat.append(izloci_besedo(s))

    return rezultat

def zberi_se_zacne_z(tviti, c):
    rez = []
    for i in tviti:
        rez.extend(se_zacne_z(i,c))         # extend zdruzi dva seznama, ne uporabljaj "append"!!!

    return unikati(rez)

def vse_afne(tviti):
    return zberi_se_zacne_z(tviti, "@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    seznam_oseb = vsi_avtorji(tviti)
    seznam_oseb.extend(vse_afne(tviti))
    return sorted(unikati(seznam_oseb))

def custva(tviti, hashtagi):
    rez = []
    for i in tviti:
        avt = avtor(i)                    #dobim avtorja posameznega tvita
        seznam_hastagov = se_zacne_z(i, "#")
        for h in seznam_hastagov:
            if h in hashtagi:
                rez.append(avt)

    return sorted(unikati(rez))

def se_poznata(tviti, oseba1, oseba2):
    for i in tviti:
        avt = avtor(i)
        seznam_omemb = se_zacne_z(i, "@")
        for s in seznam_omemb:
            if avt == oseba1 and s == oseba2:
                return True
            elif avt == oseba2 and s == oseba1:
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

