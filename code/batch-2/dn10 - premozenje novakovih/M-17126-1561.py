############################################################### DATA SET ###############################################################

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

############################################################### OBLIGATORY ASSIGNMENT ###############################################################

def premozenje(oseba, denar):
    """
    Function calculates family money of a selected person.

    Args:
        :param oseba (str): Chosen person from the list.
        :param denar (dict): Dictionary of a family money.

    Returns:
        Summed family money (int).
    """
    sum_money = 0
    for kid in otroci:
        if kid == oseba:
            sum_money += denar[kid]
            for grandchild in otroci[kid]:
                sum_money += premozenje(grandchild, denar)
    return sum_money


def najbogatejsi(oseba, denar):
    """
        Function gives us richest person in family.

        Args:
            :param oseba (str): Chosen person from the list.
            :param denar (dict): Dictionary of a family money.

        Returns:
            Name of a richest person in family and her/his amount of money (tuple).
        """
    richest = (oseba, denar[oseba])
    for kid in otroci:
        if kid == oseba:
            for grandchild in otroci[kid]:
                grand_richest = najbogatejsi(grandchild, denar)
                if grand_richest[1] > richest[1]:
                    richest = (grandchild, denar[grandchild])
    return richest


############################################################### EXTRA ASSIGNMENT ###############################################################

def uravnotezeni(oseba, denar):
    """
    Function tells us if family is financially balanced (they all have the same amount of money).

    Args:
        :param oseba (str): Chosen person from the list.
        :param denar (dict): Dictionary of a family money.

    Returns:
        True or False.
    """
    for kid in otroci:
        if kid == oseba:
            for i in range(1, len(otroci[kid])):
                if premozenje(otroci[kid][i - 1], denar) != premozenje(otroci[kid][i], denar):
                    return False
    return True


def neuravnotezeni(oseba, denar):
    """
    Function tells us name of a person whose family is not financially balanced (they don't have the same amount of money).

    Args:
        :param oseba (str): Chosen person from the list.
        :param denar (dict): Dictionary of a family money.

    Returns:
        Name of a person (str) or None.
    """
    for kid in otroci:
        if kid == oseba:
            if not uravnotezeni(kid, denar):
                return kid
            for grandchild in otroci[kid]:
                if neuravnotezeni(grandchild, denar) != None:
                    return neuravnotezeni(grandchild, denar)
    return None


############################################################### TESTS ###############################################################

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
