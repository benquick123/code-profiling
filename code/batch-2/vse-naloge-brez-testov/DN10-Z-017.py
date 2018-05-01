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
    vsota = 0
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    vsota += denar[oseba]
    return vsota

def najbogatejsi(oseba, denar):
    najoseba = oseba
    najdenar = denar[oseba]
    for otrok in otroci[oseba]:
        if najdenar < najbogatejsi(otrok, denar)[1]:
            najoseba = otrok
            najdenar = denar[otrok]
    return (najoseba,najdenar)

