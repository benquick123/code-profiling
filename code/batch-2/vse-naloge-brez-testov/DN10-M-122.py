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

    return sum(premozenje(ime, denar) for ime in otroci[oseba]) + denar[oseba]

def najbogatejsi(oseba, denar):

    maks = denar[oseba]
    bogatas = oseba
    for ime in otroci[oseba]:
        trojka = najbogatejsi(ime, denar)
        tmp = trojka[1]
        if tmp > maks:
            maks = tmp
            bogatas = ime

    return (bogatas, maks)



