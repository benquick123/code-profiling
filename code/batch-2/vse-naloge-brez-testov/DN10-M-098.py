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
    denrod = 0
    Osebe = otroci[oseba]
    if denrod == 0:
        denrod = denrod + denar[oseba]
    for i in Osebe:
        denrod = denrod + premozenje(i, denar)
    return denrod

def najbogatejsi(oseba, denar):
    imenajbosebe = oseba
    Osebe = otroci[oseba]
    maxdenar = denar[oseba]
    for i in Osebe:
        if najbogatejsi(i,denar)[1] > maxdenar:
            maxdenar = najbogatejsi(i,denar)[1]
            imenajbosebe = i
    return(imenajbosebe, maxdenar)







