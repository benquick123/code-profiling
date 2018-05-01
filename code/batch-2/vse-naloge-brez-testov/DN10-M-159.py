def premozenje(oseba, denar):
    return sum([premozenje(otrok, denar) for otrok in otroci[oseba]]) + denar[oseba]

def najbogatejsi(oseba, denar):
    najd = denar[oseba]
    najo = oseba
    for otrok in otroci[oseba]:
        toseba, tdenar = najbogatejsi(otrok, denar)
        if tdenar > najd:
            najd = tdenar
            najo = toseba
    return (najo, najd)


def uravnotezeni(oseba, denar):
    if len(otroci[oseba]) <= 1:
        return True
    t = premozenje(otroci[oseba][0], denar)
    for otrok in otroci[oseba]:
        if premozenje(otrok, denar) != t or not(uravnotezeni(otrok, denar)):
            return False
    else:
        return True

def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba, denar) and all([uravnotezeni(kd, denar) for kd in otroci[oseba]]):
        return oseba
    for otrok in otroci[oseba]:
            if neuravnotezeni(otrok, denar):
                return neuravnotezeni(otrok, denar)



    # return all([premozenje(otrok, denar) == premozenje(otroci[oseba, denar][0]) and uravnotezeni(otrok, denar) for otrok in otroci[oseba]])


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


