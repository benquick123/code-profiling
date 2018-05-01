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
    if otroci[oseba] == []:
        return denar[oseba]
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        vsota  += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    if otroci[oseba] == []:
        return (oseba, denar[oseba])
    b = oseba
    for otrok in otroci[oseba]:
        c = najbogatejsi(otrok, denar)[0]
        print(denar[b])
        if denar[b] < denar[c]:
            b = c
    return (b, denar[b])

def uravnotezeni(oseba, denar):
    if otroci[oseba] == []:
        return True
    val = premozenje(otroci[oseba][0], denar)
    for otrok in otroci[oseba][1:]:
        if premozenje(otrok, denar) != val:
            return False
    return True

def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba,denar):
        return oseba
    o = None
    for otrok in otroci[oseba]:
        o = neuravnotezeni(otrok, denar)
        if o is not None:
            return o
    return o


