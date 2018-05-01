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
def premozenje(oseba,denar):
    cash=denar[oseba]
    if not otroci[oseba]:
        return denar[oseba]
    for otrok in otroci[oseba]:
        cash+=premozenje(otrok,denar)
    return cash

def najbogatejsi(oseba, denar):
    max_cash=(oseba,denar[oseba])
    if not otroci[oseba]:
        return max_cash
    for otrok in otroci[oseba]:
        if denar[oseba]<najbogatejsi(otrok,denar)[1]:
            max_cash=(otrok,denar[otrok])
    return max_cash

def najbogatejsi(oseba, denar):
    naj=(oseba,denar[oseba])
    for otrok in otroci[oseba]:
        naj_o=najbogatejsi(otrok,denar)
        if naj_o[1]>naj[1]:
            naj=naj_o
    return  naj
