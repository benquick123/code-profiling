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
    skupaj = denar[oseba]
    for otrok in otroci[oseba]:
        skupaj += premozenje(otrok, denar)
    return skupaj


def najbogatejsi(oseba, denar):
    naj = denar[oseba]
    najOseba = oseba
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok, denar)[1] > naj:
            najOseba, naj = najbogatejsi(otrok, denar)
    return najOseba, naj


def uravnotezeni(oseba, denar):
    seznam = []
    for otrok in otroci[oseba]:
        uravnotezeni(otrok, denar)
        seznam.append(premozenje(otrok, denar))
    for i in seznam:
        if i != seznam[0]:
            return False
    return True


def neuravnotezeni(oseba, denar):
    seznam = []
    for otrok in otroci[oseba]:
        neuravnotezeni(otrok, denar)
        seznam.append((oseba, premozenje(otrok, denar)))
    for i in seznam:
        ime, vsota = i
        if vsota != seznam[0][1]:
            return ime


