#Obvezni del
#1. naloga
def premozenje(oseba,denar):
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok,denar)
    return vsota

#2. naloga
def najbogatejsi(oseba,denar):
    najbogat = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        bogat = najbogatejsi(otrok, denar)
        if najbogat[1] < bogat[1]:
            najbogat = bogat
    return najbogat


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


