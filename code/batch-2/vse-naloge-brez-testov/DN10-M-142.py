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
    celotno_premozenje=denar[oseba]
    for otrok in otroci[oseba]:
        celotno_premozenje+=premozenje(otrok,denar)
    return celotno_premozenje

def najbogatejsi(oseba, denar):
    najBOGAT=(oseba,denar[oseba])
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok,denar)[1]>najBOGAT[1]:
            najBOGAT=najbogatejsi(otrok,denar)
    return najBOGAT






