def premozenje(oseba, denar):
    kolicina = denar[oseba]
    for otrok in otroci[oseba]:
        if denar[otrok] != None:
            kolicina += premozenje(otrok, denar)
    return kolicina

def najbogatejsi(oseba, denar):
    bogatun, vsota = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        if vsota < denar[otrok]:
            bogatun, vsota = najbogatejsi(otrok, denar)
    return (bogatun, vsota)



def uravnotezeni(oseba, denar):
    kolicina = []
    for otrok in otroci[oseba]:
        kolicina += [premozenje(otrok, denar)]
    if (len(set(kolicina)) == 1 or kolicina == []):
            return True
    return False

def neuravnotezeni(oseba, denar):
    for otrok in otroci[oseba]:
        neuravnotezeni(otrok, denar)
    if not uravnotezeni(oseba, denar):
        denar['Utez'] = oseba
    return denar.get('Utez', None)


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


