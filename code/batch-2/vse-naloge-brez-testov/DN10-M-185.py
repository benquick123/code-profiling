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
    s = denar[oseba]
    for otrok in otroci[oseba]:
        s = s + premozenje(otrok, denar)
    return s


def najbogatejsi(oseba, denar):
    s = (oseba,denar[oseba])
    for otrok in otroci[oseba]:
        naj = najbogatejsi(otrok, denar)
        if s[1] < naj[1]:
            s = (otrok, naj[1])
    return s


