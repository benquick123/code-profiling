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

def  premozenje(oseba, denar):
    ETH = denar[oseba]
    for otrok in otroci[oseba]:
        ETH += premozenje(otrok,denar)
    return ETH

def najbogatejsi(oseba, denar):
    ETH_master = (oseba,denar[oseba])
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok,denar)[1] > ETH_master[1]:
            ETH_master = (otrok, denar[otrok])
    return ETH_master

def uravnotezeni(oseba, denar):
    ETH = denar[oseba]
    seznam = []
    for otrok in otroci[oseba]:
        if uravnotezeni(otrok, denar) == False:
            return False
        seznam += [uravnotezeni(otrok, denar)]
    if len(seznam)> 0:
        if min(seznam)!=max(seznam):
            return False
        return ETH + seznam[0] * len(seznam)
    return ETH

def neuravnotezeni(oseba, denar):
    for otrok in otroci[oseba]:
        if neuravnotezeni(otrok,denar) != None:
            return neuravnotezeni(otrok,denar)
    if uravnotezeni(oseba,denar):
        return None
    else:
        return oseba





