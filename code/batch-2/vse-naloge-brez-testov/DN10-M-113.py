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
    prem = denar[oseba]
    if otroci[oseba]:
        for otrok in otroci[oseba]:
            prem += premozenje(otrok, denar)
    return prem

def najbogatejsi(oseba, denar):
    prem_naj = denar[oseba]
    if otroci[oseba]:
        for otrok in otroci[oseba]:
            otrok,prem_otr = najbogatejsi(otrok,denar)
            if prem_otr > prem_naj:
                prem_naj = prem_otr
                oseba = otrok
    return (oseba, prem_naj)

def uravnotezeni(oseba, denar):
    

    return True


