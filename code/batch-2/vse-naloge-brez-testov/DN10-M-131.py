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
    bogatija = denar[oseba]
    for otrok in otroci[oseba]:
        bogatija += premozenje(otrok, denar)
    return bogatija

def najbogatejsi(oseba, denar):
    denar_osebe = denar[oseba]
    najbogatejsa_oseba = oseba
    for otrok in otroci[oseba]:
        premozenje(otrok, denar)
        if denar[otrok] >= denar_osebe:
            denar_osebe = denar[otrok]
            najbogatejsa_oseba = otrok


    return (najbogatejsa_oseba, denar_osebe)


