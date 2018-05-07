def premozenje(oseba, denar):
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    najbogatejsa_oseba = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        naj_2 = najbogatejsi(otrok,denar)
        if naj_2[1] > najbogatejsa_oseba[1]:
            najbogatejsa_oseba = naj_2
    return najbogatejsa_oseba

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

if __name__ == "__main__":
    unittest.main()
