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
    premoz = denar[oseba]
    if otroci[oseba].__len__() == 0:
        return denar[oseba]
    for currOseba in otroci[oseba]:
        premoz += premozenje(currOseba, denar)
    return premoz

def najbogatejsi(oseba, denar):
    najBog = (oseba, denar[oseba])
    if otroci[oseba].__len__() == 0:
        return (oseba, denar[oseba])
    for currOseba in otroci[oseba]:
        if najBog[1] < denar[currOseba]:
            najBog = najbogatejsi(currOseba, denar)
    return najBog


