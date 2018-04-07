def unikati(s):
    sez_unikatov = []

    for element in s:
        if element in sez_unikatov:
            continue

        else:
            sez_unikatov.append(element)

    return sez_unikatov


def avtor(tvit):
    besede = tvit.split()

    return besede[0][:-1]


def vsi_avtorji(tviti):
    seznam_avtorjev = []
    for tvit in tviti:
        seznam_avtorjev.append(avtor(tvit))

    return unikati(seznam_avtorjev)


def izloci_besedo(beseda):
    indeks_zac = 0
    indeks_kon = len(beseda) - 1

    for i in range(0, len(beseda)):
        if beseda[i].isalnum():
            break

        else:
            indeks_zac += 1

    for j in range(len(beseda) - 1, -1, -1):
        if beseda[j].isalnum():
            break

        else:
            indeks_kon -= 1

    return beseda[indeks_zac:indeks_kon+1]


def se_zacne_z(tvit, c):
    seznam_besed = []
    tvit_besede = tvit.split()
    for beseda in tvit_besede:
        if beseda[0] == c:
            seznam_besed.append(izloci_besedo(beseda))

    return unikati(seznam_besed)


def zberi_se_zacne_z(tviti, c):
    seznam_besed = []

    for tvit in tviti:
        if c in tvit:
            tvit_besede = tvit.split()
            for beseda in tvit_besede:
                if beseda[0] == c:
                    seznam_besed.append(izloci_besedo(beseda))

                else:
                    continue
        else:
            continue

    return unikati(seznam_besed)


def vse_afne(tviti):
    seznam_afn = zberi_se_zacne_z(tviti, "@")
    seznam_afn = unikati(seznam_afn)

    for i in range(0, len(seznam_afn)):
        seznam_afn[i] = izloci_besedo(seznam_afn[i])

    return seznam_afn


def vsi_hashtagi(tviti):
    seznam_hashov = zberi_se_zacne_z(tviti, "#")
    seznam_hashov = unikati(seznam_hashov)

    for i in range(0, len(seznam_hashov)):
        seznam_hashov[i] = izloci_besedo(seznam_hashov[i])

    return seznam_hashov


def vse_osebe(tviti):
    sez_avtorjev = vsi_avtorji(tviti)
    sez_omenjenih = vse_afne(tviti)

    sez_vseh = sez_avtorjev+sez_omenjenih
    sez_vseh.sort()

    return unikati(sez_vseh)


def custva(tviti, hashtagi):
    sez_avtorjev = []

    for tvit in tviti:
        if "#" not in tvit:
            continue

        else:
            tvit_besede = tvit.split()

            for beseda in tvit_besede:
                if beseda[0] == "#":
                    if beseda[1:] in hashtagi:
                        sez_avtorjev.append(avtor(tvit))

                    else:
                        continue

                else:
                    continue

    sez_avtorjev = unikati(sez_avtorjev)
    sez_avtorjev.sort()

    return sez_avtorjev


def se_poznata(tviti, oseba1, oseba2):
    for tvit in tviti:
        if "@" not in tvit:
            continue

        else:
            tvit_besede = tvit.split()

            for beseda in tvit_besede:
                if beseda[0] == "@":
                    if (izloci_besedo(beseda) == oseba1 and avtor(tvit) == oseba2) or \
                            (izloci_besedo(beseda) == oseba2 and avtor(tvit) == oseba1):
                        return True

                    else:
                        continue

                else:
                    continue

    return False


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

