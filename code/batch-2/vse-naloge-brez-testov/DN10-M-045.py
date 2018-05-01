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
    denarcki = denar[oseba]
    for i in otroci[oseba]:
        denarcki += premozenje(i, denar)
    return denarcki


def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        primerjava = najbogatejsi(otrok, denar)
        if primerjava[1] > naj[1]:
            naj = primerjava
    return naj



def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return premozenje(oseba, denar)
    seznam = []
    vrednost2 = premozenje(otroci[oseba][0], denar)
    for otrok in otroci[oseba]:
        vrednost1 = premozenje(otrok, denar)
        if vrednost2 != vrednost1:
            return False
        seznam.append(uravnotezeni(otrok, denar))
    return bool(seznam)


def neuravnotezeni(oseba, denar):
    vred = uravnotezeni(oseba, denar)
    if not vred:
        return oseba
    for otrok in otroci[oseba]:
        if neuravnotezeni(otrok, denar):
            return neuravnotezeni(otrok, denar)
        if not uravnotezeni(otrok, denar):
            return otrok


