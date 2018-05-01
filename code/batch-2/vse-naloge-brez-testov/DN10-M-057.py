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
    if not oseba or not denar:
        return 0

    use = denar[oseba]
    for otrok in otroci[oseba]:
        use += premozenje(otrok, denar)

    return use


def najbogatejsi(oseba,denar):

    najvec = (oseba,denar[oseba])
    for x in otroci[oseba]:
        neki = najbogatejsi(x,denar)
        if neki[1] >= najvec[1]:
           najvec = (x,neki[1])

    return najvec




