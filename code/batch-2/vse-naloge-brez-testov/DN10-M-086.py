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
#   return sum([denar[oseba]] + [premozenje(otrok, denar) for otrok in otroci[oseba]])

    dolares = denar[oseba]
    for otrok in otroci[oseba]:
        dolares += premozenje(otrok, denar)
    return dolares


def najbogatejsi(oseba, denar):
    froc_denar = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        najbol_bogat = najbogatejsi(otrok, denar)
        if najbol_bogat[1] > froc_denar[1]:
            froc_denar = najbol_bogat
    return froc_denar



