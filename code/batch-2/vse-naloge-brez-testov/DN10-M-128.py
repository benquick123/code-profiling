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
    naj =(oseba, denar[oseba])
    for otrok in otroci[oseba]:
        naj_test = najbogatejsi(otrok, denar)
        if naj_test[1] > naj[1]:
            naj = naj_test
    return(naj)

