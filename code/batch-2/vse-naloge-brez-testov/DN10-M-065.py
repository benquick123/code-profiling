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
    skupno_premozenje = denar[oseba]

    for otrok in otroci[oseba]:
        skupno_premozenje += premozenje(otrok, denar)

    return skupno_premozenje


def najbogatejsi(oseba, denar):
    bogatun = (oseba, denar[oseba])

    for otrok in otroci[oseba]:
        bogatunski_otrok = najbogatejsi(otrok, denar)

        if bogatunski_otrok[1] > bogatun[1]:
            bogatun = bogatunski_otrok

    return bogatun

def uravnotezeni(oseba, denar):
    premozenja = []

    for otrok in otroci[oseba]:
        premozenja.append((premozenje(otrok, denar), uravnotezeni(otrok, denar)))

    for i in range(len(premozenja) - 1):
        if not (premozenja[i][1] and premozenja[i + 1][1] and premozenja[i][0] == premozenja[i + 1][0]):
            return False

    return True


def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba, denar):
        for otrok in otroci[oseba]:
            _oseba = neuravnotezeni(otrok, denar)

            if _oseba is not None:
                return _oseba

        return oseba

    return None


