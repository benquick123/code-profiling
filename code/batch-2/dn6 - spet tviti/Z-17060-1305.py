random_tviti = ["sandra: Spet ta dež. #dougcajt",
                "berta: @sandra Delaj domačo za #programiranje1",
                "sandra: @berta Ne maram #programiranje1 #krneki - 1",
                "ema2: @benjamin @ana #split? po dvopičju, za začetek2?1",
                "ana: kdo so te @berta, @cilka, @dani? #krneki",
                "cilka: jst sm pa #luft",
                "benjamin: pogrešam ano #zalosten",
                "ema: @benjamin @ana #split? po dvopičju, za začetek?",
                "sandra: @berta Ne maram #programiranje1 #krneki - 2",
                "ema2: @benjamin @ana #split? po dvopičju, za začetek2?",
                "sandra: @benjamin @ana #split? po dvopičju, za začetek2?223"]



#1
def besedilo(tvit):
    rezultat = ""
    if ":" in tvit:
        if tvit.split(':', 1)[1] != '':
            rezultat = tvit.split(':', 1)[1].lstrip()
    return rezultat


#2
def zadnji_tvit(random_tviti):
    tvit_slovar = {}
    posamezni_tvit = random_tviti[:]
    i = 0
    while i < len(posamezni_tvit):
        pretty_name = posamezni_tvit[i].split(":")[0]
        if pretty_name != '':
            tvit_slovar[pretty_name] = posamezni_tvit[i].split(":")[1]
        i = i + 1
    return tvit_slovar


#3
def prvi_tvit(random_tviti):
    tvit_slovar = {}
    posamezni_tvit = random_tviti[:]
    avtorji = []
    i = 0
    while i < len(posamezni_tvit):
        pretty_name = posamezni_tvit[i].split(":")[0]
        if pretty_name != '' and pretty_name not in avtorji: #v primeru, da nimamo osebe, ki je zapisala tvit...
            tvit_slovar[pretty_name] = posamezni_tvit[i].split(":")[1]
            avtorji.append(pretty_name)
        i = i + 1
    return tvit_slovar


#4
def prestej_tvite(random_tviti):
    tvit_slovar = {}
    posamezni_tvit = random_tviti[:]
    avtorji = []
    i = 0
    while i < len(posamezni_tvit):
        pretty_name = posamezni_tvit[i].split(":")[0]
        if pretty_name != '' and pretty_name not in avtorji: #v primeru, da nimamo osebe, ki je zapisala tvit...
            tvit_slovar[pretty_name] = 1
            avtorji.append(pretty_name)
        else:
            tvit_slovar[pretty_name] += 1
        i = i + 1
    return tvit_slovar

#5
def vse_afne_v_enem_tvitu(tvit):
    besede = []
    beseda = ""
    zapisuj = False
    for chrka in tvit:
        if chrka == "@":
            zapisuj = True
        elif not chrka.isalnum() and beseda:
            if not beseda in besede:
                besede.append(beseda)
            beseda = ""
            zapisuj = False
        elif zapisuj:
            beseda += chrka
    if beseda and not beseda in besede:
        besede.append(beseda)
    return besede


def omembe(tviti):
    tvit_slovar = {}
    posamezni_tvit = random_tviti[:]
    avtorji = []
    i = 0
    while i < len(posamezni_tvit):
        pretty_name = posamezni_tvit[i].split(":")[0]
        if pretty_name != '':  # v primeru, da nimamo osebe, ki je zapisala tvit...
            tvit_slovar[pretty_name] = vse_afne_v_enem_tvitu(posamezni_tvit[i])
            avtorji.append(pretty_name)
        i = i + 1
    return tvit_slovar

#6
def neomembe(ime, omembe):
    rezultat = []
    ime = ime.lower()
    omembe_ime = ""
    if ime in omembe: # Ana mora biti v seznamu
        omembe_ime = omembe[ime]
    else: return rezultat

    vsi_avtorji_v_omembe = [] #avtorji_tvitov
    for avtor in omembe:
        vsi_avtorji_v_omembe.append(avtor)
    vsi_avtorji_v_omembe.remove(ime)

    for avtor, avtorji_omenjeni in omembe.items():
        if avtor != ime and omembe_ime != '':  # avtor ni ana - izključimo 
            rezultat = vsi_avtorji_v_omembe
            for avtor_omenjeni in omembe_ime:
                if avtor_omenjeni in rezultat:
                    rezultat.remove(avtor_omenjeni)
    return rezultat


import unittest

class TestObvezna(unittest.TestCase):
    maxDiff = 10000

    def test_1_besedilo(self):
        self.assertEqual(besedilo("sandra: Spet ta dež. #dougcajt"),
                         "Spet ta dež. #dougcajt")
        self.assertEqual(besedilo("ana: kdo so te: @berta, @cilka, @dani? #krneki"),
                         "kdo so te: @berta, @cilka, @dani? #krneki")



if __name__ == "__main__":
    unittest.main()


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


