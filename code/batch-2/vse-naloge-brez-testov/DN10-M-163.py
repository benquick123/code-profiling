


def premozenje(oseba, denar):
    vsota=0
    for otrok in otroci[oseba]:
        vsota+=premozenje(otrok, denar)
    return vsota + denar[oseba]


def najbogatejsi(oseba, denar):
    max_oseba = oseba
    max_d = denar[oseba]

    for otrok in otroci[oseba]:
        max_otrok = najbogatejsi(otrok, denar)
        if max_otrok[1]> max_d:
            max_d = max_otrok[1]
            max_oseba = max_otrok[0]

    ime = (max_oseba, max_d)
    return ime



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


