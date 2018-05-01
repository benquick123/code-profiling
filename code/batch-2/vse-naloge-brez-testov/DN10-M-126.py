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

