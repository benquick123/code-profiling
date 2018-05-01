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
    premozenje_otrok = 0
    for otrok in otroci[oseba]:
        premozenje_otrok += premozenje(otrok, denar)
    return denar[oseba] + premozenje_otrok

def najbogatejsi(oseba, denar):
    imax = oseba
    cmax = denar[oseba]
    for otrok in otroci[oseba]:
        i, c = najbogatejsi(otrok, denar)
        if c > cmax:
            imax = i
            cmax = c
    return (imax, cmax)

