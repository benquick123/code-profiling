def premozenje(oseba, denar):
    imetje = denar[oseba]
    for otrok in otroci[oseba]:
        imetje = imetje + premozenje(otrok, denar)
    return imetje

def najbogatejsi(oseba, denar):
    naj = [(oseba, denar[oseba])]
    for otrok in otroci[oseba]:
        naj.append(najbogatejsi(otrok, denar))
    return max(naj, key=lambda x: x[1])

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

