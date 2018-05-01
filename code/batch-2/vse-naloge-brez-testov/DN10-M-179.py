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
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok,denar)
    return vsota


def najbogatejsi(oseba, denar):
    najbogatejsa = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        najbogatejsa_do_zdaj = najbogatejsi(otrok, denar)
        if najbogatejsa_do_zdaj[1] > najbogatejsa[1]:
            najbogatejsa = najbogatejsa_do_zdaj
    return najbogatejsa



def uravnotezeni(oseba, denar):
    money = []
    for otrok in otroci[oseba]:
        money.append(premozenje(otrok, denar))
    money = all(x == money[0] for x in money)
    return money


def neuravnotezeni(oseba, denar):
    dejalec = None
    if not uravnotezeni(oseba, denar):
        return oseba
    for otrok in otroci[oseba]:
        if not uravnotezeni(otrok, denar):
            return otrok
        dejalec = neuravnotezeni(otrok, denar)
    return dejalec


