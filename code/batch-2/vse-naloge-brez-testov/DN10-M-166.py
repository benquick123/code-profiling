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
    v = 0
    for otrok in otroci[oseba]:
        v += premozenje(otrok, denar)
    return v + int(denar[oseba])



def najbogatejsi(oseba, denar):
    maxmoney = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        naj_den = najbogatejsi(otrok, denar)
        if naj_den[1] > maxmoney[1]:
            maxmoney = naj_den
    return maxmoney



