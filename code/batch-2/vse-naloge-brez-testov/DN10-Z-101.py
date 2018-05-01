def premozenje(oseba,denar):
    v = denar[oseba]
    for otrok in otroci[oseba]:
        v+= premozenje(otrok, denar)
    return v

#Napiši funkcijo najbogatejsi(oseba, denar), ki vrne terko z imenom najbogatejše osebe in količino njenega denarja.

def najbogatejsi(oseba, denar):
    ime = oseba
    kes = denar[oseba]
    for otrok in otroci[oseba]:
        potomec, kes_potomca = najbogatejsi(otrok,denar)
        if kes_potomca > kes:
            ime = potomec
            kes = kes_potomca
    return ime,kes



















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


