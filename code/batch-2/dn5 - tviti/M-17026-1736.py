'''
    avtor: Blaž Kumer
    opis: Različne naloge s stringi in seznami in operacijami nad stringi
    datum: 12. 11. 2017

'''




import unittest

def unikati(s):
    if len(s)!=0:
        uni=[s[0]]
        for pod in s:
            for poda in uni:
                if pod==poda:
                    break
            else:
                uni.append(pod)
        return uni
    else:
        return []

def avtor(str):
    s=str.split(":")
    return s[0]

def vsi_avtorji(tviti):
    seznam=[]
    for tvit in tviti:
        s=tvit.split(":")
        seznam.append(s[0])
    return unikati(seznam)

def izloci_besedo(beseda):
    while True:
        if len(beseda)!=0:
            x=beseda[0]
            if x.isalnum():
                break
            else:
                beseda=beseda[1:]
    while True:
        if len(beseda)!=0:
            x=beseda[-1]
            if x.isalnum():
                break
            else:
                beseda=beseda[:-1]
    return beseda

def se_zacne_z(tviti,c):
    kandidati=[]
    seznam=tviti.split(" ")
    for str in seznam:
        if str[0]==c:
            kandidati.append(str)
    for i in range(len(kandidati)):
        kandidati[i]=izloci_besedo(kandidati[i])
    return kandidati

def zberi_se_zacne_z(tviti,c):
    kandidati=[]
    for i in tviti:
        seznam = i.split(" ")
        for el in seznam:
            if el[0]==c:
                kandidati.append(el)
    for i in range(len(kandidati)):
        kandidati[i]=izloci_besedo(kandidati[i])
    return unikati(kandidati)

def vse_afne(tviti):
    kandidati = []
    for i in tviti:
        seznam = i.split(" ")
        for el in seznam:
            if el[0] == "@":
                kandidati.append(el)
    for i in range(len(kandidati)):
        kandidati[i]=izloci_besedo(kandidati[i])
    return unikati(kandidati)

def vsi_hashtagi(tviti):
    kandidati = []
    for i in tviti:
        seznam = i.split(" ")
        for el in seznam:
            if el[0] == "#":
                kandidati.append(el)
    for i in range(len(kandidati)):
        kandidati[i]=izloci_besedo(kandidati[i])
    return unikati(kandidati)

def vse_osebe(tviti):
    kandidati = []
    for i in tviti:
        seznam = i.split(" ")
        kandidati.append(seznam[0])
        for el in seznam:
            if el[0] == "@":
                kandidati.append(el)
    for i in range(len(kandidati)):
        kandidati[i] = izloci_besedo(kandidati[i])
    kandidati=unikati(kandidati)
    return sorted(kandidati)

def custva(tviti,hashtagi):
    koncni=[]
    for i in range(len(tviti)):
        s=tviti[i].split(" ")
        for x in s:
            if x[0]=="#":
                x=izloci_besedo(x)
                for h in hashtagi:
                    if x==h:
                        koncni.append(izloci_besedo(s[0]))
    koncni=unikati(koncni)
    return sorted(koncni)

def se_poznata(tviti,o1,o2):
    kanTv=[]
    for t in tviti:
        if t.startswith(o1) or t.startswith(o2):
            kanTv.append(t)
    for x in kanTv:
        tv=x.split(" ")
        for t in tv:
            if t.startswith("@"):
                if  izloci_besedo(t)==o1 or izloci_besedo(t)==o2:
                    return True
    return False
tviti = [
        "sandra: Spet ta dež. #dougcajt",
        "berta: @sandra Delaj domačo za #programiranje1",
        "sandra: @berta Ne maram #programiranje1 #krneki",
        "ana: kdo so te @berta, @cilka, @dani? #krneki",
        "cilka: jst sm pa #luft",
        "benjamin: pogrešam ano #zalosten",
        "ema: @benjamin @ana #split? po dvopičju, za začetek?",
    ]
print(se_poznata(tviti, "sandra","berta"))


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
