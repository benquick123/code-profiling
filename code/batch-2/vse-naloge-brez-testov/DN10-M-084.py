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
    imetje = denar[oseba]
    for otrok in otroci[oseba]:
        imetje += premozenje(otrok, denar)
    return imetje

def najbogatejsi(oseba, denar):
    najvec = denar[oseba]
    najbog = oseba
    for otrok in otroci[oseba]:
        koliko = najbogatejsi(otrok, denar)[1]
        if koliko > najvec:
            najvec = koliko
            najbog = otrok
    return (najbog, najvec)

def uravnotezeni(oseba, denar):
    moj_den = denar[oseba]
    otrok_den_prev = None
    for otrok in otroci[oseba]:
        otrok_den = uravnotezeni(otrok, denar)
        if otrok_den_prev != None and otrok_den != otrok_den_prev:
            return False
        otrok_den_prev = otrok_den
        moj_den += otrok_den
    return moj_den

def uravnotezeni2(oseba, denar):
    moj_den = denar[oseba]
    otrok_den_prev = None
    for otrok in otroci[oseba]:
        otrok_den = uravnotezeni2(otrok, denar)
        if not isinstance(otrok_den, int):
            return otrok_den
        if otrok_den_prev is not None and otrok_den != otrok_den_prev:
            return oseba
        otrok_den_prev = otrok_den
        moj_den += otrok_den
    return moj_den

def neuravnotezeni(oseba, denar):
    res = uravnotezeni2(oseba, denar)
    if not isinstance(res, int):
        return res

