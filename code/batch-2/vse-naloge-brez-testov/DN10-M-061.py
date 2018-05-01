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
    vsota=denar[oseba]
    otroci_=otroci[oseba]
    for o in otroci_:
        vsota+=premozenje(o, denar)
    return vsota

def najbogatejsi(oseba, denar):
    najvec_denarja=(oseba,denar[oseba])
    otroci_ = otroci[oseba]
    for o in otroci_:
        if najbogatejsi(o, denar)[1]>najvec_denarja[1]:
            najvec_denarja=(o, denar[o])
    return najvec_denarja

def uravnotezeni(oseba, denar):
    otroci_=otroci[oseba]
    premozenje_temp=None
    uravnotezeno=False
    for o in otroci_:
        if not premozenje_temp:
            premozenje_temp=premozenje(o,denar)
        else:
            if premozenje_temp==premozenje(o, denar):
                uravnotezeno=True
            else:
                return False
    return True

