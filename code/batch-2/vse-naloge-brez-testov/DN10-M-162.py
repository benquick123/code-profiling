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
    denari = denar[oseba]
    for otrok in otroci[oseba]:
        denari += premozenje(otrok, denar)
    return denari


def najbogatejsi(oseba, denar):
    najbogat = denar[oseba]
    najbogat_ime = oseba
    for otrok in otroci[oseba]:
        b = najbogatejsi(otrok, denar)
        if b[1] > najbogat:
            najbogat = b[1]
            najbogat_ime = b[0]
    return najbogat_ime, najbogat


def uravnotezeni(oseba, denar):
    s = []
    for otrok in otroci[oseba]:
        if uravnotezeni(otrok, denar):
            s.append(premozenje(otrok, denar))
        else:
            return False
    return all([s[0] == ks for ks in s])


def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba, denar):
        for otrok in otroci[oseba]:
            if not uravnotezeni(otrok, denar):
                return neuravnotezeni(otrok, denar)
        return oseba

