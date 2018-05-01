
def premozenje(oseba, denar):
    su = denar[oseba]
    for otrok in otroci[oseba]:
        su += premozenje(otrok,denar)
    return su

def najbogatejsi(oseba, denar):
    tep=(oseba,denar[oseba])
    for otrok in otroci[oseba]:
        if denar[otrok] > tep[1]:
            tep = najbogatejsi(otrok, denar)
    return tep

def uravnotezeni(oseba, denar):
    for otrok in otroci[oseba]:
        if premozenje(otrok,denar) != (sum([premozenje(otrok,denar) for otrok in otroci[oseba]])/len(otroci[oseba])):
            return False
        uravnotezeni(otrok,denar)
    return True

def neuravnotezeni(oseba, denar):
    for otrok in otroci[oseba]:
        if uravnotezeni(otrok, denar) == False:
            neuravnotezeni(otrok,denar)
            return otrok
    return None

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


