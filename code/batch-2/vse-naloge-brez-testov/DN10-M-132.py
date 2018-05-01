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
    denar_osebe = 0
    for otrok in otroci[oseba]:
        denar_osebe += premozenje(otrok, denar)
    return denar_osebe + denar[oseba]

def najbogatejsi(oseba, denar):
    najbogatejsa_oseba = (oseba, denar[oseba])
    for otrok in otroci[oseba]:
        najbogatejsi_pod = najbogatejsi(otrok, denar)
        if najbogatejsi_pod[1] >= najbogatejsa_oseba[1]:
            najbogatejsa_oseba = najbogatejsi_pod
    return najbogatejsa_oseba

def uravnotezeni(oseba, denar):
    st_otrok = len(otroci[oseba])
    st_uravnotezenih_otrok = 0
    premoznja_otrok = []
    for otrok in otroci[oseba]:
        premoznja_otrok.append(premozenje(otrok, denar))
        if uravnotezeni(otrok, denar):
            st_uravnotezenih_otrok += 1
    # True, če imajo vsi rodovi otrokov enako premožnje
    # IN če imajo tudi rodovi njihovih otrokov enako premoženje
    return (len(set(premoznja_otrok)) <= 1) and (st_otrok == st_uravnotezenih_otrok)

def neuravnotezeni(oseba, denar):
    neur = None
    if not uravnotezeni(oseba, denar):
        neur = oseba
    for otrok in otroci[oseba]:
        neur_pod = neuravnotezeni(otrok, denar)
        if neur_pod != None:
            neur = neur_pod
    return neur


