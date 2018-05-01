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
    for otrok in otroci[oseba]:
        abc = premozenje(otrok, denar)
        if abc is not None:
            money += abc
    return money

def najbogatejsi(oseba, denar):
    for i in denar:
        if i == oseba:
            maxMoney = denar[i]
            najvec = i, denar[i]

    for otrok in otroci[oseba]:
        abc = najbogatejsi(otrok, denar)
        if abc is not None:
            a, b = abc
            if b > maxMoney:
                maxMoney = b
                for j in denar:
                    if j == a:
                        najvec = j, denar[j]
    return najvec



