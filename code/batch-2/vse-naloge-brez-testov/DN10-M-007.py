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

def premozenje(oseba, denar, skupni_denar = 0):
    skupni_denar += denar[oseba]
    for otrok in otroci[oseba]:
        skupni_denar += premozenje(otrok, denar)
    return skupni_denar

def najbogatejsi(oseba, denar, bogati = []):
    if bogati == [] or denar[oseba] > bogati[1]:
        bogati = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        bogati = najbogatejsi(otrok, denar, bogati)
    return bogati

