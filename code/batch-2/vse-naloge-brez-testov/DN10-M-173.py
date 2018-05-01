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
    sestevek = denar[oseba]
    for otrok in otroci[oseba]:
        stanje = premozenje(otrok, denar)
        sestevek += stanje
    return sestevek


def najbogatejsi(oseba, denar):
    clan, premozenje = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        naj = najbogatejsi(otrok, denar)
        if premozenje < naj[1]:
            clan, premozenje = naj
    return (clan, premozenje)


