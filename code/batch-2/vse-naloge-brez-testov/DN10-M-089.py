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
    skup = 0
    for otrok in otroci[oseba]:
        skup += premozenje(otrok, denar)
    return skup + denar[oseba]

def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    if len(otroci[oseba]) == 0:
        return naj
    for otrok in otroci[oseba]:
        naj_pod = najbogatejsi(otrok, denar)
        if naj_pod[1] > naj[1]:
            naj = naj_pod
    return naj















