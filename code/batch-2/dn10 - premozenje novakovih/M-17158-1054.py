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
    res = denar[oseba]
    for name in otroci[oseba]:
        res += premozenje(name, denar)
    return res

def najbogatejsi(oseba, denar):
    max_t = (oseba, denar[oseba])
    for name in otroci[oseba]:
        max_t1 = najbogatejsi(name, denar)
        if max_t[1] < max_t1[1]:
            max_t = max_t1
    return max_t



def uravnotezeni(oseba, denar):  #works faster for some reason
    for name, name1 in zip(otroci[oseba], otroci[oseba][1:]):
       if premozenje(name, denar) != premozenje(name1, denar) or not uravnotezeni(name, denar) or not uravnotezeni(name1, denar):
           return False
    return True

"""
def uravnotezeni(oseba, denar):
    if len(otroci[oseba]):
        res = premozenje(otroci[oseba][0], denar)
        if not uravnotezeni(otroci[oseba][0], denar):
            return False
    for name in otroci[oseba][1:]:
        res_t = premozenje(name, denar)
        if not uravnotezeni(name, denar) or res != res_t:
            return False
        res = res_t
    return True
"""


def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba, denar):
        return None
    for name in otroci[oseba]:
        if not uravnotezeni(name, denar):
            return neuravnotezeni(name, denar)
    return oseba


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
