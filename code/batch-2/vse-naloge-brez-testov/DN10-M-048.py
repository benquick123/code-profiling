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
    wealth = denar[oseba]
    for child in otroci[oseba]:
        wealth += premozenje(child, denar)

    return wealth

def najbogatejsi(oseba, denar):
    wealthiest_person = (oseba, denar[oseba])
    for child in otroci[oseba]:
        if najbogatejsi(child, denar)[1] > wealthiest_person[1]:
            wealthiest_person = (child, denar[child])

    return wealthiest_person

