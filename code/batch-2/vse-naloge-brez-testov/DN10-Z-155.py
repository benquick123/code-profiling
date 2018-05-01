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
    djeca = otroci[oseba]
    vsota = denar[oseba]
    if len(djeca)==0:
        return vsota
    else:
        for otrok in djeca:
            vsota+=premozenje(otrok, denar)

    return vsota

def najbogatejsi(oseba, denar):
    djeca = otroci[oseba]
    najvec = denar[oseba]
    naj_ime = oseba
    if len(djeca) == 0:
        return (oseba, najvec)
    else:
        for otrok in djeca:
            (ime, naj_denar) = najbogatejsi(otrok, denar)
            if naj_denar > najvec:
                najvec = naj_denar
                naj_ime = ime

    return (naj_ime, najvec)

def uravnotezeni(oseba, denar):
    if uravnotezeni_rec(oseba, denar) == False:
        return False
    else:
        return True

def uravnotezeni_rec(oseba, denar):
    djeca = otroci[oseba]
    vsota = denar[oseba]
    premozenja = []
    if len(djeca) == 0:
        return vsota
    else:
        for otrok in djeca:
            premozenja.append(uravnotezeni_rec(otrok, denar))
        if len(set(premozenja)) > 1:
            return False

    return sum(premozenja) + vsota

def neuravnotezeni(oseba, denar):
    tmp = neuravnotezeni_rec(oseba, denar)
    if isinstance(tmp, str):
        return tmp
    else:
        return None

def neuravnotezeni_rec(oseba, denar):
    djeca = otroci[oseba]
    vsota = denar[oseba]
    premozenja = []
    if len(djeca) == 0:
        return vsota
    else:
        for otrok in djeca:
            premozenja.append(neuravnotezeni_rec(otrok, denar))
        if len(set(premozenja)) > 1:
            for el in premozenja:
                if isinstance(el, str):
                    return el
            return oseba

    return sum(premozenja) + vsota

