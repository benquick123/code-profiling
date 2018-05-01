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
    for otrok in otroci[oseba]:
        vsota += premozenje(otrok, denar)
    return vsota

def najbogatejsi(oseba, denar):
    richest, amount = oseba, denar[oseba]
    for otrok in otroci[oseba]:
        if najbogatejsi(otrok, denar)[1] > amount:
            richest, amount = najbogatejsi(otrok, denar)
    return (richest, amount)



def uravnotezeni(oseba, denar):
    if otroci[oseba] == [] or \
                    all(uravnotezeni(otrok, denar) for otrok in otroci[oseba]) and \
                    otroci[oseba][0] == all(otroci[oseba][1:]):
        return True
    else:
        return False

