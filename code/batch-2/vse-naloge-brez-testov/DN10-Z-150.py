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
    sum = 0
    for otrok in rodbina(oseba):
        sum += denar[otrok]
    return sum


def najbogatejsi(oseba, denar):
    najbogatejsi = ("", 0)
    for otrok in rodbina(oseba):
        if denar[otrok] > najbogatejsi[1]:
            najbogatejsi = (otrok, denar[otrok])
    return najbogatejsi


def rodbina(oseba):
    rodbinaReturn = [oseba]
    for otrok in otroci[oseba]:
        rodbinaReturn.extend(rodbina(otrok))
    return rodbinaReturn


