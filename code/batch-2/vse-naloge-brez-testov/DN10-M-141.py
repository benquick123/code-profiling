def rodbina(oseba):
    z = [oseba]
    for ime in otroci[oseba]:
        z.extend(rodbina(ime))
    return z

def premozenje(oseba, denar):
    money = denar[oseba]
    for clan in rodbina(oseba):
        if clan == oseba: pass
        else: money += denar[clan]
    return money

def najbogatejsi(oseba, denar):
    richment = (oseba, denar[oseba])
    for clan in rodbina(oseba):
        if richment[1] <= denar[clan]:
            richment = (clan, denar[clan])
    return richment




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


