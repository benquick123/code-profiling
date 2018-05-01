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
    dincki = denar[oseba]
    for otrok in otroci[oseba]:
        dincki += premozenje(otrok,denar)
    return dincki

def najbogatejsi(oseba,denar):
    najvec_dinckov = (oseba,denar[oseba])
    for otrok in otroci[oseba]:
        dincki = najbogatejsi(otrok,denar)
        if najvec_dinckov[1] <= dincki[1]:
            najvec_dinckov = dincki
    return najvec_dinckov

