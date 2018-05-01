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
    skupen = denar[oseba]
    for clovk in otroci[oseba]:
        skupen += premozenje(clovk, denar)
    return skupen


def najbogatejsi(oseba, denar):
    bogat = (oseba, denar[oseba])
    for x in otroci[oseba]:
        naj = najbogatejsi(x, denar)
        if naj[1] > bogat[1]:
            bogat = naj
            #print(bogat)
    return bogat

def uravnotezeni(oseba, denar):
    



    return











