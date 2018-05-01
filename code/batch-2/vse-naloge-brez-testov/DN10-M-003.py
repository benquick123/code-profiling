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
    bogastvo = 0
    bogastvo += denar[oseba]
    for otrok in otroci[oseba]:
        bogastvo += premozenje(otrok, denar)
    return bogastvo

def najbogatejsi(oseba, denar):
    oligarh, najvec = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        x, y = najbogatejsi(otrok, denar)
        if y > najvec:
            oligarh, najvec = x, y
    return (oligarh, najvec)


def uravnotezeni(oseba, denar):
    ekvilibrij, bogastvo = True, []
    for otrok in otroci[oseba]:
        if premozenje(otrok, denar) not in bogastvo:
            bogastvo.append(premozenje(otrok, denar))
        if len(bogastvo) > 1 or not uravnotezeni(otrok, denar):
            ekvilibrij = False
    return ekvilibrij


def rodbina(oseba):
    x = oseba + " "
    y = []
    for otrok in otroci[oseba]:
        x += rodbina(otrok)
    return x

def neuravnotezeni(oseba, denar):
    x, z = rodbina(oseba).split(), []
    for y in x:
        y.strip()
        if not uravnotezeni(y, denar):
            z.append(y)
    if z:
        return z[-1]
    else:
        return None




