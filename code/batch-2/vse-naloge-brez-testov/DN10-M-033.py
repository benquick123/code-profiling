def premozenje(oseba, denar):
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    najbogatejsa_oseba = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        naj_2 = najbogatejsi(otrok,denar)
        if naj_2[1] > najbogatejsa_oseba[1]:
            najbogatejsa_oseba = naj_2
    return najbogatejsa_oseba

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


