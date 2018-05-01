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
    skupaj_denar = 0
    skupaj_denar += denar[oseba]
    for otrok in otroci[oseba]:
        skupaj_denar += premozenje(otrok, denar)
    return skupaj_denar

def najbogatejsi(oseba, denar):
    najbog_oseba = oseba
    for otrok in otroci[oseba]:
        tren = najbogatejsi(otrok, denar)
        tren_otrok = tren[0]
        tren_denar = denar[tren_otrok]
        if tren_denar > denar[najbog_oseba]:
            najbog_oseba = tren_otrok
    return (najbog_oseba, denar[najbog_oseba])


