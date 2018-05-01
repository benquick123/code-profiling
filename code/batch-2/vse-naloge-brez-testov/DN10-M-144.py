def premozenje(oseba, denar):
    x= 0
    if len(otroci[oseba]) < 1:
        return denar[oseba]
    for i in range(len(otroci[oseba])):
        x+= premozenje((otroci[oseba])[i], denar)
    return x+denar[oseba]

def najbogatejsi(oseba, denar):
    najbog= oseba
    bogastvo= denar[oseba]
    if len(otroci[oseba]) < 1:
        x= (oseba, bogastvo)
        return x
    for i in range(len(otroci[oseba])):
        if (denar[(otroci[oseba])[i]] > bogastvo):
            najbog= (otroci[oseba])[i]
            bogastvo=denar[(otroci[oseba])[i]]
    y=(najbog, bogastvo)
    return y

















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


