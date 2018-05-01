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
    v = denar[oseba]
    for otrok in  otroci[oseba]:
        v += premozenje(otrok,denar)
    return v

def najbogatejsi(oseba, denar):
    naj = (oseba,denar[oseba])
    for otrok in  otroci[oseba]:
        if najbogatejsi(otrok,denar)[1] > naj[1]:
            naj = najbogatejsi(otrok,denar)
    return naj


