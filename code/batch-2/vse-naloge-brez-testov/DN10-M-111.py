"""def premozenje(oseba, denar):
    premoz = 0
    for otrok in otroci[oseba]:
        premoz += premozenje(otrok, denar)
    return premoz + denar[oseba]"""

def premozenje(oseba, denar):
    return sum(premozenje(otrok,denar) for otrok in otroci[oseba]) + denar[oseba]


def najbogatejsi(oseba, denar):
    max_ime = oseba
    max_denar = denar[oseba]
    for otrok in otroci[oseba]:
        najbog_otrok = najbogatejsi(otrok, denar)
        if najbog_otrok[1] > max_denar:
            max_denar = najbog_otrok[1]
            max_ime = najbog_otrok[0]
    return (max_ime, max_denar)


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


