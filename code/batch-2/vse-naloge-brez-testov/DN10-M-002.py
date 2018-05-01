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

def premozenje (oseba, denar):
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    najbogatejsa = (oseba,denar[oseba])
    denaar = 0
    for otrok in otroci[oseba]:
        najbogatejsi(otrok, denar)
        if denar[otrok] >= denaar and denar[otrok] > denar[oseba]:
            najbogatejsa = (otrok, denar[otrok])
            denaar = denar[otrok]
    return najbogatejsa

