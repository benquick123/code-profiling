def premozenje(oseba, denar):
    denar_otrok = 0
    for otrok in otroci[oseba]:
        denar_otrok += premozenje(otrok, denar)
    return denar[oseba] + denar_otrok

def premozenje(oseba, denar):
    return denar[oseba] + sum([premozenje(otrok, denar) for otrok in otroci[oseba]])

def najbogatejsi(oseba, denar):
    max_premozenje = denar[oseba]
    max_ime = oseba
    for otrok in otroci[oseba]:
        max_otrok = najbogatejsi(otrok, denar)
        if max_otrok[1] > max_premozenje:
            max_premozenje = max_otrok[1]
            max_ime = max_otrok[0]
    return (max_ime, max_premozenje)

def uravnotezeni(oseba, denar):
    seznam_premozenj = list()
    for otrok in otroci[oseba]:
        seznam_premozenj.append(premozenje(otrok, denar))
        gg = uravnotezeni(otrok, denar)
        if not gg:
            return False
    for x, y in zip(seznam_premozenj, seznam_premozenj[1:]):
        if x != y:
            return False
    return True

def neuravnotezeni(oseba, denar):
    seznam_premozenj = list()
    for otrok in otroci[oseba]:
        seznam_premozenj.append(premozenje(otrok, denar))
        gg = neuravnotezeni(otrok, denar)
        if isinstance(gg, str):
            return gg
    for x, y in zip(seznam_premozenj, seznam_premozenj[1:]):
        if x != y:
            return oseba
    return None

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


