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
    vsota = [denar[oseba]]
    for otrok in otroci[oseba]:
        vsota.append(premozenje(otrok, denar))
    return sum(vsota)

def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        koliko = najbogatejsi(otrok, denar)
        if koliko[1] >= naj[1]:
            naj = koliko
    return naj


