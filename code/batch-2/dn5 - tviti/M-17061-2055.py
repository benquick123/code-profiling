import unittest

def unikati(s):
    u = []
    for item in s:
        if not item in u:
            u.append(item)
    return u


def avtor(tvit):
    return tvit.split(":")[0]


def vsi_avtorji(tviti):
    avtorji = []
    for t in tviti:
        a = avtor(t)
        if not a in avtorji:
            avtorji.append(a)
    return avtorji


def izloci_besedo(beseda):
    seznam_crk = list(beseda)
    i = 0
    while i < len(seznam_crk):
        if not seznam_crk[i].isalnum():
            del seznam_crk[i]
            i=0
        else:
            break
    j = len(seznam_crk)-1
    while j >= 0:
        if not seznam_crk[j].isalnum():
            seznam_crk.pop(j)
        else: break
        j-=1
    return "".join(seznam_crk)

def se_zacne_z(tvit, c):
    besede = tvit.split()
    ujemajoce_besede = []
    for b in besede:
        if b[0] == c:
            ujemajoce_besede.append(izloci_besedo(b))
    return ujemajoce_besede


def zberi_se_zacne_z(tviti, c):
    vse_ujemajoce_besede = []
    for t in tviti:
        vse_ujemajoce_besede.extend(se_zacne_z(t,c))
    unikatne_ujemajoce_besede = []
    for b in vse_ujemajoce_besede:
        if not b in unikatne_ujemajoce_besede:
            unikatne_ujemajoce_besede.append(b)
    return unikatne_ujemajoce_besede


def vse_afne(tviti):
    return zberi_se_zacne_z(tviti,"@")

def vsi_hashtagi(tviti):
    return zberi_se_zacne_z(tviti, "#")

def vse_osebe(tviti):
    podvojene_osebe = []
    podvojene_osebe.extend(vse_afne(tviti))
    podvojene_osebe.extend(vsi_avtorji(tviti))
    vse_osebe_unikatne = []
    for o in podvojene_osebe:
        if not o in vse_osebe_unikatne:
            vse_osebe_unikatne.append(o)
    return sorted(vse_osebe_unikatne)


def custva(tviti, hashtagi):
    avtorji_hashtagov_podvojeni = []
    for tvit in tviti:
        for hashtag in se_zacne_z(tvit,"#"):
            if hashtag in hashtagi:
                avtorji_hashtagov_podvojeni.append(avtor(tvit))
                break
    unikatni_avtorji = []
    for a in avtorji_hashtagov_podvojeni:
        if not a in unikatni_avtorji:
            unikatni_avtorji.append(a)
    return sorted(unikatni_avtorji)


def se_poznata(tviti, oseba1, oseba2):
    tviti_prve = []
    tviti_druge = []
    for tvit in tviti:
        if avtor(tvit) == oseba1:
            tviti_prve.append(tvit)
        if avtor(tvit) == oseba2:
            tviti_druge.append(tvit)
    mentioni_prve = []
    mentioni_druge = []
    for t1 in tviti_prve:
        mentioni_prve.extend(se_zacne_z(t1,"@"))
    for t2 in tviti_druge:
        mentioni_druge.extend(se_zacne_z(t2,"@"))
    if oseba1 in mentioni_druge: return True
    if oseba2 in mentioni_prve: return True
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

