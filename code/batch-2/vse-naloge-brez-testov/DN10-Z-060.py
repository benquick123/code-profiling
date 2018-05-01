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
# 1: Napiši funkcijo premozenje(oseba, denar), ki pove, kolikor denarja imajo (skupaj) člani rodbine podane oseb.
def premozenje(oseba, denar):
    return sum(premozenje(otrok,denar) for otrok in otroci[oseba]) + denar[oseba]

def najbogatejsi(oseba, denar):
    najbogatejsa_oseba = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        najbogatejsi_otrok = najbogatejsi(otrok, denar)
        if najbogatejsi_otrok[1] > najbogatejsa_oseba[1]:
            najbogatejsa_oseba = najbogatejsi_otrok
    return najbogatejsa_oseba


