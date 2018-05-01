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
    p = denar[oseba]
    for otrok in otroci[oseba]:
        p += premozenje(otrok,denar)
    return p

def najbogatejsi(oseba, denar):
    najb = (oseba,denar[oseba])
    for otrok in otroci[oseba]:
        prem = najbogatejsi(otrok,denar)
        if prem[1] > najb[1]:
            najb = prem
    return najb

