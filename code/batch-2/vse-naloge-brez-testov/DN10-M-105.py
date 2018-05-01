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
    skupaj = denar[oseba]
    for otrok in otroci[oseba]:
        skupaj += premozenje(otrok, denar)
    return skupaj

def najbogatejsi(oseba, denar):
    najbogat = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok,denar)[1] > najbogat[1]:
            najbogat = (otrok, denar[otrok])
    return najbogat

def uravnotezeni(oseba, denar):
    uravnotezena = denar[oseba]
    for otrok in otroci[oseba]:
        return (denar[otrok] + uravnotezeni(otrok,denar)) == uravnotezena
    return uravnotezena

