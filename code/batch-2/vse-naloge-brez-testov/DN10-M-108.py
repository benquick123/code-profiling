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

denar = {
    "Adam": 42,
    "Aleksander": 3,
    "Alenka": 3,
    "Barbara": 37,
    "Cilka": 242,
    "Daniel": 4,
    "Erik": 32,
    "Elizabeta": 8,
    "Franc": 16,
    "Herman": 12,
    "Hans": 55,
    "Jožef": 7,
    "Jurij": 5,
    "Ludvik": 37,
    "Margareta": 20,
    "Matjaž": 142,
    "Petra": 3,
    "Tadeja": 45,
    "Viljem": 55
}

def premozenje(oseba, denar):
    vesdenar = 0
    for otrok in otroci[oseba]:
        vesdenar +=  premozenje(otrok, denar)

    return vesdenar + denar[oseba]



def funkcija_denar(oseba):
    seznam = [denar[oseba]]
    for otrok in otroci[oseba]:
        seznam.extend(funkcija_denar(otrok))

    return seznam

def funkcija_osebe(oseba):
    seznam = [oseba]
    for otrok in otroci[oseba]:
        seznam.extend(funkcija_osebe(otrok))

    return seznam


def najbogatejsi(oseba, denar):
    a = max(funkcija_denar(oseba))
    b = funkcija_osebe(oseba)

    for ime, kovanci in denar.items():
        if kovanci == a and ime in b:
            return ((ime, a))


