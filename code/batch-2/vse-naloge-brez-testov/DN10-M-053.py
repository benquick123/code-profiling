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
    vsota += denar[oseba]
    for potomec in otroci[oseba]:
        vsota += premozenje(potomec, denar)
    return vsota

def najbogatejsi(oseba, denar):
    ime, najvec = None, False
    for potomec in otroci[oseba]:
        if denar[potomec] > najvec:
            ime, najvec = potomec, denar[potomec]
        ime2, najvec2 = najbogatejsi(potomec, denar)
        if najvec2 > najvec:
            ime, najvec = ime2, najvec2
    if denar[oseba] > najvec:
        return oseba, denar[oseba]
    return ime, najvec

def uravnotezeni(oseba, denar):
    for potomec in otroci[oseba]:
        if premozenje(potomec, denar) != (premozenje(oseba, denar) - denar[oseba]) / len (otroci[oseba]):
            return False
        if not uravnotezeni(potomec, denar):
            return False
    return True



