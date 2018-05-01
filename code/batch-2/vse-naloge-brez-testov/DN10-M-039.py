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
def imena_v_rodbini(ime):
    xs = [ime]
    for otrok in otroci[ime]:
        xs.extend(imena_v_rodbini(otrok))
    return xs

def premozenje(oseba,denar):
    v= 0
    for otrok in otroci[oseba]:
      v +=  premozenje(otrok,denar)
    return v+ denar[oseba]


def najbogatejsi2(oseba,denar):
    xs = denar[oseba]
    for otrok in otroci[oseba]:
        if denar[oseba]<denar[otrok]:
            xs = najbogatejsi2(otrok,denar)
    return xs

def najbogatejsi(oseba,denar):
    childrens = otroci[oseba]
    xs= []
    if len(childrens) == 0:
        return (oseba,denar[oseba])
    for child in childrens:
        money = denar[child]
        if money == najbogatejsi2(oseba,denar):
            xs.append(child)
    if len(xs)>1:
        return [(xs[0],money),(xs[1],money)]
    else:
        return (xs[0], money)


