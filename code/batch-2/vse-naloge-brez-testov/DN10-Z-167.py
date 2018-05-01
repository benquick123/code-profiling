
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
    return sum(premozenje(otrok,denar) for otrok in otroci[oseba]) + denar[oseba]

"""def najbogatejsi(oseba,denar):
    bogat = [(oseba, denar[oseba])]
    for otrok in otroci[oseba]:
        bogat.append((otrok, denar[otrok]))
        for vnuk in otroci[otrok]:
            bogat.append((vnuk,denar[vnuk]))
    return"""

def najbogatejsi(oseba,denar):
    bogat = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok, denar)[1] >= bogat[1]:
            bogat = najbogatejsi(otrok, denar)
    return bogat

