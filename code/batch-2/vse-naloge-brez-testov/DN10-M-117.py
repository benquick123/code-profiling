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
    vsota = denar[oseba]
    if otroci[oseba] == None:
        return vsota
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota



def najbogatejsi(oseba, denar):
    naj_bogt = (denar[oseba], oseba)
    for otrok in otroci[oseba]:
        vsota = tuple(int(i) for i in naj_bogt)
        if denar[otrok] > vsota:
            naj_bogt = (najbogatejsi(otrok, denar), oseba)
    return naj_bogt




