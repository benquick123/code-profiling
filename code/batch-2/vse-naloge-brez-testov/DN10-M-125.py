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
    return sum(premozenje(otrok, denar) for otrok in otroci[oseba]) + denar[oseba]

def najbogatejsi(oseba, denar):
    najoseba = oseba
    najdenar = denar[najoseba]
    for otrok in otroci[oseba]:
        naj_otrok = najbogatejsi(otrok, denar)
        if denar[naj_otrok[0]] > denar[najoseba]:
            najoseba = naj_otrok[0]
            najdenar = naj_otrok[1]
    return (najoseba, najdenar)



