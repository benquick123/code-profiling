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
    children = otroci[oseba]
    for otrok in children:
        vsota += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    naj_ime, naj_denar = oseba, denar[oseba]
    children = otroci[oseba]
    for otrok in children:
        ime, premozenje = najbogatejsi(otrok, denar)
        if premozenje > naj_denar:
            naj_ime, naj_denar = ime, premozenje
    return (naj_ime, naj_denar)

def uravnotezeni(oseba, denar):
    children = otroci[oseba]
    if not children:
        return True
    for otrok in children:
        prvo = premozenje(children[0], denar)
        if uravnotezeni(otrok, denar) and all(premozenje(otrok, denar) == prvo for otrok in children):
            return True
    return False

def neuravnotezeni(oseba, denar):
    children = otroci[oseba]
    if not children:
        return None
    prvo = premozenje(children[0], denar)
    if not all(premozenje(otrok, denar) == prvo for otrok in children):
        return oseba
    for otrok in children:
        poskus = neuravnotezeni(otrok, denar)
        if poskus != None:
            return poskus

