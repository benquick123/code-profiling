
# Obvezna naloga

def premozenje(oseba, denar):
    vsota = denar[oseba]
    for otrok in otroci[oseba]:
        v = premozenje(otrok, denar)
        if v != None:
            vsota += v
    return vsota


def najbogatejsi(oseba, denar):
    x = denar[oseba]
    y = oseba
    for otrok in otroci[oseba]:
        naj = najbogatejsi(otrok, denar)
        if naj[1] > x:
            x = naj[1]
            y = naj[0]
    return (y, x)

# Dodatna

def uravnotezeni(oseba, denar):
    denarnica = []
    for otrok in otroci[oseba]:
        s = premozenje(otrok, denar)
        denarnica.append(s)
        m = uravnotezeni(otrok, denar)
        if m == False:
            return False
    for d in denarnica:
        if d != denarnica[0]:
            return False
    return True

def neuravnotezeni(oseba, denar):
    denarnica = []
    for otrok in otroci[oseba]:
        s = premozenje(otrok, denar)
        denarnica.append(s)
        m = neuravnotezeni(otrok, denar)
        if m != None:
            return m
    for d in denarnica:
        if d != denarnica[0]:
            return oseba







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


