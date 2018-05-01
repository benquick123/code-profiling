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
    d = 0
    d += denar[oseba]
    for otrok in otroci[oseba]:
        d+= premozenje(otrok,denar)
    return(d)
def najbogatejsi(oseba, denar):
    maks = (oseba,denar[oseba])
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok,denar)[1]> maks[1]:
            maks = (otrok,denar[otrok])
    return(maks)
#dodatne
def uravnotezeni(oseba, denar):
    sez = []
    for otrok in otroci[oseba]:
        sez.append(premozenje(otrok,denar))
    if all(x == sez[0] for x in sez):
        return(True)
    else:
        return(False)
def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba,denar):
        return(oseba)
    else:
        for otrok in otroci[oseba]:
            a = neuravnotezeni(otrok,denar)
            if a != None:
                return(a)

