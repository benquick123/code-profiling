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
    prem = denar[oseba]
    for otrok in otroci[oseba]:
        prem += premozenje(otrok,denar)
    return prem

def najbogatejsi(oseba, denar):
    max = denar[oseba]
    ime = oseba
    for otrok in otroci[oseba]:
        a = najbogatejsi(otrok,denar)
        if denar[a[0]] > max:
            max = denar[otrok]
            ime = otrok
    return ime, max

def uravnotezeni(oseba,denar):
    n = True
    for i, otrok in enumerate(otroci[oseba]):
        if i > 0:
            if premozenje(otroci[oseba][i],denar) == premozenje(otroci[oseba][i-1],denar) and uravnotezeni(otrok,denar):
                continue
            else:
                n= False
    return n

def neuravnotezeni(oseba, denar):
    a = ""
    if not uravnotezeni(oseba,denar):
        a += oseba
        return a
    for otrok in otroci[oseba]:
        if neuravnotezeni(otrok,denar):
            a += (neuravnotezeni(otrok,denar))
            return a




