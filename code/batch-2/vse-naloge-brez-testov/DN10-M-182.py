def premozenje(oseba, denar):
    return sum(premozenje(otrok, denar) for otrok in otroci[oseba]) + denar[oseba]


def najbogatejsi(oseba, denar):
    najvec = denar[oseba]
    ime = oseba
    for otrok in otroci[oseba]:
        najvec_o = najbogatejsi(otrok, denar)
        if najvec_o[1] >= najvec:
            najvec = najvec_o[1]
            ime = otrok
    return (ime, najvec)

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


