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

def imena_v_rodbini(oseba):
    seznam = [oseba]
    for otrok in otroci[oseba]:
        seznam.extend(imena_v_rodbini(otrok))
    return seznam

def premozenje(oseba, denar):
    seznam = []
    for ime in imena_v_rodbini(oseba):
        for clovek, stevilka in denar.items():
            if ime == clovek:
                seznam.append(stevilka)
    return sum(seznam)

def najbogatejsi(oseba, denar):
    vrni = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        if denar[otrok] >= vrni[1]:
            vrni = (otrok, denar[otrok])
        else:
            najbogatejsi(otrok, denar)
    return vrni


