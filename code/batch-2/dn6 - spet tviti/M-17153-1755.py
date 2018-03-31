import collections

# Iz prejšnje naloge:

def avtor(tvit):
    s = tvit.split(":")
    return s[0]

def unikati(s):
    s2 = []
    for i in s:
        if i not in s2:
            s2.append(i)
    return s2

def vsi_avtorji(tviti):
    s = [i.split(":")[0] for i in tviti]
    s2 = []
    for i in s:
        s2.append(i)
    return s2

def se_zacne_z(tvit, c):
    s = []
    t = tvit.split()

    for e in t:
        if e.startswith(c):
            if e[-1].isalnum() == True:
                s.append(e[1:])
            else:
                s.append(e[1:][:-1])
    return s


# Funkcija besedilo(tvit) prejme tvit in vrne besedilo - torej vse, kar sledi prvemu dvopičju.
# Klic besedilo("ana: kdo so te: @berta, @cilka, @dani?") vrne "kdo so te: @berta, @cilka, @dani?.

def besedilo(tvit):
    s = tvit.split(":", 1)
    return s[1].lstrip()


# Funkcija zadnji_tvit(tviti) prejme seznam tvitov in vrne slovar, katerega ključi so avtorji tvitov, vrednosti pa njihovi tviti.
# Če je en in isti avtor napisal več tvitov, naj bo v slovarju njegov zadnji tvit. Rezultat je lahko, recimo
#   {"berta": "@sandra Delaj domačo za #programiranje1",
#    "sandra": "@berta Ne maram #programiranje1 #krneki",
#    "ana": "kdo so te: @berta, @cilka, @dani? #krneki"}
# če so to edini trije avtorji in so to njihovi (zadnji) tviti.

def zadnji_tvit(tviti):
    s = {}
    for i in tviti:
        if unikati(i):
            s[avtor(i)] = besedilo(i)
    return s


# Funkcija prvi_tvit(tviti) je jako podobna, le da v primeru, da je ista oseba napisala več tvitov, obdrži njen prvi tvit.

def prvi_tvit(tviti):
    s = {}
    for i in tviti:
        if avtor(i) in s:
            continue
        else:
            s[avtor(i)] = besedilo(i)
    return s


# Funkcija prestej_tvite(tviti) vrne slovar, katerega ključi so (spet) avtorji, pripadajoče vrednosti pa število tvitov,
# ki so jih napisali, na primer {"sandra": 2, "berta": 1, "ana": 1, "cilka": 4, "benjamin": 1}

def prestej_tvite(tviti):
    return collections.Counter(vsi_avtorji(tviti))


# Funkcija omembe(tviti) vrne slovar, katerega ključi so avtorji tvitov, vrednosti pa seznami oseb, ki so jih ti avtorji omenjali v svojih tvitih.
# Vrstni red oseb mora biti enak vrstnemu redu omenjanj. Funkcija lahko vrne, recimo
#   {"sandra": ["berta", "benjamin", "ana"],
#   "benjamin": [],
#   "cilka": [],
#   "berta": ["sandra"],
#   "ana": ["berta", "cilka", "dani"]}

def omembe(tviti):
    s = {}
    for i in tviti:
        if avtor(i) in s:
            s[avtor(i)].extend((se_zacne_z(i, "@")))
        else:
            s[avtor(i)] = (se_zacne_z(i, "@"))
    return s


# Funkcija neomembe(ime, omembe) prejme ime neke osebe in takšen slovar, kakršnega vrne gornja funkcija.
# Vrniti mora seznam vseh ljudi, ki so avtorji kakega tvita, podana oseba (ime) pa jih ni omenjala.
# Če funkciji kot argument podamo ime "Ana" in gornji slovar, mora vrniti ["sandra", "benjamin], saj Ana ni omenjala Sandre in Benjamina, Cilko in Berto pa je.
# Iz seznama naj bo seveda izključena oseba sama (v tem primeru Ana). Vrstni red oseb v seznamu je lahko poljuben.

def neomembe(ime, omembe):
    s = []
    s_neomenjeni = omembe[ime]
    for i in omembe:
        if i in s_neomenjeni or i == ime:
            continue
        else:
            s.append(i)
    return s


# Napišite funkcijo se_poznata(ime1, ime2, omembe), ki je podobna kot v prejšnji domači nalogi, le da kot argument namesto tvitov dobi gornji slovar.
# Povedati mora, ali je prva oseba kdaj omenila drugo (ali obratno) ali ne. Funkcija vrne True ali False.

def se_poznata(ime1, ime2, omembe):
    for tvit in omembe:
        pisec = avtor(tvit)
        omenjeni = se_zacne_z(tvit, "@")
        if ime1 == pisec and ime2 in omenjeni or ime2 == pisec and ime1 in omenjeni:
            return True
    return False


# Napišite funkcijo hashtagi(tviti), ki prejme seznam tvitov in vrne slovar, katerega ključi so hashtagi (brez znaka #),
# pripadajoče vrednosti pa seznami avtorjev, ki so uporabili ta hashtagi. Avtorji naj bodo urejeni po abecedi.

def hashtagi(tviti):
    return


import unittest

