otroci = {
    "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": ["Herman", "Erik"],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}



def premozenje(oseba, denar):
    moneymoneymoneymustbefunnyinarichmansworld = denar[oseba]
    for otrok in otroci[oseba]:
        moneymoneymoneymustbefunnyinarichmansworld += premozenje(otrok, denar)
    return moneymoneymoneymustbefunnyinarichmansworld

"BP - Abba"

def najbogatejsi(oseba, denar):
    rich = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        alsorich = najbogatejsi(otrok, denar)
        if rich[1] < alsorich[1]:
            rich = alsorich
    return rich

"Denar je teoretičen!!" \
"Matjaž si izračuna da ima 2 denarja. Nato vpraša svojega otroka, kdo je najbogatejši v tvoji rodbini." \
"Viljem izračuna da ima 5 denarjev in isto vprašanje postavi še svojemu otroku. Tadeja sporoči vrednost 12." \
"Viljem nato primerja kdo od njiju je bogatejši in ime in denar sporoči matjažu. matjaž nato isto primerja svojo" \
"bogastvo in bogatsvo, ki mu ga sporočil Viljem. Returna najbogatejšega."

"------------------------------ EXTRA -------------------------------"


def uravnotezeni(oseba, denar):
    dinarcki = denar[oseba]
    dinarcki_otrok = []
    for otrok in otroci[oseba]:
        denar_otroka = uravnotezeni(otrok, denar)
        dinarcki_otrok.append(denar_otroka)
    if not otroci[oseba]:
        return dinarcki
    if len(set(dinarcki_otrok)) == 1:
        dinarcki += sum(dinarcki_otrok)
        return dinarcki
    else:
        return 0

"Funkcija uravnoteženi vrne ali premoženje cele rodbine ali 0. Naloga sicer zahteva True ali False, ampak sej po eni strani" \
"pozitivna številka je True, medtem ko je 0 enako False."

def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba, denar):
        return
    else:
        return ime_revnega(oseba, denar)[1]



def ime_revnega(oseba, denar):
    denar_osebe = denar[oseba], oseba
    denarji_otrok = []
    for otrok in otroci[oseba]:
        denar_otroka = ime_revnega(otrok, denar)
        denarji_otrok.append(denar_otroka)
    if not otroci[oseba]:
        return denar_osebe
    elif [denarji_otrok[x] for x in range(len(denarji_otrok)) if "reven" in denarji_otrok[x]]:
        return [denarji_otrok[x] for x in range(len(denarji_otrok)) if "reven" in denarji_otrok[x]][0]
    elif len(set([denarji_otrok[0][0] for x,y in zip(denarji_otrok, denarji_otrok[1:]) if x[0] == y[0]])) == 1:
        denar_tmp = denar_osebe[0] + (denarji_otrok[0][0] * len(denarji_otrok))
        denar_osebe = denar_tmp, oseba
        return denar_osebe
    elif len(denarji_otrok) == 1:
        denar_tmp = denar_osebe[0] + denarji_otrok[0][0]
        denar_osebe = denar_tmp, oseba
        return denar_osebe
    else:
        denar_osebe = "reven", oseba
        return denar_osebe

"Za prvo osebo izračunamo terko denar_osebe, ki je formatu (8, IME), ustvarimo tudi prazen seznam." \
"Nato za vsakega otroka od osebe in vse njihove podotroke naredimo(gremo od najnižje osebe do najstarejše:" \
"Za Alenko zračunamo denar_osebe in ker nima pod otrok to terko vrnemo jožefu, nato to ponovimo še za ostala dva otroka." \
"Ko smo vse tri terke otrok dali v denarji_otrok, najprej preverimo, če je beseda reven v kateri koli terki, ker je ni preverimo s " \
"funkcijo set ali so vse tri številke enake(set odstrani podvojene, potrojene..., zato primerjamo z 1.) ker to drži izračunamo denar_tmp" \
"kar je denar osebe + vsota vseh otrok, to nato vstavimo v denar_osebe, kar tudi vrnemo Juriju. Jurij je že prej zračinal " \
"premoženje Franca. Nato ponovi cel postopek in vrne svojo novo vsoto elizabeti. Elizabeta ima v seznamu denarji otrok" \
"[(37, 'Ludvik'), (38, 'Jurij'), (37, 'Barbara')] in gre čez vse if in elif. Ker ima elizabeta otroke, prvega preskoči, ker v seznamu" \
"nima reven drugega preskoči, pravtako tretjega in četrtega, zato naredi else, ki vrne (reven, elizabeta). elizabeta to vrne danielu" \
"ki ima tako v seznamu reven, elizabeta in (vsota premoženja), hans. drugi pogoj je true, zato daniel vrne adamu (reven, elizabeta)" \
"to vrne tudi adam."

