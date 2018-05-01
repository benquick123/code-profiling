def premozenje(oseba, denar):
    vsota=0
    vsota=vsota+denar[oseba]
    for lol in otroci[oseba]:
        kok=premozenje(lol,denar)
        vsota=vsota+kok
    return vsota
def najbogatejsi(oseba, denar):
    normaln=(oseba,denar[oseba])
    for lol in otroci[oseba]:
        koliko=najbogatejsi(lol,denar)
        ime,d=koliko
        i,n=normaln
        if d>n:


            normaln=koliko

    return normaln

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