class TestObvezna(unittest.TestCase):
    maxDiff = 10000

    def test_1_besedilo(self):
        self.assertEqual(besedilo("sandra: Spet ta dež. #dougcajt"),
                         "Spet ta dež. #dougcajt")
        self.assertEqual(besedilo("ana: kdo so te: @berta, @cilka, @dani? #krneki"),
                         "kdo so te: @berta, @cilka, @dani? #krneki")

    def test_2_zadnji_tvit(self):
        self.assertDictEqual(
            zadnji_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"berta": "@sandra Delaj domačo za #programiranje1",
             "sandra": "@berta Ne maram #programiranje1 #krneki",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten",
             "cilka": "@benjamin @ana #split? po dvopičju, za začetek?"})

        self.assertDictEqual(
            zadnji_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "sandra: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "sandra: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten",
             "sandra": "@benjamin @ana #split? po dvopičju, za začetek?"})

        self.assertDictEqual(
            zadnji_tvit(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki"})

        self.assertEqual(zadnji_tvit([]), {})


    def test_3_prvi_tvit(self):
        self.assertDictEqual(
            prvi_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": "Spet ta dež. #dougcajt",
             "berta": "@sandra Delaj domačo za #programiranje1",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "cilka": "jst sm pa #luft",
             "benjamin": "pogrešam ano #zalosten"})

        self.assertDictEqual(
            prvi_tvit([
                "sandra: Spet ta dež. #dougcajt",
                "sandra: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "sandra: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": "Spet ta dež. #dougcajt",
             "ana": "kdo so te: @berta, @cilka, @dani? #krneki",
             "benjamin": "pogrešam ano #zalosten"})

        self.assertDictEqual(
            prvi_tvit(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": "kdo so te: @berta, @cilka, @dani? #krneki"})

        self.assertEqual(prvi_tvit([]), {})

    def test_4_prestej_tvite(self):
        self.assertDictEqual(
            prestej_tvite([
                "sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki",
                "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "cilka: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": 2, "berta": 1, "ana": 1, "cilka": 2, "benjamin": 1})

        self.assertDictEqual(
            prestej_tvite([
                    "sandra: Spet ta dež. #dougcajt",
                    "sandra: @sandra Delaj domačo za #programiranje1",
                    "sandra: @berta Ne maram #programiranje1 #krneki",
                    "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                    "sandra: jst sm pa #luft",
                    "benjamin: pogrešam ano #zalosten",
                    "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": 5, "ana": 1, "benjamin": 1})

        self.assertDictEqual(
            prestej_tvite(["ana: kdo so te: @berta, @cilka, @dani? #krneki"]),
            {"ana": 1})

        self.assertEqual(prestej_tvite([]), {})

    def test_5_omembe(self):
        self.assertDictEqual(
            omembe(["sandra: Spet ta dež. #dougcajt",
                    "berta: @sandra Delaj domačo za #programiranje1",
                    "sandra: @berta Ne maram #programiranje1 #krneki",
                    "ana: kdo so te: @berta, @cilka, @dani? #krneki",
                    "cilka: jst sm pa #luft",
                    "benjamin: pogrešam ano #zalosten",
                    "sandra: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {"sandra": ["berta", "benjamin", "ana"],
             "benjamin": [],
             "cilka": [],
             "berta": ["sandra"],
             "ana": ["berta", "cilka", "dani"]}
        )

    def test_6_neomembe(self):
        omembe = {"sandra": ["berta", "benjamin", "ana"],
                  "benjamin": [],
                  "cilka": [],
                  "berta": ["sandra"],
                  "ana": ["berta", "cilka", "dani", "benjamin", "sandra"]}

        self.assertEqual(neomembe("sandra", omembe), ["cilka"])
        self.assertEqual(neomembe("ana", omembe), [])
        self.assertEqual(set(neomembe("benjamin", omembe)), set(omembe) - {"benjamin"})

class TestDodatna(unittest.TestCase):
    def test_1_se_poznata(self):
        omembe = {"sandra": ["berta", "benjamin", "ana"],
                  "benjamin": [],
                  "cilka": [],
                  "berta": ["sandra"],
                  "ana": ["berta", "cilka", "dani"]}

        self.assertTrue(se_poznata("ana", "berta", omembe))
        self.assertTrue(se_poznata("berta", "ana", omembe))
        self.assertTrue(se_poznata("sandra", "benjamin", omembe))
        self.assertTrue(se_poznata("benjamin", "sandra", omembe))

        self.assertFalse(se_poznata("benjamin", "ana", omembe))
        self.assertFalse(se_poznata("ana", "benjamin", omembe))

        self.assertFalse(se_poznata("cilka", "dani", omembe))
        self.assertFalse(se_poznata("pavel", "peter", omembe))

    def test_2_hashtagi(self):
        self.assertDictEqual(
            hashtagi(["sandra: Spet ta dež. #dougcajt",
                      "berta: @sandra Delaj domačo za #programiranje1",
                      "sandra: @berta Ne maram #programiranje1 #krneki",
                      "ana: kdo so te @berta, @cilka, @dani? #krneki",
                      "cilka: jst sm pa #luft",
                      "benjamin: pogrešam ano #zalosten",
                      "ema: @benjamin @ana #split? po dvopičju, za začetek?"]),
            {'dougcajt': ['sandra'],
             'krneki': ['ana', 'sandra'],
             'luft': ['cilka'],
             'programiranje1': ['berta', 'sandra'],
             'split': ['ema'],
             'zalosten': ['benjamin']})


if __name__ == "__main__":
    unittest.main()


