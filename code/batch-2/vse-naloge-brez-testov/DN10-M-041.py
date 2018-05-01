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
    skupaj = denar[oseba]
    for otrok in otroci[oseba]:
        skupaj += premozenje(otrok, denar)
    return skupaj


def najbogatejsi(oseba, denar):
    terka = [(oseba, denar[oseba])]
    for otrok in otroci[oseba]:
        terka += [najbogatejsi(otrok, denar)]
    return max(terka, key=lambda x:x[1])






