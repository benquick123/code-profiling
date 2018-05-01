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
    a = 0
    if not denar:
        return denar
    for relative in otroci[oseba]:
        a += premozenje(relative, denar)
    return a + denar[oseba]

def najbogatejsi(oseba, denar):
    a = (oseba, denar[oseba])
    if not denar:
        return denar
    for relative in otroci[oseba]:
        b = najbogatejsi(relative, denar)
        if b[1::] > a[1::]:
            a = b
    return a

def uravnotezeni(oseba, denar):
    a = []
    if not denar:
        return denar
    for relative in otroci[oseba]:
        a.append((premozenje(relative, denar), uravnotezeni(relative, denar)))
    for i in range(len(a)-1):
        if not (a[i][1] and a[i + 1][1] and a[i][0] == a[i + 1][0]):
            return False
    return True

def neuravnotezeni(oseba, denar):
    if not denar:
        return denar
    if not uravnotezeni(oseba, denar):
        for relative in otroci[oseba]:
            a = neuravnotezeni(relative, denar)
            if a != None:
                return a
        return oseba
    return None

