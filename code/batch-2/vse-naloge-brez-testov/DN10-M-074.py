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
    d = denar[oseba]
    for otrok in otroci[oseba]:
        d += premozenje(otrok, denar)
    return d

def najbogatejsi(oseba, denar):
    naj = denar[oseba]
    o = oseba
    for otrok in otroci[oseba]:
        x, k = najbogatejsi(otrok, denar)
        if k >= naj:
            naj = k
            o = otrok
    return (o, naj)

def uravnotezeni(oseba, denar):
    return


def neuravnotezeni(oseba, denar):
    return


