def premozenje(oseba, denar):
    if not otroci[oseba]:
        return denar[oseba]
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    najvecji = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        temp = najbogatejsi(otrok, denar)
        if temp[1] > najvecji[1]:
            najvecji = temp
    return najvecji


def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True
    for otrok in otroci[oseba]:
        if not uravnotezeni(otrok, denar):
            return False
    temp = premozenje(otroci[oseba][0], denar)
    for otrok in otroci[oseba]:
        if premozenje(otrok, denar) != temp:
            return False
    return True


def neuravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return None
    if uravnotezeni(oseba, denar):
        return None
    for otrok in otroci[oseba]:
        if not uravnotezeni(otrok, denar):
            return neuravnotezeni(otrok, denar)
    return oseba


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


