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
    money = denar[oseba]
    money_1 = 0
    for potomec in otroci[oseba]:
        e = premozenje(potomec,denar)
        money_1+= e
    return money + money_1
def najbogatejsi(oseba, denar):
    sez = (oseba,denar[oseba])
    for potomec in otroci[oseba]:
        e = najbogatejsi(potomec, denar)
        if e[1] >= sez[1]:
            sez = (potomec,e[1])
    return sez






