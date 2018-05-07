import unittest

def unikati(s):
    nov = []
    for item in s:
        if item not in nov:
            nov.append(item)
    return nov


def avtor(tvit):
    nov = ""
    for item in tvit:
        if item == ":":
            break
        nov += item
    return nov


def vsi_avtorji(tviti):
    nov1 = ""
    nov2 = []
    for item in tviti:
        niz = str(item)
        for i in niz:
            if i == ":":
                if nov1 not in nov2:
                    nov2.append(nov1)
                nov1 = ""
                break
            nov1 += i
    return nov2


def izloci_besedo(beseda):
    for item in beseda:
        if not item.isalnum():
            beseda = beseda.replace(item, "")
        else:
            break
    besedar = beseda[::-1]
    for i in besedar:
        if not i.isalnum():
            besedar = besedar.replace(i, "")
        else:
            break
    return besedar[::-1]


def se_zacne_z(tvit, c):
    nov = tvit.split(" ")
    niz = []
    n = []
    for item in nov:
        if item.startswith(c):
            niz.append(item)

    for item in niz:
        for i in item:
            if not i.isalnum():
                item = item.replace(i, "")
            else:
                break
        itemr = item[::-1]
        for j in itemr:
            if not j.isalnum():
                itemr = itemr.replace(j, "")
            else:
                break
        n.append(itemr[::-1])
    return n


def zberi_se_zacne_z(tviti, c):
    niz = []
    n = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i not in niz and i.startswith(c):
                niz.append(i)

    for item in niz:
        for i in item:
            if not i.isalnum():
                item = item.replace(i, "")
            else:
                break
        itemr = item[::-1]
        for j in itemr:
            if not j.isalnum():
                itemr = itemr.replace(j, "")
            else:
                break
        n.append(itemr[::-1])
    s = n[::-1]
    result = []
    seen = set()
    for item in s:
        if item not in seen:
            result.append(item)
            seen.add(item)
    result.reverse()
    return result


def vse_afne(tviti):
    niz = []
    n = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i not in niz and i.startswith("@"):
                niz.append(i)

    for item in niz:
        for i in item:
            if not i.isalnum():
                item = item.replace(i, "")
            else:
                break
        itemr = item[::-1]
        for j in itemr:
            if not j.isalnum():
                itemr = itemr.replace(j, "")
            else:
                break
        n.append(itemr[::-1])
    s = n[::-1]
    result = []
    seen = set()
    for item in s:
        if item not in seen:
            result.append(item)
            seen.add(item)
    result.reverse()
    return result


def vsi_hashtagi(tviti):
    niz = []
    n = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i not in niz and i.startswith("#"):
                niz.append(i)

    for item in niz:
        for i in item:
            if not i.isalnum():
                item = item.replace(i, "")
            else:
                break
        itemr = item[::-1]
        for j in itemr:
            if not j.isalnum():
                itemr = itemr.replace(j, "")
            else:
                break
        n.append(itemr[::-1])
    s = n[::-1]
    result = []
    seen = set()
    for item in s:
        if item not in seen:
            result.append(item)
            seen.add(item)
    result.reverse()
    return result


def vse_osebe(tviti):
    niz = []
    n = []
    for item in tviti:
        nov = item.split(" ")
        for i in nov:
            if i not in niz and (i.startswith("@") or i.endswith(":")):
                niz.append(i)

    for item in niz:
        for i in item:
            if not i.isalnum():
                item = item.replace(i, "")
            else:
                break
        itemr = item[::-1]
        for j in itemr:
            if not j.isalnum():
                itemr = itemr.replace(j, "")
            else:
                break
        n.append(itemr[::-1])
    s = n[::-1]
    result = []
    seen = set()
    for item in s:
        if item not in seen:
            result.append(item)
            seen.add(item)
    result.reverse()
    result.sort()
    return result


def custva(tviti, hashtagi):
    niz = []
    n = []
    for item in tviti:
        nov = item.split(" ")
        stev = 0
        for y in nov:
            stev += 1
            if y.startswith("#"):
                nov[stev-1] = y.replace(y[0], "")
        for x in hashtagi:
            if x in nov:
                for i in nov:
                    if i not in niz and i.endswith(":"):
                        niz.append(i)

    for item in niz:
        for i in item:
            if not i.isalnum():
                item = item.replace(i, "")
            else:
                break
        itemr = item[::-1]
        for j in itemr:
            if not j.isalnum():
                itemr = itemr.replace(j, "")
            else:
                break
        n.append(itemr[::-1])
    s = n[::-1]
    result = []
    seen = set()
    for item in s:
        if item not in seen:
            result.append(item)
            seen.add(item)
    result.reverse()
    result.sort()
    return result


def se_poznata(tviti, oseba1, oseba2):
    os1 = []
    os2 = []
    for item in tviti:
        nov = item.split(" ")
        for y in nov:
            if y.startswith("@"):
                os2.append(y)
            if y.endswith(":"):
                os1.append(y)

    o1 = oseba1 + ":"
    o2 = "@" + oseba2
    for item in tviti:
        nov = item.split(" ")
        for i in os1:
            if i in nov and i == o1:
                for j in os2:
                    if j in nov and (j == o2 or j == o2 + ","):
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

