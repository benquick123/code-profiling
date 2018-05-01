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
    skupnidenar = denar[oseba]
    if not otroci[oseba] == "":
        a = otroci[oseba]
        for otrok in a:
            skupnidenar = skupnidenar + premozenje(otrok, denar)
    else:
        skupnidenar = skupnidenar + denar[oseba]
    return skupnidenar

def najbogatejsi(oseba, denar):
    najdenar = denar[oseba]
    najoseba = oseba
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok, denar)[1] > najdenar:
            najdenar = najbogatejsi(otrok, denar)[1]
            najoseba = najbogatejsi(otrok, denar)[0]
    return (najoseba, najdenar)

