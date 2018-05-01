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
    v = 0
    for otrok in otroci[oseba]:
        if premozenje(otrok, denar):
            v += premozenje(otrok, denar)
    return v + denar[oseba]


def najbogatejsi(oseba, denar):
    v = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok, denar):
            naj = (otrok, denar[otrok])
            if naj[1] >= v[1]:
                v = naj
    return v

