def premozenje(oseba, denar):
    p = 0
    for otrok in otroci[oseba]:
        p += premozenje(otrok, denar)
    return p + denar[oseba]

def najbogatejsi(oseba, denar):
    nb = ("", 0)
    for naslednik in otroci[oseba]:
        if nb[1] < najbogatejsi(naslednik, denar)[1]:
            nb = (naslednik, denar[naslednik])
    if nb[1] > denar[oseba]:
        return nb
    return (oseba, denar[oseba])

def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True

    for otrok in otroci[oseba]:
        for bs in otroci[oseba]: #bs -> brat/sesta
            if premozenje(otrok, denar) != premozenje(bs, denar):
                return False
    return True

#-------------------------------------------------------------------
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


