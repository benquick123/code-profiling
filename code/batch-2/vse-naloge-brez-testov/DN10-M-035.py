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

def premozenje(oseba,denar):
    denar_skupaj = denar[oseba]
    for otrok in otroci[oseba]:
        denar_skupaj += premozenje(otrok,denar)
    return(denar_skupaj)


def najbogatejsi(oseba,denar):
    bogata_oseba = (oseba,denar[oseba])
    for otrok in otroci[oseba]:
        druga_oseba = najbogatejsi(otrok,denar)
        if(druga_oseba[1] > bogata_oseba[1]):
            bogata_oseba = druga_oseba
    return(bogata_oseba)



