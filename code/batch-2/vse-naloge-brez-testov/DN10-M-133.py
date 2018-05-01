


def premozenje(oseba, denar):
    return sum(premozenje(otrok, denar) for otrok in otroci[oseba]) + denar[oseba]



def najbogatejsi(oseba, denar):
    naj_bogatejsi = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        if denar[otrok] > naj_bogatejsi[1]:
            naj_bogatejsi = otrok, denar[otrok]
    return naj_bogatejsi



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


