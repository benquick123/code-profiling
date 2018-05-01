
def premozenje(oseba, denar):
    sez = imena_v_rodbini(oseba)
    sk = 0
    for e in sez:
        for i in denar:
            if i == e:
                sk += denar[i]
    return sk


def imena_v_rodbini(ime):
    xs = [ime]
    for otrok in otroci[ime]:
        xs.extend(imena_v_rodbini(otrok))
    return xs



def najbogatejsi(oseba, denar):
    najbog = (oseba, denar[oseba])
    for e in otroci[oseba]:
        if najbogatejsi(e, denar)[1] > najbog[1]:
            najbog = (e,denar[e])
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


