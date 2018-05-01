from operator import itemgetter

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
    return denar[oseba] + sum(premozenje(x, denar) for x in otroci[oseba])

def najbogatejsi(oseba, denar):
    a = denar[oseba]
    clovek = oseba
    for s in otroci[oseba]:
        if denar[s] > a:
            a = denar[s]
            clovek = s
        najbogatejsi(s, denar)
    return ((clovek, denar[clovek]))

