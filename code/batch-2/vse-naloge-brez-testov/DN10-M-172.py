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
    vsota = denar.get(oseba)
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    ime = oseba
    vred = denar.get(oseba)
    for otrok in otroci[oseba]:
        podatek = najbogatejsi(otrok, denar)
        if podatek[1] > vred:
            vred = podatek[1]
            ime = otrok

    return (ime, vred)



