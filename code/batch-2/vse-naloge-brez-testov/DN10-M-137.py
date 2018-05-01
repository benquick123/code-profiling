def premozenje(oseba, denar):
    dnar = denar[oseba]
    for otrok in otroci[oseba]:
        dnar += premozenje(otrok,denar)

    return dnar


def najbogatejsi(oseba, denar):
    najblbgat = oseba
    dnar = denar[oseba]
    for otrok in otroci[oseba]:
        bgat = najbogatejsi(otrok, denar)
        if bgat[1] > dnar:
            najblbgat = bgat[0]
            dnar = bgat[1]
    return (najblbgat, dnar)





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


