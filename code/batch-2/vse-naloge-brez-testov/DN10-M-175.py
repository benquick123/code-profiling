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
    if not otroci[oseba]:
        return denar[oseba]
    return denar[oseba] + sum([premozenje(otrok, denar) for otrok in otroci[oseba]])

def najbogatejsi(oseba, denar):
    if not otroci[oseba]:
        return oseba, denar[oseba]
    najbogatejsi_ = oseba, denar[oseba]
    for oseba_ in otroci[oseba]:
        if najbogatejsi(oseba_, denar)[1] > najbogatejsi_[1]:
            najbogatejsi_ = najbogatejsi(oseba_, denar)
    return najbogatejsi_

def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True
    premozenja = [premozenje(otrok, denar) for otrok in otroci[oseba]]
    return premozenja.count(premozenja[0]) == len(premozenja)\
           and all([uravnotezeni(otrok, denar) for otrok in otroci[oseba]])

def neuravnotezeni(oseba, denar):
    if not otroci[oseba] or uravnotezeni(oseba, denar):
        return None
    for otrok in otroci[oseba]:
        if not uravnotezeni(otrok, denar):
            return neuravnotezeni(otrok, denar)
    return oseba

