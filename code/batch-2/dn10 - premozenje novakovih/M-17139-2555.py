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

from operator import itemgetter


def premozenje(oseba, denar):
    d = 0

    for otrok in otroci[oseba]:
        d += premozenje(otrok, denar)

    d = d + denar[oseba]

    return d


def najbogatejsi(oseba, denar):
    d = [(oseba, denar[oseba])]

    for otrok in otroci[oseba]:
        d = d + [najbogatejsi(otrok, denar)]

    if len(otroci[oseba]) == 0:
        return d[0]

    else:
        return max(d, key=itemgetter(1))


def uravnotezeni(oseba, denar):
    d = []

    for otrok in otroci[oseba]:
        d = d + [premozenje(otrok, denar)]

    if len(otroci[oseba]) == 0:
        return True

    else:
        return len(set(d)) == 1


def neuravnotezeni_rezultat(oseba, denar):
    d = []

    for otrok in otroci[oseba]:
        d = d + [neuravnotezeni_rezultat(otrok, denar)]

    for rez in d:
        if type(rez) is str:
            return rez

    if len(otroci[oseba]) == 0:
        return denar[oseba]

    if len(set(d)) == 1:
        return premozenje(oseba, denar)

    else:
        return oseba


def neuravnotezeni(oseba, denar):
    rezultat = neuravnotezeni_rezultat(oseba, denar)

    if type(rezultat) is str:
        return rezultat

    else:
        return None


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
