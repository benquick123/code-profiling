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
    vs = denar[oseba]
    for otrok in otroci[oseba]:
        vs += premozenje(otrok, denar)
    return vs

def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        op = najbogatejsi(otrok, denar)
        if op[1] > naj[1]:
            naj = (otrok, denar[otrok])
    return naj

def uravnotezeni(oseba, denar):
    s = []
    for otrok in otroci[oseba]:
        s.append(premozenje(otrok, denar))
    if not s:
        return True

    if sum(s)/len(s) == s[0]:
        return True

def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba, denar):
        return None
    for otrok in otroci[oseba]:
        if not uravnotezeni(otrok, denar):
            return neuravnotezeni(otrok, denar)


