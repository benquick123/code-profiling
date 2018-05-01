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
    r = [denar[oseba]]
    for otrok in otroci[oseba]:
        r += [premozenje(otrok, denar)]
    return sum(r)

def najbogatejsi(oseba, denar):
    naj = denar[oseba]
    ime = oseba
    for otrok in otroci[oseba]:
        if denar[otrok] > naj:
            naj = denar[otrok]
            ime = otrok
        najbogatejsi(otrok,denar)
    t = (ime,naj)
    return t


