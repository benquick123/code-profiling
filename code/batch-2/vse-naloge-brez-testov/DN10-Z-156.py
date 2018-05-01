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
    vsota = 0
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota + denar[oseba]


def najbogatejsi(oseba, denar):
    osebaa, največ_denarja = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        najbogatejši = najbogatejsi(otrok, denar)
        if najbogatejši[1] > največ_denarja:
            osebaa = najbogatejši[0]
            največ_denarja = najbogatejši[1]
    return (osebaa, največ_denarja)


def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True
    t = []
    for otrok in otroci[oseba]:
        t.append(premozenje(otrok, denar))
    return sum(t) / len(t) == t[0]

def neuravnotezeni5(oseba, denar):
    d = []
    for otrok in otroci[oseba]:
        d.append(neuravnotezeni(otrok, denar))

    for e1, e2 in d:
        if e2 == None:
            return e1
    return (oseba, uravnotezeni(oseba, denar))

def neuravnotezeni(oseba, denar):
    if not uravnotezeni(oseba,denar):
        return oseba

    for otrok in otroci[oseba]:
        tmp = neuravnotezeni(otrok,denar)
        if tmp:
            return tmp


