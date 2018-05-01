
def premozenje(oseba, denar):
    denar1 = denar[oseba]
    for otrok in otroci[oseba]:
        denar1 += premozenje(otrok, denar)
    return denar1

def najbogatejsi(oseba, denar):
    najbog = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        najbog1 = najbogatejsi(otrok, denar)
        if najbog1[1] > najbog[1]:
            najbog = najbog1
    return najbog





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


