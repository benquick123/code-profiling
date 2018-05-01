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
    k = 0
    for o in otroci[oseba]:
        k += premozenje(o, denar)
    return k + denar[oseba]

def premozenje(oseba, denar):
    return sum(premozenje(o, denar) for o in otroci[oseba]) + denar[oseba]

def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    for o in otroci[oseba]:
        n = najbogatejsi(o, denar)
        if n[1] > naj[1]:
            naj = n
    return naj

def uravnotezeni(oseba, denar):
    k = premozenje(oseba, denar)
    l = []
    if len(otroci[oseba]) > 0:
        k = (k - denar[oseba]) / len(otroci[oseba])
    for o in otroci[oseba]:
        l.append(k == premozenje(o, denar))
    return all(l)

def uravnotezeni(oseba, denar):
    return all([(premozenje(oseba, denar) - denar[oseba]) / len(otroci[oseba]) == premozenje(o, denar)
                if len(otroci[oseba]) > 0
                else premozenje(oseba, denar) == premozenje(o, denar)
                for o in otroci[oseba]])

def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba, denar):
        return oseba
    for o in otroci[oseba]:
        if len(otroci[o]) > 1:
            return neuravnotezeni(o, denar)



