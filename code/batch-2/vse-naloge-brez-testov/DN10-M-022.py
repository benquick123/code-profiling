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
        p += premozenje(otrok, denar)
    return p

def najbogatejsi(oseba, denar):
    najbogatejsa_oseba = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        if denar[otrok] >= najbogatejsa_oseba[1]:
            najbogatejsa_oseba = najbogatejsi(otrok, denar)
    return najbogatejsa_oseba

def uravnotezeni(oseba, denar):
    a = [premozenje(otrok, denar) for otrok in otroci[oseba]]
    return a[1:] == a[:-1]

neuravnotezene_osebe = []
def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba, denar):
        neuravnotezene_osebe.append(oseba)
    for otrok in otroci[oseba]:
        neuravnotezeni(otrok, denar)
    if neuravnotezene_osebe:
        return neuravnotezene_osebe[-1]

