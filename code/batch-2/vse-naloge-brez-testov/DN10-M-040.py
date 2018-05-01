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
    d = denar[oseba]
    for otrok in otroci[oseba]:
        d += premozenje(otrok,denar)
    return d

def najbogatejsi(oseba, denar):
    dnar = denar[oseba]
    t = (oseba, dnar)
    for otrok in otroci[oseba]:
        if premozenje(otrok, denar) > dnar:
            dnar = denar[otrok]
            t = (otrok, dnar)
        najbogatejsi(otrok, denar)
    return t
