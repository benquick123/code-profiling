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
    kolicina = denar[oseba]
    for os in otroci[oseba]:
        kolicina += premozenje(os, denar)
    return kolicina

def najbogatejsi(oseba, denar):
    najbogat = oseba
    najvec = denar[oseba]
    for os in otroci[oseba]:
        if denar[os] > najvec:
            najbogat, najvec = najbogatejsi(os, denar)
    return najbogat, najvec

