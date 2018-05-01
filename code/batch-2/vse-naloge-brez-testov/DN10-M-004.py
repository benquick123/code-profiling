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
    cekini = denar[oseba]
    for oseba1 in otroci[oseba]:
        cekini = cekini + premozenje(oseba1, denar)
    return cekini

def najbogatejsi(oseba, denar):
    cekini = (oseba, denar[oseba])
    for oseba1 in otroci[oseba]:
        if denar[oseba1] > cekini[1]:
            cekini = najbogatejsi(oseba1, denar)
    return cekini


