import unittest


def unikati(s):
    tmp = []
    for i in s:
        if i not in tmp:
            tmp.append(i)
    return tmp

def avtor(tvit):
    besede = tvit.split()
    author = besede[0]
    author = list(author)
    author.pop()
    author = ''.join(author)
    return author

def vsi_avtorji(tviti):
    list_avtorjev = []
    for t in tviti:
        list_avtorjev.append(avtor(t))
    return unikati(list_avtorjev)

def izloci_besedo(beseda):
    # string razibjem v list
    beseda = list(beseda)
    # dokler prvi element v listu beseda ni alfanumerična ponavljaj
    while not(beseda[0].isalnum()):
        # izbriši prvi element lista ( ker ni alfanumeričen )
        del(beseda[0])
    # isti princip kot zgornja zanka, samo da preverjam od odzadaj
    while not(beseda[-1].isalnum()):
        del(beseda[-1])
    beseda = ''.join(beseda)
    return beseda

def se_zacne_z(tvit, c):
    tvit = tvit.split()
    besede_s_pravo_zacetnico = []
    for beseda in tvit:
        if beseda[0] == c:
            besede_s_pravo_zacetnico.append(izloci_besedo(beseda))
    return besede_s_pravo_zacetnico

def zberi_se_zacne_z(tviti,c):
    besede = []
    for tvit in tviti:
        if se_zacne_z(tvit, c) != []:
            besede += se_zacne_z(tvit,c)
    besede = unikati(besede) #['sandra', 'berta', 'cilka', 'dani', 'benjamin', 'ana']
    return besede

def vse_afne(tviti):
    afne = []
    for tvit in tviti:
        afne += se_zacne_z(tvit,'@')
    afne = unikati(afne)
    return afne

def vsi_hashtagi(tviti):
    hashtagi =[]
    for tvit in tviti:
        hashtagi += se_zacne_z(tvit, '#')
    hashtagi = unikati(hashtagi)
    return hashtagi

def vse_osebe(tviti):
    osebe = vsi_avtorji(tviti)
    osebe += vse_afne(tviti)
    osebe = list(set(osebe))
    osebe.sort()
    return osebe

# za to resitev po vsej vrjetnosti obstaja boljsa resitev, vendar si nisem uzel časa da bi jo našel
def custva(tviti, hashtagi):
    avtorji = []
    for tvit in tviti:
        hashtag = se_zacne_z(tvit, '#')
        for h in hashtag:
            if h in hashtagi:
                avtorji.append(avtor(tvit))

    avtorji = list(set(avtorji))
    avtorji.sort()
    return avtorji

def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            omenjen = se_zacne_z(tvit, '@')
            if oseba2 in omenjen:
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

