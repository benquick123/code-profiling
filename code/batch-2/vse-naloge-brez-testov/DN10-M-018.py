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
    d = denar[oseba]
    for otrok in otroci[oseba]:
        d += premozenje(otrok, denar)
    return d



def najbogatejsi(oseba, denar):
    naj_denar = denar[oseba]
    naj_oseba = oseba
    for otrok in otroci[oseba]:
        ret_oseba, ret_denar = najbogatejsi(otrok, denar)
        if ret_denar > naj_denar:
            naj_denar = ret_denar
            naj_oseba = ret_oseba

    return (naj_oseba, naj_denar)


def uravnotezeni(oseba, denar):
    if otroci[oseba] == []:
        return True

    d = premozenje(otroci[oseba][0], denar)
    for otrok in otroci[oseba][1:]:
        if not d == premozenje(otrok, denar):
            return False

    return True

def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba, denar):
        return None
    else:
        ne_oseba = oseba
        for otrok in otroci[oseba]:
            if not uravnotezeni(otrok, denar):
                ne_oseba = neuravnotezeni(otrok, denar)
        return ne_oseba

