def premozenje(oseba, denar):
    skupno = 0
    for otrok in otroci[oseba]:
        skupno += premozenje(otrok, denar)
    skupno += denar[oseba]
    return skupno

def najbogatejsi(oseba, denar):
    najbogatejsa = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        if najbogatejsa[1] < najbogatejsi(otrok, denar)[1]:
            najbogatejsa = najbogatejsi(otrok, denar)
    return najbogatejsa

def uravnotezeni(oseba, denar):
    s = set()
    for otrok in otroci[oseba]:
        s.add(premozenje(otrok, denar))
    if len(s) > 1:
        return False
    else:
        return True

def neuravnotezeni(oseba, denar):
    for otrok in otroci[oseba]:
        neuravnotezeni(otrok, denar)
    denar[uravnotezeni(oseba, denar)] = oseba
    return denar.get(False, None)

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


