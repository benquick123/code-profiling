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

'''
Imam rekurzivno migreno. 
'''

def premozenje(oseba, denar):
    prem = 0
    if not otroci[oseba]:
        return denar[oseba]
    else:
        for otrok in otroci[oseba]:
            prem += premozenje(otrok, denar)
    return prem + denar[oseba]

def najbogatejsi(oseba, denar):
    naj = (oseba, denar[oseba])
    if not otroci[oseba]:
        return naj
    else:
        for otrok in otroci[oseba]:
            tre = najbogatejsi(otrok, denar)
            if tre[1] > naj[1]:
                naj = tre
    return naj

def uravnotezeni(oseba, denar):
    container = []
    if not otroci[oseba]:
        return True
    else:
        for otrok in otroci[oseba]:
            prem = premozenje(otrok, denar)
            container.append(prem)
            if not uravnotezeni(otrok, denar):
                return False
    return all([True if x == container[0] else False for x in container])

def neuravnotezeni(oseba, denar):
    if not otroci[oseba]:
        return None
    elif not uravnotezeni(oseba, denar):
        for otrok in otroci[oseba]:
            if not uravnotezeni(otrok, denar):
                return neuravnotezeni(otrok, denar)
        return oseba if all([True if uravnotezeni(o, denar) else False for o in otroci[otrok]]) else None
    else:
        return None

