def premozenje(oseba, denar):
    v = 0
    for otrok in otroci[oseba]:
        v += premozenje(otrok, denar)
    return v + denar[oseba]


def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        naj_otrok = najbogatejsi(otrok, denar)
        if naj[1] < naj_otrok[1]:
            naj = naj_otrok
    return naj


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


