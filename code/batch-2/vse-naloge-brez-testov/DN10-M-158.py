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
    res = denar[oseba]
    for name in otroci[oseba]:
        res += premozenje(name, denar)
    return res

def najbogatejsi(oseba, denar):
    max_t = (oseba, denar[oseba])
    for name in otroci[oseba]:
        max_t1 = najbogatejsi(name, denar)
        if max_t[1] < max_t1[1]:
            max_t = max_t1
    return max_t



def uravnotezeni(oseba, denar):  #works faster for some reason
    for name, name1 in zip(otroci[oseba], otroci[oseba][1:]):
       if premozenje(name, denar) != premozenje(name1, denar) or not uravnotezeni(name, denar) or not uravnotezeni(name1, denar):
           return False
    return True

"""
def uravnotezeni(oseba, denar):
    if len(otroci[oseba]):
        res = premozenje(otroci[oseba][0], denar)
        if not uravnotezeni(otroci[oseba][0], denar):
            return False
    for name in otroci[oseba][1:]:
        res_t = premozenje(name, denar)
        if not uravnotezeni(name, denar) or res != res_t:
            return False
        res = res_t
    return True
"""


def neuravnotezeni(oseba, denar):
    if uravnotezeni(oseba, denar):
        return None
    for name in otroci[oseba]:
        if not uravnotezeni(name, denar):
            return neuravnotezeni(name, denar)
    return oseba


