def premozenje    (oseba, denar):

    denar_skupni = 0

    denar_skupni = denar_skupni + denar[oseba]

    for posameznik in otroci[oseba]:
        denar_skupni = denar_skupni + premozenje (posameznik, denar)

    return denar_skupni




def najbogatejsi  (oseba, denar, premozni=[]):

    if premozni==[] or   denar[oseba] > premozni[1]:
        premozni=(oseba, denar[oseba])

    for posameznik in otroci[oseba]:
        premozni = najbogatejsi (posameznik, denar, premozni)

    return premozni




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


