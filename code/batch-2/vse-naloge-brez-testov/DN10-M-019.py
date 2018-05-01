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
    gold = denar[oseba]
    a = premozenjeotrok(oseba,denar)
    return  gold + a

def premozenjeotrok(oseba,denar):
    return sum(denar[otrok] + premozenjeotrok(otrok, denar) for otrok in otroci[oseba])


def premozenje(oseba, denar):
    return sum(denar[otrok] + premozenjeotrok(otrok, denar) for otrok in otroci[oseba]) + denar[oseba]

'''def najbogatejsi(oseba, denar):
    naj = ((oseba, denar[oseba]))
    for otrok in otroci[oseba]:
        if denar[otrok] or najbogatejsi(otrok,denar)[1] > naj[1]:
            naj = ((otrok, denar[otrok]))

    return naj
'''
def najbogatejsi(oseba, denar):
    naj = ((oseba, denar[oseba]))
    for otrok in otroci[oseba]:
        naja = najbogatejsi(otrok, denar)
        if naja[1] > naj[1]:
            naj = naja
    return naj




