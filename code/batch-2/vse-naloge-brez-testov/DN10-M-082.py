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
    prem = []
    for o in otroci[oseba]:
        prem.append(premozenje(o, denar))
    prem.append(denar[oseba])
    return sum(prem)


def najbogatejsi(oseba, denar):
    najvec, najbogat = denar[oseba], oseba
    for otrok in otroci[oseba]:
        najbogat_2, najvec_2 = najbogatejsi(otrok, denar)
        if najvec_2 > najvec:
            najvec, najbogat = najvec_2, najbogat_2
    return najbogat, najvec


def uravnotezeni(oseba, denar):
    u = True
    for o in otroci[oseba]:
        if not uravnotezeni(o, denar):
            u = False
            break
    if len(set([premozenje(o, denar) for o in otroci[oseba]])) > 1:
        u = False
    return u


def neuravnotezeni(oseba, denar):
    if len(set([premozenje(o, denar) for o in otroci[oseba]])) > 1:
        return oseba
    for o in otroci[oseba]:
        if neuravnotezeni(o, denar):
            return neuravnotezeni(o, denar)


