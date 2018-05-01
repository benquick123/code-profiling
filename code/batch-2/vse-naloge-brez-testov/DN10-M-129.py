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
    v=0
    for otrok in otroci[oseba]:
        v+=premozenje(otrok, denar)
    return v+int(denar[oseba])

def najbogatejsi(oseba, denar):
    z=(oseba, denar[oseba])
    for otrok in otroci[oseba]:
        p=najbogatejsi(otrok, denar)
        if p[1]>z[1]:
            z=p
    return z

def uravnotezeni(oseba, denar):
    t=[]
    for otrok in otroci[oseba]:
        p = premozenje(otrok, denar)
        t.append(p)
    return all(x == t[0] for x in t)

def neuravnotezeni(oseba, denar):
    u=uravnotezeni(oseba,denar)
    if u==False:
        return oseba
    for otrok in otroci[oseba]:
        z=neuravnotezeni(otrok,denar)
        if z!=None:
            return z
    return None

