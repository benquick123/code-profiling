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
    if not otroci[oseba]:
        return denar[oseba]
    else:
        premozen=denar[oseba]
        for ime in otroci[oseba]:
            premozen=premozen+premozenje(ime, denar)
    return premozen

def najbogatejsi(oseba, denar):
    if not otroci[oseba]:
        return (oseba,denar[oseba])
    else:
        najBog= (oseba,denar[oseba])
        for ime in otroci[oseba]:
            if najBog[::-1] < (denar[ime],ime):
                najBog=(ime,denar[ime])
            najbogatejsi(ime, denar)
    return najBog




