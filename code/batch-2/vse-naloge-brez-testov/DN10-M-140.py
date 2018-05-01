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
    najvec = denar[oseba]
    najbogatejsi = oseba
    for otrok in otroci[oseba]:
        d = denar[otrok]
        if d > najvec:
            najvec = d
            najbogatejsi = otrok
    return (najbogatejsi, najvec)
