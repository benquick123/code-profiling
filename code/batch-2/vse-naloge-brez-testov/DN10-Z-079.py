def premozenje(oseba, denar):
    vseskupaj = denar[oseba]
    for otrok in otroci[oseba]:
        vseskupaj += premozenje(otrok, denar)
    return vseskupaj

def najbogatejsi(oseba, denar):
    x = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        naj = najbogatejsi(otrok, denar)
        if naj[1] > x[1]:
           x = naj
    return x


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


