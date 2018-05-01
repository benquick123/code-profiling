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

def premozenje (oseba, denar):
    cash = denar[oseba]
    for otrok in otroci[oseba]:
        cash +=premozenje(otrok, denar)
    return cash

def najbogatejsi(oseba, denar):
    maks = denar[oseba]
    ime = oseba
    for otrok in otroci[oseba]:
        ime2, maks2 = najbogatejsi(otrok, denar)
        if maks2 > maks:
            maks = maks2
            ime = ime2

    return ime, maks




