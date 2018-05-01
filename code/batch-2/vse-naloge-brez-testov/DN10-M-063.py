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
    kes = 0
    for otrok in otroci[oseba]:
        kes += premozenje(otrok, denar)
    return kes + denar[oseba]

def najbogatejsi(oseba, denar):
    xs = [(oseba, denar[oseba])]
    if otroci[oseba] == []:
        return xs[0]
    else:
        for otrok in otroci[oseba]:
            xs.append(najbogatejsi(otrok, denar))
    max_kes = 0
    seznam = []
    for clovek,kes in xs:
        if kes > max_kes:
            max_kes = kes
    for clovek,kes in xs:
        if kes == max_kes:
            seznam.append((clovek,kes))
    return seznam[0]

