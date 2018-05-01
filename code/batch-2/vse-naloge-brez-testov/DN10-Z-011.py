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
    if otroci[oseba]:
        for otrok in otroci[oseba]:
            skupaj += premozenje(otrok, denar)
    return skupaj

def najbogatejsi(oseba, denar):
    najvec = oseba, denar[oseba]
    if otroci[oseba]:
        for otrok in otroci[oseba]:
            if denar[otrok]>najvec[1]:
                najvec = otrok, denar[otrok]
            najbogatejsi(otrok, denar)
    return najvec

def uravnotezeni(oseba, denar):
    if otroci[oseba]:
        for i, otrok in enumerate(otroci[oseba]):
            if premozenje(otrok, denar) != premozenje(otroci[oseba][i-1], denar):
                return False
    return True

def neuravnotezeni(oseba, denar):


    if not uravnotezeni(oseba, denar):
        return oseba
    for otrok in otroci[oseba]:
        if neuravnotezeni(otrok, denar):
            return otrok

    return None 

