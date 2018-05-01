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
    skupni = denar[oseba]
    for i in otroci[oseba]:
        skupni = skupni + premozenje(i, denar)
    return skupni

def najbogatejsi(oseba, denar):
    terka = (oseba, denar[oseba])
    for i in otroci[oseba]:
        bogat = najbogatejsi(i, denar)
        if terka[1]<bogat[1]:
            terka = bogat
    return terka

def uravnotezeni(oseba, denar):
    if len(otroci[oseba])>0:
        prem = premozenje(otroci[oseba][0], denar)
        for i in otroci[oseba]:
            if not uravnotezeni(i, denar):
                return False
            if not prem == premozenje(i, denar):
                return False
    return True

def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba,denar):
        return None
    for i in otroci[oseba]:
        if not uravnotezeni(i, denar):
            return i


