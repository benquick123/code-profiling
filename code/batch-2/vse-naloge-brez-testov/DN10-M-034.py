def premozenje(oseba,denar):
    vsota = 0
    if oseba in otroci:
        kes = denar[oseba]
        vsota += kes
        potomci = otroci[oseba]
        for posameznik in potomci:
            vsota += premozenje(posameznik,denar)
    else:
        return None

    return vsota

def najbogatejsi(oseba, denar):
    x = oseba
    y = denar[oseba]
    for potomci in otroci[oseba]:
        kes = denar[potomci]
        if y < kes:
            x = potomci
            y = kes
    return x,y

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


