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


def premozenje(oseba,denar):
    x = denar[oseba]
    for i in otroci[oseba]:
        x += premozenje(i,denar)
    return x

def najbogatejsi(oseba, denar):
    x = [(oseba, denar[oseba])]
    for i in otroci[oseba]:
        x.append(najbogatejsi(i, denar))
        x.sort(key=lambda a: a[1], reverse=True)
    return x[0]




