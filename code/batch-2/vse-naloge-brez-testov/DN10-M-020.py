
def premozenje(oseba, denar):
    p = 0
    if not otroci[oseba]:
        return denar[oseba]
    for otrok in otroci[oseba]:
        p += premozenje(otrok, denar)
    return p + denar[oseba]


def najbogatejsi(oseba, denar):
    naj_ime, naj_denar = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        ime, dnar = najbogatejsi(otrok, denar)
        if dnar > naj_denar:
            naj_ime, naj_denar = ime, dnar
    return (naj_ime, naj_denar)


def uravnotezeni(oseba, denar):
    t = []
    for otrok1 in otroci[oseba]:
        a = premozenje(otrok1, denar)
        for otrok2 in otroci[oseba]:
            b = premozenje(otrok2, denar)
            t += [a == b]
        uravnotezeni(otrok1, denar)
    return all(t)


def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba, denar):
        return oseba
    for otrok in otroci[oseba]:
        ime = neuravnotezeni(otrok, denar)
        if ime is not None:
            return ime


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


