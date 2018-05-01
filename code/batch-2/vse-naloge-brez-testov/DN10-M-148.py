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
    naj = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        umesn_oseba, umesn_denar = najbogatejsi(otrok, denar)
        ime_naj, denar_naj = naj
        if umesn_denar > denar_naj:
            naj = umesn_oseba, umesn_denar
    return naj

def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True
    skupaj = premozenje(otroci[oseba][0],denar)
    for otrok in otroci[oseba]:
        umesn = premozenje(otrok, denar)
        if umesn != skupaj:
            return False
    return True



