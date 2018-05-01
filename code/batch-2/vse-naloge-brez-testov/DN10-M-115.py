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
    seznam = [(denar[oseba])]
    for otrok in otroci[oseba]:
        seznam.append(premozenje(otrok, denar))
    return sum(seznam)

def najbogatejsi(oseba, denar):
    terka = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        a = najbogatejsi(otrok, denar)
        if a[1] > terka[1]:
            terka = a
    return terka


