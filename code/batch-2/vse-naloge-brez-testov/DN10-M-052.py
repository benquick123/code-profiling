def premozenje(oseba, denar):
    skupenDenar = denar[oseba]
    for otrok in otroci[oseba]:
        skupenDenar += premozenje(otrok,denar)
    return skupenDenar

def najbogatejsi(oseba, denar):
    osebaZNajvecDenarja = (oseba,denar[oseba])
    for otrok in otroci[oseba]:
        if denar[otrok] > denar[osebaZNajvecDenarja[0]]:
            osebaZNajvecDenarja = najbogatejsi(otrok, denar)
    return (osebaZNajvecDenarja)


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


