


def premozenje(oseba, denar):
    skupno_premozenje = denar[oseba]
    for otrok in otroci[oseba]:
        skupno_premozenje += premozenje(otrok, denar)
    return skupno_premozenje

def najbogatejsi(oseba, denar):
    najpremozenje = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        if denar[otrok] > najpremozenje[1]:
            najpremozenje = najbogatejsi(otrok, denar)
    return najpremozenje




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