import unittest
class TestObvezna(unittest.TestCase):
    denar = {
        "Adam": 42,
        "Aleksander": 3,
        "Alenka": 3,
        "Barbara": 37,
        "Cilka": 242,
        "Daniel": 4,
        "Erik": 32,
        "Elizabeta": 8,
        "Franc": 16,
        "Herman": 12,
        "Hans": 55,
        "Jožef": 7,
        "Jurij": 5,
        "Ludvik": 37,
        "Margareta": 20,
        "Matjaž": 142,
        "Petra": 3,
        "Tadeja": 45,
        "Viljem": 55
    }

    def test_obv_01_premozenje(self):
        self.assertEqual(premozenje("Adam", self.denar), 768)
        self.assertEqual(premozenje("Petra", self.denar), 3)
        self.assertEqual(premozenje("Jožef", self.denar), 16)

        denar2 = self.denar.copy()
        denar2["Petra"] = 5
        self.assertEqual(premozenje("Jožef", denar2), 18)

    def test_obv_02_najbogatejši(self):
        self.assertIn(najbogatejsi("Elizabeta", self.denar), [("Ludvik", 37), ("Barbara", 37)])
        self.assertEqual(najbogatejsi("Ludvik", self.denar), ("Ludvik", 37))
        self.assertEqual(najbogatejsi("Jurij", self.denar), ("Franc", 16))
        self.assertEqual(najbogatejsi("Hans", self.denar), ("Hans", 55))
        self.assertEqual(najbogatejsi("Adam", self.denar), ("Cilka", 242))


class TestDodatna(unittest.TestCase):
    denar = {
        "Adam": 42,
        "Aleksander": 3,
        "Alenka": 3,
        "Barbara": 37,
        "Cilka": 242,
        "Daniel": 4,
        "Erik": 32,
        "Elizabeta": 8,
        "Franc": 16,
        "Herman": 12,
        "Hans": 55,
        "Jožef": 7,
        "Jurij": 5,
        "Ludvik": 37,
        "Margareta": 20,
        "Matjaž": 142,
        "Petra": 3,
        "Tadeja": 45,
        "Viljem": 55
    }

    def test_dod_01_uravnotezeni(self):
        self.assertTrue(uravnotezeni("Adam", self.denar))
        self.assertTrue(uravnotezeni("Ludvik", self.denar))
        self.assertTrue(uravnotezeni("Elizabeta", self.denar))

        denar2 = self.denar.copy()
        denar2["Jurij"] = 6
        self.assertTrue(uravnotezeni("Jurij", denar2))
        self.assertTrue(uravnotezeni("Jožef", denar2))
        self.assertTrue(uravnotezeni("Hans", denar2))
        self.assertTrue(uravnotezeni("Matjaž", denar2))
        self.assertFalse(uravnotezeni("Elizabeta", denar2))
        self.assertFalse(uravnotezeni("Daniel", denar2))
        self.assertFalse(uravnotezeni("Adam", denar2))

    def test_dod02_neuravnotezeni(self):
        self.assertIsNone(neuravnotezeni("Adam", self.denar))
        self.assertIsNone(neuravnotezeni("Elizabeta", self.denar))

        denar2 = self.denar.copy()
        denar2["Jurij"] = 6
        denar2["Elizabeta"] = 7
        self.assertIsNone(neuravnotezeni("Jurij", denar2))
        self.assertIsNone(neuravnotezeni("Jožef", denar2))
        self.assertIsNone(neuravnotezeni("Hans", denar2))
        self.assertIsNone(neuravnotezeni("Matjaž", denar2))
        self.assertEqual(neuravnotezeni("Elizabeta", denar2), "Elizabeta")
        self.assertEqual(neuravnotezeni("Daniel", denar2), "Elizabeta")
        self.assertEqual(neuravnotezeni("Adam", denar2), "Elizabeta")


if __name__ == "__main__":
    unittest.main()
