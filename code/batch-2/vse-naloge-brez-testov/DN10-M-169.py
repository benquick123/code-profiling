def premozenje(oseba, denar):
    vrednost = denar[oseba]
    for otrok in otroci[oseba]:
        vrednost += premozenje(otrok, denar)
    return vrednost

def najbogatejsi(oseba, denar):
    naj = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        naj_p = najbogatejsi(otrok, denar)
        if naj_p[1] > naj[1]:
            naj = naj_p
    return naj

def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True
    for otrok in otroci[oseba]:
        p = premozenje(otrok, denar)
        for dete in otroci[oseba]:
            if p != premozenje(dete, denar):
                return False
        else:
            return True
        uravnotezeni(otrok, denar)

def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba, denar):
        return oseba
    for otrok in otroci[oseba]:
        os = neuravnotezeni(otrok, denar)
        if os != None:
            return os










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


