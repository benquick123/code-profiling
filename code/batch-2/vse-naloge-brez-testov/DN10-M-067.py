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
    premozenje_sku = denar[oseba]
    for otrok in otroci[oseba]:
        premozenje_sku += premozenje(otrok,denar)
    return premozenje_sku


def najbogatejsi(oseba, denar):
    naj_denar = denar[oseba]
    najbogatejsi_os = oseba
    for otrok in otroci[oseba]:
        naj = najbogatejsi(otrok, denar)
        if naj[1] > naj_denar:
            naj_denar = naj[1]
            najbogatejsi_os = naj[0]
    return (najbogatejsi_os,naj_denar)



