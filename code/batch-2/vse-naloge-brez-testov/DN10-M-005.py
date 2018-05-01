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
    for ime in otroci[oseba]:
        skupaj += premozenje(ime, denar)
    return skupaj


def najbogatejsi(oseba, denar):
    ime, naj = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        kdo, bogat = najbogatejsi(otrok, denar)
        if bogat > naj:
            ime, naj = kdo, bogat
    return ime, naj


def uravnotezeni(oseba, denar):
    return len(set([premozenje(otrok, denar) for otrok in otroci[oseba]])) < 2


def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba, denar):
        return oseba
    for otrok in otroci[oseba]:
        oseba = neuravnotezeni(otrok, denar)
        if oseba:
            return oseba


