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
    vsota_denarja=denar[oseba]
    for mulac in otroci[oseba]:
        if mulac in denar:
            vsota_denarja+=premozenje(mulac,denar)
    return (vsota_denarja)

def najbogatejsi(oseba, denar):
    najvecji=(oseba,denar[oseba])
    for otrok in otroci[oseba]:
        najbogatejsi_otrok=najbogatejsi(otrok,denar)
        maks = najvecji[1]
        if najbogatejsi_otrok[1]>maks:
            najvecji=najbogatejsi_otrok
    return (najvecji)
