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
    vrednost = denar[oseba]
    for ime,potomci in otroci.items():
        if ime == oseba:
            for potomec in potomci:
                vrednost += premozenje(potomec, denar)
    return vrednost

def najbogatejsi(oseba, denar):
    oseba2 = oseba
    vred = denar[oseba]
    for ime,potomci in otroci.items():
        if ime == oseba:
            for potomec in potomci:
                oseba, kes = najbogatejsi(potomec, denar)
                if kes > vred:
                    oseba2 = potomec
                    vred = kes
    return (oseba2, vred)



