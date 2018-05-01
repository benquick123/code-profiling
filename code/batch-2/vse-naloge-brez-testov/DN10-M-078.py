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
    vsota = 0
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota + denar[oseba]


def najbogatejsi(oseba, denar):
    naj_oseba = oseba
    najvec = denar[oseba]
    for otrok in otroci[oseba]:
        if premozenje(otrok, denar) > najvec:
            naj_oseba, najvec = najbogatejsi(otrok, denar)
    return naj_oseba, najvec


def uravnotezeni(oseba, denar):
    vsota = []
    for otrok in otroci[oseba]:
        x = uravnotezeni(otrok, denar)
        vsota.append(premozenje(otrok, denar))
        if not x:
            return False
    if len(set(vsota)) <= 1:
        return True
    else:
        return False


def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba, denar):
        return None
    for otrok in otroci[oseba]:
        x = neuravnotezeni(otrok, denar)
        if x is not None:
            return x
    return oseba


