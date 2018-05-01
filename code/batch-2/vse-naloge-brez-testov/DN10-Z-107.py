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
    money = 0
    for people in otroci[oseba]:
        money += premozenje(people, denar)
    money += denar[oseba]
    return money

def najbogatejsi(oseba, denar):
    personX = (oseba, denar[oseba])
    for i in otroci[oseba]:
        personY = najbogatejsi(i, denar)
        if personY[1] > personX[1]:
            personX = personY
    return personX

