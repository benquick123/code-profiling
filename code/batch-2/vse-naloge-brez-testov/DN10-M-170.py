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
    vsota = denar[oseba]
    for potomci in otroci[oseba]:
        vsota += premozenje(potomci, denar)
    return vsota

def najbogatejsi(oseba, denar):
    najbogatejsa_oseba = oseba
    najvec = denar[oseba]
    for potomci in otroci[oseba]:
        if najvec < najbogatejsi(potomci, denar)[1]:
            najvec = denar[potomci]
            najbogatejsa_oseba = potomci
    return najbogatejsa_oseba, najvec

def uravnotezeni(oseba, denar):
    if otroci[oseba] == []:
        return True
    premozenja_rodbin = list()
    for potomci in otroci[oseba]:
        premozenja_rodbin.append(premozenje(potomci, denar))
    if len(set(premozenja_rodbin)) == 1:
        return True
    return False

def neuravnotezeni(oseba, denar):
    ime = None
    for potomci in otroci[oseba]:
        novo_ime = neuravnotezeni(potomci, denar)
        if novo_ime != None:
            ime = novo_ime
    if not uravnotezeni(oseba, denar):
        ime = oseba
    return ime



