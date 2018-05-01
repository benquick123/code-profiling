
def premozenje(oseba, denar):
    vs = denar[oseba]
    for otrok in otroci[oseba]:
        vs += premozenje(otrok, denar)
    return vs


def najbogatejsi(oseba, denar):
    naj = denar[oseba]
    os = oseba
    for otrok in otroci[oseba]:
        d = najbogatejsi(otrok, denar)[1]
        if d > naj:
            naj = d
            os = otrok
    return os, naj



def uravnotezeni(oseba, denar):
    s = []
    for otrok in otroci[oseba]:
        s.append(premozenje(otrok, denar))
    return s[1:] == s[:-1]


def uravnotezeni(oseba, denar):
    s = []
    for otrok in otroci[oseba]:
        s.append(premozenje(otrok, denar))
    return s[1:] == s[:-1]




def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba, denar):
        return None
    else:
        for otrok in otroci[oseba]:
            if not uravnotezeni(otrok, denar):
                return otrok
            else:
                neuravnotezeni(otrok, denar)



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


