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
    return sum(premozenje(otrok, denar) for otrok in otroci[oseba]) + denar[oseba]


def najbogatejsi(oseba, denar):
    naj_b = oseba

    for otrok in otroci[oseba]:
        d = najbogatejsi(otrok, denar)
        if d[1] > denar[naj_b]:
            naj_b = otrok

    return naj_b, denar[naj_b]


