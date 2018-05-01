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

def premozenje(oseba,denar):
    denar_skupaj = denar[oseba]
    for otrok in otroci[oseba]:
        denar_skupaj += premozenje(otrok,denar)
    return denar_skupaj

def najbogatejsi(oseba,denar):
    naj_ime, naj_denar = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        if naj_denar < denar[najbogatejsi(otrok,denar)[0]]:
            naj_ime, naj_denar = najbogatejsi(otrok,denar)
    return (naj_ime, naj_denar)

def uravnotezeni(oseba,denar):
    premozenje_rodbine = None
    for otrok in otroci[oseba]:
        if premozenje_rodbine == None:
            premozenje_rodbine = premozenje(otrok,denar)
        elif premozenje_rodbine != premozenje(otrok,denar) or not uravnotezeni(otrok,denar):
            return False
    return True

def neuravnotezeni(oseba,denar):
    result = None
    if not uravnotezeni(oseba,denar):
        result = oseba

    for otrok in otroci[oseba]:
        if neuravnotezeni(otrok,denar) is not None:
            return neuravnotezeni(otrok,denar)
    return result

