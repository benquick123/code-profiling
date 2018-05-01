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

from operator import itemgetter


def premozenje(oseba, denar):
    d = 0

    for otrok in otroci[oseba]:
        d += premozenje(otrok, denar)

    d = d + denar[oseba]

    return d


def najbogatejsi(oseba, denar):
    d = [(oseba, denar[oseba])]

    for otrok in otroci[oseba]:
        d = d + [najbogatejsi(otrok, denar)]

    if len(otroci[oseba]) == 0:
        return d[0]

    else:
        return max(d, key=itemgetter(1))


def uravnotezeni(oseba, denar):
    d = []

    for otrok in otroci[oseba]:
        d = d + [premozenje(otrok, denar)]

    if len(otroci[oseba]) == 0:
        return True

    else:
        return len(set(d)) == 1


def neuravnotezeni_rezultat(oseba, denar):
    d = []

    for otrok in otroci[oseba]:
        d = d + [neuravnotezeni_rezultat(otrok, denar)]

    for rez in d:
        if type(rez) is str:
            return rez

    if len(otroci[oseba]) == 0:
        return denar[oseba]

    if len(set(d)) == 1:
        return premozenje(oseba, denar)

    else:
        return oseba


def neuravnotezeni(oseba, denar):
    rezultat = neuravnotezeni_rezultat(oseba, denar)

    if type(rezultat) is str:
        return rezultat

    else:
        return None


