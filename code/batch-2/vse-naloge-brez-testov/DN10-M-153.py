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


# Napiši funkcijo premozenje(oseba, denar), ki pove, kolikor denarja imajo (skupaj) člani rodbine podane oseb.

def premozenje(oseba, denar):
    vsota = [denar[oseba]]

    for otrok in otroci[oseba]:
        vsota.append(premozenje(otrok, denar))

    return sum(vsota)


# Napiši funkcijo najbogatejsa(oseba, denar), ki vrne terko z imenom najbogatejše osebe in količino njenega denarja.

def najbogatejsi(oseba, denar):
    najbogat = (oseba, denar[oseba])

    for otrok in otroci[oseba]:
        koliko = (najbogatejsi(otrok, denar))

        if koliko[1] > najbogat[1]:
            najbogat = koliko

    return najbogat


