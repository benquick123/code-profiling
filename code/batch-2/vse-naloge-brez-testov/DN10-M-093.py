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
    if not otroci[oseba]:
        return vsota
    else:
        for otrok in otroci[oseba]:
            vsota += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    najvec = (oseba, denar[oseba])
    if not otroci[oseba]:
        return najvec
    else:
        for otrok in otroci[oseba]:
            naj_otrok = najbogatejsi(otrok, denar)
            if naj_otrok[1] > najvec[1]:
                najvec = naj_otrok
        return najvec


def uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True
    else:
        prem = []
        for otrok in otroci[oseba]:
            prem += [premozenje(otrok, denar)]
            if not all(x == prem[0] for x in prem):
                return False
        for otrok in otroci[oseba]:
            if not uravnotezeni(otrok, denar):
                return False
        return True

def vsi_otroci_uravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return True
    else:
        s = []
        for otrok in otroci[oseba]:
            s += [uravnotezeni(otrok, denar)]
        if all(s):
            return True
        else:
            return False




def neuravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return None
    else:
        if vsi_otroci_uravnotezeni(oseba, denar) and not uravnotezeni(oseba, denar):
                return oseba
        for otrok in otroci[oseba]:
            if not uravnotezeni(otrok, denar):
                return neuravnotezeni(otrok, denar)
            else:
                continue
        return None

#==================================== TESTI ==================================#

