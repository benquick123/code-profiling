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
    if oseba in denar:
        skupen_denar = denar[oseba]
        for otrok in otroci[oseba]:
            skupen_denar = skupen_denar + premozenje(otrok, denar)
        return skupen_denar

def najbogatejsi(oseba, denar):
    if oseba in denar:
        bogata_oseba = oseba
        najvec_denarja = denar[oseba]
        for otrok in otroci[oseba]:
            neka_oseba, nekaj_denarja = najbogatejsi(otrok, denar)
            if nekaj_denarja > najvec_denarja:
                bogata_oseba = neka_oseba
                najvec_denarja = nekaj_denarja
        return bogata_oseba, najvec_denarja

def uravnotezeni(oseba, denar):
    if oseba:
        if None in otroci[oseba]:
            return True
        for otrok in otroci[oseba]:
            denar = denar[otrok]


