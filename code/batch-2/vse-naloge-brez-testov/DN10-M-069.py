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

def premozenje(oseba,denar):
    v = denar[oseba]
    if not otroci[oseba]:
        return denar[oseba]
    else:
        for a in otroci[oseba]:
            v += premozenje(a,denar)
    return v

def najbogatejsi(oseba, denar):
    terka = (oseba, denar[oseba])
    if not otroci[oseba]:
        return (oseba, denar[oseba])
    else:
        for a in otroci[oseba]:
            max_otroka = najbogatejsi(a,denar)[1]
            if max_otroka > terka[1]:
                terka = (a, max_otroka)
    return terka

