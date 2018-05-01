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
    vsota=denar[oseba]
    for otrok in otroci[oseba]:
        kolicina = premozenje(otrok, denar)
        vsota += kolicina
    return vsota

def najbogatejsi(oseba, denar):
    bilanca= denar[oseba]
    najbogat= oseba
    for otrok in otroci[oseba]:
        primerjava= najbogatejsi(otrok, denar)

        if primerjava[1] > bilanca:
            bilanca= primerjava[1]
            najbogat=otrok
    return (najbogat, bilanca)

